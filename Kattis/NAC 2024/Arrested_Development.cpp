#include <bits/stdc++.h>
using namespace std;
void solve(){
  int n;
  cin >> n;
  vector<pair<int, int>> times;
  int MX = pow(10, 8);
  int aT = 0;
  for(int i = 0; i < n; i++){
    int a; int b; cin >> a >> b;
    aT += a;
    times.emplace_back(a,b);
  }

  vector<vector<int>> dp(n, vector<int>(aT+1, MX));

  dp[0][times[0].first] = 0;
  dp[0][0] = times[0].second;

  for(int i = 1; i < n; i++){
    for(int j = 0; j <= aT; j++){
      //take it for intern B
      dp[i][j] = dp[i-1][j] + times[i].second;
      //take it for intern A
      if(j >= times[i].first){
        dp[i][j] = min(dp[i][j], dp[i-1][j-times[i].first]);
      }
    }
  }
  int ans = MX;
  for(int i = 0; i <= aT; i++){
    //cout << i << " H E R E " << dp[n-1][i] << endl;
    ans = min(ans, max(i, dp[n-1][i]));
  }
  cout << ans;
}

int main(){
  solve();
  return 0;
}