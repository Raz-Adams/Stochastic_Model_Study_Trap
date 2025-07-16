import numpy as np
import matplotlib.pyplot as plt

# Defining the Markov Model
states = ["Sunny", "Rainy"]

# Creating a transition matrix to hold out probabilities

#            to: sunny | to: rainy
#from: sunny: [ 0.8,       0.2 ]
#from: rainy: [ 0.4,       0.6 ]

transition_matrix = np.array([[0.8,0.2], [0.4,0.6]])

#Simulation Parameters
num_days = 365

#Creating a representatino of our weather condition in a day
current_state_index = 0                         #an index of 0=sunny
weather_history = [current_state_index]         #storing the weather for each day

#Creating the simulation loop
for _ in range(num_days-1):
    #obtaining the row of probabilities for the current state
    probabilities = transition_matrix[current_state_index]
    #finding what the next state is i.e sunny or rainy
    next_state_index = np.random.choice([0,1], p=probabilities)
    #change the weather history
    weather_history.append(next_state_index)

#Analysing and plotting results
weather_in_words = [states[i] for i in weather_history]

#Counting frequency of each state
sunny_days = weather_in_words.count("Sunny")
rainy_days = weather_in_words.count("Rainy")
ratio = sunny_days/rainy_days

print(f"Simulation Results for {num_days} days:")
print(f"Number of Sunny days: {sunny_days}")
print(f"Number of Rainy days: {rainy_days}")
print(ratio)

#Creating a bar chart
plt.figure(figsize=(8,6))
#plt.bar(states, [sunny_days, rainy_days], color= ['gold','dodgerblue'])
bars = plt.bar(states, [sunny_days, rainy_days], color= ['gold','dodgerblue'])
plt.title("Weather Simulation Results")
plt.ylabel("Total Number of Days")
plt.ylim(0, num_days)

for bar in bars:
    yval = bar.get_height()     #saving height of y axis as a variable

    #bar.get_x() + bar.get_width()/2 = position on x-axis, yval = position on y
    #va, ha = vertical, horizontal alignment
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va= 'bottom', ha= 'center', fontsize = 12, weight = 'bold')

plt.show()