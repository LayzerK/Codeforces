#include <bits/stdc++.h>
using namespace std;
vector<int> par;
vector<int> rnk;
int comps;

int find(int node){
  if(par[node] != node){
    par[node] = find(par[node]);
  }
  return par[node];
}

void unite(int n1, int n2){
  int p1 = find(n1);
  int p2 = find(n2);

  if(p1 == p2){
    return;
  }
  comps--;

  if(rnk[p1] > rnk[p2]){
    par[p2] = p1;
  }
  else if(rnk[p2] > rnk[p1]){
    par[p1] = p2;
  }
  else{
    par[p2] = p1;
    rnk[p1]++;
  }
}

void solve(){
  int n, m; cin >> n >> m;
  comps = n;
  par.assign(n, 0);
  rnk.assign(n, 1);
  iota(par.begin(), par.end(), 0);

  for(int i = 0; i < m; i++){
    int a, b;
    cin >> a >> b;
    a--;b--;
    unite(a, b);
  }
  cout << comps - 1 << endl;
  for(int i = 0; i < n; i++){
    if(find(i) != find(0)){
      cout << 1 << " " << i + 1 << endl;
      unite(i, 0);
    }
  }
}

int main(){
  solve();
  return 0;
}