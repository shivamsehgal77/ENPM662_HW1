#Enter angle value in radians
#Enter other values in metric

#using values 

from cmath import cos
import math
import matplotlib.pyplot as plt 

x_initial,y_initial,theta_initial=float(input("Enter initial value of x at O =")),float(input("Enter initial value of y at O =")),float(input("Enter initial value of theta at 0 ="))
print(type(x_initial))
print(type(y_initial))
print(type(theta_initial))
steering_angle=float(input("Enter steering angle ="))
diameter_wheel=(0.5)/2 #This is used as the radius in the code.
angular_velocity=float(input("Enter initial angular velocity ="))
chasis_lenght=4.0
#Orientation_angle=float(input("Enter initial orientation angle ="))
theta_dot=float((diameter_wheel*angular_velocity*math.tan(steering_angle))/chasis_lenght)
print(theta_dot)
x_dot=0

y_dot=0

#trajectory=math.sqrt((x_final**2)+(y_final**2))
# x axis values
x=[]
y=[]
theta=[]
delta_t=1000/1000 # for T=1000(time) and N=1000(data points)
for t in range (0,1000):
    if (t!=0):
        t_inital=t-1
    else:
        t_inital=0
    t_final=t
    x_initial=x_initial + x_dot*(t_final-t_inital)
    y_initial=y_initial + y_dot*(t_final-t_inital)
    theta_initial=theta_initial + theta_dot*(t_final-t_inital)
    x_dot=diameter_wheel*angular_velocity*(math.sin(theta_initial))
    y_dot=diameter_wheel*angular_velocity*(math.cos(theta_initial))
    
    x.append(x_initial)
# corresponding y axis values
    y.append(y_initial)
    
    
  
# plotting the points 

plt.plot(x, y)
  
# naming the x axis
plt.xlim(-30,30)
plt.ylim(-30,30)
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Trajectory of point O')
  
plt.show()
