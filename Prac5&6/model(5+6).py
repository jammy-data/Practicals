import random
import operator
import matplotlib.pyplot
import time
import agentframework
import csv

#a = agentframework.Agent(environment, agents)
#a.o_agents


#input agent from agentframework
start = time.clock()

##################################################################
#####                DISTANCE CALC                           #####
################################################################## 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

##################################################################
#####                    PARAMETERS                          #####
##################################################################
num_of_agents = 5
num_of_iterations = 1
neighbourhood = 20

##################################################################
#####                INITIALISE VARIABLES                    #####
##################################################################
agents = []
data = []
processed_data = []

##################################################################
#####                GETTING THE ENVIRONMENT                 #####
##################################################################
#initialising environment
environment = []
#initialising the csv reader to convert .txt to .csv
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    #append the environment in a loop
    environment.append(rowlist)
    for value in row: 
        rowlist.append(value)
        #print(value) # Floats
f.close() 
# Fill with random data.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        datarow.append(random.randint(0,99))
    data.append(datarow)
    
    
# =============================================================================
# #ensuring dataset is rectangular i.e. col value for every row value
# nrows = len(environment)
# print (nrows)
# ncols = len(environment[0])
# print (ncols)
# #show the 299th by 299th value for ref
# #print(environment[299][299])
#total = 0
#for row in nrows
    #for col in cols:
        #total += environment[row][col]
# =============================================================================

#random.seed(10) #uncomment for testing purposes
    
    
##################################################################
#####                CREATE AGENTS                           #####
##################################################################
for i in range(num_of_agents):
    y = random.randint(0,299)
    x = random.randint(0,299)
    agents.append(agentframework.Agent(environment, agents, y, x))

#shuffle the agent list
random.shuffle(agents)
#Commence movement & mastication
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#plot the data
matplotlib.pyplot.ylim(299, 0)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#identify the left and rightmost agents
# =============================================================================
# ## Agents do not support indexing so this section ##
# ## cannot be executed                             ##
# leftmostagent = min(agents, key=operator.itemgetter(0))
# rightmostagent = max(agents, key=operator.itemgetter(0))
# matplotlib.pyplot.scatter(leftmostagent[0],leftmostagent[1], color='green')
# matplotlib.pyplot.scatter(rightmostagent[0],rightmostagent[1], color='red')
# =============================================================================

matplotlib.pyplot.show()

#calculate the maximum distance
#max_distance = distance_between(agents[1], agents[0])
print("*"*20)
for i in range (0,num_of_agents):
    for j in range (i+1 ,num_of_agents):
        distance = distance_between(agents[i], agents[j])
        #max_distance = max(max_distance, distance)
        print("distance between agent", i, "and", j, distance)
        #print(max_distance)
        
f2 = open('dataout.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=' ')
for row in data:
    writer.writerow(row) # List of values.
f2.close()
        
end=time.clock()

print("time=",str(end-start))
print(agents[i])