## AdjointTransform
Adjoint matrix form a transformation matrix.
```
VAR_INPUT
    T_product:ARRAY [1..4,1..4] OF REAL;
END_VAR
VAR_OUTPUT
    AdT:ARRAY [1..6,1..6] OF REAL;
END_VAR

PROGRAM
    AdjointTransform(Transform4x4:= T_product, 
                AdT=>AdT );
END_PROGRAM
```

## angVelToSkewSymMatrix
Skew symmetric matrix in so(3).
```
VAR_INPUT
    pi_omg:ARRAY [1..3] OF REAL;
END_VAR
VAR_OUTPUT
    so3mat:ARRAY [1..3,1..3] OF REAL;
END_VAR

PROGRAM
	angVelToSkewSymMatrix(omg:= pi_omg,
	 	so3mat=>so3mat );
END_PROGRAM
```

## BodyJacobian
Body Jacobian (6xn real numbers). From joint coordinates and the joint screw axes.
```
VAR_INPUT
	Blist:ARRAY[*,*] OF REAL;
	thetalist:ARRAY[*] OF REAL;//as output
END_VAR
VAR_OUTPUT
    Jb:ARRAY [1..GVL.pInv_dim1,1..GVL.pInv_dim2] OF REAL;	
END_VAR

PROGRAM
    BodyJacobian(Blist:=Blist , thetalist:=thetalist ,
                 Jb:=Jb );
END_PROGRAM
```

## expToRotAxisAndAngle
From matrix exponential to Rotation matrix and Angle.
```
VAR_INPUT
    omgtheta:ARRAY [1..3] OF REAL;//I suppose 3vector
END_VAR
VAR_OUTPUT
    omghat:ARRAY [1..3] OF REAL;
    theta:REAL;
END_VAR

PROGRAM
	expToRotAxisAndAngle(expc3:= omgtheta
		,omghat=> omghat, theta=> theta);//outs
END_PROGRAM
```

## Exp_se3_fromTrans
se(3) representation of exponential coordinates.
```
VAR_INPUT
    T:ARRAY[1..4,1..4] OF REAL;
END_VAR
VAR_OUTPUT
    expmat:ARRAY[1..4,1..4] OF REAL;
END_VAR

PROGRAM
    Exp_se3_fromTrans(T:= MatMul_out);
    Exp_se3_fromTrans.expmat
END_PROGRAM
```

## Exp_so3_fromRot
Extracts the exponential coordinates from a given rotation matrix
```
VAR_INPUT
    Rot:ARRAY [1..3,1..3] OF REAL;
END_VAR
VAR_OUTPUT
    so3mat:ARRAY [1..3,1..3] OF REAL;
END_VAR

PROGRAM
    Exp_so3_fromRot(Rot:= R_mat, 
        so3mat=> omgmat);
END_PROGRAM
```

## fastInverseTransform
Inverts a Transformation matrix using its properties for efficiency avoiding normal matrix inversion.
```
VAR_INPUT
	T:ARRAY[1..4,1..4] OF REAL;
END_VAR
VAR_OUTPUT
	invT:ARRAY[1..4,1..4] OF REAL;
END_VAR

PROGRAM
    fastInverseTransform(T:=getFwdKinematics_Body.T);
    fastInverseTransform.invT
END_PROGRAM
```

## getFwdKinematics_Body
Computes the forward kinematics using the exponential form. It needs the M, Blist and thetalist matrices.
```
VAR_INPUT
	M:ARRAY [1..4,1..4] OF REAL;
   	Blist:ARRAY [*,*] OF REAL;//6rows x njoints
	thetalist:ARRAY [*] OF REAL;//number of joints
END_VAR
VAR_OUTPUT
	T:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    getFwdKinematics_Body(M:=M , Blist:=Blist , thetalist:=thetalist_FK ,
                 T=> T_FK);
END_PROGRAM
```

## getInvKinematics_Body
Computes the inverse kinematics
```
VAR_INPUT
    M:ARRAY[1..4,1..4] OF REAL;
	T:ARRAY[1..4,1..4] OF REAL;
	eomg:REAL;
	ev:REAL;
    Blist:ARRAY[*,*] OF REAL;
END_VAR
VAR_OUTPUT
    thetalist:ARRAY[*] OF REAL;//as output
	success:BOOL;
END_VAR

PROGRAM
    getInvKinematics_Body(
		M:=M , 
		T:=T , 
		eomg:= eomg, 
		ev:= ev, 
		Blist:=Blist , 
		thetalist0:= thetalist0, 
		thetalist:=thetalist , 
		success=> success);	
END_PROGRAM
```

## RotSO3_fromExpso3
Rotation in SO3 from Exponential form in so3.
```
VAR_INPUT
	so3mat:ARRAY [1..3,1..3] OF REAL;//so3x3
END_VAR
VAR_OUTPUT
	R_Matrix:ARRAY [1..3,1..3] OF REAL;//SO3x3
END_VAR

PROGRAM
	RotSO3_fromExpso3(so3mat:= se3mat3x3,
				R_Matrix=> R_Matrix);
END_PROGRAM
```


## se3ToSpatialVel
Gets the spatial velocity from a se3 matrix.
```
VAR_INPUT
	se3mat:ARRAY [1..4,1..4] OF REAL;
END_VAR
VAR_OUTPUT
	V:ARRAY [1..6] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```


## so3ToAngularVelocity
Gets Angular velocity from a so3 matrix.
```
VAR_INPUT
    matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;//matrix with the second 
END_VAR
VAR_OUTPUT
    InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```


## spatialVelToSE3Matrix
Spatial velocity to an SE3 matrix

```
VAR_INPUT
    matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;//matrix with the second 
END_VAR
VAR_OUTPUT
    InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```

## TransSE3_fromExp_se3
Transformation matrix in SE3 from exponential from in s3.

```
VAR_INPUT
    matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;//matrix with the second 
END_VAR
VAR_OUTPUT
    InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```

## TransSE3_ToRotAndPos
Rotation and Position from a Transformation matrix in SE3 form.

```
VAR_INPUT
    matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;//matrix with the second 
END_VAR
VAR_OUTPUT
    InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```
