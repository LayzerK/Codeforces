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
    
    for (int i = 0; i < size-1; i++){
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

int compress(vector<int>& nums, int val){
  return upper_bound(nums.begin(), nums.end(), val) - nums.begin() - 1;
}

void solve(){
  int n, q;
  cin >> n >> q;
  
  vector<int> nums;
  vector<int> salaries(n,0);
  vector<tuple<char, int, int>> queries;

  for(int i = 0; i < n; i++){
    cin >> salaries[i];
    nums.push_back(salaries[i]);
  }

  for(int i = 0; i < q; i++){
    char type; int a; int b; cin >> type >> a >> b;
    queries.push_back(make_tuple(type, a, b));

    if(type == '?'){
      nums.push_back(a);
    }
    nums.push_back(b);
  }

  sort(nums.begin(), nums.end());
  nums.erase(unique(nums.begin(), nums.end()), nums.end());


  int size = nums.size();
  vector<int> freqs(size, 0);

  for(int salary : salaries){
    freqs[compress(nums, salary)] += 1;
  }

  Fenny fen = Fenny(freqs);


  for(auto& query : queries){
    char type = get<0>(query);

    if(type == '?'){
      int lb = compress(nums, (get<1>(query)));
      int rb = compress(nums, (get<2>(query)));

      cout << fen.sum(lb, rb) << endl;
    }
    else{
      int k = get<1>(query);
      int new_val = get<2>(query);

      int old_val = salaries[k-1];
      salaries[k-1] = new_val;
      if(new_val != old_val){
        fen.update(compress(nums, old_val), -1);
        fen.update(compress(nums, new_val), 1);
      }
    }
  }


}

int main(){
  solve();
  return 0;
}