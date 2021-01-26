# Greedy Algorithm for a Optimisation Problem

# Defined a class for item, 
# with its name, value and cost
class Itm(object):
    def __init__(self, name, val, cost):
        self.name = name
        self.val = val
        self.cost = cost
        
    def getvalue(self):
        return self.val
    
    def getcost(self):
        return self.cost
    
    def __str__(self):
        return self.name 
  
# Defining a function for building a List 
# which generates list of items that are 
# available at supermart   
def buildlist(names, values, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Itm(names[i], values[i], costs[i]))
    return menu

# Implementation of greedy algorithm 
# to choose one of the optimum choice
def greedy(items, maxcal, keyfunction):
    itemscopy = sorted(items, key = keyfunction, reverse = True)
    
    result = []
    totalval = 0 
    totalcal = 0
    
    for i in range(len(items)):
        if (totalcal + itemscopy[i].getcost() <= maxcal):
            result.append(itemscopy[i])
            totalval = totalval + itemscopy[i].getvalue()
            totalcal = totalcal + itemscopy[i].getcost()
            
    return (result, totalval)


# Main Function
# All values are random    
names = ['Ball', 'Gloves', 'Notebook', 'Bagpack', 'Charger', 'Pillow', 'Cakes', 'Pencil']
values = [89,90,95,100,90,79,50,10]
costs = [123,154,25,145,365,150,95,195]
Itemrs = buildlist(names, values, costs)
maxcost = 500 # maximum money he have to spend

taken, totvalue = greedy(Itemrs, maxcost, Itm.getvalue)

print('Total vaule taken : ', totvalue)

# Printing the list of item slected for optimum value
for i in range(len(taken)):
    print('  ', taken[i])