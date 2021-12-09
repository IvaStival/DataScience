//
//  Adaline.cpp
//  IrisClassificationStudy
//
//  Created by ivastival on 26/11/21.
//

#include "Adaline.hpp"

extern bool _DEBUG;

// eta IS USED TO REGULATE THE WEIGHT DECREASE STEP, IF IT NOT EXISTS THE STEP WILL BE MUCH BIGGER AND WE NOT GET THE SMALLER WEIGHT
// iter_num IS THE NUMBER OF ITERETIONS
// seed IS USED TO SET THE RANDOM INITIALIZATIOS
Adaline::Adaline(){
    this->eta = 0.01;
    this->iter_num = 10;
    this->seed = 45;
    this->std = false;
}

Adaline::Adaline(float eta, int iter_num, int seed, bool std){
    this->eta = eta;
    this->iter_num = iter_num;
    this->seed = seed;
    this->std = std;
}

Adaline::~Adaline(){}

void Adaline::fit(const vector< vector<float> > &X, const vector<int> &Y){
    // SET THE WEIGHTS SIZE, IT'S THE TOTAL COLUMNS (CHARACTERISTICS) + THE BIAS WEIGHT
//    unsigned long var_number = X[0].size()+1;
//    this->W = new vector<float>(var_number,0);
    this->W = new vector<float>({0.01, 0.01, 0.01});

    srand(1);
    
    // POPULATE WITH RANDOM VALUES
//    std::generate(this->W->begin(), this->W->end(), [](){
//        return ((rand() % 10)/ 10.0) + 0.01;
//    });
    vector<vector<float>> x;
    
    // IF WE WANT THE X VALUES STANDARDIZED ...
    if(this->std) x = this->stdX(X);
    else x = X;

    
    float error;
    
    // INIT FOR BY THE NUMBER OF ITERATIONS CHOOSED
    for(int i=0; i < this->iter_num; ++i){
        vector<vector<float>>::const_iterator x_it = x.begin();
        vector<int>::const_iterator y_it = Y.begin();
        
        vector<float> errors;
        error = 0.0;
        
        
        for(; x_it != x.end(); ++x_it, ++y_it){
            float net_result = this->net_input(*x_it);
            float output = this->activation(net_result);
            error = (*y_it - output);
            
            errors.push_back(error);
        }
        
        // UPDATE THE WEIGHTS USING THE SSE (SUM SQUARED ERROR) DERIVADE 
        this->updateWeights(errors, X);
        
        // SAVE THE MSE
        this->cost.push_back(UtilsMath::squareError(errors));
    }
    
}

// PREDICT METHOD RETURN THE CLASS BASED ON THE net_input METHOD RETURN
float Adaline::predict(const vector<float> &X){
    if(this->activation(this->net_input(X) >= 0.0)) return 1; else return -1;
}

// BASED ON THE X VALUES PREDICT A VALUE USED TO PREDICT THE CLASS
float Adaline::net_input(const vector<float> &X){
    vector<float> w_temp(this->W->begin() + 1, this->W->end());
    
    // FIRST DEGREE FUNCTION (y = ax + b)
    return UtilsMath::dot(X, w_temp) + (*this->W)[0];
}

// NOW RETURN THE NET_INPUT RESULT y', AFTER WE WILL USE ACTIVATIONS FUNCTIONS
float Adaline::activation(float y_line){
    return y_line;
}

// METHOD TO UPDATE THE WEIGHTS
// HERE WE USE THE MSE DERIVETIVE TO DECREASE THE WEIGHTS
void Adaline::updateWeights(vector<float> errors, const vector< vector<float> > &X){
    
    (*this->W)[0] += this->eta * UtilsMath::sum(errors);
    
    vector<float> w_temp(this->W->begin()+1, this->W->end());

    vector<float> n_correction = UtilsMath::dot(UtilsMath::transpose(X), errors);
    n_correction = n_correction * this->eta;
    
    if(_DEBUG) Utils::printMatrix(*this->W);
    for(int i = 0; i < n_correction.size(); ++i){
        (*this->W)[i+1] = (*this->W)[i+1] + n_correction[i];
    }
    if(_DEBUG) Utils::printMatrix(*this->W);
    
}

vector<vector<float>> Adaline::stdX(vector<vector<float>> X){
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

void Adaline::printErrors(){
    copy(this->cost.begin(), this->cost.end(), std::ostream_iterator<int>(cout, ", "));
    
}

// ACCESSORS
vector<float>& Adaline::getCost(){
    return this->cost;
}
