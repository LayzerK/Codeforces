#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
using namespace std;
void solve(){
  int n; int tc; int start;
  cin >> n; cin >> tc; cin >> start;

  set<int> people;
  people.insert(start);

  for(int i = 1; i <= tc; i++){
    int dist;
    set<int> np;
    char ways;
    cin >> dist; cin >> ways;
    for(auto&loc : people){
      if(ways == '0' or ways == '?'){
        int right = ((loc + dist - 1) % n) + 1;
        np.insert(right);
      }
      if(ways == '1' || ways == '?'){
        int left = ((loc - dist - 1 + n) %n) + 1;
        np.insert(left);
      }
    }
    people = np;
  }

  cout << people.size() << "\n";
  for(auto&person : people){
    cout << person << " ";
  }



  
}

int main(){
  int tc;
  
  cin >> tc;

  while(tc--){
    solve();
  }
  return 0;
}