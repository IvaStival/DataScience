//
//  AdalineSGD.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 06/12/21.
//

#ifndef AdalineSGD_hpp
#define AdalineSGD_hpp

#include <iostream>
#include <vector>

#include "Model.hpp"

using std::cout;
using std::endl;
using std::vector;

class AdalineSGD : public Model{

public:
    AdalineSGD();
    AdalineSGD(float eta, int iter_num, int seed, bool std);
    ~AdalineSGD();
    
    void fit(const vector<vector<float>> &X, const vector<int> &Y);
};

#endif /* AdalineSGD_hpp */
