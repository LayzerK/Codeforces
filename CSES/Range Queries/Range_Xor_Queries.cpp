#include <bits/stdc++.h>
using namespace std;
void solve(){
  int n; int q; 
  cin >> n >> q;
  vector<long long> prefix(n+1, 0);
  for(int i = 1; i <= n; i++){
    long long v; cin >> v;
    prefix[i] = prefix[i-1] ^ v;
  }
  for(int i = 0; i < q; i++){
    int l; int r; cin >> l >> r;
    cout << (prefix[r] ^ prefix[l-1]) << endl;
  }
}

int main(){
  solve();
  return 0;
}