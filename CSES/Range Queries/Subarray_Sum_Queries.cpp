#include <bits/stdc++.h>
using namespace std;
struct Node{
  long long max_subarray;
  long long max_prefix;
  long long max_suffix;
  long long whole_sum;

  Node(long long subval, long long preval, long long sufval, long long sum){
    max_subarray = subval;
    max_prefix = preval;
    max_suffix = sufval;
    whole_sum = sum;
  }

  Node(){
    max_subarray = 0;
    max_prefix = 0;
    max_suffix = 0;
    whole_sum = 0;
  }
};
struct Seggy{
  vector<int> vals;
  vector<Node> tree;
  int n;

  Node combine(Node left_node, Node right_node){

    
    long long overlap = left_node.max_suffix + right_node.max_prefix;
    long long new_whole_sum = left_node.whole_sum + right_node.whole_sum;
    
    long long new_sub = max(overlap, max(left_node.max_subarray, right_node.max_subarray));

    long long new_prefix = max(left_node.max_prefix, left_node.whole_sum + right_node.max_prefix);
    long long new_suffix = max(right_node.max_suffix, right_node.whole_sum + left_node.max_suffix);


    return Node(new_sub, new_prefix, new_suffix, new_whole_sum);
  }

  Seggy(vector<int> const &arr){
    n = arr.size();
    vals.assign(n, 0);
    for(int i = 0; i < n; i++){
      vals[i] = arr[i];
    }
    while(__builtin_popcount(n) != 1){
      n++;
      vals.push_back(0);
    }
    
    tree.assign(2*this->n, Node());

    for(int i = 0; i < this->n; i++){
      tree[n+i] = Node(vals[i], vals[i], vals[i], vals[i]);
    }
    for(int i = n-1; i >= 1; i--){
      tree[i] = combine(tree[2*i], tree[2*i+1]);
    }
  }

  Node query(int node, int node_low, int node_high, int query_low, int query_high){
    if(query_low <= node_low and node_high <= query_high){
      return tree[node];
    }
    if(node_high < query_low || query_high < node_low){
      return Node(0, 0, 0, 0);
    }

    int mid = (node_low + node_high)/2;
    Node left  = query(2*node, node_low, mid, query_low, query_high);
    Node right = query(2*node+1, mid+1, node_high, query_low, query_high);
    Node res = combine(left, right);
    

    return res;

  }

  long long query(int lb, int rb){
    long long q_val = query(1, 0, n-1, lb, rb).max_subarray;
    return max(0LL, q_val);
  }

  void update(int node, int node_low, int node_high, int query_low, int query_high, int new_val){
    if(query_low <= node_low and node_high <= query_high){
      tree[node] = Node(new_val, new_val, new_val, new_val);
      return;
    }
    if(node_high < query_low || query_high < node_low){
      return;
    }

    int mid = (node_low + node_high)/2;

    update(node*2, node_low, mid, query_low, query_high, new_val);
    update(node*2+1, mid+1, node_high, query_low, query_high, new_val);
    tree[node] = combine(tree[node*2], tree[node*2+1]);
  }

};

void solve(){ 
  int n,q; cin >> n >> q;
  vector<int> arr(n, 0);

  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  Seggy seg = Seggy(arr);
  
  n = seg.vals.size();
  for(int i = 0; i < q; i++){
    int index, new_val; cin >> index >> new_val;
    index--;
    seg.update(1, 0, n-1, index, index, new_val);
    cout << seg.query(0, n-1) << endl;
  }
}

int main(){
  solve();
  return 0;
}