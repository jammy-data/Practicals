'''PROJECT WOLF'''
import random
class Agent_Wolf():
    def __init__(self, sheep_list):
        self.x = random.randint(0,200)
        self.y = random.randint(0,200)
        self.sheep_eaten = 0
        self.sheep_all = sheep_list
        self.target = None
    
    def distance_between(self, sheep):
        return (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5
    
    #Provide a kill radius for the wolf reliant on distance
    def target_sheep(self, kill_radius):
        min_dis = kill_radius
        for sheep in self.sheep_all:
            dis = self.distance_between(sheep)
            if dis < min_dis:
                
                min_dis = dis
                self.target=sheep
            #if dis < kill_radius:
                #self.target = sheep
                
    def eat_sheep(self,sheep):
        
       
        self.sheep_eaten+=1
        #print(len(self.sheep_all))
        if self.target in self.sheep_all:
            print("****** SHEEP EATEN!!!!!! *****")
            self.sheep_all.remove(sheep)
            #reset the target to None to continue random movement
            self.target = None
            print("there are" , len(self.sheep_all), "sheep left")
                
    def move(self):
        #if no sheep in sight random move
        if self.target == None:
            if random.random() < 0.5:
                self.x = (self.x + 3) % 200
            else:
                self.x = (self.x - 3) % 200

            if random.random() < 0.5:
                self.y = (self.y + 3) % 200
            else:
                self.y = (self.y - 3) % 200
                
                
                
        #if sheep in sight - move to sheep
        else:
            if self.x > self.target.x:
                self.x -= 1
                
            elif self.x < self.target.x:
                self.x += 1
                
            else:
                pass
            
            if self.y > self.target.y:
                self.y -= 1
            elif self.y < self.target.y:
                self.y += 1
            else:
                pass
            
            
            
        
            
    
                