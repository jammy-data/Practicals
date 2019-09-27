import random
import operator
import matplotlib.pyplot


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
#Remove y0,x0 and replace with the randoms within parenthesis
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


#assign a random number to Rando; 
#also available is randint(x,y)



# Modify each agents first element
for j in range(num_of_iterations):    
    for i in range (num_of_agents):
        Rando = random.random()
    #print(i)
        if Rando < 0.5:
            agents[i][0] =  (agents[i][0]+1) % 100
        else:
            agents[i][0] =  (agents[i][0]-1) % 100
        # Check if off edge, if so, set value to bounce off edge.
        if agents[i][0] < 0:
            agents[i][0] = 0
        if agents[i][1] < 0:
            agents[i][0] = 0
        if agents[i][0] > 99:
            agents[i][0] = 99
        if agents[i][1] > 99:
           agents[i][0] = 99

# Modify each agents second element
for j in range(num_of_iterations):
    for i in range (num_of_agents):
        Rando = random.random()
        if Rando < 0.5:
            agents[i][1] =  (agents[i][1]+1) % 100
        else:
            agents[i][1] =  (agents[i][1]-1) % 100
        # Check if off edge and adjust.
        if agents[i][0] < 0:
            agents[i][0] = 0
        if agents[i][1] < 0:
            agents[i][0] = 0
        if agents[i][0] > 99:
            agents[i][0] = 99
        if agents[i][1] > 99:
           agents[i][0] = 99

print(agents)
#distance = (((y1-y0)**2) + ((x1-x0)**2))**0.5
#print("Distance equals " + str(distance))
#print(max(agents, key=operator.itemgetter(1)))
#print(max(agents, key=operator.itemgetter(0)))

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
