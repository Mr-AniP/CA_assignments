import m5
from m5.objects import *

root = Root(full_system = False)
root.vectorObject = VectorOperations()

a=int(input("Would You like to set input ticks ? ( 0 : N0 / (1 : Yes )"))
while(a not in [0,1]):
    print("Please type either 0 or 1")
    a=int(input("Would You like to set input ticks ? ( 0 : N0 / (1 : Yes )"))
if(a==1):
    root.vectorObject.tickproduct=str(int(input("Tick time of VectorCrossProduct event")))+"ps"
    root.vectorObject.ticknormalize=str(int(input("Tick time of NormalizeVector event")))+"ps"
    root.vectorObject.ticksubtraction=str(int(input("Tick time of VectorSubtraction event")))+"ps"

a=int(input("Would You like to set input Vectors ? ( 0 : N0 / (1 : Yes )"))
while(a not in [0,1]):
    print("Please type either 0 or 1")
    a=int(input("Would You like to set input Vectors ? ( 0 : N0 / (1 : Yes )"))
if(a==1):
    root.vectorObject.A0,root.vectorObject.A1,root.vectorObject.A2=[float(i) for i in input("Input vector A (Space seperated): ").split()]
    root.vectorObject.B0,root.vectorObject.B1,root.vectorObject.B2=[float(i) for i in input("Input vector B (Space seperated): ").split()]

m5.instantiate()
print("Beginning simulation!")
event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), event.getCause()))