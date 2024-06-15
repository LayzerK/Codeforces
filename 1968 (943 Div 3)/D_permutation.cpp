  #include <iostream>
  #include <cstdio>
  #include <cstdlib>
  #include <algorithm>
  #include <cmath>
  #include <vector>
  #include <set>
  #include <map>
  #include <unordered_set>
  #include <unordered_map>
  #include <queue>
  #include <ctime>
  #include <cassert>
  #include <complex>
  #include <string>
  #include <cstring>
  #include <chrono>
  #include <random>
  #include <bitset>
  #include <array>
  using namespace std;
  vector<int> perm;
  vector<int> vals;
  long long dfs(int start, int k, vector<int>& perm, vector<int>& vals);
  void solve(){
    int n; int k; int b_start; int s_start;
    cin >> n; cin >> k; cin >> b_start; cin >> s_start;
    perm.assign(n, 0);
    vals.assign(n, 0);

    for(int i = 0; i < n; i++){
      cin >> perm[i];
      perm[i] -= 1;
      //cout << perm[i] << "\n";
    }
    for(int i = 0; i < n; i++){
      cin >> vals[i];
    }

    //you want to go to the max val eventually. So basically answer for each val is computed as dfs until cycle or max and compute value at each step


    long long b_score = dfs(b_start-1, k, perm, vals);
    long long s_score = dfs(s_start-1, k, perm, vals);

    if(b_score == s_score){
      cout << "Draw";
    }
    else if (b_score > s_score){
      cout << "Bodya";
    }
    else{
      cout << "Sasha";
    }
    
    cout << "\n";
    
  }
    long long dfs(int start, int k, vector<int>& perm, vector<int>&vals){
    //cout << perm.size() << "   H  E E E" << "\n";
    set<int> visited;
    vector<tuple<int, int, int>> stack;
    stack.push_back(tuple(start, 0, k));
    long long ans = 0;
    long long score = 0;
    int curr = start;
    long long rem = k;
    //cout << "PRE  " << visited.count(curr) << "   " << rem <<  "\n";
    while(visited.count(curr) == 0 && rem != 0){
      long long stay = score + rem * vals[curr];
      score += vals[curr];
      ans = max(ans, stay);
      
      
      visited.insert(curr);
      rem -= 1;
      //cout << "B4  " << curr <<"\n";
      curr = perm[curr];
      //cout << stay <<" eeeee " << curr << "\n";
    }
    //cout << " HEEERE " << ans << " AANS" << "\n";
    return ans;

  }


  int main(){
    int tc;
    
    cin >> tc;

    while(tc--){
      solve();
    }
    return 0;
  }