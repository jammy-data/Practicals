import matplotlib
import tkinter
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
import time
import SheepFramework
import csv
import matplotlib.animation
import requests
import bs4
import WolfFramework


start = time.clock()

#set up the function to calculate point distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

##################################################################
#####                    PARAMETERS                          #####
##################################################################
#identify the number of agents
num_of_sheep = 35
num_of_wolves = 7
neighbourhood = 20
kill_radius = 10

##################################################################
#####                INITIALISE VARIABLES                    #####
##################################################################
#initialise various inputs
sheep = []
data = []
environment = []
wolves = []

##################################################################
####        extract and parse the xy data from webpage       #####
##################################################################
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#separate the xy elements
for i in range(num_of_sheep):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    
##################################################################
#####                CREATE AGENTS                           #####
##################################################################  
#Create agents with this co-ordinate data
#separate the xy elements
for i in range(num_of_sheep):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    sheep.append(SheepFramework.Agent_Sheep(environment, sheep, y, x))

for i in range(num_of_wolves):
    wolves.append(WolfFramework.Agent_Wolf(sheep))
    
##################################################################
#####                GETTING THE ENVIRONMENT                 #####
##################################################################
#initialising the csv reader to convert .txt to .csv
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    #append the environment in a loop
    environment.append(rowlist)
    for value in row: 
        rowlist.append(value)
f.close() 

# =============================================================================
#ensuring dataset is rectangular i.e. col value for every row value
# nrows = len(environment)
# print (nrows)
# ncols = len(environment[0])
# print (ncols)
#show the 299th by 299th value for ref
#print(environment[299][299])
#total = 0
#for row in nrows
    #for col in cols:
        #total += environment[row][col]
# =============================================================================



# Fill with random data.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

#######################################################

fig = matplotlib.pyplot.figure(figsize=(15, 15))
ax = fig.add_axes([0, 0, 1, 1])    

carry_on = True

#Create the update function for the animation
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    #shuffle the agent list
    random.shuffle(sheep)
    #Commence movement & mastication
    

    #plot the data   
    matplotlib.pyplot.ylim(299, 0)
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.imshow(environment)
    
    ##################################################################
    #####                AGENT ACTION LOOP                       #####
    ##################################################################    
    for i in range(len(sheep)):
        sheep[i].move()
        sheep[i].eat()
        sheep[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(sheep[i].x,sheep[i].y, color='black')
    
    for i in range(len(wolves)):
        wolves[i].target_sheep(kill_radius)
        wolves[i].move()
        if wolves[i].target != None:
            if (wolves[i].x == wolves[i].target.x) and (wolves[i].y == wolves[i].target.y):
                wolves[i].eat_sheep(wolves[i].target)
            
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color='red')    
        
        
        
    #######################################################
    ## New stopping condition if all sheep have a full belly
    counter = 0   
    for i in range(len(sheep)):
        agent_full = sheep[i].check_agent_full() 
        if agent_full ==1:
            print("full belly reached, {}".format(sheep[i].store))
            counter += 1
    
    if counter == (len(sheep)):
        carry_on = False
        print ("stopping condition")
        
#==============================================================================
#     if random.random() < 0.01:
#         carry_on = False
#         print ("stopping condition")
#         
#==============================================================================

#identify the left and rightmost agents
#Agents do not support indexing so this section
#   cannot be executed
#leftmostagent = min(agents, key=operator.itemgetter(0))
#rightmostagent = max(agents, key=operator.itemgetter(0))


def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#create a function to run the animation
def run(): 
    
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)
    canvas.draw() #updated from canvas.show()
    #to save animation use Animation.save

#create a function to kill the tkinter loop
def kill():  
    global root
    root.destroy()
    root.quit()
    
def ChangeVariables():
    print(num_of_sheep)
    
    
    
##################################################################
#####                INITIATE TKINTER                        #####
##################################################################     
root = tkinter.Tk()

root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#menu_bar=tkinter.Menu(root)
#root.config(menu=menu_bar)
Button1 =tkinter.Button(root, text="Submit", command = ChangeVariables)
Button1._tkcanvas.pack()
#create the menubar labels
#run_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="Model", menu=run_menu)
#run_menu.add_command(label="run model", command=run)
#run_menu.add_command(label="kill", command=kill)



tkinter.mainloop() 
