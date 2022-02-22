//
//  Model.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 06/12/21.
//

#ifndef Model_hpp
#define Model_hpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

#include "UtilsMath.hpp"
#include "Utils.hpp"

using std::vector;

class Model{
protected:
    float eta;
    int   iter_num;
    int   seed;
    bool  std;
    
    vector<float> *W;
    vector<float> cost;

public:
    Model();
    Model(float eta, int iter_num, int seed, bool std);
    ~Model();
    
    float net_input(const vector<float> &X);
    
    float predict(const vector<float> &X);
    
    float activation(float y_line);
    
    void updateWeigths(vector<float> &errors, const vector<vector<float>> &X);
    
    vector<vector<float>> stdX(const vector<vector<float>> &X);
    
    vector<vector<float>> shuffle(const vector<vector<float>> &X);
};

#endif /* Model_hpp */
