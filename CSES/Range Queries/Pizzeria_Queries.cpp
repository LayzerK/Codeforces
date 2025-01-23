#include <bits/stdc++.h>
using namespace std;
struct Node{
  int node_min;

  Node(int min){
    node_min = min;
  }

  Node(){
    node_min = INT_MAX;
  }
};
struct Seggy{
  vector<int> vals;
  vector<Node> tree;
  int n;

  Node combine(Node left_node, Node right_node){
    long long new_min = min(left_node.node_min, right_node.node_min);
    return Node(new_min);
  }

  Seggy(vector<int> const &arr){
    n = arr.size();
    vals.assign(n, 0);
    for(int i = 0; i < n; i++){
      vals[i] = arr[i];
    }
    while(__builtin_popcount(n) != 1){
      n++;
      vals.push_back(INT_MAX);
    }
    
    tree.assign(2*this->n, Node());

    for(int i = 0; i < this->n; i++){
      tree[n+i] = Node(vals[i]);
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
      return Node(INT_MAX);
    }

    int mid = (node_low + node_high)/2;
    Node left  = query(2*node, node_low, mid, query_low, query_high);
    Node right = query(2*node+1, mid+1, node_high, query_low, query_high);
    Node res = combine(left, right);
    

    return res;

  }

  int query(int lb, int rb){
    int q_val = query(1, 0, n-1, lb, rb).node_min;
    return q_val;
  }

  void update(int node, int node_low, int node_high, int query_low, int query_high, int new_val){
    if(query_low <= node_low and node_high <= query_high){
      tree[node] = Node(new_val);
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
  int n; int q;
  cin >> n >> q;
  vector<int> lval(n, 0);
  vector<int> rval(n, 0);
  for(int i = 0; i < n; i++){
    int val; cin >> val;
    lval[i] = val - i;
    rval[i] = val + i;
  }

  Seggy left = Seggy(lval);
  Seggy right = Seggy(rval);
  n = left.n;
  for (int i = 0; i < q; i++){
    int type;
    cin >> type;
    if(type == 1){
      int index, new_val;
      cin >> index >> new_val;
      index--;
      left.update(1, 0, n-1, index, index, new_val - index);
      right.update(1, 0, n-1, index, index, new_val + index);
    }
    else{
      int mid;
      cin >> mid;
      mid--;
      int l_val = left.query(0, mid) + mid;
      int r_val = right.query(mid, n-1) - mid;

      cout << min(l_val, r_val) << endl;
    }
  }



}

int main(){
  solve();
}