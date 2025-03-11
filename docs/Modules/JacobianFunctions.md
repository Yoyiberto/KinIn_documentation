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
"""Computes the body Jacobian for an open chain robot

    :param Blist: The joint screw axes in the end-effector frame when the
                  manipulator is at the home position, in the format of a
                  matrix with axes as the columns
    :param thetalist: A list of joint coordinates
    :return: The body Jacobian corresponding to the inputs (6xn real
             numbers)

    Example Input:
        Blist = np.array([[0, 0, 1,   0, 0.2, 0.2],
                          [1, 0, 0,   2,   0,   3],
                          [0, 1, 0,   0,   2,   1],
                          [1, 0, 0, 0.2, 0.3, 0.4]]).T
        thetalist = np.array([0.2, 1.1, 0.1, 1.2])
    Output:
        np.array([[-0.04528405, 0.99500417,           0,   1]
                  [ 0.74359313, 0.09304865,  0.36235775,   0]
                  [-0.66709716, 0.03617541, -0.93203909,   0]
                  [ 2.32586047,    1.66809,  0.56410831, 0.2]
                  [-1.44321167, 2.94561275,  1.43306521, 0.3]
                  [-2.06639565, 1.82881722, -1.58868628, 0.4]])
    """
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
"""Converts a 3-vector of exponential coordinates for rotation into
    axis-angle form

    :param expc3: A 3-vector of exponential coordinates for rotation
    :return omghat: A unit rotation axis
    :return theta: The corresponding rotation angle

    Example Input:
        expc3 = np.array([1, 2, 3])
    Output:
        (np.array([0.26726124, 0.53452248, 0.80178373]), 3.7416573867739413)
    """
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
"""Computes the matrix logarithm of a homogeneous transformation matrix

    :param R: A matrix in SE3
    :return: The matrix logarithm of R

    Example Input:
        T = np.array([[1, 0,  0, 0],
                      [0, 0, -1, 0],
                      [0, 1,  0, 3],
                      [0, 0,  0, 1]])
    Output:
        np.array([[0,          0,           0,           0]
                  [0,          0, -1.57079633,  2.35619449]
                  [0, 1.57079633,           0,  2.35619449]
                  [0,          0,           0,           0]])
    """
## Exp_so3_fromRot
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
Extracts the exponential coordinates from a given rotation matrix
"""Computes the matrix logarithm of a rotation matrix

    :param R: A 3x3 rotation matrix
    :return: The matrix logarithm of R

    Example Input:
        R = np.array([[0, 0, 1],
                      [1, 0, 0],
                      [0, 1, 0]])
    Output:
        np.array([[          0, -1.20919958,  1.20919958],
                  [ 1.20919958,           0, -1.20919958],
                  [-1.20919958,  1.20919958,           0]])
    """
## fastInverseTransform
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
Inverts a Transformation matrix using its properties for efficiency avoiding normal matrix inversion.
"""Inverts a homogeneous transformation matrix

    :param T: A homogeneous transformation matrix
    :return: The inverse of T
    Uses the structure of transformation matrices to avoid taking a matrix
    inverse, for efficiency.

    Example input:
        T = np.array([[1, 0,  0, 0],
                      [0, 0, -1, 0],
                      [0, 1,  0, 3],
                      [0, 0,  0, 1]])
    Output:
        np.array([[1,  0, 0,  0],
                  [0,  0, 1, -3],
                  [0, -1, 0,  0],
                  [0,  0, 0,  1]])
    """
## getFwdKinematics_Body
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
Computes the forward kinematics using the exponential form. It needs the M, Blist and thetalist matrices.
FKinBody
"""Computes forward kinematics in the body frame for an open chain robot

    :param M: The home configuration (position and orientation) of the end-
              effector
    :param Blist: The joint screw axes in the end-effector frame when the
                  manipulator is at the home position, in the format of a
                  matrix with axes as the columns
    :param thetalist: A list of joint coordinates
    :return: A homogeneous transformation matrix representing the end-
             effector frame when the joints are at the specified coordinates
             (i.t.o Body Frame)

    Example Input:
        M = np.array([[-1, 0,  0, 0],
                      [ 0, 1,  0, 6],
                      [ 0, 0, -1, 2],
                      [ 0, 0,  0, 1]])
        Blist = np.array([[0, 0, -1, 2, 0,   0],
                          [0, 0,  0, 0, 1,   0],
                          [0, 0,  1, 0, 0, 0.1]]).T
        thetalist = np.array([np.pi / 2.0, 3, np.pi])
    Output:
        np.array([[0, 1,  0,         -5],
                  [1, 0,  0,          4],
                  [0, 0, -1, 1.68584073],
                  [0, 0,  0,          1]])
    """
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
MatrixExp3
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
"""Computes the matrix exponential of a matrix in so(3)

    :param so3mat: A 3x3 skew-symmetric matrix
    :return: The matrix exponential of so3mat

    Example Input:
        so3mat = np.array([[ 0, -3,  2],
                           [ 3,  0, -1],
                           [-2,  1,  0]])
    Output:
        np.array([[-0.69492056,  0.71352099,  0.08929286],
                  [-0.19200697, -0.30378504,  0.93319235],
                  [ 0.69297817,  0.6313497 ,  0.34810748]])
    """
## se3ToSpatialVel
Gets the spatial velocity from a se3 matrix.
se3ToVec
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
""" Converts an se3 matrix into a spatial velocity vector

    :param se3mat: A 4x4 matrix in se3
    :return: The spatial velocity 6-vector corresponding to se3mat

    Example Input:
        se3mat = np.array([[ 0, -3,  2, 4],
                           [ 3,  0, -1, 5],
                           [-2,  1,  0, 6],
                           [ 0,  0,  0, 0]])
    Output:
        np.array([1, 2, 3, 4, 5, 6])
    """
## spatialVelToSE3Matrix
Spatial velocity to an SE3 matrix
VecTose3
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
"""Converts a spatial velocity vector into a 4x4 matrix in se3

    :param V: A 6-vector representing a spatial velocity
    :return: The 4x4 se3 representation of V

    Example Input:
        V = np.array([1, 2, 3, 4, 5, 6])
    Output:
        np.array([[ 0, -3,  2, 4],
                  [ 3,  0, -1, 5],
                  [-2,  1,  0, 6],
                  [ 0,  0,  0, 0]])
    """
## TransSE3_fromExp_se3
Transformation matrix in SE3 from exponential from in s3.
MatrixExp6
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
"""Computes the matrix exponential of an se3 representation of
    exponential coordinates

    :param se3mat: A matrix in se3
    :return: The matrix exponential of se3mat

    Example Input:
        se3mat = np.array([[0,          0,           0,          0],
                           [0,          0, -1.57079632, 2.35619449],
                           [0, 1.57079632,           0, 2.35619449],
                           [0,          0,           0,          0]])
    Output:
        np.array([[1.0, 0.0,  0.0, 0.0],
                  [0.0, 0.0, -1.0, 0.0],
                  [0.0, 1.0,  0.0, 3.0],
                  [  0,   0,    0,   1]])
    """
## TransSE3_ToRotAndPos
Rotation and Position from a Transformation matrix in SE3 form.
TransToRp
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
"""Converts a homogeneous transformation matrix into a rotation matrix
    and position vector

    :param T: A homogeneous transformation matrix
    :return R: The corresponding rotation matrix,
    :return p: The corresponding position vector.

    Example Input:
        T = np.array([[1, 0,  0, 0],
                      [0, 0, -1, 0],
                      [0, 1,  0, 3],
                      [0, 0,  0, 1]])
    Output:
        (np.array([[1, 0,  0],
                   [0, 0, -1],
                   [0, 1,  0]]),
         np.array([0, 0, 3]))
    """ 
