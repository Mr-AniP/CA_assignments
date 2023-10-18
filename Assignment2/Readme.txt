************************************************************************************************************************************************************************
> Start of Readme file 


> This Readme file is for the assignment 2 of Computer architecture course done by Animesh Pareek.


> How to Run the code
1)First place the all files accept the run_mysimObject.py in the gem5/src/assignment2 folder .
2)Place run_mysimObject.py in the gem5/config folder
3)Now rebuild gem5 -> python3 (which scons) build/X86/gem5.opt
4)Run the file by -> build/X86/gem5.opt --debug-flags=VECTOR,RESULTCROSS,RESULTSUB,NORMALIZE configs/ca/Animeshpareek_2021131_SA2/run_mysimObject.py
** Note -> Please run above two commands in correct directory


> Code Explanation
)!-_-!( Readme file  is the info file ( just to be precise :) )

)!-_-!( run_mysimObject.py file does => 
******* Creation of our VectorOperations object
******* Taking inputs and then passing them as params to our Vectoroperations Object
******* Doing Similation of created object
******* It is the Configuration script of our assignment

)!-_-!( MysimObject.py file does =>
******* Maintainence of python class VectorObject ( As a Simulation Object )
******* Also Keeping track of additional paramaters of this class which then can be used by our .cc file

)!-_-!( VectorOperations.hh file does =>
******* Declearation of our File Macro ( for use of internel gem5 files )
******* Maintainence of Declarations of our .cc file Including the class structure and various events for our Simulation object
******* It is the Header file for our object after all

)!-_-!( SConscript file does => 
******* Generating Debug Flags
******* Keeping track of our code files and object files
******* To build the object (Basically to help integration of our custom object to m5 object so that we can use it in our configuration scripts [ in configs folder ] )
******* It is a scons file after all ( use to build stuff via the python )

)!-_-!( VectorOperations.cc file does =>
******* Maintain the Defination of our Functions declared in the header file
******* Here first constructor Sets all events and Vectors
******* Startup function sets the srtart time of all the events
******* At the end we define the event-process functions of these 3 events
******* I personaly don't feel that there is much to explain in the event-processes
******* C'mon they are just hardcoded logic functions of basic vector multiplication, subtraction and normalization
******* Refer to pre-Jee notes to understand maths/Logic of this Operations, then you'll get them


> EndNote-> Please be carefull of the fact that this code was created to support 2 float 3*1 vector Operations.
            Thus Please give input carefully.


> End of Readme file 
************************************************************************************************************************************************************************
