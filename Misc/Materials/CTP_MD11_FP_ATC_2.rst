

                                RESULTS FILE

******************************************************************************
                            Test Results Summary

          Percentage of Comparisons Passed    : 100.0000%   

          Total Number of Comparisons Failed  : 0           
          Total Number of Unknown Comparisons : 0           
          Total Number of Comparisons Passed  : 632         
          Total Number of Comparisons         : 632         
          Total Number of Test Cases Included : 91          

          Test Complete          

                                                                              

******************************************************************************


Test Start Time: May 02 09:26:43 2014

FILE: CTP_MD11_FP_ATC_2.TDF

PEGASUS COMPONENT TEST PLAN

PACKAGE: FP_ROUTE_UPLINK_PKG

PROCEDURE: FP_LATERAL_PKG.REQUEST_PROCESSOR
           FP_ROUTE_UPLINK_PKG.EXECUTIVE
           FP_ROUTE_UPLINK_PKG.FIND_REV_PT
           FP_ROUTE_UPLINK_PKG.GET_NEXT_ELEMENT
           FP_ROUTE_UPLINK_PKG.INIT
           FP_ROUTE_UPLINK_PKG.IS_ALT_A_CRZ_FL
           FP_ROUTE_UPLINK_PKG.PROCESS_AIRPORT
           FP_ROUTE_UPLINK_PKG.PROCESS_AIRWAY
           FP_ROUTE_UPLINK_PKG.PROCESS_ARRIVAL
           FP_ROUTE_UPLINK_PKG.PROCESS_ATO
           FP_ROUTE_UPLINK_PKG.PROCESS_CONSTRAINT
           FP_ROUTE_UPLINK_PKG.PROCESS_DIRECT_FIX
           FP_ROUTE_UPLINK_PKG.PROCESS_DUPLICATE_FIX
           FP_ROUTE_UPLINK_PKG.PROCESS_ERROR
           FP_ROUTE_UPLINK_PKG.PROCESS_HOLD
           FP_ROUTE_UPLINK_PKG.PROCESS_LAT_OFFSET
           FP_ROUTE_UPLINK_PKG.PROCESS_REVISE
           FP_ROUTE_UPLINK_PKG.PROCESS_RTA
           FP_ROUTE_UPLINK_PKG.ROUTE_CONSTRUCTION
           FP_ROUTE_UPLINK_PKG.STRING_ARRIVAL
           FP_ROUTE_UPLINK_PKG.GENORGDEST
           FP_ROUTE_UPLINK_PKG.SETUP_ATC
           FP_ROUTE_UPLINK_PKG.PROCESS_ATC_DEPARTURE

TITLE:  Test for FP_ROUTE_UPLINK_PKG
                 FP_LATERAL_PKG

PREPARED BY: Schukin Vladimir              DATE: 18 May       2000
MODIFIED BY: Schukin Vladimir              DATE: 14 August    2000 Changes were made for MD11 LD10A.
MODIFIED BY: Schukin Vladimir              DATE: 17 October   2000 Several tests were changed or added to increase coverage statistics.
MODIFIED BY: Schukin Vladimir              DATE:  5 December  2000 Changes (not great) were made for MD11 LD20A.
MODIFIED BY: Schukin Vladimir              DATE: 19 December  2000 Several cases have been changed to increase coverage statistic.
MODIFIED BY: Schukin Vladimir              DATE: 18 January   2001 Changes were made for MD11 LD20C.
MODIFIED BY: Schukin Vladimir              DATE: 22 May       2001 Failures exist now. I have added explanation.
MODIFIED BY: Schukin Vladimir              DATE: 10 June      2001 I have added new breakpoint to decrease the count of errors.
                                                                   Explanation for error exists.
MODIFIED BY: Ni, Jiangrong     24044.02    DATE: 28 Oct       2013 Update the hardbreakpoint since the build is changed to MD11_922_807.
MODIFIED BY: Ni, Jiangrong     24044.02    DATE: 12 Feb       2014 Rework after review, updated MOD history
                                                                   Added SCR number, run on build MD11_922_807.
MODIFIED BY: Gu Ling           24123.03    DATE: 6  Mar       2014 Updated On new build MD11_922_A03
                                                                   1. Updated TC:90 as per anchor FPLN_SRD_4360,FPLN_SRD_4362 and FPLN_SRD_4345 changed.
                                                                   2. Removed FPLN_SRD_4345 and added FPLN_SRD_4360,IO_SRD_7176,FPLN_SRD_4361,
                                                                      FPLN_SRD_4362, FPLN_SRD_4363 in SOURCE.
                                                                   4. Added TC:91 as per new anchor FPLN_SRD_4361,FPLN_SRD_4363 and IO_SRD_7176.
                                                                   5. Added robust TC:92 to verify anchor FPLN_SRD_4360,FPLN_SRD_4361,FPLN_SRD_4362,FPLN_SRD_4363.
                                                                   6. Updated Test Case description of point c,d,e,Note and SUT_VARS.
MODIFIED BY: Gu Ling           24193.03    DATE: 2  May       2014 Updated On new build MD11_922_A10
                                                                   Updated hard breakpoint as per build changed.

TRACEBILITY TO REQUIREMENTS/CODE
OVERALL TESTING APPROACH: VERIFY COMPLIANCE WITH SRD SECTION:
ATC Flight Plan Uplinks..........................5.2.3.1

-- -- -- ANCHOR  : MD11_FPLN_TEST_3004
-- -- -- SOURCE  : FPLN_SRD_3949, FPLN_SRD_2280, FPLN_SRD_2281, FPLN_SRD_2282, FPLN_SRD_2285, FPLN_SRD_2286,
-- -- --           FPLN_SRD_2288, FPLN_SRD_2289, FPLN_SRD_3901, FPLN_SRD_3902, FPLN_SRD_3903, FPLN_SRD_3904,
-- -- --           FPLN_SRD_3905, FPLN_SRD_3906, FPLN_SRD_3907, FPLN_SRD_3908, FPLN_SRD_3910, FPLN_SRD_3911,
-- -- --           FPLN_SRD_4360, FPLN_SRD_3918, FPLN_SRD_3942, FPLN_SRD_3945, FPLN_SRD_3946, FPLN_SRD_3947,
-- -- --           FPLN_SRD_3948, IO_SRD_7176,   FPLN_SRD_4361, FPLN_SRD_4362, FPLN_SRD_4363
-- -- --

-- -- --        BEGIN PROCESSING INCLUDE FILE C:\Program Files\honeywell_eng\TGS_v4_5_2\bin\debug_cmds.inc
-- -- --        END PROCESSING INCLUDE FILE C:\Program Files\honeywell_eng\TGS_v4_5_2\bin\debug_cmds.inc
-- -- -- ******************************************************************
-- -- --                    INITIALIZATION SECTION
-- -- -- ******************************************************************


CONSTANT                                                                                                       VALUE
--------------------------------------------------------------------------------------------------  --------------------------
FP_DEF_TOL                                                                                                               0.001


define symbol Test_Data := "Test_MD11_fp_atc_pkg"
define symbol Rejection := "Test_MD11_fp_atc_pkg.Test_Rejection_Data"
define symbol Fpx := "Fpx_Uplink_Buffer_Pkg:body"
define symbol Fpx_t := "Fpx_Buffer_Types"
define symbol Approach := Fmcs_Base_Types.Viatype'(Fmcs_Base_Types.Approach)
define symbol Auto_Transition_Inhibit := "Options_And_Data_Pkg:body.All_Options.Auto_Transition_Inhibit"
define symbol F_t := "Flight_Pln_Hdr_Types"
define symbol List := "Nam_Tap_Ptdata_Pkg:body.Test_List"
define symbol Test_Increased_Defined_Wpt_Storage := "Options_And_Data_Pkg:body.All_Options.Increased_Defined_Wpt_Storage"


DEFAULTS                                                                                                       VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.No_Assert                                                                                                         0
^Test_Data.Test_Fplan                                                                                                        1
^Test_Data.Test_Fprequest.Fplan                                                                                              1
^Test_Data.Test_Firstleg                                                                                                     1
^Test_Data.Test_Originwpt                                                                                                    0
^Test_Data.Test_Destwpt                                                                                                      0
^Test_Data.Test_leg(1).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(4).Fixident                                                                                      "       "
^Test_Data.Test_leg(5).Fixident                                                                                      "       "
^Test_Data.Test_leg(6).Fixident                                                                                      "       "
^Test_Data.Test_leg(7).Fixident                                                                                      "       "
^Test_Data.Test_leg(8).Fixident                                                                                      "       "
^Test_Data.Test_leg(9).Fixident                                                                                      "       "
^Test_Data.Test_leg(10).Fixident                                                                                     "       "
^Test_Data.Test_leg(11).Fixident                                                                                     "       "
^Test_Data.Test_leg(1).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(4).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(5).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(6).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(7).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(8).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(9).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(10).Fixtype                                                                      Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(11).Fixtype                                                                      Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_Duplicates_Exist(1)                                                                                      False
^Test_Data.t_Display_Message_Text(1..22)                                                              "                      "
^Test_Data.Via_Valid                                                                                                      True
^Test_Data.Test_Next_Offset                                                                                                  0
^Test_Data.Ident_exist_in_database14                                                                    Nam_Iftypes.Successful
^Test_Data.database_error                                                                                                False
^Test_Data.Test_Origaptexist                                                                                             False
^Test_Data.Test_Sidstar_Tapfile                                                                           Nam_Iftypes.Standard
^Test_Data.Test_Sid_Trans_List_Count                                                                                         2


CONSTANT                                                                                                       VALUE
--------------------------------------------------------------------------------------------------  --------------------------
DBG_TIMEOUT                                                                                                                300


TESTID: 1

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Procedure_Type(1)                                                                         ^Fpx_t.Fpx_Departure
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                        Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 2

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                         ^Fpx_t.Fpx_Departure
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                       Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 3

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Test_Data.Test_Fprequest.Tapsel.Sidstarval                                                                               True
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                              ^Fpx_t.Fpx_Airport
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFH   "
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Firstapprleg                                                                                                 5
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Airport
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                   Fmcs_Fp_Guid_Btypes.Navaid
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                      Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 4

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEF    "
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Firstapprleg                                                                                                 5
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                   Fmcs_Fp_Guid_Btypes.Navaid
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                   Fmcs_Fp_Guid_Btypes.Runway
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                      Fmcs_Fp_Guid_Btypes.Runway          (N/A)                      RUNWAY  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 5

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGH  "
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 5
^Test_Data.Test_Firstapprleg                                                                                                 0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                   Fmcs_Fp_Guid_Btypes.Runway
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                    Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                       Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 6

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFI   "
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 5
^Test_Data.Test_Firstapprleg                                                                                                 0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                    Fmcs_Fp_Guid_Btypes.Waypt
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                     Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                        Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 7

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFG   "
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 5
^Test_Data.Test_Firstapprleg                                                                                                 0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                     Fmcs_Fp_Guid_Btypes.Ndrb
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Airport
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                     Fmcs_Fp_Guid_Btypes.Airport          (N/A)                     AIRPORT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 8

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Dup_Fix_Type                                                                            Fmcs_Fp_Guid_Btypes.Oneonly
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                       Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 9

   Verify resolving duplicate waypoints.
   SOURCE FPLN_SRD_3949


  case N,N+1: Duplicate fix ([PublishedIdent]) is the first fix.
              [RouteClearance] contains a [ProcedureDeparture].
    Matching fix shall be searched in departure procedure/transition.
   SOURCE FPLN_SRD_3942
  case N+2 - N+6: Duplicate fix ([PublishedIdent]) is the last fix.
              [RouteClearance] contains a [ProcedureArrival] or [ProcedureApproach].
    Matching fix shall be searched in arrival or approach procedure/transition.
   SOURCE FPLN_SRD_3945
  case N+7: Duplicate fix is [PlaceBearingDistance].
  case N+8: Duplicate fix is [PublishedIdent].
            (but cannot resolved per requirements for [PublishedIdent])
    FMS shall use the duplicate closest to preceding flight plan fix or the aircraft position.
   SOURCE FPLN_SRD_3946


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 5
^Test_Data.Test_Firstapprleg                                                                                                 0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^List(1).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(1).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Oneonly
^List(2).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(2).Fix.Tofixdbptr.Dbptrtype                                                                  Fmcs_Fp_Guid_Btypes.Airport
^List(3).Ptheader.Ptcode                                                                                    Fmcs_Base_Types.Df
^List(3).Fix.Tofixdbptr.Dbptrtype                                                                    Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Airport_Ident                                                                                                "DEFG"
^Test_Data.Navaid_Ident                                                                                                 "DEFH"
^Test_Data.Rwy_Ident                                                                                                     "DEF"
^Test_Data.Waypt_Ident                                                                                                 "DEFGH"
^Test_Data.Ndrb_Ident                                                                                                   "DEFI"
^Test_Data.Dup_Fix_Type                                                                           Fmcs_Fp_Guid_Btypes.Cstwaypt
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                    Fmcs_Fp_Guid_Btypes.Cstwaypt          (N/A)                    CSTWAYPT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 10

   This case is added with the goal of increasing the coverage statistics.

  case X : DATABASE ERROR exists during Duplicate Waypoint Resolution.

  Allocation of the code:
  procedure Fp_Route_Uplink_Pkg.Process_Duplicate_Fix
  540          if Leg_Count = 0 then
  541            -- DATABASE ERROR
  542            Fp_Error_Processing_Pkg.Process_Error (Fprequest => Fprequest,                                   -- in out
  543                                                   New_Error_Status => Fprequestrec_Types.Nam_Error,         -- in
  544                                                   Failure_Code => Fp_Error_Code_Dpkg.Pt_List_Size_Is_Zero); -- in
  545
  546          else

   SOURCE FPLN_CODE_1921


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(4)                                                                                ^Fpx_t.Fpx_Atwpt
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                       True
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_Fix_Type(1)                                                                         Fmcs_Fp_Guid_Btypes.Fmcwpt
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 5
^Test_Data.Test_Firstapprleg                                                                                                 0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Dup_Fix_Type                                                                           Fmcs_Fp_Guid_Btypes.Cstwaypt
^Test_Data.database_error                                                                                                 True
^Test_Data.Test_Lastsidleg                                                                                                   4
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "       "
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "       "
^Test_Data.Test_leg(3).Fixtype                                                                        Fmcs_Fp_Guid_Btypes.Ndrb
^Test_Data.Fix_Type_for_duplication                                                                              Qrec.Fix_Type


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.Fix_Type_for_duplication                    Fmcs_Fp_Guid_Btypes.Cstwaypt          (N/A)                    CSTWAYPT  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 2 Comparisons Passed <====


TESTID: 11

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(7).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 12

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(7).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 13

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(7).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Fixident(1..2)                                          "RW"          (N/A)                        "RW"  P
^Test_Data.Test_leg(7).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 14

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 15

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 16

   Verify [RunwayArrival].
   SOURCE FPLN_SRD_3949


  case I - I+2 (Element 83)
    [Position] is not a fix in flight plan.
   case I: There is no destination airport.
   case I+1: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+2: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2289
  case I+3 - I+5 (Element 83)
    [Position] is a fix in flight plan.
   case I+3: There is no destination airport.
   case I+4: There is destination airport.
          Runway is not valid at the destination airport.
   [RunwayArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3901
   case I+5: There is destination airport.
          [RunwayArrival] is loadable.
          The [RunwayArrival] shall be strung.(as IF leg)
   SOURCE FPLN_SRD_3902
   SOURCE FPLN_SRD_2288
  cases I - I+1,I+3 -I+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  case I+2 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Fixident(1..2)                                                                                     "  "
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Fixident(1..2)                                          "RW"          (N/A)                        "RW"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 5 Comparisons Passed <====


TESTID: 17

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 18

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 19

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 7 Comparisons Passed <====


TESTID: 20

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 7 Comparisons Passed <====


TESTID: 21

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 7 Comparisons Passed <====


TESTID: 22

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 7 Comparisons Passed <====


TESTID: 23

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 24

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 25

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 26

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 27

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 28

   Verify [ProcedureArrival].
   SOURCE FPLN_SRD_3949


 case J - J+5 (Element 83)
   [Position] is not a fix in flight plan.
  case J: There is no destination airport.
  case J+1: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case J+2,J+3: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+4,J+5: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case J+6 - J+11 (Element 83)
   [Position] is a fix in flight plan.
  case J+6: There is no destination airport.
  case J+7: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
   [ProcedureArrival] shall be considered unloadable.
   SOURCE FPLN_SRD_3906
  case J+8,J+9: There is destination airport.
          [ProcedureArrival] is compatible with arrival airport.
          [ProcedureArrival] is incompatible with an existing destination runway.
  case J+10,J+11: There is destination airport.
          [ProcedureArrival] is incompatible with arrival airport.
          [ProcedureArrival] is compatible with an existing destination runway.
          [ProcedureArrival] shall be strung into Flight Plan.
          (each leg of [ProcedureArrival] shall be strung immediately following destination runway,
           if enroute transition is not specified)
   SOURCE FPLN_SRD_3907
   SOURCE FPLN_SRD_2288
  cases J - J+1,J+6 - J+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases J+2 - J+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 29

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 30

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database11                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 31

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viaenrtrns
^Test_Data.Ident_exist_in_database11                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(8).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(9).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(10).Viacode                                Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(11).Viacode                                Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(12).Viacode                                Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 10 Comparisons Passed <====


TESTID: 32

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 33

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database11                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 34

   Verify Arrival Transition.
   SOURCE FPLN_SRD_3949


 case K - K+2 (Element 83)
   [Position] is not a fix in flight plan.
  case K: [ProcedureArrival] was not valid.
  case K+1: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+2: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_2285
   SOURCE FPLN_SRD_2289
 case K+3 - K+5 (Element 83)
   [Position] is a fix in flight plan.
  case K+3: [ProcedureArrival] was not valid.
  case K+4: [ProcedureArrival] is valid.
         Arrival Transition is not valid transition of the [ProcedureArrival].
          Arrival Transition shall be considered unloadable.
  case K+5: [ProcedureArrival] is valid.
         Arrival Transition is valid transition of the [ProcedureArrival].
          Arrival Transition shall be strung into the flight plan along with its associated [ProcedureArrival].
          [ProcedureArrival] shall be inserted immediately following the last leg of Arrival Transition.
   SOURCE FPLN_SRD_3908
   SOURCE FPLN_SRD_2288
  cases K,K+3 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases K+1 - K+2,K+4 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Type                                                                             ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viaenrtrns
^Test_Data.Ident_exist_in_database11                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(6).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Startrans          (N/A)                   STARTRANS  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(10).Viacode                                Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 9 Comparisons Passed <====


TESTID: 35

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 36

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 37

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         0
^Auto_Transition_Inhibit                                                                                                  True
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(8).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(9).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 7 Comparisons Passed <====


TESTID: 38

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         0
^Auto_Transition_Inhibit                                                                                                  True
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(11).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(12).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 10 Comparisons Passed <====


TESTID: 39

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         1
^Auto_Transition_Inhibit                                                                                                 False
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
Fprequest.Tapsel.Runwayval                                                                                                True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(8).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(9).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(11).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(12).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 10 Comparisons Passed <====


TESTID: 40

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(13).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(14).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(15).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         1
^Auto_Transition_Inhibit                                                                                                 False
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise
Fprequest.Tapsel.Runwayval                                                                                                True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(10).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(11).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(12).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(13).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(14).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(15).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 13 Comparisons Passed <====


TESTID: 41

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 42

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 43

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Runway
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Runway_Type                                                                             ^Fpx_t.Fpx_Destination
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         0
^Auto_Transition_Inhibit                                                                                                  True
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(6).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(7).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 6 Comparisons Passed <====


TESTID: 44

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         0
^Auto_Transition_Inhibit                                                                                                  True
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(9).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 9 Comparisons Passed <====


TESTID: 45

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         1
^Auto_Transition_Inhibit                                                                                                 False
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
Fprequest.Tapsel.Runwayval                                                                                                True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(6).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(8).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(9).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 9 Comparisons Passed <====


TESTID: 46

   Verify [ProcedureApproach].
   SOURCE FPLN_SRD_3949


 case L - L+7 (Element 83)
   [Position] is not a fix in flight plan.
  case L: There is no destination airport.
  case L+1: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_2287
  case L+2,L+3: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+4,L+5: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+2: no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+3: [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+4: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+5: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case L+6 - L+11 (Element 83)
   [Position] is a fix in flight plan.
  case L+6: There is no destination airport.
  case L+7: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
   [ProcedureApproach] shall be considered unloadable.
   SOURCE FPLN_SRD_3903
  case L+8,L+9: There is destination airport.
          [ProcedureApproach] is compatible with arrival airport.
          [ProcedureApproach] is incompatible with arrival runway.
  case L+10,L+11: There is destination airport.
          [ProcedureApproach] is incompatible with arrival airport.
          [ProcedureApproach] is compatible with arrival runway.
          (Without an approach transition)
       L+8 : no [ProcedureArrival] exist,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following revise point.
       L+9 : [ProcedureArrival] exist   ,automatic selection of an approach transition is not possible
            The [ProcedureApproach] shall be strung without an approach transition.
            The [ProcedureApproach] shall be inserted immediately following the last leg of the [ProcedureArrival].
       L+10: no [ProcedureArrival] exist,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the revise point.
            [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
       L+11: [ProcedureArrival] exist   ,automatic selection of an approach transition is possible
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
            [ProcedureApproach] shall be inserted immediately following Approach Transition.
   SOURCE FPLN_SRD_3904
   SOURCE FPLN_SRD_2288
  cases L - L+1,L+6 - L+7 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases L+2 - L+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(13).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Approach_Trans_Count                                                                                         1
^Auto_Transition_Inhibit                                                                                                 False
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise
Fprequest.Tapsel.Runwayval                                                                                                True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(9).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(10).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(11).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(12).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(13).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 12 Comparisons Passed <====


TESTID: 47

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 48

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Ident_exist_in_database12                                                                  Nam_Iftypes.Unsuccessful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 49

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database12                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(8).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(9).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(11).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(12).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 10 Comparisons Passed <====


TESTID: 50

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(5)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(13).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(14).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(15).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database12                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Firststarleg                                                                                                 3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(9).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(10).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(11).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(12).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(13).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(14).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(15).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 13 Comparisons Passed <====


TESTID: 51

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                   Nam_Iftypes.Unsuccessful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                      False
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 52

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Ident_exist_in_database12                                                                  Nam_Iftypes.Unsuccessful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 53

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database12                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(6).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(7).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(8).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(9).Viacode                                             Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(10).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 9 Comparisons Passed <====


TESTID: 54

   Verify Approach Transition.
   SOURCE FPLN_SRD_3949


 case M - M+3 (Element 83)
   [Position] is not a fix in flight plan.
  case M: The [ProcedureApproach] was not valid.
  case M+1: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+2,M+3: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+2: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+3: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_2286
   SOURCE FPLN_SRD_2289
 case M+4 - M+7 (Element 83)
   [Position] is a fix in flight plan.
  case M+4: The [ProcedureApproach] was not valid.
  case M+5: The [ProcedureApproach] is valid.
         Approach Transition is not valid transition of the [ProcedureApproach].
          Approach Transition shall be considered unloadable.
  case M+6,M+7: The [ProcedureApproach] is valid.
         Approach Transition is valid transition of the [ProcedureApproach].
          The Approach Transition shall be inserted with its associated [ProcedureApproach].
       M+6: no [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the revise point.
       M+7: [ProcedureArrival] exist,
            Approach Transition will be inserted immediately following the last leg of [ProcedureArrival].
          [ProcedureApproach] shall be inserted immediately following the last leg of Approach Transition.
   SOURCE FPLN_SRD_3905
   SOURCE FPLN_SRD_2288
  cases M,M+4 : All of the elements of the uplink are unloadable
  The scratchpad message 'UNABLE TO LOAD F-PLN' shall be displayed
   SOURCE FPLN_SRD_3948
  cases M+1 - M+3,M+5 : Some of the elements are unloadable, and some of the elements are loadable.
  The scratchpad message 'PARTIAL F-PLN LOADED' shall be displayed
   SOURCE FPLN_SRD_3947


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(4)                                                                            ^Fpx_t.Fpx_Procedure
^Test_Data.Type_of_Elements(5)                                                                           ^Fpx_t.Fpx_Transition
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Procedure_Type(1)                                                                           ^Fpx_t.Fpx_Arrival
^Test_Data.Test_Procedure_Type(2)                                                                          ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Type                                                                            ^Fpx_t.Fpx_Approach
^Test_Data.Test_Transition_Id                                                                                       "CDEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(6).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(7).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(8).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(9).Viacode                                                                             Fmcs_Base_Types.Sid
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_leg(10).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(11).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(12).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Test_leg(13).Viacode                                                                            Fmcs_Base_Types.Sid
^Test_Data.Ident_exist_in_database1                                                                     Nam_Iftypes.Successful
^Test_Data.Ident_exist_in_database2                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Rwy_And_Star_Compat                                                                                       True
^Test_Data.Test_Rwy_And_Appr_Compat                                                                                       True
^Test_Data.Test_Via_2(1)                                                                                Nam_Base_Types.Viastar
^Test_Data.Test_Via_2(2)                                                                                Nam_Base_Types.Viaappr
^Test_Data.Test_Via                                                                                  Nam_Base_Types.Viarwytrns
^Test_Data.Ident_exist_in_database12                                                                    Nam_Iftypes.Successful
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Rwynavdbptr                                                                                                  0
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(6).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(7).Viacode                                 Fmcs_Base_Types.Star          (N/A)                        STAR  P
^Test_Data.Test_leg(8).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(9).Viacode                            Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(10).Viacode                           Fmcs_Base_Types.Apprtrans          (N/A)                   APPRTRANS  P
^Test_Data.Test_leg(11).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(12).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.Test_leg(13).Viacode                                            Approach          (N/A)                    APPROACH  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 12 Comparisons Passed <====


TESTID: 56

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                            Fmcs_Base_Types.Cruise
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "UNABLE TO LOAD F-PLN  "          (N/A)    "UNABLE TO LOAD F-PLN  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                           False          (N/A)                       FALSE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 57

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 16 Comparisons Passed <====


TESTID: 58

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(5).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(6).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 22 Comparisons Passed <====


TESTID: 59

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                           Fmcs_Base_Types.Descent
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 16 Comparisons Passed <====


TESTID: 60

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       4
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(5).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(6).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 22 Comparisons Passed <====


TESTID: 61

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 16 Comparisons Passed <====


TESTID: 62

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(5)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(5).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(6).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 22 Comparisons Passed <====


TESTID: 63

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 16 Comparisons Passed <====


TESTID: 64

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(5)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(5).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(5).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(2).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(2).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(3).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(3).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(3).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(3).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(5).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(6).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 22 Comparisons Passed <====


TESTID: 65

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(6).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(7).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(7).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(7).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(7).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(7).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(8).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(8).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(8).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(8).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 17 Comparisons Passed <====


TESTID: 66

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(5)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "PARTIAL F-PLN LOADED  "          (N/A)    "PARTIAL F-PLN LOADED  "  P
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(6).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(7).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(7).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(7).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(7).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(8).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(8).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(8).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(9).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(9).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(9).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(9).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(10).Viacode                              Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(10).Viaident(1..6)                                     "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(10).Pathterm                                 Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(10).Fixtype                            Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 23 Comparisons Passed <====


TESTID: 67

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          4
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                          Fmcs_Base_Types.Approach
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                       Nam_Base_Types.Disconty
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(5).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(6).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 16 Comparisons Passed <====


TESTID: 68

   Verify situation, when Airway is an element of route uplink.
   SOURCE FPLN_SRD_3949


 case O - O+2 (Element 73)
  case O : After preflight.
   Airway shall be considered unloadable.
   SOURCE FPLN_SRD_2275
  case O+1 : All fixed waypoint (from first fix to the termination fix of the airway segment)
        shall be inserted into the flight plan.
        Discontinuity (if it exist) shall be strung along with the airway.
        The airway segment will be inserted as


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       5
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(4)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Type_of_Elements(5)                                                                               ^Fpx_t.Fpx_Airway
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Airway_Start_Index(1)                                                                                        1
^Test_Data.Test_Airway_End_Index(1)                                                                                          2
^Test_Data.Test_Intersection_Type(1)                                                                      Airway_Types.Awy2Fix
^Test_Data.Test_Airway_Start_Index(2)                                                                                        3
^Test_Data.Test_Airway_End_Index(2)                                                                                          3
^Test_Data.Test_Intersection_Type(2)                                                                    Airway_Types.Commonfix
^Test_Data.Test_Airway_Start_Index(3)                                                                                        3
^Test_Data.Test_Airway_End_Index(3)                                                                                          4
^Test_Data.Test_Intersection_Type(3)                                                                    Airway_Types.Commonfix
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_Destwpt                                                                                                      6
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight
^Test_Data.Ident_exist_in_database3                                                                     Nam_Iftypes.Successful
^Test_Data.Test_Ident                                                                                                 "ACEGBD"
^Test_Data.Test_Awydata_Record(1).Fix_Descriptor                                                     Nam_Base_Types.Essnwptfix
^Test_Data.Test_Awydata_Record(2).Fix_Descriptor                                                     Nam_Base_Types.Trnswptfix
^Test_Data.Test_Awydata_Record(3).Fix_Descriptor                                                         Nam_Base_Types.Navfix
^Test_Data.Test_Awydata_Record(4).Fix_Descriptor                                                        Nam_Base_Types.Ndrbfix


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(4).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(4).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(5).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(5).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(5).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(5).Fixtype                            Fmcs_Fp_Guid_Btypes.Waypt          (N/A)                       WAYPT  P
^Test_Data.Test_leg(6).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(6).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(6).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(7).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(7).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(7).Pathterm                                  Fmcs_Base_Types.Sf          (N/A)                          SF  P
^Test_Data.Test_leg(7).Fixtype                           Fmcs_Fp_Guid_Btypes.Navaid          (N/A)                      NAVAID  P
^Test_Data.Test_leg(8).Viacode                               Fmcs_Base_Types.Airway          (N/A)                      AIRWAY  P
^Test_Data.Test_leg(8).Viaident(1..6)                                      "ACEGBD"          (N/A)                    "ACEGBD"  P
^Test_Data.Test_leg(8).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.Test_leg(8).Fixtype                             Fmcs_Fp_Guid_Btypes.Ndrb          (N/A)                        NDRB  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 22 Comparisons Passed <====


TESTID: 69

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 70

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 71

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          73
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Flight_Phase                                                                         Fmcs_Base_Types.Preflight


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 72

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Df          (N/A)                          DF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 73

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Df          (N/A)                          DF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 74

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       2
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          80
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Firststarleg                                                                                                 0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Df          (N/A)                          DF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 75

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Fix_Identifier(2)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(2)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(2)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 76

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Fix_Identifier(2)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(2)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 77

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "IJKLMNO"
^Test_Data.Test_Fix_Identifier(2)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(2)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(1).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 78

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 79

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 80

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          79
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Originwpt                                                                                                    3
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Nextfpn                                                                                               3


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(2).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 81

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      4


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 82

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      4


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 83

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      4


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                          True          (N/A)                        TRUE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 84

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 85

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      2.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 86

   If Fix is loadable, then it shall be strung as enroute fix.
   (TF leg shall be strung)

  case a,  a+3,a+6,a+9, a+12,a+15 : Fix is [PublishedIdentifier].
  case a+1,a+4,a+7,a+10,a+13,a+16 : Fix is [LatitudeLongitude].
  case a+2,a+5,a+8,a+11,a+14,a+17 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3910


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                               ^Fpx_t.Atc_Fix
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           4.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Pathterm                                                                             Fmcs_Base_Types.Af
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Pathterm                                  Fmcs_Base_Types.Tf          (N/A)                          TF  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 87

   If Fix is not loadable, then a discontinuity shall be strung.

  case b   : Fix is [PublishedIdentifier].
  case b+1 : Fix is [LatitudeLongitude].
  case b+2 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3911


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                       ^Fpx_t.Atc_Initial_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                      False
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHI "
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Discon                                                                                            False
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 88

   If Fix is not loadable, then a discontinuity shall be strung.

  case b   : Fix is [PublishedIdentifier].
  case b+1 : Fix is [LatitudeLongitude].
  case b+2 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3911


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                       ^Fpx_t.Atc_Initial_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                      False
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Lat_Lon
^Test_Data.Test_Lat_Lon.Lat                                                                                                2.0
^Test_Data.Test_Lat_Lon.Lon                                                                                                2.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fromlatlon.Lat                                                                                      2.0
^Test_Data.Test_leg(2).Fromlatlon.Lon                                                                                      1.0
^Test_Data.Test_leg(2).Llfixtype                                                               Fmcs_Fp_Guid_Btypes.Plainlatlon
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Discon                                                                                            False
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 89

   If Fix is not loadable, then a discontinuity shall be strung.

  case b   : Fix is [PublishedIdentifier].
  case b+1 : Fix is [LatitudeLongitude].
  case b+2 : Fix is [PlaceBearingDistance].

   SOURCE FPLN_SRD_3911


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Fix_Identifier(1)                                                                       ^Fpx_t.Atc_Initial_Fix
^Test_Data.Test_Duplicates_Exist(1)                                                                                      False
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                      Fpx_Buffer_Types.Pbd
^Test_Data.Test_Parent_Ident                                                                                           "ABCDE"
^Test_Data.Test_Distance                                                                                                   3.0
^Test_Data.Test_Bearing_Is_True                                                                                          False
^Test_Data.Test_Bearing                                                                                                    4.0
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Llfixtype                                                                    Fmcs_Fp_Guid_Btypes.Pbdwpt
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(2).Pbdparent                                                                                       "ABCDE"
^Test_Data.Test_leg(2).Fixbrgmag                                                                                           5.0
^Test_Data.Test_leg(2).Fixdist                                                                                             3.0
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(4).Discon                                                                                            False
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.Test_leg(4).Discon                                                  True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 90

   If the pilot defined waypoint list is full and the OPC flag INCREASED DEFINED
   WPTS STORAGE is false, and an attempt to insert a new waypoint identifier into
   the pilot defined waypoint list fails, the new waypoint identifier will be unloadable
    and the scratchpad message 'LIST OF FORTY IN USE' shall be displayed on the MCDU.
---Here message 'LIST OF FORTY IN USE' of IO_SRD_7176 in Table 4 is also verified.
   SOURCE FPLN_SRD_4360,FPLN_SRD_4362,IO_SRD_7176


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
Fpx_Uplink_Buffer_Pkg:body.Pilot_Def_Wpt_List_Status                                                     Fpx_Buffer_Types.Full
^Test_Increased_Defined_Wpt_Storage                                                                                      False


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "LIST OF FORTY IN USE  "          (N/A)    "LIST OF FORTY IN USE  "  P
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 91

   If the pilot defined waypoint list is full and the OPC flag INCREASED DEFINED WPTS STORAGE is true,
   and an attempt to insert a new waypoint identifier into the pilot defined waypoint list fails,
   the new waypoint identifier will be unloadable and the scratchpad message 'DEFINED WPTS LIST FULL'
   shall be displayed on the MCDU.
---Here message 'DEFINED WPTS LIST FULL' of IO_SRD_7176 in Table 4 is also verified.
   SOURCE FPLN_SRD_4361,FPLN_SRD_4363,IO_SRD_7176


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
Fpx_Uplink_Buffer_Pkg:body.Pilot_Def_Wpt_List_Status                                                     Fpx_Buffer_Types.Full
^Test_Increased_Defined_Wpt_Storage                                                                                       True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "DEFINED WPTS LIST FULL"          (N/A)    "DEFINED WPTS LIST FULL"  P
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


TESTID: 92

   If the pilot defined waypoint list is not full and no matter of opc flag INCREASED DEFINED WPTS STORAGE
   No message shall displayed on the MCDU.
-- Here's robust case
-- SOURCE FPLN_SRD_4360,FPLN_SRD_4361,FPLN_SRD_4362,FPLN_SRD_4363


INPUT                                                                                                          VALUE
--------------------------------------------------------------------------------------------------  --------------------------
^Test_Data.SUT_Entry                                                                                         ^Test_Data.CASE_2
^Test_Data.Test_Fprequest.Fpreq                                                                Allfprequest_Types.Route_Uplink
^Test_Data.Test_Fprequest.Buffer_Is_Aoc                                                                                  False
^Fpx.Buffer_Pointer(^Fpx_t.Atc_Buffer)                                                                                       3
^Fpx.Buffer_Status(^Fpx_t.Atc_Buffer)                                                                         ^Fpx_t.Buffer_Ok
^Test_Data.Type_of_Elements(1)                                                                        ^Fpx_t.Fpx_Atc_Indicator
^Test_Data.Type_of_Elements(2)                                                                                  ^Fpx_t.Fpx_Rta
^Test_Data.Type_of_Elements(3)                                                                                  ^Fpx_t.Fpx_Fix
^Test_Data.Test_Atc_Element_Number                                                                                          83
^Test_Data.Test_Rta_Fix                                                                                              "IJKLMNO"
^Test_Data.Test_Waypoint_Type_Fix(1)                                                                  Fpx_Buffer_Types.Fixname
^Test_Data.Test_Fix_Ident(1)                                                                                         "DEFGHIJ"
^Test_Data.Test_leg(1).Prevfpn                                                                                               0
^Test_Data.Test_leg(1).Nextfpn                                                                                               2
^Test_Data.Test_leg(2).Prevfpn                                                                                               1
^Test_Data.Test_leg(2).Nextfpn                                                                                               3
^Test_Data.Test_leg(2).Fixident                                                                                      "DEFGHIJ"
^Test_Data.Test_leg(2).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(2).Fixtype                                                                       Fmcs_Fp_Guid_Btypes.Waypt
^Test_Data.Test_leg(3).Prevfpn                                                                                               2
^Test_Data.Test_leg(3).Nextfpn                                                                                               4
^Test_Data.Test_leg(3).Fixident                                                                                      "IJKLMNO"
^Test_Data.Test_leg(3).Pathterm                                                                             Fmcs_Base_Types.Fm
^Test_Data.Test_leg(4).Prevfpn                                                                                               3
^Test_Data.Test_leg(4).Nextfpn                                                                                               5
^Test_Data.Test_leg(5).Prevfpn                                                                                               4
^Test_Data.Test_leg(5).Nextfpn                                                                                               6
^Test_Data.Test_leg(6).Prevfpn                                                                                               5
^Test_Data.Test_leg(6).Nextfpn                                                                                               7
^Test_Data.Test_leg(7).Prevfpn                                                                                               6
^Test_Data.Test_leg(7).Nextfpn                                                                                               8
^Test_Data.Test_leg(8).Prevfpn                                                                                               7
^Test_Data.Test_leg(8).Nextfpn                                                                                               9
^Test_Data.Test_leg(9).Prevfpn                                                                                               8
^Test_Data.Test_leg(9).Nextfpn                                                                                              10
^Test_Data.Test_leg(10).Prevfpn                                                                                              9
^Test_Data.Test_leg(10).Nextfpn                                                                                              0
^Test_Data.Test_Lastleg                                                                                                     10
^Test_Data.Test_Destwpt                                                                                                      6
Fpx_Uplink_Buffer_Pkg:body.Pilot_Def_Wpt_List_Status                                                     Fpx_Buffer_Types.Okay
^Test_Increased_Defined_Wpt_Storage                                                                                       True


OUTPUT                                                          EXPECTED               TOLERANCE              ACTUAL            P/F
----------------------------------------------------  -----------------------------  -------------  --------------------------  ----
^Test_Data.t_Display_Message_Text(1..22)                   "                      "          (N/A)    "                      "  P
Fp_Dl_Dpkg.Unloadable                                                         False          (N/A)                       FALSE  P
Fp_Dl_Dpkg.Loadable                                                            True          (N/A)                        TRUE  P
^Test_Data.No_Assert                                                              1          (N/A)                           1  P


====> All 4 Comparisons Passed <====


Test End Time: May 02 09:30:52 2014
Test Generation System (TGS) Version v4.5.2, ps4082887-103
Current Program Library
   c:\builds\md11\hw\hads_root\a29_cert_system.alb (root)
   c:\builds\md11\hw\common_software\pegasus_29050_v014\csw.alb
   c:\builds\md11\hw\bld_hw\libraries\com.alb
   C:\BUILDS\MD11\HW\BLD_HW\Libraries\fm.alb
   C:\MD11_Project\CTP\24193.01\SLTP\CTP_MD11_FP_ATC\my_fm.alb
