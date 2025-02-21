#include <bits/stdc++.h>
using namespace std;
int timer = 0;
int SIZE;
vector<int> depth;
vector<vector<pair<int, int>>> adj;
vector<int> tin;
vector<int> tout;
vector<vector<int>> up;
vector<bool> shops;
vector<pair<int, int>> edges;
void solve(){
  int n, s, queries, exit;
  cin >> n >> s >> queries >> exit;


  depth.resize(n, -1);
  adj.resize(n, vector<pair<int, int>>());
  tin.resize(n,0);
  tout.resize(n, 0);

  SIZE = floor(log2(n)) + 1;

  up.resize(n, vector<int>(SIZE + 1, exit));

  for(int i = 0; i < n - 1; i++){
    int a, b, length;
    cin >> a >> b >> length;
    a--, b--;
    adj[a].push_back(make_pair(b, length));
    adj[b].push_back(make_pair(a, length));
    edges.push_back(make_pair(a, b));
  }

  for(int i = 0; i < s; i++){
    int shop; cin >> shop;
    shop--;

    shops[shop] = true;
  }



  build_table(exit, exit);

  //tree rooted @ exit



  for(int q = 0; q < queries; q++){
    int banned; int node;
    cin >> banned >> node;
    banned--; node--;

    int b1 = edges[banned].first;
    int b2 = edges[banned].second;
    
    //we want the "bottom" of b1/b2 since that will form the root of the new substree in the second case
    int new_root = isancestor(b1, b2) ? b2 : b1;

    if(!isancestor(new_root, node)){
      cout << "escaped";
    }
    else{
      //in this case we know that we are cut off and now exist in some subtree rooted at the "bottom" (i.e. the reachable) part of the cut off edge
      //For all shops in this subtree, the path from shop -> node will have an LCA that exists on the path from node -> new_root
      //this is trivially true because the only ancestors of the node lie on that path lol
    }

  }
  




}


void build_table(int curr, int par){
  tin[curr] = ++timer;
  up[curr][0] = par;
  depth[curr] = depth[par] + 1;
  for(int i = 1; i <= SIZE; i++){
    up[curr][i] = up[up[par][i-1]][i-1];
  }

  for (pair<int, int> c : adj[curr]){
    int child = c.first;
    if(child != par){
      build_table(child, curr);
    }
  }
  tout[curr] = timer++;
}

bool isancestor(int ancestor, int child){
  return tin[ancestor] <= tin[child] and tout [ancestor] >= tout[child];
}

int main(){
  

  solve();
  return 0;
}