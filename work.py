import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravitational acceleration (m/s^2)
v0 = 20    # Initial speed (m/s)

# Launch angles
angles = [30, 60, 45]

# Time of flight, max range, and max height
def calculate_trajectory(v0, angle):
    angle_rad = np.radians(angle)  # Convert angle to radians
    t_flight = 2 * v0 * np.sin(angle_rad) / g  # Time of flight
    t = np.linspace(0, t_flight, num=500)  # Time points
    
    # Horizontal and vertical components of velocity
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    # Equations of motion
    x = v0x * t  # Horizontal distance
    y = v0y * t - 0.5 * g * t**2  # Vertical distance
    
    return x, y, t

# Create the plot
plt.figure(figsize=(10, 6))

# Plot trajectories for each angle
for angle in angles:
    x, y, t = calculate_trajectory(v0, angle)
    plt.plot(x, y, label=f'Angle = {angle}°')

# Customize the plot
plt.title('Projectile Motion for Different Launch Angles')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 30)

# Show the plot
plt.show()
