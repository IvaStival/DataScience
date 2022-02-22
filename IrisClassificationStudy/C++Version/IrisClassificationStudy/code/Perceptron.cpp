//
//  Perceptron.cpp
//  IrisClassificationStudy
//
//  Created by ivastival on 22/11/21.
//

#include "Perceptron.hpp"

Perceptron::Perceptron(){
    this->seed = 45;
    this->eta  = 0.01;
    this->iter_num = 50;
}

Perceptron::Perceptron(int seed, float eta, int iter_num){
    this->seed = seed;
    this->eta  = eta;
    this->iter_num = iter_num;
}

Perceptron::~Perceptron(){
    delete this->W;
}

void Perceptron::fit(const vector< vector<float> >& X, const vector<int>& Y){
    
    // SET THE WEIGHTS SIZE, IT'S THE TOTAL COLUMNS (CHARACTERISTICS) + THE BIAS WEIGHT
    unsigned long var_number = X[0].size()+1;
    this->W = new vector<float>(var_number,0);
    
    srand(1);
    
    // POPULATE WITH RANDOM VALUES
    std::generate(this->W->begin(), this->W->end(), [](){
        return ((rand() % 10)/ 5.0) + 0.01;
    });
    
    float update = 0.0;
    int error;
    
    for(int i=0; i < this->iter_num; ++i){
        vector<vector<float>>::const_iterator x_it = X.begin();
        vector<int>::const_iterator y_it = Y.begin();
        error = 0.0;
        
        for(; x_it != X.end(); ++x_it, ++y_it){
            update = this->eta * (*y_it - this->predict(*x_it));
            
            if(update != 0) error += 1;
            
            this->updateWeights(update, *x_it);
        }
        this->errors.push_back(error);
    }
//    copy(this->W->begin(), this->W->end(), std::ostream_iterator< float >(cout, ", "));
}

// PREDICT RETURN A SIMPLE PREDTICTION RESULT IF THE net_input() IS BIGGER OR EQUAL TO 0 RETURN 1 ELSE RETURN -1
int Perceptron::predict(const vector<float> &X){
    if(this->net_input(X) >= 0.0) return 1; else return -1;
}

// LINEAR FUNCTION BETWEEN THE X DATA CHARACTERISTICS AND RANDOM GENERATED WEIGHTS
float Perceptron::net_input(const vector<float> &X){

    vector<float> w_temp(this->W->begin() + 1, this->W->end());
    float result = UtilsMath::dot(X, w_temp) + (*this->W)[0];
    return result;
}

// FUNCTION TO UPDATE THE WEIGHTS BASED ON THE ERROR OF PREDICT
void Perceptron::updateWeights(float update, const vector<float> &X){
    // UPDATE THE BIAS WEIGHT
    (*this->W)[0] += update;
    
    vector<float>::iterator w_it = this->W->begin();
    vector<float>::const_iterator x_it = X.begin();

    // UPDATE EACH CHARACTERISTICS WEIGHTS
    vector<float> w_temp(this->W->begin() + 1, this->W->end());
    for(;w_it != this->W->end(); ++w_it, ++x_it){
        *w_it += update * *x_it;
    }
}


void Perceptron::printErrors(){
    copy(this->errors.begin(), this->errors.end(), std::ostream_iterator<int>(cout, " ,"));
}
