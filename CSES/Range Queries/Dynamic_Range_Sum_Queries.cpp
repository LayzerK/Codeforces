#include <bits/stdc++.h>
using namespace std;
struct Sqrt{
  int block_size;
  vector<int> nums;
  vector<long long> blocks;
  Sqrt(int b_size, vector<int> arr) : block_size(b_size), blocks(b_size, 0){
    nums = arr;
    for(int i = 0; i < nums.size(); i++){
      blocks[i/block_size] += nums[i];
    }
  }

  long long query(int l, int r){
    long long ret = 0;
    int left_block = l/block_size;
    int right_block = r/block_size;

    if(left_block == right_block){
      for(int i = l; i <= r; i++){
        ret += nums[i];
      }
    }
    else{
      int l_end = (left_block + 1) * block_size - 1;
      for(int i = l; i <= l_end; i++){
        ret += nums[i];
      }
      for(int i = left_block + 1; i <= right_block - 1; i++){
        ret += blocks[i];
      }
      for(int i = right_block * block_size; i <= r; i++){
        ret += nums[i];
      }
    }
    return ret;
  }

  void set(int i, int new_val){
    int block = i/block_size;
    blocks[block] -= nums[i];
    nums[i] = new_val;
    blocks[block] += new_val;
  }
};

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

void sqrt_solve(){
  int n; int q; cin >> n >> q;
  vector<int> arr(n, 0);
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  Sqrt sqrtD = Sqrt(ceil(sqrt(n)), arr);

  for(int i = 0; i < q; i++){
    int type; cin >> type;

    if(type == 1){
      int change_index; int new_val; cin >> change_index >> new_val;
      sqrtD.set(--change_index, new_val);
    }
    else{
      int l; int r; cin >> l >> r;
      cout << sqrtD.query(--l ,--r) << endl;
    }
  }
}

void fenny_solve(){
  int n; int q; cin >> n >> q;
  vector<int> arr(n, 0);
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  Fenny fen = Fenny(arr);

  for(int i = 0; i < q; i++){
    int type; cin >> type;

    if(type == 1){
      int change_index; int new_val; cin >> change_index >> new_val;
      fen.set(--change_index, new_val);
    }
    else{
      int l; int r; cin >> l >> r;
      cout << fen.sum(--l ,--r) << endl;
    }
  }
}

int main(){
  //sqrt_solve();
  fenny_solve();
  return 0;
}