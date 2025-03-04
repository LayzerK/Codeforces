#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
vector<int> colors;
vector<int> path;
int n, m;
int dfs(int curr, int par){
  colors[curr] = 1;
  path.push_back(curr);
  for(int nei : adj[curr]){
    if (nei == par){
      continue;
    }
    if(colors[nei] == 1){
      return nei;
    }
    int res = dfs(nei, curr);
    if(res != -1){
      return res;
    }
  }

  path.pop_back();
  colors[curr] = 2;
  return -1;
}
void solve(){
  cin >> n >> m;
  adj.resize(n, vector<int>());
  colors.resize(n, 0);

  for(int i = 0; i < m; i++){
    int a,b;
    cin >> a >> b;
    a--;b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for(int i = 0; i < n; i++){
    if(colors[i] == 0){
      int start = dfs(i, -1);
      //cout << path.size() << "  HE R E " << endl;
      if(!path.empty()){
        int j = 0;
        while(path[j] != start){
          j++;
        }
        cout << path.size() - j + 1<< endl;
        while(j < (int) path.size()){
            cout << path[j] + 1 << " ";
            j++;
        }
        cout << start + 1;
        return;
      }
    }
  }

  cout << "IMPOSSIBLE";
}


int main(){
  solve();
  return 0;
}