

#structure stores all relivant info a process needs
class processStruct:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival= arrival
        self.burst= burst




#we start at time 0 for our scheduling processes
time=0

#Stores the each process that havent been put into the queue yet
processesToDo=[]

#Opens a file 
f = open("inputFile.in", "r")
processFileReader=[]
#Stores all seperate words in a file
for lines in f:
  for word in lines.split():
    processFileReader.append(word)
f.close()
#stores the amount of processes this input file has
processcount=int(processFileReader[1])
#gives us the amount of time we have to run these processes
runfor=processFileReader[3]
#the method we want to use for scheduling
use=processFileReader[5]

for process in range(processcount):
  processesToDo.append(processStruct(processFileReader[process*7+8],processFileReader[process*7+10],processFileReader[process*7+12]))
  print(processesToDo[process].arrival)

if(use=='fifo'):
  print('hi')
elif use=='sjf':
  print('hi2')
elif use=='rr':
  print('hi3')

  
