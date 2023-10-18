from m5.SimObject import SimObject
from m5.params import *
import array as arr
class VectorOperations(SimObject):
    type = 'VectorOperations'
    cxx_header = "assignment2/VectorOperations.hh"
    cxx_class = "gem5::VectorOperations"
    tickproduct = Param.Latency("150ps","Scheduling tick of VectorCrossProduct Event")
    ticknormalize = Param.Latency("1500ps","Scheduling tick of NormalizeVector Event")
    ticksubtraction = Param.Latency("15000ps","Scheduling tick of VectorSubtraction Event")
    A0= Param.Float(1.1, "First Vector[0]")
    A1= Param.Float(2.2, "First Vector[1]")
    A2= Param.Float(3.3, "First Vector[2]")
    B0= Param.Float(0.1, "Second Vector[0]")
    B1= Param.Float(0.2, "Second Vector[1]")
    B2= Param.Float(0.3, "Second Vector[2]")