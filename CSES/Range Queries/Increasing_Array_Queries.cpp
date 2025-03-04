#include <bits/stdc++.h>
using namespace std;
struct Node{
  int sz;
  int first;
  int last;
  long long cost;
  long long total;

  Node(int nsz, int fval, int lval, long long c, long long t){
    sz = nsz;
    first = fval;
    last = lval;
    cost = c;
    total = t;
  }

  Node(){
    sz = 0;
    first = 0;
    last = 0;
    cost = 0;
    total = 0;
  }
};
struct Seggy{
  vector<int> vals;
  vector<Node> tree;
  int n;

  Node combine(Node left_node, Node right_node){
    if(left_node.sz == -1){
      return right_node;
    }
    else if(right_node.sz == -1){
      return left_node;
    }
    int lbound = left_node.last;

    int rbound = right_node.first;
    long long extra_cost = 0;
    long long new_total = left_node.total + right_node.total;
    if(lbound > rbound){
      extra_cost += right_node.sz * lbound - right_node.total;
      rbound = lbound;
    }
    return Node(left_node.sz + right_node.sz, 
      lbound, rbound, 
      extra_cost + left_node.cost + right_node.cost, 
      new_total + extra_cost);
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
      tree[n+i] = Node(1, vals[i], vals[i], 0, vals[i]);
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
      return Node(-1, -1, -1, -1, -1);
    }

    int mid = (node_low + node_high)/2;
    Node left  = query(2*node, node_low, mid, query_low, query_high);
    Node right = query(2*node+1, mid+1, node_high, query_low, query_high);
    Node res = combine(left, right);
    

    return res;

  }

  long long query(int lb, int rb){
    long long q_val = query(1, 0, n-1, lb, rb).cost;
    return max(0LL, q_val);
  }

  void update(int node, int node_low, int node_high, int query_low, int query_high, int new_val){
    if(query_low <= node_low and node_high <= query_high){
      tree[node] =  Node(1, new_val, new_val, 0, new_val);
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
    int lb, rb; cin >> lb >> rb;
    lb--; rb--;
    cout << seg.query(lb, rb) << endl;
  }
}

int main(){
  solve();
  return 0;
}