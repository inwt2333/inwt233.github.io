---
title: 并查集 模版
date: Thu, 06 Ma
summary:      题源：【模版】并查集 P3367    题目描述    如题，现在有一个并查集，你需要完成合并和查询操作。    输入格式    第一行包含两个整数 $N,M$ ,表示...
---

<!-- wp:paragraph -->
<p>题源：<a href="https://www.luogu.com.cn/problem/P3367">【模版】并查集 P3367</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">题目描述</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>如题，现在有一个并查集，你需要完成合并和查询操作。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输入格式</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>第一行包含两个整数 $N,M$ ,表示共有 $N$ 个元素和 $M$ 个操作。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>接下来 $M$ 行，每行包含三个整数 $Z_i,X_i,Y_i$ 。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当 $Z_i=1$ 时，将 $X_i$ 与 $Y_i$ 所在的集合合并。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当 $Z_i=2$ 时，输出 $X_i$ 与 $Y_i$ 是否在同一集合内，是的输出 <code>Y</code> ；否则输出 <code>N</code> 。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输出格式</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>对于每一个 $Z_i=2$ 的操作，都有一行输出，每行包含一个大写字母，为 <code>Y</code> 或者 <code>N</code> 。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输入输出样例</h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>// 输入#1
4 7
2 1 2
1 1 2
2 1 2
1 3 4
2 1 4
1 2 3
2 1 4
// 输出#1
N
Y
N
Y</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">代码</h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;iostream&gt;
using namespace std;
int father&#91;200010], n,times;

void init(int n) { // 初始化
    for (int i = 1; i &lt;= n; i++) {
        father&#91;i] = i; // 每个节点的父节点都是自己
    }
}

int find(int x) { // 寻找该节点的根节点
    return x == father&#91;x] ? x : father&#91;x] = find(father&#91;x]);
    // 如果这个点的父节点就是自己，那么他就是父亲中的父亲，是根节点，那就直接返回自己
    // 如果这个点的父节点是另一个节点，那么就递归查找这个父节点是否还有父节点
    // 同时如果这个点的父节点不是自己，那么还要更新自己的父节点到根节点，从而完成路径压缩操作
}

void merge(int i, int j) {
    i = find(i);
    j = find(j);
    // 将i和j更改为其根节点
    father&#91;i] = j;
    // 把其中一个根节点的父节点设置为另一个根节点
}

bool isEqual(int i, int j) {
    return find(i) == find(j);
    // 如果两个点的根节点相同，返回true，否则返回false
}

int main() {
    cin &gt;&gt; n &gt;&gt; times;
    init(n);
    int op,a,b;
    for (int i = 1; i &lt;= times; i++) {
        cin &gt;&gt; op &gt;&gt; a &gt;&gt; b;
        if (op == 1) {
            merge(a, b);
        } else if (op == 2) {
            if (isEqual(a, b)) {
                cout &lt;&lt; "Y" &lt;&lt; endl;
            } else {
                cout &lt;&lt; "N" &lt;&lt; endl;
            }
        }
    }
    return 0;
}</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">加权并查集</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>有了并查集之后，聪明的小朋友并不止步于此。他们肯定会想，我要是把这个集合改造成队列，merge时将i元素所在的队列整体连接到j元素所在的队列之后，并且增加查询元素在其所在队列中的位置，那有没有办法呢？</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>有的兄弟有的，这么强势的方法有很多，不仅仅可以用链表来遍历，并查集也是能够实现的！</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>请看代码：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;iostream>
#include &lt;cmath>
#define N 1000000
using namespace std;
int father&#91;N+10], length&#91;N+10] = {0}, num&#91;N+10];
// father存储每一个节点的根节点，length存储的是每一个节点距离其根节点的距离，num存储的是该根节点所连接的集合的长度（若该节点不是根节点则长度为0）

void init() {
    for (int i = 1; i &lt;= N; i++) {
        father&#91;i] = i;
        // 初始化每个节点的根节点是自己
        num&#91;i] = 1;
        // 初始化每个根节点的长度都是1
        length&#91;i] = 0;
        // 初始化每个节点距离自己根节点的距离都是0
    }
}

int find(int x) {
    // 寻找某一个节点的根节点
    if(father&#91;x] == x) {return father&#91;x];}
    // 如果这个点已经是根节点了，那么就返回这个根节点
    int fx = find(father&#91;x]);
    // 新建一个变量，递归寻找根节点，此时这个fx已经是参数x的根节点了
    length&#91;x] += length&#91;father&#91;x]];
    // 正常情况下，father&#91;x]已经是根节点了，因此length&#91;father&#91;x]]的值为0，length&#91;x]不会更新
    // 但是在本来的根节点接到了别的队列的末尾时，根节点的length被更新（在merge函数里，被更新成了另一个队列的长度）
    // 因此这个队列里每一个节点都要加上另一个队列的长度
    return father&#91;x] = fx;
    // 将根节点的值赋给这个队列里的每一个节点的father后返回这个值
}

void merge(int i, int j) {
    // merge函数传入的参数应为两个根节点，因此如果给了队列里两个点i，j，应该传入的是merge(find(i),find(j));
    length&#91;i] += num&#91;j];
    // 原来队列根节点的length原来是0，现在需要加上另一个队列的长度
    father&#91;i] = j;
    // 原来队列根节点的father更新成另一个队列的根节点
    num&#91;j] += num&#91;i];
    // 另一个队列的长度加上原来队列的长度
    num&#91;i] = 0;
    // 原来队列根节点的长度更新为0（因为它不再是根节点了）
}

bool isEqual(int i, int j) {
    return find(i) == find(j);
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>当然，不同的题目，权值的含义是不同的，权值计算的方式也是不同的，还需要具体题目具体分析。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>例题：<a href="https://www.luogu.com.cn/problem/P1196">P1196 [NOI2002] 银河英雄传说</a></p>
<!-- /wp:paragraph -->