# Linear algebra

## Eye
Gets identity matrix.
```
VAR_IN_OUT
	eyeN:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Eye(eye:= eyeN);
END_PROGRAM
```

## isValueNegligible
Evaluates whether the quantity is negligible.
```
VAR_INPUT
    omgtheta:ARRAY [1..3] OF REAL;
VAR_OUTPUT
	judge:INT;
END_VAR

PROGRAM
    isValueNegligible(nearArray:=omgtheta);
    isValueNegligible.judge=1
END_PROGRAM
```

## MatMul
Matrix multiplication.
```
VAR_INPUT
    matrixTrans:ARRAY [1..GVL.pInv_dim2,1..GVL.pInv_dim1] OF REAL;
    matrix:ARRAY [1..GVL.pInv_dim1,1..GVL.pInv_dim2] OF REAL;
END_VAR
VAR_OUTPUT
    matSquareSize2:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    MatMul(mat1:= matrixTrans, mat2:= matrix, 
        MatResult:= matSquareSize2);
END_PROGRAM
```

## Mat_byScalar
Matrix multiplication by a scalar.
```
VAR_INPUT
    Rot_temp:ARRAY [1..3,1..3] OF REAL;
    temp_scalar:REAL;
END_VAR
VAR_OUTPUT
    so3mat:ARRAY [1..3,1..3] OF REAL;
END_VAR

PROGRAM
	Mat_byScalar(Matrix:=Rot_temp, scalar:= temp_scalar, 
			MatrixByScalar:= so3mat);
END_PROGRAM
```

## norm
Computes the norm of a matrix.
```
VAR_INPUT
    expc3:ARRAY [*] OF REAL;//vector
END_VAR
VAR_OUTPUT
    theta:REAL;
END_VAR

PROGRAM
    norm(vector:=expc3,
            normValue=>theta);
END_PROGRAM
```

## Trace
Trace of a matrix.
```
VAR_INPUT
    R_mat:ARRAY[1..3,1..3] OF REAL;
END_VAR
VAR_OUTPUT
    trace_R:REAL;
END_VAR

PROGRAM
	Trace(Matrix:= R_mat,
	 trace=> trace_R);
END_PROGRAM
```
