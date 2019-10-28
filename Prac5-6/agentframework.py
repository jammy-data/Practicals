import random
class Agent():
    def __init__(self, agent_environment, o_agents, y, x):
        self.o_agents = o_agents
#        self.x = random.randint(0,299)
#        self.y = random.randint(0,299)
        self.environment = agent_environment
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
        
    
    def eat(self):        
        #define name for the pixel value
            pixel_value = self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= min(pixel_value, 10)
            # store 'store' value before modifying it for printing
            before_store = self.store
            self.store += min(pixel_value, 10)
            #find difference to test that <10 units have been eaten
            if pixel_value < 10:
                print("The greedy sheep ate {} pixels".format(self.store - before_store))
            
    #Function for movement        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
    
    #function for checking if belly is full
    def check_agent_full(self):
        if self.store > 100:
            full = 1
        else:
            full = 0
        
        return full
    
    #neighbour share
    def share_with_neighbours(self, neighbourhood):
        
        # Loop through the agents in self.agents
        for agent in self.o_agents:
        # Calculate the distance between self and the current other agent:
            
            if agent != self:
                distance = self.distance_between(agent)
               
                # If distance is less than or equal to the neighbourhood
                if distance <= neighbourhood:
                    print("----------")
                    print("agents within sharing neighbourhood")
                    
                    # Sum self.store and agent.store .
                    sum_store = self.store + agent.store
                    # Divide sum by two to calculate average.
                    avg = sum_store / 2
                    # self.store = average
                    self.store = avg
                    
                    # agent.store = average
                    agent.store = avg
                    print("stores are {} and {}".format(self.store, agent.store))
                    print("sharing " + str(distance) + " " + str (avg))
        
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    #create the function to display information
    def __str__(self):
        return '{0} - ({1}, {2})'.format(self.store, self.x, self.y)
    
                  
             