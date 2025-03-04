#include <bits/stdc++.h>
using namespace std;
void solve(){
  int n,m,q; cin >> n >> m >> q;
  vector<vector<long long>> costs(n, vector<long long>(n, LLONG_MAX));
  for(int i = 0; i < m; i++){
    int a,b; long long cost; cin >> a >> b >> cost;
    a--;b--;
    costs[a][b] = min(costs[a][b], cost);
    costs[b][a] = min(costs[a][b], cost);
  }

  for(int i = 0; i < n; i++){
    costs[i][i] = 0;
  }
  for(int mid = 0; mid < n; mid++){
    for(int start = 0; start < n; start++){
      for(int end = 0; end < n; end++){
        if(costs[start][mid] + costs[mid][end] < costs[start][end] && costs[start][mid] != LLONG_MAX && costs[mid][end] != LLONG_MAX){
          costs[start][end] = costs[start][mid] + costs[mid][end];
        }
      }
    }
  }

  for(int i = 0; i < q; i++){
    int start, end; cin >> start >> end;
    start--; end--;
    if(costs[start][end] == LLONG_MAX){
      cout << -1 << endl;
    }
    else{
      cout << costs[start][end] << endl;
    }
  }

}

int main(){
  solve();
  return 0;
}