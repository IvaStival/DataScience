//
//  Utils.hpp
//  IrisClassificationStudy
//
//  Created by ivastival on 30/11/21.
//

#ifndef Utils_hpp
#define Utils_hpp

#include <iostream>
#include <ostream>
#include <vector>
#include <iomanip>

using std::vector;

class Utils{
private:
    Utils();
    ~Utils();
    
public:
    template<typename T>
    static void printMatrix(const vector<vector<T>>& matrix);
    
    template<typename T>
    static void printMatrix(const vector<T>& matrix);
    
};

//OPERATOR OVERLOAD
template<typename T>
std::ostream& operator << (std::ostream& os, const vector<vector<T>>& v){
    
    for(typename vector<vector<T>>::const_iterator it_row = v.begin(); it_row != v.end(); ++it_row){
        for(typename vector<T>::const_iterator it_col = (*it_row).begin(); it_col != (*it_row).end(); ++it_col){
            std::cout << std::setw(8) << *it_col << " ";
        }
        std::cout << std::endl;
    }
    return os;
}

//// SUM
template<typename T>
vector<T> operator + (vector<T> &a, vector<T> &b){
    
    vector<T> result(a.size(),0);
    
    if(a.size() != b.size()) {
        std::cout << "Wrong vector size." << std::endl;
        return {};
    }
    
    for(int i = 0; i < a.size(); ++i){
        result[i] = a[i] + b[i];
    }
    
    return result;
}

template<typename T>
vector<T> operator + (T &a, vector<T> &b){
    
    vector<T> result(b.size(),0);
    
    for(int i = 0; i < b.size(); ++i){
        result[i] = a + b[i];
    }
    
    return result;
}

template<typename T>
vector<T> operator + (vector<T> &b, T &a){
    
    vector<T> result(b.size(),0);
    
    for(int i = 0; i < b.size(); ++i){
        result[i] = a + b[i];
    }
    
    return result;
}

//// MULTIPLICATION
template<typename T>
vector<T> operator * (T &a, vector<T> &b){
    
    vector<T> result(b.size(),0);
    
    for(int i = 0; i < b.size(); ++i){
        result[i] = a * b[i];
    }
    
    return result;
}

template<typename T>
vector<T> operator * (vector<T> &b, T &a){
    
    vector<T> result(b.size(),0);
    
    for(int i = 0; i < b.size(); ++i){
        result[i] = a * b[i];
    }
    
    return result;
}

template<typename T>
vector<vector<T>> operator * (vector<vector<T>> &b, T &a){
    
    vector<vector<T>> result(b.size(),vector<T>(b[0].size(),0));
    
    for(int i = 0; i < b.size(); ++i){
        for(int j = 0; j < b[i].size(); ++j){
            result[i][j] = a * b[i][j];
        }
    }
    return result;
}

template<typename T>
vector<vector<T>> operator * (T &a, vector<vector<T>> &b){
    
    vector<vector<T>> result(b.size(),vector<T>(b[0].size(),0));
    
    for(int i = 0; i < b.size(); ++i){
        for(int j = 0; j < b[i].size(); ++j){
            result[i][j] = a * b[i][j];
        }
    }
    
    return result;
}

// PRINT MATRIX
template<typename T>
void Utils::printMatrix(const vector<vector<T>>& matrix){
    std::cout << matrix << std::endl;
}

template<typename T>
void Utils::printMatrix(const vector<T>& matrix){
    
//    std::cout << std::fixed << std::setprecision(2);
    for(typename vector<T>::const_iterator it = matrix.begin(); it != matrix.end(); ++it){
        std::cout << std::setw(6) << *it << std::endl;
    }
    std::cout << std::endl;
}

#endif /* Utils_hpp */








