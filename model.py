import random
y0, x0 = int(random.randint(0,99)), int(random.randint(0,99))
y1,x1 = int(random.randint(0,99)), int(random.randint(0,99))

print(type(y0))

#assign a random number to Rando; 
#also available is randint(x,y)
Rando = random.random()

#random walk one step
if Rando < 0.5:
    y0 = y0+1
else:
    y0 = y0-1

if Rando < 0.5:
    x0 = x0+1
else:
    x0 = x0-1

print(y0, x0)

#this is step one -------------------------------------

#assign a random number to Rando; 
#also available is randint(x,y)
Rando = random.random()

#random walk one step
if Rando < 0.5:
    y1 = y1+1
else:
    y1 = y1-1

if Rando < 0.5:
    x1 = x1+1
else:
    x1 = x1-1

print(y1, x1)
distance = (((y1-y0)**2) + ((x1-x0)**2))**0.5
print("Distance equals " + str(distance))