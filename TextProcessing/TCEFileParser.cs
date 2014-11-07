/// by Liu Mingyang

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace WindowsFormsApplication1.Logic
{
    public class TCEFileParser
    {        
        public bool ReuseExcuse(String oldTCEFilePath, String newTCEFilePath, String outputFilePath)
        {
            if (!(File.Exists(oldTCEFilePath) && File.Exists(newTCEFilePath)))
            {                
                return false;
            }

            StreamWriter swOutputFile = new StreamWriter(outputFilePath);
            if (null == swOutputFile)
                return false;

            Dictionary<String, String> oldDisposedHoles = new Dictionary<String, String>();
            Dictionary<String, String> newHolesTBD = new Dictionary<String, String>();
            StreamReader srOldTCEFile = new StreamReader(oldTCEFilePath);
            StreamReader srNewTCEFile = new StreamReader(newTCEFilePath);            

            // Subunit start: SubUnit: ATC_UL_MSG_PROCESSOR_PKG.PROCESS_161_NOT_FOUND
            //            or: SubUnit: ATC_UL_MSG_PROCESSOR_PKG.GET_DL_ELEMENT  (0.0% Coverage)
            // Subunit end: ******************** 
#warning    May "Subunit" blocks end with ..............?
            const String SUBUNIT_BLOCK_END_MARK_PATTERN = @"^[*]{20,}?";
            const String SUBUNIT_BLOCK_PATTERN = @"^SubUnit:\s*(\S+).*?\n" +  // procedure line
                                                 @"([^\e]*?)" +                 // holes and possible excuse
                                                 SUBUNIT_BLOCK_END_MARK_PATTERN;
            // e.g., {protective_code}
            const String EXECUSE_PATTERN = @"{[\w\s]+}";
            // const String EXECUSE_PATTERN = @"({[\w\s]+}\s*\n[^\e]+?)([[]\d+-\d+\s+[A-Z]{2,}])?";            
            const String HOLE_PREFIX = @"([[]\d+-\d+\s+[A-Z]{2,}])";  // e.g., [1-101 JMP]
            const String ANY_NORMAL_TEXT = @"[^\e]+";
            const String MULTIPLE_EXCUSES_SPECIAL_VALUE = "{MULTIPLE_EXCUSES}";  // program-defined value for multiple excuses

            #region collect matches from old TCE file
            /// 如果一个 subunit 只有一个 excuse, 那就以这个 subunit 的名字为 KEY, 以其 excuse 为 VALUE.
            /// 如果一个 subunit 有多个 excuses, 那就先以该 subunit 的名字为 KEY, 以特殊值 MULTIPLE_EXCUSES_SPECIAL_VALUE 为 VALUE
            /// 再以该 subunit 中的每个 coverage hole 的第一行为 KEY, 该 coverage hole 的 excuse 为 VALUE.
            /// 也就是通过一个特殊值 MULTIPLE_EXCUSES_SPECIAL_VALUE 把本来应该有两级的 KEY-VALUE 扁平化为一级。
            MatchCollection subunitBlocks = Regex.Matches(srOldTCEFile.ReadToEnd(),
                                                          SUBUNIT_BLOCK_PATTERN,
                                                          RegexOptions.Multiline);
            srOldTCEFile.Close();
            foreach (Match subunitBlock in subunitBlocks)
            {
                MatchCollection matches = Regex.Matches(subunitBlock.Groups[2].Value, EXECUSE_PATTERN);
                if (1 == matches.Count)  // single excuse in one subunit
                    oldDisposedHoles.Add(subunitBlock.Groups[1].Value,
                        Regex.Match(subunitBlock.Groups[2].Value, EXECUSE_PATTERN + ANY_NORMAL_TEXT).Value);
                else if (1 < matches.Count)  
                #region multiple matches in one subunit
                /*
                {
                    // ([[]\d+-\d+\s+[A-Z]{2,}])(.+)[^\e]+{[\w\s]+}[^\e]+?([[]\d+-\d+\s+[A-Z]{2,}])
                    // ([[]\d+-\d+\s+[A-Z]{2,}])  (.+)  [^\e]+  ({[\w\s]+}[^\e]+?)  ([[]\d+-\d+\s+[A-Z]{2,}])
                    // matches a hole block between two [1-101 JMP] (inclusive)
                    MatchCollection excuses = Regex.Matches(subunitBlock.Groups[2].Value,
                        HOLE_PREFIX + @"(.+)" + ANY_NORMAL_TEXT + "(" + EXECUSE_PATTERN + ANY_NORMAL_TEXT + @"?)" + HOLE_PREFIX);
                    foreach (Match excuse in excuses)
                        // KEY: NON-executed source lines 83 - 83 follow.
                        // VALUE: {protective_code}\n This code insures ...
                        oldDisposedHoles.Add(excuse.Groups[2].Value, excuse.Groups[3].Value);                    

                    // the last excuse does not end with a HOLE_PREFIX, so match it separately. But how?

                }
                */
                {
                    oldDisposedHoles.Add(subunitBlock.Groups[1].Value, MULTIPLE_EXCUSES_SPECIAL_VALUE);
                    foreach (String split in Regex.Split(subunitBlock.Groups[2].Value, HOLE_PREFIX))
                    {
                        // ([^\n]+)[^\e]+({[\w\s]+}[^\e]+)
                        Match match = Regex.Match(split, @"([^\n]+)" + ANY_NORMAL_TEXT + 
                                                  "(" + EXECUSE_PATTERN + ANY_NORMAL_TEXT + ")");
                        if (match.Success)
                            oldDisposedHoles.Add(match.Groups[1].Value, match.Groups[2].Value);
                    }
                }
                #endregion multiple matches in this subunit
            }            
            #endregion collect matches from old TCE file

            #region collect holes not disposed in new TCE file
            // matches at the whole file level
            subunitBlocks = Regex.Matches(srNewTCEFile.ReadToEnd(),
                                          SUBUNIT_BLOCK_PATTERN,
                                          RegexOptions.Multiline);            
            foreach (Match subunitBlock in subunitBlocks)
            {
                Match match = Regex.Match(subunitBlock.Groups[2].Value, EXECUSE_PATTERN);
                if (match.Success)
                    continue;  // already has an execuse
                else if (!newHolesTBD.ContainsKey(subunitBlock.Groups[1].Value)) 
                    // overloaded procedures have the same name
                    newHolesTBD.Add(subunitBlock.Groups[1].Value, subunitBlock.Groups[2].Value);
            }            
            #endregion collect holes not disposed in new TCE file
                        
            #region generate TCE file
            // matches at per line level
            srNewTCEFile.BaseStream.Seek(0, SeekOrigin.Begin);
            // e.g., SubUnit: ATC_ENCODER_UTILITY_PKG.ENCODE_STRING            
            const String MISSEDOUT_EXCUSE = "{missed_out}\n\n";
            const String DONE = "DONE";                        
            while (!srNewTCEFile.EndOfStream)
            {
                String line = srNewTCEFile.ReadLine();

                #region TCE file coverage report header
                // change disposed TBD to DONE

                // ATC_MONITOR_PKG.ELEM137.ELEM137   93.5    n/a    n/a    93.5   93.4     0   0     TBD                
                Match match = Regex.Match(line, @"^([\w.]*)(\s+\d+.+\d+\s+)TBD", RegexOptions.Compiled);
                if (match.Success && oldDisposedHoles.ContainsKey(match.Groups[1].Value))
                {
                    swOutputFile.WriteLine(match.Groups[1].Value + match.Groups[2].Value + DONE);
                    continue;  // continue to the next line
                }
                                
                // *) ATC_UL_MSG_PROCESSOR_PKG.STOR -
                //      E_UPLINK                        90.0    n/a    n/a   100.0  100.0     0   0     TBD
                // *) ATC_MONITOR_PKG.PROCESS_ADS_T -
                //      TG_ON_NCM.PROCESS_ADS_TTG_O -
                //      N_NCM                           91.7    n/a    n/a    93.8   89.7     0   0     TBD
                // const String COMPILATION_UNIT_MULTI_LINE = @"(^[\w.-\s]+\s+-\n)(\s*[\w.]+\s-\n)*(\s*[\w.]+)(\s+\d+.+\d+\s+)TBD";
                match = Regex.Match(line, @"(^[\w.-]+)\s+-$", RegexOptions.Compiled);
                if (match.Success)
                {
                    List<String> procedureNameLines = new List<String>();                    
                    // restore the broken procedure name
                    String combinedProcedureName = null;
                    while (!Regex.Match(line, @"^\s*[\w.\s]+\s+\d+.+\d+\s+(TBD|DONE)").Success)                          
                    {                        
                        procedureNameLines.Add(line);
                        combinedProcedureName += line;
                        line = srNewTCEFile.ReadLine();
                    }
                    procedureNameLines.Add(line);
                    combinedProcedureName += line;   
                    match = Regex.Match(combinedProcedureName.Replace("\n", "").Replace("-", ""),
                                        @"(^[\s\w.]+)\s+\d+.+\d+\s+TBD$");
                    if (match.Success && oldDisposedHoles.ContainsKey(match.Groups[1].Value.Replace(" ", "")))
                    {
                        foreach (var item in procedureNameLines)
                            swOutputFile.WriteLine(item.Replace("TBD", DONE));
                    }
                    else
                        foreach (var item in procedureNameLines)
                            swOutputFile.WriteLine(item);
                    continue;
                }

                #endregion TCE file coverage report header

                #region TCE file body
                match = Regex.Match(line, @"^SubUnit:\s*(\S+)", RegexOptions.Compiled);
                if (match.Success)
                {
                    swOutputFile.WriteLine(line);  // write the subunit name
                    String procedureName = match.Groups[1].Value;
                    // this is a hole to be disposed
                    if (newHolesTBD.ContainsKey(procedureName))
                    {
                        // if the excuse is found in old TCE file
                        if (oldDisposedHoles.ContainsKey(procedureName))
                        {
                            // multiple holes to be disposed, and has multiple excuses in old TCE file.
                            if (MULTIPLE_EXCUSES_SPECIAL_VALUE.Equals(oldDisposedHoles[procedureName]))
                            {
                                foreach (String split in Regex.Split(newHolesTBD[procedureName], HOLE_PREFIX))
                                {
                                    if (Regex.Match(split, HOLE_PREFIX).Success)
                                    {
                                        // filter the HOLE_PREFIX in splitted substrings
                                        swOutputFile.Write(split);
                                        continue;
                                        // is the order betwwen HOLE_PREFIX and holeTile guaranteed?
                                    }
                                    match = Regex.Match(split, @"([^\n]+)\n[^\e]+");
                                    String holeTitle = match.Groups[1].Value;  // e.g., NON-executed source lines 89 - 89 follow.
                                    if (match.Success)
                                    {
                                        swOutputFile.Write(split);  // 1. write the hole as is
                                        swOutputFile.Write(oldDisposedHoles.ContainsKey(holeTitle) ?
                                            oldDisposedHoles[holeTitle] : MISSEDOUT_EXCUSE);
                                    }
                                    else
                                        swOutputFile.Write(split);
                                }
                            }
                            else  // only ONE excuse in old TCE file
                            {
                                swOutputFile.Write(newHolesTBD[procedureName]); // 1. write the hole as is
                                swOutputFile.Write(oldDisposedHoles[procedureName]);  // 2. write the excuse from old TCE file
                            }
                        }
                        else  // the execuse is not found
                        {
                            swOutputFile.Write(newHolesTBD[procedureName]);  // write the hole as is
                            swOutputFile.Write(MISSEDOUT_EXCUSE);
                        }

                        // the subunit block has been rearranged, so advance to the end of this subunit block
                        // while (!Regex.Match(srNewTCEFile.ReadLine(),
                        //                     SUBUNIT_BLOCK_END_MARK_PATTERN, RegexOptions.Compiled).Success)
                        //     ;
                        for (;
                             !Regex.Match(line, SUBUNIT_BLOCK_END_MARK_PATTERN, RegexOptions.Compiled).Success;
                             line = srNewTCEFile.ReadLine())
                            ;
                        swOutputFile.WriteLine(line);
                    }                    
                }
                else  // ordinary line, write as is.
                    swOutputFile.WriteLine(line);
                #endregion TCE file body
            }
            srNewTCEFile.Close();
            swOutputFile.Close();
            #endregion generate TCE file 

            return true;
        }
    }
}
