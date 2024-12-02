#include <bits/stdc++.h>
using namespace std;
struct Seggy{
  vector<int> vals;
  vector<int> tree;
  int n;

  Seggy(vector<int> const &arr){
    int n = arr.size();
    vals.assign(n, 0);
    for(int i = 0; i < n; i++){
      vals[i] = arr[i];
    }
    while(__builtin_popcount(n) != 1){
      n++;
      vals.push_back(0);
    }

    tree.assign(2*n, 0);

    for(int i = 0; i < n; i++){
      tree[n+i] = vals[i];
    }
    for(int i = n-1; i >= 1; i--){
      tree[i] = max(tree[2*i], tree[2*i+1]);
    }
  }

  int query(int node, int node_low, int node_high, int query_low, int query_high){
    if(query_low <= node_low and node_high <= query_high){
      return tree[node];
    }
    if(node_high < query_low || query_high < node_low){
      return -1;
    }

    int mid = (node_low + node_high)/2;

    return max(query(2*node, node_low, mid, query_low, query_high), query(2*node+1, mid+1, node_high, query_low, query_high));
  }

  void update(int node, int node_low, int node_high, int query_low, int query_high, int new_val){
    if(query_low <= node_low and node_high <= query_high){
      tree[node] = new_val;
      return;
    }
    if(node_high < query_low || query_high < node_low){
      return;
    }

    int mid = (node_low + node_high)/2;

    update(node*2, node_low, mid, query_low, query_high, new_val);
    update(node*2+1, mid+1, node_high, query_low, query_high, new_val);
    tree[node] = max(tree[node*2], tree[node*2+1]);
  }

  int get_first(int node, int node_low, int node_high, int query_low, int query_high, int val){
    //first i >= val in the seg tree
    if(node_low> query_high || query_high < node_low){
      return -1;
    }
    if(tree[node] < val){
      return -1;
    }

    if(node_low == node_high){
      return node_low;
    }

    int mid = (node_low + node_high)/2;

    int left = get_first(2*node, node_low, mid, query_low, query_high, val);
    if(left != -1){
      return left;
    }
    return get_first(2*node+1, mid+1, node_high, query_low, query_high, val);
  }

};

void solve(){
  int n, q;
  cin >> n >> q;
  
  vector<int> hotels(n,0);
  for(int i = 0; i < n; i++){
    cin >> hotels[i];
  }

  Seggy seg = Seggy(hotels);
  n = seg.vals.size();
  for(int i = 0; i < q; i++){
    int req;
    cin >> req;

    int room = seg.get_first(1, 0, n-1, 0, n-1, req);

    if(room == -1){
      cout << 0 << " ";
    }
    else{
      cout << room + 1 << " ";
      hotels[room] -= req;
      seg.update(1, 0, n-1, room, room, hotels[room]);
    }
  }

  
}

int main(){
  solve();
  return 0;
}