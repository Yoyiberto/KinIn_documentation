The MATLAB directory provides all files required for the demonstration.

To replicate the mechanism's positions A and B as presented in the paper, execute 'paper_examples.m'. This script generates 'robot_PositionA.png' and 'robot_PositionB.png'. These figures can also be viewed interactively within the MATLAB environment.

For customized position testing, utilize 'plot_robot.m'. Modify the following code segment to specify the desired configuration:

```matlab
conf = [10*pi/180,15*pi/180,0.500,20*pi/180,25*pi/180,0];

```
This will produce 'robot_plot.png', which can also be interactively visualized in MATLAB.