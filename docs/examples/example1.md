```
PROGRAM PLC_PRG
VAR
getFwdKinematics_Body:getFwdKinematics_Body;
M :ARRAY [1..4,1..4] OF REAL:= 
[1,	0,	0,	2849.8,
0,	1,	0,	582.9,
0,	0,	1,	-1122.5,
0,	0,	0,	1];
T_FK:ARRAY [1..4,1..4] OF REAL;
thetalist_FK:ARRAY [1..GVL.nJoints] OF REAL:=
[15*3.1415/180,
15*3.1415/180,
0,
0,
0];

eomg:REAL := 0.1;
ev:REAL := 0.1;
nIterationsIK:DINT:=20
thetalist:ARRAY [1..GVL.nJoints] OF REAL;
q_IKsuccess:BOOL;
s_IK_message:STRING;
Blist :ARRAY [1..6,1..GVL.nJoints]OF REAL:= [
0.00000000E+00,  0.00000000E+00, -3.20510345E-09,  1.00000000E+00,0.00000000E+00,  
0.00000000E+00,  1.00000000E+00, -1.00000000E+00, -3.20510345E-09,1.00000000E+00,
1.00000000E+00, -3.20510345E-09,  3.20510345E-09,  1.02726882E-17,-3.20510345E-09, 
-5.82899996E+02, -1.12250000E+03,  1.14700000E+03,  3.67625366E-06,-8.82000000E+02, 
2.84980000E+03, -8.42878107E-06, -2.98395132E-06,  1.14700000E+03,-3.62176690E-07, 
0.00000000E+00, -2.62980000E+03,  2.16000000E+02,  5.82899997E+02,-1.13000000E+02];

END_VAR

getFwdKinematics_Body(M:=M , Blist:=Blist , thetalist:=thetalist_FK , T=> T_FK);

INV_KINEMATICS(
	M:= M, 
	T:= T_FK, 
	eomg:= eomg, 
	ev:= ev, 
	nIterationsIK:= nIterationsIK, 
	Blist:= Blist, 
	thetalist=> thetalist, 
	q_IKsuccess=> q_IKsuccess, 
	s_IK_message=> s_IK_message );

END_PROGRAM

```
