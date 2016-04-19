// Compile it with:
// clang 
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
// #include "gnuplot-iostream.h"
// compile command: clang -fms-compatibility-version=19 .\cpp_read_file.cxx -o cpp_reader

using namespace std;

bool replace(std::string& str, const std::string& from, const std::string& to) {
    size_t start_pos = str.find(from);
    if(start_pos == std::string::npos)
        return false;
    str.replace(start_pos, from.length(), to);
    return true;
}

int main(int argc, char* argv[]) {
//  	Gnuplot gp;
    string line;
    ifstream myfile("data.csv");
    vector<float> y_values;
    vector<float> x_values;
  //  std::vector<boost::tuple<double, double> > pts_A;
    int first_read = 0;
    float iterator = 0.0;
    if (myfile.is_open()) {
        while ( getline (myfile,line) ) {
            if (first_read == 0) {
              first_read = 1;
              continue;
            }
            line.erase(0, line.find(';') + 1);
            string token = line.substr(0, line.find(';'));
            replace(token, ",", ".");
            float val = atof(token.c_str());
            y_values.push_back(val);
            x_values.push_back(iterator);
            iterator += 1.0;
        }
    myfile.close();
 // 	gp.send1d(pts_A);
 // 	gp.send1d(boost::make_tuple(x_values, y_values));
    }
    return 0;
}
