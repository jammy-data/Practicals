import random
import operator
import matplotlib.pyplot
agents = []

random.seed(10)
#Remove y0,x0 and replace with the randoms within parenthesis
agents.append([random.randint(0,99),random.randint(0,99)])


#assign a random number to Rando; 
#also available is randint(x,y)
Rando = random.random()

#random walk one step
if Rando < 0.5:
    agents[0][0] =  agents[0][0]+1
else:
     agents[0][0] =  agents[0][0]-1

if Rando < 0.5:
     agents[0][1] = agents[0][1]+1
else:
    agents[0][1] = agents[0][1]-1



#this is step one -------------------------------------

agents.append([random.randint(0,99),random.randint(0,99)])
#assign a random number to Rando; 
#also available is randint(x,y)
Rando = random.random()

#random walk one step
if Rando < 0.5:
    agents[0][0] =  agents[0][0]+1
else:
     agents[0][0] =  agents[0][0]-1

if Rando < 0.5:
     agents[0][1] = agents[0][1]+1
else:
    agents[0][1] = agents[0][1]-1

y0 = agents[0][1]
y1 = agents[1][1]
x0 = agents[0][0]
x1 = agents[1][0]
print(agents)
distance = (((y1-y0)**2) + ((x1-x0)**2))**0.5
print("Distance equals " + str(distance))

#Prac 2 ---------------------------------------------

agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])

print(max(agents, key=operator.itemgetter(1)))
print(max(agents, key=operator.itemgetter(0)))
#plot the data
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][0],agents[0][1])
matplotlib.pyplot.scatter(agents[1][0],agents[1][1])
#topmostagent = max(agents, key=operator.itemgetter(1))
topmostagent = max(agents, key=operator.itemgetter(1))
bottommostagent = min(agents, key=operator.itemgetter(1))
leftmostagent = min(agents, key=operator.itemgetter(0))
rightmostagent = max(agents, key=operator.itemgetter(0))
matplotlib.pyplot.scatter(topmostagent[0],topmostagent[1], color='red')
matplotlib.pyplot.scatter(bottommostagent[0],bottommostagent[1], color='blue')
matplotlib.pyplot.scatter(leftmostagent[0],leftmostagent[1], color='green')
matplotlib.pyplot.show()
