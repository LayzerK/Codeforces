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
  int n; cin >> n;
  vector<int> arr(n, 0);
  Fenny fen = Fenny(n);

  for(int i = 0; i < n; i++){
    cin >> arr[i];
    fen.set(i, 1);
  }

  for(int i = 0; i < n; i++){
    int rem; cin >> rem;

    int l = 0; int r = n-1;

    while(l <= r){
      int mid = (l+r)/2;
      
      int valid = fen.sum(mid);

      if(valid < rem){
        l = mid + 1;
      }
      else{
        r = mid - 1;
      }
    }

    cout << arr[l] << " ";
    fen.update(l, -1);
  }
}

int main(){
  solve();
  return 0;
}