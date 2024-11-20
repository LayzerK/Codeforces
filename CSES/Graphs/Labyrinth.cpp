#include <bits/stdc++.h>
using namespace std;
bool explore(vector<vector<char>>& grid, int rLen, int cLen, int row, int col){
constexpr array<std::pair<int, int>, 4> directions = {{{0, 1},{0, -1}, {1, 0}, {-1, 0}}};  
queue<pair<int, int>> q;
  q.emplace(make_pair(row, col));
  while(!q.empty()){
    pair<int, int> curr = q.front();
    q.pop();
    for(auto [dr, dc] : directions){
      int nr = curr.first + dr;
      int nc = curr.second + dc;
      if((0 <= nr && nr < rLen) && (0 <= nc && nc < cLen) && (grid[nr][nc] != '#')){
        if(grid[nr][nc] == 'B'){
          return true;
        }
        q.emplace(make_pair(nr, nc));
        grid[nr][nc] = '#';
      }
    }
  }
  return false;
}

void solve(){
  int rLen; int cLen; cin >> rLen; cin >> cLen;
  vector<vector<char>> grid(rLen);
  string row;
  for(int r = 0; r < rLen; r++){
    cin >> row;
    for(char c : row){
      grid[r].push_back(c);
    }
  }
  int rooms = 0;
  for(int r = 0; r < rLen; r++){
    for(int c = 0; c < cLen; c++){
      if(grid[r][c] == 'A'){
        if(explore(grid, rLen, cLen, r, c)){
          cout << "YES" << endl;
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