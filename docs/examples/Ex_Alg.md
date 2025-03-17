# Linear algebra

## Eye
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
```
VAR
    isValueNegligible:isValueNegligible;
    nearArray:ARRAY [1..3] OF REAL:=
	    [0.00000001,0.00000002,0.00000003];
    judge:INT;
END_VAR

PROGRAM
    isValueNegligible(nearArray:= nearArray,
			 judge=>judge );
END_PROGRAM
```

OUTPUT:
```
judge=1;
```
## MatMul
```
VAR
    MatMul:MatMul;
    mat1:ARRAY [1..4,1..4] OF REAL:=
        [11,	2,	3,	14,
        2,	22,	3,	24,
        1,	6,	33,	34,
        8,	5,	9,	44];
    mat2:ARRAY [1..4,1..4] OF REAL:=	
        [11,	0,	5,	14,
        2,	22,	0,	24,
        1,	0,	33,	34,
        2,	0,	4,	1];	
    MatResult:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    MatMul(mat1:=mat1 , mat2:=mat2,
            MatResult:=MatResult );
END_PROGRAM
```

OUTPUT:
```
MatResult = 
        [156,          44,         210,         318,
         117,         484,         205,         682,
         124,         132,        1230,        1314,
         195,         110,         513,         582];
```

## Mat_byScalar
```
VAR
    Mat_byScalar:Mat_byScalar;
    scalar:REAL:=3;
    Matrix:ARRAY [1..4,1..4] OF REAL:=
        [11,	2,	3,	14,
        2,	22,	3,	24,
        1,	6,	33,	34,
        8,	5,	9,	44];
    MatrixByScalar:ARRAY [1..4,1..4] OF REAL;
END_VAR

PROGRAM
    Mat_byScalar(scalar:=scalar , Matrix:=Matrix ,
            MatrixByScalar:= MatrixByScalar);
END_PROGRAM
```

OUTPUT:
```
MatrixByScalar =     
    [33,     6,     9,    42,
     6,    66,     9,    72,
     3,    18,    99,   102,
    24,    15,    27,   132]
```

## norm
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
normValue = 5.48;
```

## Trace
```
VAR
   Trace:Trace;
    Matrix_1:ARRAY [1..4,1..4] OF REAL:=
        [11,	3,	2,	2,
        5,	7,	0,	9,
        7,	2,	33,	5,
        0,	5,	0,	1];
    trace_1:REAL;
END_VAR

PROGRAM
    Trace(Matrix:=Matrix_1 ,
        trace=>trace_1 );
END_PROGRAM
```

OUTPUT:
```
trace_1 = 52;
```