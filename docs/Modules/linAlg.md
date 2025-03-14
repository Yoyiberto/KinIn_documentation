# Linear algebra

## Eye
Gets identity matrix.
```
VAR_IN_OUT
    //inputs a blank matrix
	eyeN:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    //modifies the input matrix to make it an eye matrix of N size
    Eye(eye:= eyeN);
END_PROGRAM
```

Example:
```
VAR
    Eye:Eye;
    eye_1:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    Eye(eye:= eye_1);
END_PROGRAM
```

OUTPUT:
```
eye_1 = [1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1];
```

## isValueNegligible
Evaluates whether the quantity is negligible.
```
VAR_INPUT
    omgtheta:ARRAY [1..3] OF REAL;//I suppose 3vectorEND_VAR
VAR_OUTPUT
	judge:INT;
END_VAR

PROGRAM
    isValueNegligible(nearArray:=omgtheta);
    isValueNegligible.judge=1
END_PROGRAM
```

Example:
```
VAR
    isValueNegligible:isValueNegligible;
    nearArray:ARRAY [1..3] OF REAL:=
        [0.00001,0.00002,0.00003];
    judge:INT;
END_VAR

PROGRAM
    isValueNegligible(nearArray:= nearArray,
			 judge=>judge );
END_PROGRAM
```

OUTPUT:
```
XXXXX
```
## MatMul
Matrix multiplication.
```
VAR_INPUT
    matrixTrans:ARRAY [1..GVL.pInv_dim2,1..GVL.pInv_dim1] OF REAL;//transpose matrix
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
Example:
```
VAR
    MatMul:MatMul;
    mat1:ARRAY [1..4,1..4] OF REAL:=
        [11,	0,	0,	2.8498,
        0,	22,	0,	0.5829,
        0,	0,	33,	-1.1225,
        0,	0,	0,	1];	;
    mat2:ARRAY [1..4,1..4] OF REAL:=	
        [11,	0,	0,	14,
        0,	22,	0,	24,
        0,	0,	33,	34,
        0,	0,	0,	1];	;
    MatResult:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    MatMul(mat1:=mat1 , mat2:=mat2,
            MatResult:=MatResult );
END_PROGRAM
```

OUTPUT:
```
XXXXXXX
eye_1 = [1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1];
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

Example:
```
VAR
    Mat_byScalar:Mat_byScalar;
    scalar:REAL;
    Matrix:ARRAY [1..4,1..4] OF REAL;
    MatrixByScalar:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    Mat_byScalar(scalar:=scalar , Matrix:=Matrix ,
            MatrixByScalar:= MatrixByScalar);
END_PROGRAM
```

OUTPUT:
```
eye_1 = [1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1];
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

Example:
```
VAR
    norm:norm;
    vector:ARRAY [1..4] OF REAL:=
            [1,2,3,4];
    normValue:REAL;
END_VAR

PROGRAM
    norm(vector:=vector , 
        normValue=>normValue );
END_PROGRAM
```

OUTPUT:
```
eye_1 = [1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1];
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

Example:
```
VAR
   Trace:Trace;
    Matrix_1:ARRAY [1..4,1..4] OF REAL:=
        [11,	0,	0,	2.8498,
        0,	22,	0,	0.5829,
        0,	0,	33,	-1.1225,
        0,	0,	0,	1];
    trace_1:REAL;
END_VAR

PROGRAM
    Trace(Matrix:=Matrix_1 ,
        trace=>trace_1 );
END_PROGRAM
```

OUTPUT:
```
eye_1 = [1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1];
```