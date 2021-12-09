//
//  AdalineSGD.cpp
//  IrisClassificationStudy
//
//  Created by ivastival on 06/12/21.
//

#include "AdalineSGD.hpp"

AdalineSGD::AdalineSGD(){}

AdalineSGD::AdalineSGD(float eta, int iter_num, int seed, bool std) : Model(eta, iter_num, seed, std){}

AdalineSGD::~AdalineSGD(){}

void AdalineSGD::fit(const vector<vector<float>> &X, const vector<int> &Y){
    cout << this->eta << endl;
}
