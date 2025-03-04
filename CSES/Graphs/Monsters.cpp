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

constexpr array<std::pair<int, int>, 4> directions = {{{0, 1},{0, -1}, {1, 0}, {-1, 0}}};  
std::map<std::pair<int, int>, char> dmap = {
  {{1, 0}, 'D'},
  {{-1, 0}, 'U'},
  {{0, 1}, 'R'},
  {{0, -1}, 'L'}
};

int rLen, cLen;
vector<vector<int>> mdist;
vector<vector<prior>> backtrack;
vector<vector<char>> grid;

void monster_bfs(deque<tuple<int, int, int>> q){

  while(!q.empty()){
    tuple<int, int, int> curr = q.front();
    q.pop_front();

    int row, col, dist;
    tie(row, col, dist) = curr;

    for(pair<int, int> dir : directions){
      int dr = dir.first, dc = dir.second;
      int nr = row + dr;
      int nc = col + dc;

      if(0 <= nr && nr < rLen && 0 <= nc && nc < cLen && mdist[nr][nc] == INT32_MAX && grid[nr][nc] != '#'){
        mdist[nr][nc] = dist + 1;
        q.push_back(make_tuple(nr, nc, dist + 1));
      }
    }
  }

}
pair<int, int> explore(int row, int col){
  grid[row][col] = '#';
  queue<tuple<int, int, int>> q;
    q.emplace(make_tuple(row, col, 0));
    while(!q.empty()){
      tuple<int, int, int> curr = q.front();
      q.pop();
      int r, c, d;
      tie(r,c,d) = curr;
      //cout << r << " H E R E " << c << endl;
      for(auto [dr, dc] : directions){
        int nr = r + dr;
        int nc = c + dc;
        int nd = d + 1;
        if((0 <= nr && nr < rLen) && (0 <= nc && nc < cLen) && (grid[nr][nc] != '#') && mdist[nr][nc] > nd){
          backtrack[nr][nc] = prior(r, c, dmap[make_pair(dr, dc)]);
          if(nr == rLen - 1 || nc == cLen - 1 || (nr && nc == 0)){
            return make_pair(nr, nc);
          }
          grid[nr][nc] = '#';
          q.emplace(make_tuple(nr, nc, nd));
        }
      }
    }
    return make_pair(-1, -1);
}

void solve(){
  cin >> rLen; cin >> cLen;
  mdist.assign(rLen, vector<int>(cLen, INT32_MAX));
  grid.assign(rLen, vector<char>());
  string row;
  backtrack.assign(rLen, vector<prior>(cLen, prior(-1, -1, 'd') ));

  int startRow = -1, startCol = -1;
  for(int r = 0; r < rLen; r++){
    cin >> row;
    for(char c : row){
      grid[r].push_back(c);
    }
  }

  deque<tuple<int, int, int>> starts;
  for(int i = 0; i < rLen; i++){
    for(int j = 0; j < cLen; j++){
      if(grid[i][j] == 'M'){
        mdist[i][j] = 0;
        starts.push_back(make_tuple(i, j, 0));
      }
      else if(grid[i][j] == 'A'){
        startRow = i;
        startCol = j;
      }
    }
  }
  if(startRow == 0 || startRow == rLen - 1 || startCol == 0 || startCol == cLen - 1){
    cout << "YES" << endl;
    cout << 0;
    return;
  }
  monster_bfs(starts);
  pair<int, int> res = explore(startRow, startCol);
  if(res.first == -1){
    cout << "NO" << endl;
    return;
  }
  else{
    cout << "YES" << endl;
    string path;
    while(res.first != startRow || res.second != startCol){
      prior p = backtrack[res.first][res.second];
      path += p.dir;
      res = make_pair(p.prow, p.pcol);
    }
    reverse(path.begin(), path.end());
    cout << path.size() << endl;
    cout << path;
  }
}

int main(){
  solve();
  return 0;
}