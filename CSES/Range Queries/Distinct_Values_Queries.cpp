#include <bits/stdc++.h>
using namespace std;
int counts[200000];
struct Query{
  int left;
  int right;
  int index;

  Query(int l, int r, int i){
    left = l;
    right = r;
    index = i;
  }

  static bool cmp(const Query& a, const Query& b){
    return a.right < b.right;
  }
};

void solve(){
  int n; int q;
  cin >> n >> q;
  vector<int> arr(n, 0);
  int block_size = ceil(sqrt(n));
  memset(counts, 0, sizeof counts);
  map<int, int> compress;
  int compressVal;
  for(int i = 0; i < n; i++){
    int v; cin >> v;
    if(compress.find(v) == compress.end()){
      compress[v] = ++compressVal;
    }
    arr[i] = compress[v];
  }
  vector<vector<Query>> queries(block_size, vector<Query>());

  for(int i = 0; i < q; i++){
    int l; int r;
    cin >> l >> r;
    l--, r--;
    int block_index = l/block_size;
    queries[block_index].push_back(Query(l, r, i));
    //cout << "HERE" << endl;
  }

  int left = -1;
  int right = -1;
  int distinct = 0;

  vector<int> ans(q, 0);

  for(int i = 0; i < block_size; i++){
    sort(queries[i].begin(), queries[i].end(), Query::cmp);
    for(Query query : queries[i]){
      while(left < query.left){
        counts[arr[left]]--;
        if((counts[arr[left]]) == 0){
          distinct--;
        }
        left++;
      }
      while(left > query.left){
        left--;
        counts[arr[left]]++;
        if(counts[arr[left]] == 1){
          distinct++;
        }
      }

      while(right > query.right){
        counts[arr[right]]--;
        if(counts[arr[right]] == 0){
          distinct--;
        }
        right--;
      }
      
      while(right < query.right){
        right++;
        counts[arr[right]]++;
        if(counts[arr[right]] == 1){
          distinct++;
        }
      }
      
      ans[query.index] = distinct;
    }
  }

  for(int qv : ans){
    cout << qv << endl;
  }
}

int main(){
  
  solve();
  return 0;
}