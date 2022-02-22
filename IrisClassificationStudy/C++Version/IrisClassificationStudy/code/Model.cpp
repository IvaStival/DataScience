//
//  Model.cpp
//  IrisClassificationStudy
//
//  Created by ivastival on 06/12/21.
//

#include "Model.hpp"

Model::Model(){}

Model::Model(float eta, int iter_num, int seed, bool std) : eta(eta), iter_num(iter_num), seed(seed), std(std){}

Model::~Model(){}

float Model::net_input(const vector<float> &X){
    vector<float> w_temp(this->W->begin()+1, this->W->end());
    
    return UtilsMath::dot(X, w_temp) + (*this->W)[0];
}

float Model::predict(const vector<float> &X){
    
    if(this->activation(this->net_input(X)) >= 0.0) return 1; else return -1;
}

float Model::activation(float y_line){
    return y_line;
}


void Model::updateWeigths(vector<float> &errors, const vector<vector<float>> &X){
    (*this->W)[0] += this->eta * UtilsMath::sum(errors);
    
    vector<float> w_temp(this->W->begin() + 1, this->W->end());
    
    vector<float> n_correction = UtilsMath::dot(UtilsMath::transpose(X), errors);
    n_correction = n_correction * this->eta;
    
    for(int i = 0; i < n_correction.size(); ++i){
        (*this->W)[i+1] = (*this->W)[i+1] + n_correction[i];
    }
}

vector<vector<float>> Model::stdX(const vector<vector<float>> &X){
    vector<vector<float>> x_temp = UtilsMath::transpose(X);
    
    for(vector<vector<float>>::iterator it = x_temp.begin(); it != x_temp.end(); ++it){
        float mean = UtilsMath::mean(*it);
        float std  = UtilsMath::std(*it);
        
        for(vector<float>::iterator it2 = it->begin(); it2 != it->end(); ++it2){
            *it2 = (*it2 - mean) / std;
        }
    }
    return UtilsMath::transpose(x_temp);
}

vector<vector<float>> Model::shuffle(const vector<vector<float>> &X){
    vector<vector<float>> x_temp(X.begin(), X.end());
    vector<int> index(X.size(),0);
    
    int count = 0;
    std::generate(index.begin(), index.end(), [count]() mutable { return (count++);} );
    
    auto rng  = std::default_random_engine{};
    std::shuffle(index.begin(), index.end(), rng);
    
    Utils::printMatrix(index);
    
    return x_temp;
}
