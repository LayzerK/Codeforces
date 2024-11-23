#include <bits/stdc++.h>
using namespace std;
struct Sqrt{
  int block_size;
  vector<int> nums;
  vector<int> blocks;
  Sqrt(int b_size, vector<int> arr) : block_size(b_size), blocks(b_size, INT_MAX){
    nums = arr;
    for(int i = 0; i < nums.size(); i++){
      blocks[i/block_size] = min(blocks[i/block_size], nums[i]);
    }
  }

  int query(int l, int r){
    int mn = INT_MAX;
    int left_block = l/block_size;
    int right_block = r/block_size;

    if(left_block == right_block){
      for(int i = l; i <= r; i++){
        mn = min(mn,  nums[i]);
      }
    }
    else{
      int l_end = (left_block + 1) * block_size - 1;
      for(int i = l; i <= l_end; i++){
        mn = min(mn, nums[i]);
      }
      for(int i = left_block + 1; i <= right_block - 1; i++){
        mn = min(mn, blocks[i]);
      }
      for(int i = right_block * block_size; i <= r; i++){
        mn = min(mn, nums[i]);
      }
    }
    return mn;
  }

  void update(int idx, int v){
    int block = idx/block_size;
    int l = block*block_size;
    nums[idx] = v;
    blocks[block] = INT_MAX;
    for(int i = l; i < l + block_size; i++){
      blocks[block] = min(blocks[block], nums[i]);
    }
  }
};

void solve(){
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
      sqrtD.update(--change_index, new_val);
    }
    else{
    int l; int r; cin >> l >> r;
    cout << sqrtD.query(--l ,--r) << endl;
  }
}
}

int main(){
  solve();
  return 0;
}