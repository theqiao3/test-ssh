#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;

// struct TreeNode {
//      int val;
//      TreeNode *left;
//      TreeNode *right;
//      TreeNode() : val(0), left(nullptr), right(nullptr) {}
//      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//  };


int main() {
    system("chcp 65001"); 
    vector<int> nums = {1, 2, 3, 4, 5};
    int target = 3;
    auto it = find(nums.begin(), nums.end(), target);
    if (it != nums.end()) {
        cout << "Found " << target << " at index " << distance(nums.begin(), it) << endl;
    }


}

