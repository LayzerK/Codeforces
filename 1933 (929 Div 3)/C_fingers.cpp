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

    long long naive_pow(int base, int power, int cap){
      long long ans = 1;
      for(int p = 0; p < power; p++){
        ans *= base;
        if(ans > cap){
          return ans;
        }
      }
      return ans;
    }

    void solve(){
      int a; int b; int goal;
      cin >> a; cin >> b; cin >> goal;
      set <int> k_vals;

      for(int x = 0; x < 20; x++){
        for(int y = 0; y < 20; y++){
          long long pair = naive_pow(a, x, goal) * naive_pow(b,y, goal);
          //cout << pair << "/" << a << b;
          if(goal % pair == 0){
            k_vals.insert(goal/pair);
          }

        }
      }
      cout << k_vals.size() << "\n";
    }

    int main(){
      int tc;
      
      cin >> tc;

      while(tc--){
        solve();
      }
      return 0;
    }