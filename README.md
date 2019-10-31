# Practicals

## Folder: Prac1-2

### Practical 1 - Agent based modelling
### Practical 2 - Code Shrinking I

Within this folder is the code I used for the first practical - Agent based modelling. The purpose of this practical was to introduce us to the concept of an agent based model, and begin to programme the model itself using Python. Within this practical are examples of **if** statements and use of the [**random**](https://docs.python.org/3/library/random.html?highlight=random#module-random) package.

Lastly we used pythagorus' theorem to calculate a distance between two randomly located agents.



## Folder: Prac 3

### Practical 3 - Code Shrinking II

In this practical I used **for** loops to clear any unneccesary repetition and shorten the code. This practical also saw the use of the remainder(_**%**_) tool, which allowed the agents to stay within the plot area.



## Folder: Prac 4

### Practical 4 - Building Tools

This practical involved defining functions, in this case to calculate a distance between sheep. Through use of this I was able to provide a distance between each sheep, using the following code to prevent repetition:

```python
for j in range (i+1 ,num_of_agents): #i+1 so it does not count itself
```


## Folder: Prac 5-6

### Practical 5 - Agents!
### Practical 6 - I/O

In these practicals I was able to define functions for the sheep eating, moving and sharing an initialised environment with one another. The environment was initialised using a [**.csv reader**](https://docs.python.org/3/library/csv.html?highlight=csv%20reader#csv.reader), which was then available for the taking (or eating) by our sheep agent.


## Folder: Prac 7-9

### Practical 7 - Communicating
### Practical 8 - Animation/behaviour
### Practical 9 - GUI/Web Scraping

These practicals covered what I thought were the more complex programming, which involved communication of information and ultimately variables between agents, animation of the model and creation of a GUI to display and run the model as a user.

The communication function is somewhat similar to the processes involved in practical 6. However the animation and GUI practicals introduced more complex code. Animation focused on plotting the functions of the agents in a 'for' loop, in its own update function. This allowed the model to run until the number of iterations had been completed, or until another stopping point had been defined and reached.
The function of the GUI (Graphical User Interface) is to allow users to run the code and interact with the model in a more user-friendly way. Whilst building a GUI, programmers often have to be mindful that the functionality of the buttons or processes need to be user-friendly.
