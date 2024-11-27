#include <bits/stdc++.h>
using namespace std;
struct Fenny2d{
  vector<vector<int>> bit;
  vector<vector<int>> vals;
  int rLen; int cLen;

  Fenny2d(int n, int m){
    this->rLen=n+1;
    this->cLen = m+1;
    bit.resize(this->rLen, vector<int>(this->cLen, 0));
    vals.resize(n, vector<int>(m, 0));
  }

  Fenny2d(vector<vector<int>> const &arr) : Fenny2d(arr.size(), arr[0].size()){
    
    for (int i = 0; i < arr.size(); i++){
      for(int j = 0; j < arr[0].size(); j++){
        set(i, j, arr[i][j]);
    }
  }
  }

  long long sum(int x, int y) {
    long long ret = 0;
    for (int i = x+1; i > 0; i -= i & -i){
      for(int j = y+1; j > 0; j -= j & -j){
        ret += bit[i][j];
      }
    }
    return ret;
  }

  long long sum(int x1, int y1, int x2, int y2){
    //x1, y1 == top left, x2, y2 == bottom right
    return sum(x2, y2) - sum(x1-1, y2) - sum(x2, y1-1) + sum(x1-1, y1-1);
  }

  void update(int x, int y, int delta) {
    vals[x][y] += delta;
    for (int i = x+1; i < rLen; i += i & -i){
      for(int j = y+1; j < cLen; j += j & -j){
        bit[i][j] += delta;
      }
    }
  }

  void set(int x, int y, int new_val){
    update(x, y, new_val - vals[x][y]);
  }
};

void solve(){
  int n; int q; cin >> n >> q;
  Fenny2d fen = Fenny2d(n, n);

  for(int x = 0; x < n; x++){
    string row; cin >> row;
    for(int y = 0; y < n; y++){
      int v = row[y] == '*' ? 1 : 0;
      fen.set(x, y, v);
    }
  }

  for(int i = 0; i < q; i++){
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << fen.sum(x1 -1, y1-1, x2-1, y2-1) << endl;
  }
}

int main(){
  solve();
  return 0;
}