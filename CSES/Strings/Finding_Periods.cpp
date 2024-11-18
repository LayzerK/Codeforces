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
  string s;
  cin >> s;
  int n = s.size();

  const int base = 9973;
  const int mod = 1e9 + 7;

  vector<long long> pows(n);
  vector<long long> hashes(n+1);

  pows[0] = 1;
  for(int i = 1; i < n; i++){
    pows[i] = (pows[i-1] * base) % mod;
  }
  for(int i = 0; i < n; i++){
    hashes[i+1] = (hashes[i] + (s[i] - 'a' + 1) * pows[i]) % mod;
  }
  vector<int> ans;
  for(int sz = 1; sz <= n; sz++){
    long long startHash = (hashes[sz] - hashes[0] + mod) % mod;
    bool valid = true;
    for(int start = 0; start < n; start += sz){
      long long subHash;
      if(start + sz > n){
        int leftOver = n-start;
        subHash = (hashes[min(n, start+sz)] - hashes[start] + mod) % mod;
        startHash = (hashes[leftOver] - hashes[0] + mod) % mod;
      }
      else{
        subHash = (hashes[min(n, start+sz)] - hashes[start] + mod) % mod;
      }
      if(subHash != (startHash * pows[start])%mod){
        valid = false;
        break;
      }
    }
    if(valid){
      ans.push_back(sz);
    }
  }
  for(int sz : ans){
    cout << sz << " ";
  }
}

int main(){
  solve();
  return 0;
}