import random

#Define inside it an Agent class, with an __init__ method. 
class Agent(): #Creating Agent Class
    
#Defining variables and environment    
    
    def __init__(self,environment,agents):
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)

#Euclidiane distance between agents as a function
#Needed to define the share_with neighbours function        
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                
#First behaviour of the Agents
#Defining the move of the agents as a function
         
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100 

#Second behaviour of the Agents            
#Defining that agents can eat their environment as a function

    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

#Third behaviour of the Agents
#Defining the share_with_neighbours as a function
#The agent will search for close neighbours, and share resources with them            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                average = (self.store + agent.store) /2
                self.store = average
                agent.store = average
                #print("sharing " + str(dist) + " " + str(average))

class Agent2(): #Creating second Agents Class
    
#Defining variables and environment    
    
    def __init__(self,environment,agents,agents2):
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.agents2 = agents2
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)

#Euclidiane distance between agents as a function
#Needed to define the chase function  
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

#Defining the movement of the Agents2   
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 5) % 100
        else:
            self.y = (self.y - 5) % 100

        if random.random() < 0.5:
            self.x = (self.x + 5) % 100
        else:
            self.x = (self.x - 5) % 100 

#Definig the chase_function of the Agents2
    def chase(self,ep_area, agents):
        list_chased = []
        for agent in self.agents:
            dist2 = self.distance_between(agent)
            if dist2 <= ep_area:
                list_chased.append(agent)
        return list_chased
    
    
                
    
            