#Import the modules needed along the code
import random
import operator
import matplotlib.pyplot as pyp
import matplotlib.animation as ani
import agentframework
import csv

#Creation of the variables
num_of_agents = 10
num_of_agents2 = 5
num_of_chased = 10
num_of_iterations = 100
neighbourhood = 15
ep_area = 20
#Empty lists
agents = []  
agents2 = [] 
chased = [] 

#Reading the environment (txt file into a 2D list)
environment = [] #Empty list of environment

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:			        # A list of rows
        rowlist = []
        for value in row:				# A list of value
            rowlist.append(value)       #Appending the values to the rowlist
        environment.append(rowlist)     #Append the rowlist to the environment
            #print(value) 				# Floats

#Creating the space for my figure
fig = pyp.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])

#Fill our lists with my two class of agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

for i in range(num_of_agents2):
    agents2.append(agentframework.Agent2(environment,agents,agents2))

#Randomising the order in which agents are processed each iteration. 
random.shuffle(agents)
random.shuffle(agents2)

carry_on = True	

def update(frame_number):
    
    fig.clear()   
    global carry_on  
    
# Omnivorous move, eat and share.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
            
# Vegetarians move and convinced omnivorous to be vegetarians.
    for j in range(num_of_iterations):
        for l in range(num_of_agents2):
            agents2[l].move()
            a_chased = agents2[l].chase(ep_area, agents)

        for k in a_chased:
            chased.append(agentframework.Agent(environment,agents))
            agents.remove(k)

#Setting the Stopping condition
#when there is iqual o more number of omnivorous transformed in vegetarians            
    if  (len(agents2) == len(chased)) |  (len(agents2) < len(chased)):
        carry_on = False
        print("stopping condition")
     
#Animation
#Displaying environment data
    pyp.xlim(0, 100)
    pyp.ylim(0, 100)
    pyp.imshow(environment)
    for a in agents:
        pyp.scatter(a.x,a.y, c="red", marker ="+")
        #print(a.x,a.y)
    for b in agents2:
        pyp.scatter(b.x,b.y, c="green", marker ="D")
        #print(b.x,b.y)
#Print converted vegetarians        
    for c in chased:
        pyp.scatter(c.x,c.y, c="blue", marker ="d")
        #print(c.x,c.y)

#Generator function
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = ani.FuncAnimation(fig, update, frames=gen_function, repeat=False)

pyp.show()


