'''https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/'''


import matplotlib
import tkinter
matplotlib.use('TkAgg')
import random
from tkinter import *
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



##################################################################
#####                    PARAMETERS                          #####
##################################################################

#identify the number of each parameter which will alter the way the model functions

num_of_sheep = 30
#num_of_wolves = 0 # un-block this to override tkinter options
neighbourhood = 20
kill_radius = 30

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

## Here I am retrieving data from a html site, and reading it in to the model ##

# the r variable here retrieves the website. content variable retrieves
# the text from the website.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

## Plug-in beautifulsoup (see import bs4) was used to parse the webpage.
soup = bs4.BeautifulSoup(content, 'html.parser')

#separate the xy elements
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

num_of_wolves=0

## the run function describes what will happen in tkinter when the run option
## is selected.
def run(): 
    selected= Lb.curselection() # find which list option has been selected
    
    #print(selected) TEST to see what the output is
    
    #based on the selection, I want to change the number of wolves in the model
    
    global num_of_wolves
    if selected == (0,):
        num_of_wolves = 0
    if selected ==(1,):
        num_of_wolves = 2
    if selected ==(2,):
        num_of_wolves = 4
    if selected ==(3,):
        num_of_wolves = 10
    else:
        pass
 

    
    ##################################################################
    #####                CREATE AGENTS                           #####
    ##################################################################
    for i in range(num_of_sheep):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        sheep.append(SheepFramework.Agent_Sheep(environment, sheep, y, x))

## Create the wolves with knowledge of the sheep
    
    for i in range(num_of_wolves):
        wolves.append(WolfFramework.Agent_Wolf(sheep))
    #animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames= gen_function) #unblock to create stopping conditions    
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
    canvas.draw() #updated from canvas.show()
    #to save animation use Animation.save



    
 
    

    
##################################################################
#####                GETTING THE ENVIRONMENT                 #####
##################################################################
    
#initialising the csv reader to convert .txt to .csv
    
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    
    #append the environment to supply a value given from the in.txt file
    
    environment.append(rowlist)
    for value in row: 
        rowlist.append(value)
f.close() 

# Fill with random data.

for i in (range(1,125)):
     datarow = []
     for j in (range(1,125)):
         datarow.append(random.randint(0,125))
     data.append(datarow)

fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])    

carry_on = True    

# =============================================================================
## TEST
## ensuring dataset is rectangular i.e. col value for every row value
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



## Create the update function for the animation ##

# This will dictate the number of times the model will run until it stops. here
# you can decide a stopping condition if you wish.
        
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    #shuffle the agent list
    
    random.shuffle(sheep)
    
    

    #plot the axis along with the plot boundaries.
    
    matplotlib.pyplot.ylim(125, 0)
    matplotlib.pyplot.xlim(0, 125)
    matplotlib.pyplot.imshow(environment)
    
    ##################################################################
    #####                AGENT ACTION LOOP                       #####
    ################################################################## 
    
    ## Initiate the action loop for all sheep.
    # The functions I have defined here are for the sheep to move, eat the
    #environment and share food with their neighbours.
    
    for i in range(len(sheep)):
        sheep[i].move()
        sheep[i].eat()
        sheep[i].share_with_neighbours(neighbourhood) 
        
        #plot the sheep on the scattergraph
        
        matplotlib.pyplot.scatter(sheep[i].x,sheep[i].y, color='white', edgecolor='black', label='sheep')
    
    ## initiate the loop for all wolves
    # The functions I have defined here are for the wolves to target sheep,
    # move around and eat sheep on the same grid co-ordinate.
    
    for i in range(len(wolves)):
        wolves[i].target_sheep(kill_radius)
        wolves[i].move()
        
        #if function to ensure that sheep get eaten when on same block as wolf
        
        if wolves[i].target != None:
            if (wolves[i].x == wolves[i].target.x) and (wolves[i].y == wolves[i].target.y):
                wolves[i].eat_sheep(wolves[i].target)
        
        #plot the wolves on the scattergraph    
        
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color='red', label="wolves", edgecolor='black')    
    matplotlib.pyplot.title("Final Model")                
    matplotlib.pyplot.ylabel("Environment")
    matplotlib.pyplot.xlabel("Environment")
        
        
        
    ##################################################################
    #####                STOPPING CONDITION                      #####
    ##################################################################  
    
    ## If sheep have full belly model stops
    
    # set the counter to 0. We want the counter to reach 1 when the sheep
    # are all full, and thus stop the model.
    counter = 0   
    for i in range(len(sheep)):
        agent_full = sheep[i].check_agent_full() 
        if agent_full ==1:
            print("full belly reached, {}".format(sheep[i].store))
            counter += 1
    
    if counter == (len(sheep)):
        carry_on = False
        print ("stopping condition")
        
        
    
    
## Create a gen_function to dictate the conditions of the animation stopping    
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        

def Stop():
    global root
    root.quit()
    print('Model terminated')

#create a function to kill the tkinter loop and close the window.
def kill():  
    global root
    root.destroy()
    root.quit()
    

## tkinter 
root = tkinter.Tk()    
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

Lb = Listbox(root)
Lb.insert(1, 'No Wolves')
Lb.insert(2, 'Wolven espionage')
Lb.insert(3, 'fifty/fifty')
Lb.insert(4, 'onslaught')
Lb.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
label= Label(root, text='Choose your model variant', justify=LEFT, foreground='blue', background= 'yellow')
label.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

run_button= Button(root, text="Run Model", command=run)
quit_button= Button(root, text="Stop Model", command=kill)
run_button.configure(bg='green')
quit_button.configure(bg='red')
quit_button.pack(side=tkinter.BOTTOM)
run_button.pack(side=tkinter.BOTTOM)

tkinter.mainloop() 







