#include <bits/stdc++.h>
using namespace std;
struct prior{
  int prow;
  int pcol;
  char dir;

  prior(int r, int c, char d){
    prow = r;
    pcol = c;
    dir = d;

  }
};
pair<int, int> explore(vector<vector<char>>& grid, vector<vector<prior>>& backtrack, int rLen, int cLen, int row, int col){
  constexpr array<std::pair<int, int>, 4> directions = {{{0, 1},{0, -1}, {1, 0}, {-1, 0}}};  
  std::map<std::pair<int, int>, char> dmap = {
    {{1, 0}, 'D'},
    {{-1, 0}, 'U'},
    {{0, 1}, 'R'},
    {{0, -1}, 'L'}
  };
  grid[row][col] = '#';
  queue<pair<int, int>> q;
    q.emplace(make_pair(row, col));
    while(!q.empty()){
      pair<int, int> curr = q.front();
      q.pop();
      for(auto [dr, dc] : directions){
        int nr = curr.first + dr;
        int nc = curr.second + dc;
        if((0 <= nr && nr < rLen) && (0 <= nc && nc < cLen) && (grid[nr][nc] != '#')){
          backtrack[nr][nc] = prior(curr.first, curr.second, dmap[make_pair(dr, dc)]);
          if(grid[nr][nc] == 'B'){
            return make_pair(nr, nc);
          }
          grid[nr][nc] = '#';
          q.emplace(make_pair(nr, nc));
        }
      }
    }
    return make_pair(-1, -1);
}

void solve(){
  int rLen; int cLen; cin >> rLen; cin >> cLen;
  vector<vector<char>> grid(rLen);
  string row;
  vector<vector<prior>> backtrack(rLen, vector<prior>(cLen, prior(-1, -1, 'd') ));
  for(int r = 0; r < rLen; r++){
    cin >> row;
    for(char c : row){
      grid[r].push_back(c);
    }
  }
  for(int r = 0; r < rLen; r++){
    for(int c = 0; c < cLen; c++){
      if(grid[r][c] == 'A'){
        pair<int, int> eval = explore(grid, backtrack, rLen, cLen, r, c);
        if(eval.first != -1){
          cout << "YES" << endl;
          int row = eval.first;
          int col = eval.second;
          string res;
          while(row != r || col != c){
            prior p = backtrack[row][col];
            res += p.dir;
            row = p.prow;
            col = p.pcol;

          }
          cout << res.size() << endl;
          reverse(res.begin(), res.end());
          cout << res;
        }
        else{
          cout << "NO" << endl;
        }
      }
    }
  }
}

int main(){
  solve();
  return 0;
}