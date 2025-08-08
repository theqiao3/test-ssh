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

// 计算模式串的部分匹配表（next数组）


// 示例测试
int main() {
    system("chcp 65001"); 
    string s;
    cin >> s; 

    // 去掉前导零
    while (s.size() > 1 && s[0] == '0') s.erase(s.begin());

    int count = s.size() - 1; // 指数
    double c = stod(s.substr(0, 3)) / 100.0; // 前两位数字形成系数
    c = round(c * 10) / 10.0; // 保留 1 位小数，四舍五入
        if(c == 10.0) {
            c = 1.0;
            count++;
        }


    cout << fixed << setprecision(1);
    cout << c << "*10^" << count << endl;
}

