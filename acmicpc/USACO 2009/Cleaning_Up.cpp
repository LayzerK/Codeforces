#include <bits/stdc++.h>
using namespace std;
void solve(){
  int n, m;
  cin >> n >> m;

  int mx = ceil(sqrt(m));
  vector<int> best(n+1, n+1);
  best[n] = 0;
  vector<int> arr(n, 0);
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  unordered_map<int, int> cnts;
  for(int i = n-1; i >= 0; i--){
    best[i] = best[i+1] + 1;
  }
  for(int sz = mx; sz >= 1; sz--){
    cnts.clear();
    int right = n-1;
    for(int i = n-1; i >= 0; i--){
      cnts[arr[i]] += 1;
      while(cnts.size() > sz){
        cnts[arr[right]] -= 1;
        if(cnts[arr[right]] == 0){
          cnts.erase(arr[right]);
        }
        right -= 1;
      }
      
      if(cnts.size() == sz){
        best[i] = min(best[i], best[right+1] + sz * sz);
        //cout << dp[i][sz] << " Here " << i << "  " << sz <<  " " << right << endl;
      }
  }
  }
  //for(int i = 0; i <= n; i++){
    //cout << best[i] << " ";
  //}
  cout << best[0];
}

int main(){
  solve();
  return 0;
}