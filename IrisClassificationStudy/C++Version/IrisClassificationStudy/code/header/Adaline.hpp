//
//  Adaline.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 26/11/21.
//

#ifndef Adaline_hpp
#define Adaline_hpp

#include <iostream>
#include <vector>

#include "UtilsMath.hpp"
#include "Utils.hpp"

using std::cout;
using std::vector;
using std::copy;

class Adaline{
private:
    float eta;
    int   iter_num;
    int   seed;
    bool  std;
    
    vector<float> *W;
    vector<float> cost;
    
public:
    Adaline();
    Adaline(float eta, int iter_num, int seed, bool std);
    ~Adaline();
    
    void fit(const vector< vector<float> > &X, const vector<int> &Y);
    float predict(const vector<float> &X);
    
    float net_input(const vector<float> &X);
    float activation(float y_line);
    
    void updateWeights(vector<float> errors, const vector< vector<float> > &X);
    vector<vector<float>> stdX(vector<vector<float>> X);
    void printErrors();
    
    vector<float>& getCost();
};

#endif /* Adaline_hpp */
