#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> adj;
vector<int> vals;
vector<vector<int>> precomp;
vector<map<int, int>> dp_prime_condense;
vector<vector<int>> dp;
int cap = 2 * 5e3;
const std::vector<int> primes = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    };
    

vector<int> factorize(int num){
  vector<int> factors;
  for(int prime : primes){
    if(num == 1){
      break;
    }
    if(num % prime == 0){
      factors.push_back(prime);
      while(num % prime == 0){
        num /= prime;
      }
    }
  }

  return factors;
}

void dfs(int curr, int par){
  for(int child : adj[curr]){
    if(child == par){
      continue;
    }
    
    dfs(child, curr);

    for(int val = 2; val <= cap; val++){
      int child_cost = cap + 1;
      for(int fac : precomp[val]){
        child_cost = min(child_cost, dp_prime_condense[child][fac]);
      }
      dp[curr][val] += child_cost;
    }
  }
  for(int prime : primes){
    int prime_cost = cap + 1;
    for(int v = prime; v <= cap; v += prime){
      prime_cost = min(prime_cost, dp[curr][v]);
    }
    dp_prime_condense[curr][prime] = prime_cost;
  }
}

void solve(){
  int n; cin >> n;
  vals.assign(n, 0);
  adj.assign(n, vector<int>());
  dp.assign(n, vector<int>(cap+1, cap+1));
  dp_prime_condense.assign(n, map<int, int>());
  precomp.assign(cap+1, vector<int>());


  for(int i = 0; i < n; i++){
    cin >> vals[i];
  }

  for(int i = 0; i < n - 1;i++){
    int a; int b; cin >> a >> b;
    a--; b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  

  for(int i = 0; i < n; i++){
    for(int val = 2; val <= cap; val++){
      if(val == vals[i]){
        dp[i][val] = 0;
      }
      else{
        dp[i][val] = val;
      }
    }
  }
  
  for(int i = 2; i <= cap; i++){
    precomp[i] = factorize(i);
  }

  dfs(0, -1);
  int ans = *min_element(dp[0].begin(), dp[0].end());
  cout << ans;
  //cout << " H E R E";
}

int main(){
  solve();
  return 0;
}