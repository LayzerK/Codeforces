#include <bits/stdc++.h>
using namespace std;
struct Fenny{
  vector<long long> bit;
  vector<int> vals;
  int size;

  Fenny(int n){
    this->size=n+1;
    bit.assign(n+1, 0);
    vals.assign(n, 0);
  }

  Fenny(vector<int> const &arr) : Fenny(arr.size()){
    
    for (int i = 0; i < size; i++){
      set(i, arr[i]);
    }
  }

  long long sum(int idx) {
      long long ret = 0;
      for (++idx; idx > 0; idx -= idx & -idx)
          ret += bit[idx];
      return ret;
  }

  long long sum(int l, int r){
    return sum(r) - sum(l-1);
  }

  void update(int idx, int delta) {
    vals[idx] += delta;
    for (++idx; idx < size; idx += idx & -idx)
        bit[idx] += delta;
  }

  void set(int idx, int new_val){
    update(idx, new_val - vals[idx]);
  }
};

void solve(){
  int n; int q; cin >> n >> q;
  Fenny fen = Fenny(n);

  for(int i = 0; i < n; i++){
    int v; cin >> v;
    fen.update(i, v);
    fen.update(i+1, -v);
  }


  for(int i = 0; i < q; i++){
    int type; cin >> type;

    if(type == 1){
      int l, r, delta; cin >> l  >> r >> delta;
      fen.update(--l, delta);
      fen.update(r, -delta);
    }
    else{
      int idx; cin >> idx;
      cout << fen.sum(--idx) << endl;
    }
  }
}

int main(){
  solve();
  return 0;
}