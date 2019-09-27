import random
import operator
import matplotlib.pyplot
import time

start = time.clock()

##################################################################
#####                    PARAMETERS                          #####
##################################################################
num_of_agents = 10
num_of_iterations = 100

##################################################################
#####                INITIALISE VARIABLES                    #####
##################################################################
agents = []
data = []
processed_data = []


# Fill with random data.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

#random.seed(10)

##################################################################
#####                CREATE AGENTS                           #####
################################################################## 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# Modify each agents first element
for j in range(num_of_iterations):    
    for i in range (num_of_agents):
    #print(i)
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


#plot the data
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1])

# =============================================================================
# #identify the left and rightmost agents
# leftmostagent = min(agents, key=operator.itemgetter(0))
# rightmostagent = max(agents, key=operator.itemgetter(0))
# #matplotlib.pyplot.scatter(leftmostagent[0],leftmostagent[1], color='green')
# #matplotlib.pyplot.scatter(rightmostagent[0],rightmostagent[1], color='red')
# =============================================================================
matplotlib.pyplot.show()


##################################################################
#####                DISTANCE                                #####
################################################################## 
#set up the function for distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#set up a cumulative 'for' loop to find and print the largest distance between agents
max_distance = distance_between(agents[1], agents[0])
for i in range (0,num_of_agents):
    for j in range (i+1 ,num_of_agents): #i+1 so it does not count itself
        distance = distance_between(agents[i], agents[j])
        max_distance = max(max_distance, distance)
        print("distance between agent", i, "and", j, distance)
        print(max_distance)
        
        
#time the process and print        
end=time.clock()

print("time=",str(end-start))
    