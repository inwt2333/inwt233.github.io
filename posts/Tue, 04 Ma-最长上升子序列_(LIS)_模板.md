---
title: 最长上升子序列 (LIS) 模板
date: Tue, 04 Ma
summary:  题源：AT_chokudai_S001_h LIS    题目描述    数列 $ a $ から好きな整数を好きなだけ取り除き、単調増加な数列を作るとき、その数列の長さの最大値を求めなさい。    ...
---

<!-- wp:paragraph -->
<p>题源：<a href="https://www.luogu.com.cn/problem/AT_chokudai_S001_h">AT_chokudai_S001_h LIS</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">题目描述</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>数列 $ a $ から好きな整数を好きなだけ取り除き、単調増加な数列を作るとき、その数列の長さの最大値を求めなさい。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>给定一个长为 <em>n</em> 的序列 <em>a<sub>i</sub></em>​，求这个序列的最长单调上升子序列长度。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>1≤<em>n</em>≤10<sup>5</sup>。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输入输出样例</h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>// 输入 #1
5
3 1 5 4 2
// 输出 #1 
2
// 输入 #2
6
1 2 3 4 5 6
// 输出 #2
6
// 输入 #3
7
7 6 5 4 3 2 1
// 输出 #3 
1
// 输入 #4
20
19 11 10 7 8 9 17 18 20 4 3 15 16 1 5 14 6 2 13 12
// 输出 #4 
6</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">说明/提示</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">制約</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>1≤N≤100,000 </li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">代码</h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;algorithm>
#include &lt;iostream>
using namespace std;
int arr&#91;100010],f&#91;100010],g&#91;100010],n,ans;
// arr为输入的数组
// f&#91;i]为以arr&#91;i]为结尾的LIS长度
// g&#91;i]为上升序列长度为i时长度的最小值

int main() {
    cin>>n;
    for (int i = 1; i &lt;= n; i++) {
        cin>>arr&#91;i];
    }
    for (int i = 1; i &lt;= n; i++) { 
    // 将这里改成for (int i = n; i >= 1; i--) 则变成查找最长单调下降子序列
        int pos = lower_bound(g + 1, g + ans + 1, arr&#91;i]) - g; 
        // 二分查找arr&#91;i]在g中的位置
        f&#91;i] = pos;
        g&#91;pos] = arr&#91;i];
        ans = max(ans, pos);
    }
    cout &lt;&lt; ans &lt;&lt; endl;
    return 0;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>该代码的时间复杂度为<em>O(nlogn)</em>。</p>
<!-- /wp:paragraph -->