#ifndef __ASSIGNMENT2_VECTOROPERATIONS_HH__
#define __ASSIGNMENT2_VECTOROPERATIONS_HH__

#include "params/VectorOperations.hh"
#include "sim/sim_object.hh"

namespace gem5
{

class VectorOperations : public SimObject
{
  private:
    float A[3],B[3];
    const Tick ticksubtraction,ticknormalize,tickproduct;
    void processVectorCrossProduct();
    void processNormalizeVector();
    void processVectorSubtraction();
    EventFunctionWrapper VectorCrossProduct;
    EventFunctionWrapper NormalizeVector;
    EventFunctionWrapper VectorSubtraction;
  public:
    VectorOperations(const VectorOperationsParams &p);
    void startup() override;
};

} // namespace gem5

#endif // __ASSIGNMENT2_MYSIiMOBJECT_HH__
