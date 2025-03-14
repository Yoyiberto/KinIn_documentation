```
VAR_INPUT
	Transform4x4:ARRAY [1..4,1..4] OF REAL:=
	[8.1500,    9.1300,    2.7800,    9.6500,
    9.0600,    6.3200,    5.4700,    1.5800,
    1.2700,    0.9800,    9.5800,    9.7100,
	0,			0,			0,			1];
END_VAR
VAR_OUTPUT
	AdT:ARRAY [1..6,1..6] OF REAL;//6x6 matrix
END_VAR

PROGRAM PLC_PRG

(*==== AdjointTransform ===*)
AdjointTransform(Transform4x4:=Transform4x4 ,
			 AdT=>AdT );

END_PROGRAM

```
```
AdT=[8.15,	9.13,	2.78,	0,	0,	0,
	9.06,	6.32,	5.47,	0,	0,	0,
	1.27,	0.98,	9.58,	0,	0,	0,
	-85.966,	-59.8188,	-37.9772949,	8.15,	9.13,	2.78,
	66.881,	79.1953,	-65.4532,	9.06,	6.32,	5.47,
	74.552,	46.5626,	48.3930969,	1.27,	0.98,	9.58];
```