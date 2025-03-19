This example is included in the project's PLC_PRG.
```
VAR
    Blist :ARRAY [1..6,1..GVL.nJoints]OF REAL:= [
        0.00000000E+00,  0.00000000E+00, -3.20510345E-09,  1.00000000E+00,   0.00000000E+00, 
        0.00000000e+00,  1.00000000e+00, -1.00000000e+00, -3.20510345e-09,   1.00000000e+00, 
        1.00000000e+00, -3.20510345e-09,  3.20510345e-09,  1.02726882e-17,  -3.20510345e-09,  
        -5.82899996e-01, -1.12250000e+00,  1.14700000e+00,  3.67625366e-09,  -8.82000000e-01, 
        2.84980000e+00, -8.42878107e-09, -2.98395132e-09,  1.14700000e+00,  -3.62176690e-10,  
        0.00000000E+00, -2.62980000E+00,  2.16000000E-01,  5.82899997E-01,  -1.13000000E-01];
	
	M :ARRAY [1..4,1..4] OF REAL:= 
		[1,	0,	0,	2.8498,
		0,	1,	0,	0.5829,
		0,	0,	1,	-1.1225,
		0,	0,	0,	1];	

    eomg:REAL := 0.01;
    ev:REAL := 0.01;
    success_A:BOOL;
    success_B:BOOL;

    getInvKinematics_Body_B:getInvKinematics_Body;
    getInvKinematics_Body_A:getInvKinematics_Body;
    thetalist0:ARRAY [1..GVL.nJoints] OF REAL:=
            [0*3.1415/180,
            -10*3.1415/180,
            0,
            10*3.1415/180,
            10*3.1415/180];
    A:ARRAY [1..4,1..4] OF REAL:=
        [0.9659, 0.0670, 0.2500, 2.5188,
        -0.0000, 0.9659, -0.2588, 0.8599,
        -0.2588, 0.2500, 0.9330, -1.5814,
        0, 0, 0, 1];
    B:ARRAY [1..4,1..4] OF REAL:=
        [0.9995, -0.0302, 0.0026, 2.8327,
        0.0302, 0.9848, -0.1710, 0.7743,
        0.0026, 0.1710, 0.9853, -0.5649,
        0, 0, 0, 1];

    thetalist0_A:ARRAY [1..GVL.nJoints] OF REAL:=
        [0,0,0,0,0];
    thetalist0_B :ARRAY [1..GVL.nJoints] OF REAL:=
        [0,0,0,0,0];

    thetalist_IK_A:ARRAY [1..GVL.nJoints] OF REAL;
    thetalist_IK_B:ARRAY [1..GVL.nJoints] OF REAL;

    getFwdKinematics_Body_A:getFwdKinematics_Body;
    getFwdKinematics_Body_B:getFwdKinematics_Body;

    T_FK_A:ARRAY [1..4,1..4] OF REAL;
    T_FK_B:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM PLC_PRG

    (*===== Examples A and B examples from the paper =====*)
    (*========== Position A ========*)
    getInvKinematics_Body_A(
        M:= M, 
        T:= A, 
        eomg:= eomg, 
        ev:= ev, 
        Blist:= Blist, 
        thetalist0:= thetalist0_A, 
        thetalist:= thetalist_IK_A, 
        success=> success_A );
        
    getFwdKinematics_Body_A(
        M:= M ,
        Blist:= Blist ,
        thetalist:= thetalist_IK_A ,
        T=> T_FK_A);
        
    (*========== Position B ========*)
    getInvKinematics_Body_B(
        M:= M, 
        T:= B, 
        eomg:= eomg, 
        ev:= ev, 
        Blist:= Blist, 
        thetalist0:= thetalist0_B, 
        thetalist:= thetalist_IK_B, 
        success=> success_B);
        
    getFwdKinematics_Body_B(
        M:= M ,
        Blist:= Blist ,
        thetalist:= thetalist_IK_B ,
        T=> T_FK_B);
END_PROGRAM

```


```
thetalist_IK_A=[-0.0000, 0.2618, -0.0001, 0.2618, -0.0001];
thetalist_IK_B=[0.0004, -0.1766, -0.0040, 0.1712, 0.1735];
```