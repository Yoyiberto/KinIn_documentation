# Structured Text Examples

This page demonstrates the custom syntax highlighting for Structured Text programming language.

## Basic Program Structure

```st
PROGRAM MainProgram
  VAR_INPUT
    Start : BOOL;
    Stop : BOOL;
  END_VAR
  
  VAR_OUTPUT
    Running : BOOL;
    Error : BOOL;
  END_VAR
  
  VAR
    Timer1 : TON;
    Counter : INT := 0;
  END_VAR
  
  // This is a comment
  IF Start AND NOT Stop THEN
    Running := TRUE;
    Counter := Counter + 1;
  ELSIF Stop THEN
    Running := FALSE;
    Error := FALSE;
  END_IF;
  
  (* This is a multi-line comment
     that spans multiple lines *)
  
  // Function call example
  Timer1(IN := Running, PT := T#5S);
  
  // Conditional logic
  CASE Counter OF
    0: 
      // Do nothing
    1..10: 
      // Do something for values 1-10
    ELSE
      Counter := 0;
  END_CASE;
  
END_PROGRAM
```

## Function Block Example

```st
FUNCTION_BLOCK MotorControl
  VAR_INPUT
    Enable : BOOL;
    Speed : REAL;
  END_VAR
  
  VAR_OUTPUT
    Running : BOOL;
    ActualSpeed : REAL;
  END_VAR
  
  VAR
    Acceleration : REAL := 0.5;
    MaxSpeed : REAL := 100.0;
  END_VAR
  
  IF Enable THEN
    Running := TRUE;
    
    // Limit speed to maximum
    IF Speed > MaxSpeed THEN
      ActualSpeed := MaxSpeed;
    ELSE
      ActualSpeed := Speed;
    END_IF;
  ELSE
    Running := FALSE;
    ActualSpeed := 0.0;
  END_IF;
  
END_FUNCTION_BLOCK
```

## Simple Function Example

```st
FUNCTION CalculateAverage : REAL
  VAR_INPUT
    Value1 : REAL;
    Value2 : REAL;
    Value3 : REAL;
  END_VAR
  
  // Calculate the average of three values
  CalculateAverage := (Value1 + Value2 + Value3) / 3.0;
  
END_FUNCTION
``` 