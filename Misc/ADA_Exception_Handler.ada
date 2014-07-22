with System;
with Ada.Text_IO;
with Ada.Exceptions;

use Ada.Text_IO;
use Ada.Exceptions;

procedure Hello is
begin
    Put_Line("Hello World");    
    raise Constraint_Error;
    
    Exception
        When e : Others =>
            Put_Line("Exception occurred:");
            Put_Line(Exception_Name(e));         -- CONSTRAINT_ERROR
            Put_Line(Exception_Message(e));      -- hello.adb:11 explicit raise
            Put_Line(Exception_Information(e));  -- Exception name: CONSTRAINT_ERROR
                                                 -- Message: hello.adb:11 explicit raise
end Hello;