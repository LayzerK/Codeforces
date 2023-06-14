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
 
using i64 = long long;

const int N = 20, M = 4;
int sz;
string num;

i64 dfs(int i, int cnt, bool upper){

  if(i >= n || cnt > 3){
    return 0;
  }

  if(i == n){
    return 1;
  }

  if(dp[i][cnt][upper] != -1){
    return dp[i][cnt][upper]
  }

  int rb;

  if(upper){
    rb = num[i];
  }
  else{
    rb = 9;
  }

  i64 ans = 0;
  int cap = num[i] - '0'
  for(int digit = 0; digit < 10; digit++){
    bool atbnd = upper && (digit == cap)

    if(digit == 0){
      ans += dfs(i+1, cnt, atbnd);
    }
    else{
      ans += dfs(i+1, cnt+1, atbnd);
    }
    if(atbnd){
      break;
    }
  }

}


i64 solve(i64 b){
  num = to_string(b);
  n = num.length();



    for (int i = 0; i < n; i++) {
        for (int j = 0; j < M; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 0; l < 2; l++) {
                    dp[i][j][k][l] = -1;
                }
            }
        }
    }

    return dfs(0,0, true);

}

void solve(){
  i64 L, R;

  cin >> L >> R;

  cout << solve(R) - solve(L-1) << "\n";
}


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t;
    cin >> t;
    while(t--) solve();
}