import random

#Create a class for the sheep agent
class Agent_Sheep():
    ## Define initial functions 
    def __init__(self, agent_environment, o_agents, y, x):
        self.o_agents = o_agents
#        self.x = random.randint(0,299)
#        self.y = random.randint(0,299)
        self.environment = agent_environment
        #Set the store to 0, this calculates how much the sheep has eaten 
        self.store = 0 
        self.x = x
        if (x == None):
            self.x= random.randint(0,100)
        else:
            self.x=x
        self.y = y
        if (y == None):
            self.y= random.randint(0,100)
        else:
            self.y=y
        
    ## This eat function allows the agent to find the value of the square it
    ## is standing on, and to take a value away from the environment and add 
    ## it to self.store
    def eat(self):        
        #define name for the pixel value
            pixel_value = self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= min(pixel_value, 10)


            
    ## Function for movement - The sheep will move in a completely random
    ## direction. When it gets to the end of the grid space, it will appear
    ## on the opposite end of the plot, similar to a torus.      
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 125
        else:
            self.x = (self.x - 1) % 125

        if random.random() < 0.5:
            self.y = (self.y + 1) % 125
        else:
            self.y = (self.y - 1) % 125
    
    #function for checking if belly is full.
    def check_agent_full(self):
        if self.store > 100:
            full = 1
        else:
            full = 0
        
        return full
    
    ## This function allows the sheep to share food with its neighbours
    ## if the neighbours are within the 'Neighbourhood' parameter.
    def share_with_neighbours(self, neighbourhood):
        
        # Loop through the agents in self.agents
        for agent in self.o_agents:
        # Calculate the distance between self and the current other agent:
            
# =============================================================================
#             if agent != self:
#                 distance = self.distance_between(agent)
#                
#                 # Test code to print when sharing
#                 #if distance <= neighbourhood:
#                     #print("----------")
#                     #print("agents within sharing neighbourhood")
# =============================================================================
                    
                    # Sum self.store and agent.store .
                sum_store = self.store + agent.store
                    # Divide sum by two to calculate average.
                avg = sum_store / 2
                    # self.store = average
                self.store = avg
                    
                    # agent.store = average
                agent.store = avg
                    #test code to ensure grass is being shared fairly
                    #print("stores are {} and {}".format(self.store, agent.store))
                    #print("sharing " + str(distance) + " " + str (avg))
                    
    ## This function calculates the distance between itself and other agents     
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    #create the function to display information
    def __str__(self):
        return '{0} - ({1}, {2})'.format(self.store, self.x, self.y)
    
                  
             