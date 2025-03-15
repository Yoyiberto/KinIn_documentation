## AdjointTransform

```
VAR
    AdjointTransform:AdjointTransform;
	Transform4x4:ARRAY [1..4,1..4] OF REAL:=
					[1, 0,  0, 0,
                      0, 0, -1, 0,
                      0, 1,  0, 3,
                      0, 0,  0, 1];
	AdT:ARRAY [1..6,1..6] OF REAL;//6x6 matrix
END_VAR

PROGRAM
    AdjointTransform(Transform4x4:=Transform4x4 ,
				 AdT=>AdT );
END_PROGRAM
```

OUTPUT:
```
    [1, 2,  3, 0, 0,  0,
    0, 4, -1, 0, 0,  0,
    0, 1,  5, 0, 0,  0,
    0, -12,  3, 1, 2,  3,
    3, 2,  -11, 0, 4, -1,
    0, 16,  -4, 0, 1,  5]

```

## angVelToSkewSymMatrix

```
VAR
    angVelToSkewSymMatrix:angVelToSkewSymMatrix;
	omg:ARRAY[1..3] OF REAL:= [11, 22, 33];
	so3mat:ARRAY[1..3,1..3] OF REAL;
END_VAR

PROGRAM
    angVelToSkewSymMatrix(omg:=omg ,
					 so3mat=>so3mat );
END_PROGRAM
```

OUTPUT:
```
   [ 0, -33,  22,
    33,  0, -11,
    -22,  11,  0]

```

## BodyJacobian

```
VAR
    BodyJacobian:BodyJacobian;
	Blist:ARRAY [1..4,1..6] OF REAL:=
			[1, 1, 0,   0, 1.3, 0.6,
			0, 1, 0,   4,   0,   3,
			1, 0, 1,   0,   2.1,   1.2,
			0, 0, 0, 0.2, 0.5, 0.9];
	thetalist:ARRAY [1..4] OF REAL:=
			[0.11, 3.5, 6.1, 2.2];
	Jb:ARRAY [1..6,1..6] OF REAL;//6xnt nt: number of theta
END_VAR

PROGRAM
    BodyJacobian(Blist:=Blist , thetalist:=thetalist ,
			 Jb:=Jb );
END_PROGRAM
```

OUTPUT:
```
Jb = [-0.821220756, -0.649771452, -0.584917, 0, 1.3, 0.6,
        -0.06205398, 1.165431, 0, 4, 0, 3,
        1.149672, 0.468580455, -0.8110931, 0, 2.1, 1.2,
        0.387096524, 0.6226631, -0.76039207, 0.2, 0.5, 0.9,
        0.5044941, 3.51398349, 6.12924576, 0, 0, 0,
        -0.205031931, -0.407009035, -1.054421, 0, 0, 0];
```

## expToRotAxisAndAngle

```
VAR
    expToRotAxisAndAngle:expToRotAxisAndAngle;
	expc3:ARRAY [1..3] OF REAL:=
			[3.7, 2.2, 5.1];
	omghat:ARRAY [1..3] OF REAL;;//scalar
	theta:REAL;
END_VAR

PROGRAM
    expToRotAxisAndAngle(expc3:=expc3 , 
					omghat=>omghat , theta=>theta );
END_PROGRAM
```

OUTPUT:
```
omghat= [0.5544043, 0.3296458, 0.764178932]
theta= 6.67382956;
```

## Exp_se3_fromTrans

```
VAR
    Exp_se3_fromTrans:Exp_se3_fromTrans;
	T:ARRAY[1..4,1..4] OF REAL:=
					[0, 0,  1, 2.1,
                      0, 1, 0, 3.5,
                      1, 0,  0, 5.2,
                      0, 0,  0, 1];

	expmat:ARRAY[1..4,1..4] OF REAL;
END_VAR

PROGRAM
    Exp_se3_fromTrans(T:=T , expmat=>expmat );
END_PROGRAM
```

OUTPUT:
```
expmat = [0, -0.0303055476, 0, 2.84398055,
        0.0303055476, 0, -0.17187646, 0.6808588,
        0, 0.17187646, 0, -0.6288096,
        0, 0, 0, 0];
```

## Exp_so3_fromRot

```
VAR
	Exp_so3_fromRot:Exp_so3_fromRot;
	Rot:ARRAY [1..3,1..3] OF REAL:=
			[0, 0, 1,
			1, 0, 0,
			0, 1, 0];

	so3mat_2:ARRAY [1..3,1..3] OF REAL;
END_VAR

PROGRAM
    Exp_so3_fromRot(Rot:=Rot , so3mat=>so3mat_2 );
END_PROGRAM
```

OUTPUT:
```
so3mat_2 = [0, -1.20919955, 1.20919955,
        1.20919955, 1, -1.20919955, 
        -1.20919955, 1.20919955, 0];
```

## fastInverseTransform

```
VAR
    fastInverseTransform:fastInverseTransform;
	T_2:ARRAY[1..4,1..4] OF REAL:=
					[1, 0,  0, 0,
                      0, 0, -1, 0,
                      0, 1,  0, 3,
                      0, 0,  0, 1];
	invT:ARRAY[1..4,1..4] OF REAL;
END_VAR

PROGRAM
    fastInverseTransform(T:=T_2 , invT=>invT );
END_PROGRAM
```

OUTPUT:
```
invT = 
        [1,  0, 0,  0,
                  0,  0, 1, -3,
                  0, -1, 0,  0,
                  0,  0, 0,  1];

```

## getFwdKinematics_Body

```
VAR
    getFwdKinematics_Body:getFwdKinematics_Body;
	M:ARRAY [1..4,1..4] OF REAL:= 
	[1,	0,	0,	2.8498,
	0,	1,	0,	0.5829,
	0,	0,	1,	-1.1225,
	0,	0,	0,	1];
	Blist_FK :ARRAY [1..6,1..GVL.nJoints]OF REAL:= [(*it used mm instead of m*)
	0.00000000E+00,  0.00000000E+00, -3.20510345E-09,  1.00000000E+00,   0.00000000E+00, 
	0.00000000e+00,  1.00000000e+00, -1.00000000e+00, -3.20510345e-09,   1.00000000e+00, 
	 1.00000000e+00, -3.20510345e-09,  3.20510345e-09,  1.02726882e-17,  -3.20510345e-09,  
	-5.82899996e-01, -1.12250000e+00,  1.14700000e+00,  3.67625366e-09,  -8.82000000e-01, 
	 2.84980000e+00, -8.42878107e-09, -2.98395132e-09,  1.14700000e+00,  -3.62176690e-10,  
	0.00000000E+00, -2.62980000E+00,  2.16000000E-01,  5.82899997E-01,  -1.13000000E-01];
	
	thetalist_FK:ARRAY [1..GVL.nJoints] OF REAL:=
		[0*3.1415/180,
		-10*3.1415/180,
		0,
		10*3.1415/180,
		10*3.1415/180];
	T_FK:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    getFwdKinematics_Body(M:=M , Blist:=Blist_FK , thetalist:=thetalist_FK , T=>T_FK );

END_PROGRAM
```

OUTPUT:
```
T_FK = [0.999541938, -0.03015193, 0.00259780884, 2.83271,
        0.03015193, 0.9848086, -0.171005234, 0.774294138,
        0.00259780884, 0.171005234, 0.9852666, -0.56488955,
        0, 0, 0, 1];
```

## getInvKinematics_Body

```
VAR
    getInvKinematics_Body:getInvKinematics_Body;
	M_IK:ARRAY[1..4,1..4] OF REAL:=
					[-1, 0,  0, 0,
                       0, 1,  0, 6,
                       0, 0, -1, 2,
                       0, 0,  0, 1];
	T_IK:ARRAY[1..4,1..4] OF REAL;
	eomg:REAL;
	ev:REAL;
	Blist_IK:ARRAY [1..6,1..GVL.nJoints]OF REAL:= [(*it used mm instead of m*)
	0.00000000E+00,  0.00000000E+00, -3.20510345E-09,  1.00000000E+00,   0.00000000E+00, 
	0.00000000e+00,  1.00000000e+00, -1.00000000e+00, -3.20510345e-09,   1.00000000e+00, 
	 1.00000000e+00, -3.20510345e-09,  3.20510345e-09,  1.02726882e-17,  -3.20510345e-09,  
	-5.82899996e-01, -1.12250000e+00,  1.14700000e+00,  3.67625366e-09,  -8.82000000e-01, 
	 2.84980000e+00, -8.42878107e-09, -2.98395132e-09,  1.14700000e+00,  -3.62176690e-10,  
	0.00000000E+00, -2.62980000E+00,  2.16000000E-01,  5.82899997E-01,  -1.13000000E-01];
	thetalist0:ARRAY[1..GVL.nJoints] OF REAL;
	thetalist_4:ARRAY [1..GVL.nJoints] OF REAL;
	success:BOOL;
END_VAR

PROGRAM
    getInvKinematics_Body(
	M:=M_IK , 
	T:=T_IK, 
	eomg:=eomg , 
	ev:=ev , 
	Blist:=Blist_IK , 
	thetalist0:=thetalist0 , 
	thetalist:=thetalist_4 , 
	success=>success );
END_PROGRAM
```

OUTPUT:
```
XXXXXXXXXXXXX
thetalist_4  = [1, 0, 0, 0,X];
success = TRUE;
```

## RotSO3_fromExpso3

```
VAR
    RotSO3_fromExpso3:RotSO3_fromExpso3;
	so3mat_3:ARRAY [1..3,1..3] OF REAL:=
							[0, -3,  2,
                            3,  0, -1,
                           -2,  1,  0];

	R_Matrix:ARRAY [1..3,1..3] OF REAL;//SO3x3
END_VAR

PROGRAM
    RotSO3_fromExpso3(so3mat:=so3mat_3 , R_Matrix=>R_Matrix );
END_PROGRAM
```

OUTPUT:
```
R_Matrix = [-0.69492056,  0.71352099,  0.08929286,
            -0.19200697, -0.30378504,  0.93319235,
            0.69297817,  0.6313497 ,  0.34810748];
```

## se3ToSpatialVel

```
VAR
    se3ToSpatialVel:se3ToSpatialVel;
	se3mat:ARRAY [1..4,1..4] OF REAL:=
					[-1, 0,  0, 0,
                       0, 1,  0, 6,
                       0, 0, -1, 2,
                       0, 0,  0, 1];
	V:ARRAY [1..6] OF REAL;
END_VAR

PROGRAM
    se3ToSpatialVel(se3mat:=se3mat , V=>V );
END_PROGRAM
```

OUTPUT:
```
eye_1 = [0, 0, 0, 0, 6, 2];
```

## so3ToAngularVelocity

```
VAR
    so3ToAngularVelocity:so3ToAngularVelocity;
	so3mat_4:ARRAY [1..3,1..3] OF REAL :=
					[ 0, -3,  2,
                            3,  0, -1,
                           -2,  1, 6];

	omg_4:ARRAY [1..3] OF REAL;//SO3x3
END_VAR

PROGRAM
    so3ToAngularVelocity(so3mat:=so3mat_4 , omg=>omg_4 );
END_PROGRAM
```

OUTPUT:
```
omg_4 = [1, 2, 3];
```

## spatialVelToSE3Matrix

```
VAR
    spatialVelToSE3Matrix:spatialVelToSE3Matrix;
	V_1:ARRAY [1..6] OF REAL:=
				[1, 2, 3, 4, 5, 6];
	se3mat_1:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    spatialVelToSE3Matrix(V:=V_1 , se3mat=>se3mat_1 );
END_PROGRAM
```

OUTPUT:
```
se3mat_1 = [0, -3, 2, 4,
        3, 0, -1, 5,
        -2, 1, 0, 6,
        0, 0, 0, 0];
```

## TransSE3_fromExp_se3

```
VAR
    TransSE3_fromExp_se3:TransSE3_fromExp_se3;
	se3mat_3:ARRAY [1..4,1..4] OF REAL:=
				[0,          0,           0,          0,
                           0,          0, -1.57079632, 2.35619449,
                           0, 1.57079632,           0, 2.35619449,
                           0,          0,           0,          0];
	T_3:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    TransSE3_fromExp_se3(se3mat:=se3mat_3 , T=>T_3 );
END_PROGRAM
```

OUTPUT:
```
T_3 = [1.0, 0.0,  0.0, 0.0,
        0.0, 0.0, -1.0, 0.0,
        0.0, 1.0,  0.0, 3.0,
        0,   0,    0,   1];

```

## TransSE3_ToRotAndPos

```
VAR
    TransSE3_ToRotAndPos:TransSE3_ToRotAndPos;
	T_4:ARRAY[1..4,1..4] OF REAL:=
				[1, 0,  0, 0,
                      0, 0, -1, 0,
                      0, 1,  0, 3,
                      0, 0,  0, 1];

	RotMat:ARRAY[1..3,1..3] OF REAL;//rotation matrix
	p:ARRAY[1..3] OF REAL;//position array
END_VAR

PROGRAM
    TransSE3_ToRotAndPos(T:=T_4 , 
                RotMat=>RotMat , p=>p );
END_PROGRAM
```

OUTPUT:
```
RotMat = [1, 0,  0,
        0, 0, -1],
        0, 1,  0];

p = [0, 0, 3];
```