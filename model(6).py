import matplotlib
import tkinter
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
import time
import agentframework
import csv
import matplotlib.animation
import requests
import bs4

start = time.clock()

#set up the function to calculate point distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

'''---------------PARAMETER SECTION----------------'''
#identify the number of agents
num_of_agents = 10
#identify the sheeps 'personal space'
neighbourhood = 20
'''------------------------------------------------'''
#initialise various inputs
agents = []
data = []
environment = []

'''##################################################################
####        #extract and parse the xy data from the webpage     #####
#####################################################################'''
#extract and parse the xy data from the webpage
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#separate the xy elements
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    #append the agents with this co-ordinate data
    agents.append(agentframework.Agent(environment, agents, y, x))
'''##################################################################'''


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
##############################################
####        Getting the environment     #####
#############################################

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
# Don't close until you are done with the reader;
#ensuring dataset is rectangular i.e. col value for every row value
nrows = len(environment)
print (nrows)
ncols = len(environment[0])
print (ncols)
#show the 299th by 299th value for ref
#print(environment[299][299])

total = 0
#for row in nrows
    #for col in cols:
        #total += environment[row][col]
# Fill with random data.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

#################################################
#Create agents using agentframework.py
#for i in range(num_of_agents):
#    agents.append(agentframework.Agent(environment, agents))

carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on
    
    #shuffle the agent list
    random.shuffle(agents)
    #Commence movement & mastication
    
    
    #######################################################
    ## New stopping condition if all sheep have a full belly
    counter = 0   
    for i in range(num_of_agents):
        agent_full = agents[i].check_agent_full() 
        if agent_full ==1:
            print("full belly reached, {}".format(agents[i].store))
            counter += 1
    
    if counter == (num_of_agents):
        carry_on = False
        print ("stopping condition")
    #######################################################
    
#==============================================================================
#     if random.random() < 0.01:
#         carry_on = False
#         print ("stopping condition")
#         
#==============================================================================
    #plot the data
    
    matplotlib.pyplot.ylim(299, 0)
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='black')
    
        

#identify the left and rightmost agents
'''Agents do not support indexing so this section
   cannot be executed
leftmostagent = min(agents, key=operator.itemgetter(0))
rightmostagent = max(agents, key=operator.itemgetter(0))
'''

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
#create a function to run the animation
def run():        
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
    canvas.show()
#create a function to kill the tkinter loop
def kill():  
    global root
    root.destroy()
    root.quit()
    
    
    
root = tkinter.Tk()
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar=tkinter.Menu(root)
root.config(menu=menu_bar)
#create the menubar labels
run_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=run_menu)
run_menu.add_command(label="run model", command=run)
run_menu.add_command(label="kill", command=kill)
tkinter.mainloop() 

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