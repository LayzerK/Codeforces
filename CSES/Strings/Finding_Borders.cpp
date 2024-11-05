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

  for(int i = 1; i < n; i++){
    int suffix_start = n - i;

    long long prefixHash = hashes[i];

    long long suffixHash = (hashes[n] - hashes[suffix_start] + mod) % mod;

    int diff = n - i;
    if((prefixHash * pows[diff]) % mod == suffixHash){
      ans.push_back(i);
    }
  }
  for(int i = 0; i < ans.size(); i++){
    cout << ans[i] << " ";
  }


  
}

int main(){
  solve();
}