//
//  math.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 22/11/21.
//

#ifndef UtilsMath_hpp
#define UtilsMath_hpp

#include <iostream>
#include <numeric>
#include <vector>
#include <math.h>

using std::vector;
using std::cout;
using std::endl;

extern bool _DEBUG;

class UtilsMath{
private:
    UtilsMath();
    ~UtilsMath();

public:
    template<typename T>
    static vector< vector<T>> dot(const std::vector< std::vector<T> > &X, const std::vector< std::vector<T> > &W);

    template<typename T>
    static vector<T> dot(const std::vector< std::vector<T> > &X, const std::vector<T> &W);
    
    template<typename T>
    static T dot(const std::vector<T> &X, const std::vector<T> &W);
    
    template<typename T>
    static vector< vector<T> > transpose(const vector< vector<T> >& v);
    
    static float sum(const std::vector<float>& v);
    
    static float squareError(const vector<float>& v);
    
    template<typename T>
    static float mean(const vector<T> v);
    
    template<typename T>
    static float std(const vector<T> v);

};
template<typename T>
std::vector< std::vector<T> > UtilsMath::dot(const std::vector< std::vector<T> > &X, const std::vector< std::vector<T> > &W){
    
    float value = 0;
    
    unsigned long x_row_size = X.size();
    unsigned long x_col_size = X[0].size();
    
    unsigned long w_row_size = W.size();
    unsigned long w_col_size = W[0].size();
    
    
    if(x_col_size != w_row_size){
        cout << "Error: Matrix size error. The column size of the X need to be equal to the row size of the W."<< endl;
        cout << x_row_size << "x" << x_col_size << " - " << w_row_size << "x" << w_col_size << endl;
        return {};
    }
    else{
        if(_DEBUG){
            cout << "OK!!" << endl;
            cout << x_row_size << "x" << x_col_size << " - " << w_row_size << "x" << w_col_size << " == " << x_row_size << "x" << w_col_size<< endl;
        }
    }
    
    vector<vector<T>> result(X.size(), vector<T>(W[0].size(), 0));
    typename vector<vector<T>>::iterator it = result.begin();
    
    vector<vector<T>> w_aux = UtilsMath::transpose(W);
    
    for(auto& vec_x : X){
        typename vector<T>::iterator it_vec = (*it).begin();
        
        for(auto& vec_w : w_aux){
            *it_vec = std::inner_product(vec_x.begin(), vec_x.end(), vec_w.begin(), 0);
            ++it_vec;
        }
        it++;
    }
    return result;
}

template<typename T>
std::vector<T> UtilsMath::dot(const std::vector< std::vector<T> > &X, const std::vector<T> &W){
    
    unsigned long x_row_size = X.size();
    unsigned long x_col_size = X[0].size();
    
    unsigned long w_row_size = W.size();
    
    if(x_col_size != w_row_size){
        cout << "Error: Matrix size error. The column size of the X need to be equal to the row size of the W." << endl;
        cout << x_row_size << "x" << x_col_size << " - " << w_row_size << "x" << 1 << endl;
        return {};
    }
    else{
        if(_DEBUG){
            cout << "OK!!" << endl;
            cout << x_row_size << "x" << x_col_size << " - " << w_row_size << "x" << 1 << " == " << x_row_size << "x" << 1 << endl;
        }
    }
    
    vector<T> result(X.size());
    typename vector<T>::iterator it = result.begin();
    
    for(auto& vec_x : X){
        *it = std::inner_product(vec_x.begin(), vec_x.end(), W.begin(), 0);
        ++it;
    }
    return result;
}

template<typename T>
T UtilsMath::dot(const vector<T> &X, const vector<T> &W){
    return std::inner_product(X.begin(), X.end(), W.begin(), 0);
}


template<typename T>
vector< vector<T> > UtilsMath::transpose(const vector< vector<T> >& v){
    
    int N = v.size();
    int M = v[0].size();
    
    vector< vector<T>> result(M, vector<T>(N,0));
    typename vector< vector<T>>::iterator it = result.begin();
    
    int count = 0;
    
    //    for(int i=0; i < M; ++i){
    //        for(int j=0; j < N; ++j){
    //            std::cout << v[j][i] <<std::endl;
    //        }
    //        std::cout <<std::endl;
    //    }
    
    for(int n = 0; n < N*M; ++n){
        int i = n/N;
        int j = n%N;
        
        (*it)[count] = v[j][i];
        count++;
        
        if(j == N-1){
            it++;
            count = 0;
        }
    }
    return result;
}


template<typename T>
float UtilsMath::mean(const vector<T> v){
    float size = v.size();
    float result = 0.0;
    for(typename vector<T>::const_iterator it = v.begin(); it != v.end(); ++it){
        result += *it;
    }
    return result / size;
}

template<typename T>
float UtilsMath::std(const vector<T> v){
    float mean = UtilsMath::mean(v);
    float result = 0.0;
    float size = v.size();
    for(typename vector<T>::const_iterator it = v.begin(); it != v.end(); ++it){
        result += pow(*it - mean, 2);
    }
    
    return result / size;
}

#endif /* math_hpp */
