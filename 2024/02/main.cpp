#!/bin/bash
#self executing -*- c++ -*- file
sed '1s/.*/#if 0/' "$0" | g++ -std=c++23 -x c++ -o /tmp/a.$$ - && exec /tmp/a.$$ "$@"
#endif
#include <algorithm>
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
     

using namespace std;

bool is_valid(vector<int>& record) {
   int lt_count = 0;
   int gt_count = 0;
   int diff_count = 0;

   int pairs = record.size() - 1;
   for (int i = 0; i < pairs; ++i) {
      lt_count += record[i] < record[i + 1];
      gt_count += record[i] > record[i + 1];
      int diff = abs(record[i] - record[i + 1]);
      diff_count += diff >= 1 && diff < 4;
   }
   return (pairs == lt_count || pairs == gt_count) && pairs == diff_count;
}

bool is_dampener_valid(vector<int>& record) {
   if (is_valid(record)) {
      return true;
   }
   for (int i = 0; i < record.size(); ++i) {
      vector<int> filtered;
      for (int j = 0; j < record.size(); ++j) {
         if (j != i) {
            filtered.push_back(record[j]);
         }
      }
      if (is_valid(filtered)) {
         return true;
      }
   }
   return false;
}

int main() {
   auto f = std::ifstream{"input.txt"};
   vector<vector<int>> records;
   string line;
   while(getline(f, line)) {
      records.emplace_back();
      istringstream iss{line};
      int n;
      while (iss >> n) {
         records.back().push_back(n);
      }
   }
   cout << std::ranges::count_if(records, [](vector<int>& record){
      return is_valid(record);
   }) << '\n';
   cout << std::ranges::count_if(records, [](vector<int>& record){
      return is_dampener_valid(record);
   }) << '\n';
}
