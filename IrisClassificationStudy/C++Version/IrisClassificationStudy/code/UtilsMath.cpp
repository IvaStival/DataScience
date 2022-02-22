//
//  math.cpp
//  IrisClassificationStudy
//
//  Created by ivastival on 22/11/21.
//

#include "UtilsMath.hpp"

UtilsMath::UtilsMath(){}

UtilsMath::~UtilsMath(){}


float UtilsMath::sum(const std::vector<float>& v){
    float result = 0.0;
    for(auto &value : v){
        result += value;
    }
    return result;
}

float UtilsMath::squareError(const vector<float>& v){
    
    float accumulator = 0.0;
    
    for(vector<float>::const_iterator it = v.begin(); it != v.end(); ++it){
        accumulator += (*it) * (*it);
    }
    
    return accumulator / 2.0;
}
