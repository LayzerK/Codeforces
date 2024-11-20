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
class TrieNode{
  public:
    bool isEnd;
    unordered_map<char, TrieNode*> children;

    TrieNode() : isEnd(false) {}
};
class Trie{
  public:
    TrieNode* root;
    Trie(){
      root = new TrieNode();
    }
    void insert(const string& word){
      TrieNode* curr = root;
      for (char c : word){
        if(!curr->children.count(c)){
          curr->children[c] = new TrieNode();
        }
        curr = curr->children[c];
      }
      curr->isEnd = true; 
    }
    ~Trie(){
      deleteTrie(root);
    }
    private:
      void deleteTrie(TrieNode* node) {
          for (auto& pair : node->children) {
              deleteTrie(pair.second);
          }
          delete node;
      }
};
void solve(){
  string s;
  int k;
  const int MOD = 1e9 + 7;
  vector<string> dictionary;
  cin >> s;
  cin >> k;
  int n = s.size();
  for(int i = 0; i < k; i++){
    string w;
    cin >> w;
    dictionary.push_back(w);
  }

  Trie trie;
  for(string w : dictionary){
    trie.insert(w);
  }
  vector<int> dp(n+1, 0);
  dp[0] = 1;
  for(int start = 1; start <= n; start++){
    TrieNode* curr = trie.root;
    for(int end = start; end <= n; end++){
      char c = s[end-1];
      int sz = end-start + 1;
      if(!curr->children.count(c)){
        break;
      }
      curr = curr->children[c];
      if(curr->isEnd){
        dp[end] = (dp[end-sz] + dp[end]) % MOD;
      }
    }
  }

  cout << dp[n];
}

int main(){
  solve();
  return 0;
}