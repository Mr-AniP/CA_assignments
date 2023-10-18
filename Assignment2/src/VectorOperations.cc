#include <iostream>
#include <cmath>

#include "base/trace.hh"
#include "debug/VECTOR.hh"
#include "debug/RESULTCROSS.hh"
#include "debug/NORMALIZE.hh"
#include "debug/RESULTSUB.hh"

#include "assignment2/VectorOperations.hh"

namespace gem5{
    VectorOperations::VectorOperations(const VectorOperationsParams &p):
        SimObject(p),
        VectorCrossProduct([this](){processVectorCrossProduct();},name()),
        NormalizeVector([this](){processNormalizeVector();},name()),
        VectorSubtraction([this](){processVectorSubtraction();},name()),
        ticknormalize(p.ticknormalize),
        tickproduct(p.tickproduct),
        ticksubtraction(p.ticksubtraction)
    {   A[0]=p.A0;A[1]=p.A1;A[2]=p.A2;
        B[0]=p.B0;B[1]=p.B1;B[2]=p.B2;
        DPRINTF(VECTOR, "A = { %f , %f , %f }\tB = { %f , %f , %f }\n",A[0],A[1],A[2],B[0],B[1],B[2]);
    }
    void VectorOperations::startup(){
        schedule(VectorCrossProduct,tickproduct);
        schedule(NormalizeVector,ticknormalize);
        schedule(VectorSubtraction,ticksubtraction);
    }
    void VectorOperations::processNormalizeVector(){
        float C[3],D[3];
        float lenA= sqrtf((A[0]*A[0]) + (A[1]*A[1]) + (A[2]*A[2]));
        float lenB= sqrtf((B[0]*B[0]) + (B[1]*B[1]) + (B[2]*B[2]));
        for(int i=0;i<3;i++){
            C[i]=A[i]/lenA;
            D[i]=B[i]/lenB;
        }
        DPRINTF(NORMALIZE, "Normalized A = { %f , %f , %f }\tNormalized B = { %f , %f , %f }\n",C[0],C[1],C[2],D[0],D[1],D[2]);
    }
    void VectorOperations::processVectorCrossProduct(){
        float C[3];
        int k,j;
        for(int i=0;i<3;i++){
            k=(i+1)%3;
            j=(k+1)%3;
            C[i]=A[k]*B[j]-B[k]*A[j];
        }
        DPRINTF(RESULTCROSS, "A x B = { %f , %f , %f }\n",C[0],C[1],C[2]);
    }
    void VectorOperations::processVectorSubtraction(){
        float C[3];
        for(int i=0;i<3;i++){
            C[i]=A[i]-B[i];
        }
        DPRINTF(RESULTSUB, "A - B = { %f , %f , %f }\n",C[0],C[1],C[2]);
    }
}
