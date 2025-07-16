import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_steps = 100

# Creating random steps
# Each choice should be either 1 or -1 (i.e forward or backward)

steps = np.random.choice([1,-1], size = num_steps, p=[0.7,0.3])

#Calculating the path
#The position at any point is the sum of the random 1000 steps taken
#np.insert(0,0) we want to have 0 as the starting position not 1 (which would have meant he has 
#already taken a step)
positions = np.cumsum(np.insert(steps,0,0))

#Visualizing our code
plt.figure(figsize=(10,6))   #create graph
plt.plot(positions)             #plot positions

#Adding Labels to Plot
plt.title("1D Random Walk (Drunkard's Path)")
plt.xlabel("Number of Steps")
plt.ylabel("Position from Start")
plt.grid(True)

plt.show()

