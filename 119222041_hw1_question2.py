#To find the joint angle velocities.
#Used the sympy library
#Found the equations by solving on paper
#This code is for mathematical use


from sympy import *
init_printing(use_unicode=True)
import shutilwhich


#Defined x,y,xot,ydot,theta_1,theta_2,theta_3,thetadot_1,thetadot_2,thetadot_3 as functions
x, y,t,xdot,ydot= symbols('x,y,t,xdot,ydot')
theta_1,theta_2,theta_3= symbols('theta_1,theta_2,theta_3')
l_1,l_2,l_3=symbols('l_1,l_2,l_3')
thetadot_1,thetasot_2,thetadot_3,phidot= symbols('thetadot_1,thetadot_2,thetadot_3,phidot')

x=Function('x')
y=Function('y')
xdot=Function('xdot')
ydot=Function('ydot')
theta_1=Function('theta_1')
theta_2=Function('theta_2')
theta_3=Function('theta_3')
thetadot_1=Function('thetadot_1')
thetadot_2=Function('thetadot_2')
thetadot_3=Function('thetadot_3')
phidot=Function('phidot')

#This is the position matrix
Position_Equation=Matrix([[l_1*cos(theta_1(t)),l_2*cos(theta_1(t)+theta_2(t)),l_3*cos(theta_1(t)+theta_2(t)+theta_3(t))], 
[l_1*sin(theta_1(t)),l_2*sin(theta_1(t)+theta_2(t)),l_3*sin(theta_1(t)+theta_2(t)+theta_3(t))], 
[theta_1(t),theta_2(t),theta_3(t)]])

#This the matrix to be inverted to find the the joint angle velocities from my calculations
Velocity_Equation=Matrix([[-l_1*(sin(theta_1(t)))-l_2*(sin(theta_1(t)+theta_2(t)))-l_3*(sin(theta_1(t)+theta_2(t)+theta_3(t))),
-l_2*(sin(theta_2(t)+theta_3(t)))-l_3*(sin(theta_1(t)+theta_2(t)+theta_3(t))),-l_3*(sin(theta_1(t)+theta_2(t)+theta_3(t)))],
[l_1*(cos(theta_1(t)))+l_2*(cos(theta_1(t)+theta_2(t)))+l_3*(cos(theta_1(t)+theta_2(t)+theta_3(t))),
l_2*(cos(theta_2(t)+theta_3(t)))+l_3*(cos(theta_1(t)+theta_2(t)+theta_3(t))),l_3*(cos(theta_1(t)+theta_2(t)+theta_3(t)))],
[1,1,1]])

#This is the velocity matrix of the end effector
Velocity_Matrix=Matrix([xdot(t),ydot(t),phidot(t)])

#Inverse of the velocity matrix
Inverse_Velocity_Equation=Velocity_Equation.inv()

#This equation gives the desired result
Joint_Velocity=Inverse_Velocity_Equation*Velocity_Matrix

#expr to reperesnt the final matrix.
#manipulations done to improve the output print

expr=(simplify(Joint_Velocity))
pprint(expr)

#This give a png file of the output
preview(expr, viewer='file', filename='output_final.png')
