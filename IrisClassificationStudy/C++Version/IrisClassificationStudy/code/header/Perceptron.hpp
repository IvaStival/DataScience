//
//  Perceptron.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 22/11/21.
//

#ifndef Perceptron_hpp
#define Perceptron_hpp

#include <iostream>
#include <numeric>
#include <vector>
#include <iterator>
#include <time.h>

#include "UtilsMath.hpp"

using std::cout;
using std::vector;
using std::iterator;
using std::copy;

class Perceptron{
private:
    int seed;
    float eta;
    int iter_num;
    
    vector< vector <float> > X;
    vector< float > *W;
    
    vector<int> errors;
    
public:
    Perceptron();
    Perceptron(int seed, float eta, int iter_num);
    ~Perceptron();
    
    void fit(const vector< vector<float> > &X, const vector<int>& Y);
    int predict(const vector<float> &X);
    float net_input(const vector<float> &X);
    
    void updateWeights(float update, const vector<float> &X);
    
    void printErrors();
};

#endif /* Perceptron_hpp */
