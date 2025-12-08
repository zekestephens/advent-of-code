#!/bin/bash
#self executing -*- c++ -*- file
sed '1s/.*/#if 0/' "$0" | g++ -x c++ -o /tmp/a.$$ - && exec /tmp/a.$$ "$@"
#endif
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
   // part one
   vector<int> rights;
   vector<int> lefts;
   int lhs, rhs;
   auto f = std::ifstream{"input.txt"};
   while (f >> lhs) {
      f >> rhs;
      lefts.push_back(lhs);
      rights.push_back(rhs);
   }
   sort(lefts.begin(), lefts.end());
   sort(rights.begin(), rights.end());

   int total = 0;
   for (int i = 0; i < lefts.size(); ++i) {
      total += abs(lefts[i] - rights[i]);
   }
   cout << total << '\n';

   int similarity = 0;
   // part two
   for (int n : lefts) {
      similarity += n*count(rights.begin(), rights.end(), n);
   }

   cout << similarity << '\n';
}
