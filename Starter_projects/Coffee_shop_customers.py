import numpy as np
import matplotlib.pyplot as plt

#Defining parameters
#Average rate of events = lambda
#Rate of customers appearing = 10 per hour
lambda_rate = 10

#Time to run the simulation (in hours)
simulation_time = 3.0

current_time = 0        #time the clock will start from
arrival_times = []      #a list to store the times customers will arrive

#Simulation loop

while current_time < simulation_time:
    #whiles we are still within the simulation time, model will pick from an exponent
    #because a poisson process picks random values in an increasing exponential order
    time_to_next_arrival = np.random.exponential(scale = 1/lambda_rate)     #1/lamda is the gap between events. So #a rate of 10 will be 1/10 = 6 minutes gap

    #Advancing the simulation clock
    current_time += time_to_next_arrival

    if current_time < simulation_time:
        arrival_times.append(current_time)

#Analyzing and plotting results
num_arrivals = len(arrival_times)
print("Simulation Complete")
print(f"Total Customers that Arrived in {simulation_time}: {num_arrivals}")

#Creating a scatter plot
plt.figure(figsize=(12,8))

plt.scatter(arrival_times, np.ones_like(arrival_times), marker='+', s=200, color='red')

#Creating a timeline
plt.title(f"Customer Arrivals with Poisson Process λ={lambda_rate}/hour)")
plt.xlabel("Time (Hours)")
plt.yticks([])      #hide y axis ticks and labels
plt.xlim(0, simulation_time)
plt.grid(axis='x', linestyle = '--')

plt.show()
