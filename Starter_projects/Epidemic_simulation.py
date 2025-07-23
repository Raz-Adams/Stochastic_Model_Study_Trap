import numpy as np
import matplotlib.pyplot as plt

# Simulate an epidemic in a population of 1000 people, starting with just one infected individual. 
# We will then plot the number of people in the S, I, and R categories over time to visualize 
# the classic "epidemic curve."
# S - susceptible, I - infected, R - recovered

#Defining parameters
population_size = 1000
beta            = 0.4       #transmission rate
gamma           = 0.1       #recovery rate. 1/gamma is average duration of illness (1/0.1 = 10 days of recovery)

#Initial conditions with one person infected
initial_S   = population_size - 1
initial_I   = 1
initial_R   = 0

#Creating list to store history of SIR
S_history = [initial_S]
I_history = [initial_I]
R_history = [initial_R]

time_history = [0]

#Keeping track of current states
current_S = initial_S
current_I = initial_I
current_R = initial_R
current_time = 0

#Creating a Gillespie simulation loop

while current_I > 0:
    #Calculating the rates of the two possible events
    rate_infection = ( beta * current_S * current_I)/ population_size
    rate_recovery  = ( gamma * current_I)

    total_rate = rate_recovery + rate_infection

    #Calculating when the next event will happen
    time_to_next_event = np.random.exponential(scale=1/total_rate)

    #Which event will it be?
    r = np.random.rand()

    if r < (rate_infection / total_rate):
        #It's an INFECTION event
        current_S -= 1
        current_I += 1
    else:
        #It's a RECOVERY event
        current_I -= 1
        current_R += 1
    
    #4. Updating the clock and recording the new state
    current_time += time_to_next_event
    
    S_history.append(current_S)
    I_history.append(current_I)
    R_history.append(current_R)
    time_history.append(current_time)


#Final Plots
plt.figure(figsize=(12, 8))
plt.plot(time_history, S_history, label='Susceptible', color='blue')
plt.plot(time_history, I_history, label='Infected', color='red', linewidth=2.5)
plt.plot(time_history, R_history, label='Recovered', color='green')

#Add labels and a legend
plt.title(f'Stochastic SIR Epidemic Simulation (β={beta}, γ={gamma})')
plt.xlabel('Time (Days)')
plt.ylabel('Number of People')
plt.legend()
plt.grid(True)
plt.xlim(0, max(time_history))
plt.ylim(0, population_size)

plt.show()


