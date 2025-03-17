## Inv
Inverse matrix.
```
VAR_INPUT
    matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR
VAR_OUTPUT
    InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    Inv(matSquare:= matSquareSize2, 
	    InverseMatrix=> InverseMatrix);
END_PROGRAM
```

## LuDecomposition
Lu Decomposition in L U terms using the doolittle's method.
```
VAR_INPUT
	matSquare:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR
VAR_OUTPUT
    L:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
	U:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    LuDecomposition(A:=matSquare , 
            L:= L, U:= U);
END_PROGRAM
```

## LuInverse
Lu inverse from L U terms using forward and backwards substitutions.
```
VAR_INPUT
	//create following matrices all with same size
	L:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
	U:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
	d:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
	eyeN:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR
VAR_OUTPUT
	InverseMatrix:ARRAY [1..GVL.nInvSize,1..GVL.nInvSize] OF REAL;
END_VAR

PROGRAM
    LuInverse(
        L:= L, 
        u:= U, 
        a:= InverseMatrix, 
        d:= d, 
        eyeN:= eyeN);
END_PROGRAM
```

## pInv
Moore – Penrose pseudo inverse matrix
```
VAR_INPUT
	Jb:ARRAY [1..GVL.pInv_dim1,1..GVL.pInv_dim2] OF REAL;
VAR_OUTPUT
	pInvMatrix:ARRAY [1..GVL.pInv_dim2,1..GVL.pInv_dim1] OF REAL;
END_VAR

PROGRAM
    pInv(matrix:=Jb , 
        pInvMatrix=>pInvMatrix );
END_PROGRAM
	
```
