---
title: 在这之前要多想：学会对题中的信息进行转化
date: Tue, 18 Ma
summary:  题源：P3956 [NOIP 2017 普及组] 棋盘    题目描述    有一个 $m \times m$ 的棋盘，棋盘上每一个格子可能是红色、黄色或没有任何颜色的...
---


<!-- wp:paragraph -->
<p>题源：<a href="https://www.luogu.com.cn/problem/P3956">P3956 [NOIP 2017 普及组] 棋盘</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">题目描述</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>有一个 $m \times m$ 的棋盘，棋盘上每一个格子可能是红色、黄色或没有任何颜色的。你现在要从棋盘的最左上角走到棋盘的最右下角。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>任何一个时刻，你所站在的位置必须是有颜色的（不能是无色的）， 你只能向上、下、左、右四个方向前进。当你从一个格子走向另一个格子时，如果两个格子的颜色相同，那你不需要花费金币；如果不同，则你需要花费 $1$ 个金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>另外， 你可以花费 $2$ 个金币施展魔法让下一个无色格子暂时变为你指定的颜色。但这个魔法不能连续使用， 而且这个魔法的持续时间很短，也就是说，如果你使用了这个魔法，走到了这个暂时有颜色的格子上，你就不能继续使用魔法； 只有当你离开这个位置，走到一个本来就有颜色的格子上的时候，你才能继续使用这个魔法，而当你离开了这个位置（施展魔法使得变为有颜色的格子）时，这个格子恢复为无色。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>现在你要从棋盘的最左上角，走到棋盘的最右下角，求花费的最少金币是多少？</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输入格式</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>第一行包含两个正整数 $ m, n$，以一个空格分开，分别代表棋盘的大小，棋盘上有颜色的格子的数量。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>接下来的 $ n $ 行，每行三个正整数 $ x, y, c$， 分别表示坐标为 $(x,y)$ 的格子有颜色 $ c$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中 $ c=1$ 代表黄色，$ c=0$ 代表红色。 相邻两个数之间用一个空格隔开。 棋盘左上角的坐标为 $(1, 1)$，右下角的坐标为 $( m, m)$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>棋盘上其余的格子都是无色。保证棋盘的左上角，也就是 $(1, 1)$ 一定是有颜色的。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输出格式</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>一个整数，表示花费的金币的最小值，如果无法到达，输出 <code>-1</code>。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">输入输出样例 </h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>// 输入#1
5 7
1 1 0
1 2 0
2 2 1
3 3 1
3 4 0
4 4 1
5 5 0

// 输出#1
8

// 输入#2
5 5
1 1 0
1 2 0
2 2 1
3 3 1
5 5 0

// 输出#2
-1</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">说明/提示</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>样例 1 说明</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>棋盘的颜色如下表格所示，其中空白的部分表示无色。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":132,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="http://inwt233.cn/wp-content/uploads/2025/03/image.png" alt="" class="wp-image-132"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>从 $(1,1)$ 开始，走到 $(1,2)$ 不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(1,2)$ 向下走到 $(2,2)$ 花费 $1$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(2,2)$ 施展魔法，将 $(2,3)$ 变为黄色，花费 $2$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(2,2)$ 走到 $(2,3)$ 不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(2,3)$ 走到 $(3,3)$ 不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(3,3)$ 走到 $(3,4)$ 花费 $1$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(3,4)$ 走到 $(4,4)$ 花费 $1$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(4,4)$ 施展魔法，将 $(4,5)$ 变为黄色，花费 $ 2$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(4,4)$ 走到 $(4,5)$ 不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $(4,5)$ 走到 $(5,5)$ 花费 $1$ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>共花费 $8 $ 枚金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>样例 2 说明</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>棋盘的颜色如下表格所示，其中空白的部分表示无色。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":133,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="http://inwt233.cn/wp-content/uploads/2025/03/image-1.png" alt="" class="wp-image-133"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>从 $( 1, 1)$ 走到 $( 1, 2)$，不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $( 1, 2)$ 走到 $( 2, 2)$，花费 $ 1 $ 金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>施展魔法将 $( 2, 3)$ 变为黄色，并从 $( 2, 2)$ 走到 $( 2, 3)$ 花费 $ 2$ 金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $( 2, 3)$ 走到 $( 3, 3)$ 不花费金币。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从 $( 3, 3)$ 只能施展魔法到达 $( 3, 2),( 2, 3),( 3, 4),( 4, 3)$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>而从以上四点均无法到达 $( 5, 5)$，故无法到达终点，输出$-1$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>数据规模与约定</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于 $30\%$ 的数据，$1 ≤ m ≤ 5, 1 ≤ n ≤ 10$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于 $60\%$ 的数据，$1 ≤ m ≤ 20, 1 ≤ n ≤ 200$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于 $100\%$ 的数据，$1 ≤ m ≤ 100, 1 ≤ n ≤ 1,000$。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">解题思路</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>最开始的时候我是想用BFS的方法分别对同色，异色，以及使用魔法的情况进行处理。但是如果这样就产生了以下几个问题：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>传统BFS的每个节点只需要入队一次，就可以处理好。不过这题要考虑到每个节点需要更新到花费最小的状态，也就是说一个点入队又出队后可能又通过其他路径降低成本，需要再次入队；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>对无色节点的处理，需要通过魔法🪄临时改变其颜色。由于我们之后还要处理这个点到后续节点的花费，所以我们务必需要记录一下我们用魔法将这个节点改成了什么颜色。不过因为变色只是临时的，我们不能直接将其记录到颜色的数组中，而需要另开一个变量去记录他。原本我的思路是对每个点另开一个“临时颜色”变量，对于一开始就有颜色的节点，其“临时颜色”与颜色相同，而对于原本无颜色的节点在使用魔法时将“临时颜色”更新为前序节点的颜色，同时压入队列中；之后每对一个节点进行处理后，如果他的颜色与“临时颜色”不同，则将“临时颜色”擦除。实际的操作之后我们又遇到了另一个难题：由于刚才每个节点可能多次入队的特性，可能在队列中同时存在一个节点，这两个节点的临时颜色可能不同；即使相同，在处理完其中一个节点后，其临时颜色就会被清除，等到处理另外一个节点的时候就会出现错误，所以这种方法并不可行。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>那么如何解决这两个问题呢？</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于第一个问题，我们可以通过使用<strong>堆</strong>来实现操作。堆是一种特殊的队列，其特点是堆顶元素必然是堆中的最大值。通过使用堆，我们可以每次取出目前花费最少的节点，这样能够有效地保证每个元素被加入堆中时成本最低，从而减少了重复访问。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于第二个问题，我们则需要对“魔法”进行一些小小的处理。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由于魔法不能连用，所以站在一个无颜色块上时，我们下一步只能移动到相邻的有颜色块上。退一步想，如果我们站在一个有颜色块上，那么我们可以通过一次更新，移动到相邻两格以内的有颜色块上。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":143,"width":"281px","height":"auto","sizeSlug":"full","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-full is-resized"><img src="http://inwt233.cn/wp-content/uploads/2025/03/image-2.png" alt="" class="wp-image-143" style="width:281px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>从now到黄色区域有颜色的节点，花费为0 + 转换颜色的代价。而从now到绿色区域有颜色的节点，花费为2 + 转换颜色的代价。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>至于为什么不更新黄色区域内没有颜色的节点，明明这些节点也能访问到啊？是因为刚才提到，从黄色无颜色节点出发时不能再次使用魔法，因此只能移动到绿色区域内有颜色节点，也就是刚才考虑过的情况。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>还有一个小问题，比如三个相同颜色的节点连在一起，在访问节点1时将节点2的代价设为0，将节点3的代价设为2，但是事实上节点1通过2到3并没有代价，这种状况怎么办呢？</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>事实上，由于大根堆的特性，我们在处理的过程中肯定是先处理节点2再处理节点3，在处理节点2的时候由于2与3相邻，就会将节点3的代价更新为0，这样后续处理节点3就没有任何问题了。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>接下来是代码展示：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;iostream>
#include &lt;queue>
#define INF 100000000
using namespace std;
int arr&#91;12]&#91;2] = {{-1,0},{1,0},{0,-1},{0,1}, {2,0}, {-2,0}, {0,2},{0,-2},{1,1},{1,-1},{-1,1},{-1,-1}};
// 一共有十二个方向，前四个方向是相邻，后八个方向是隔一步
int cost&#91;12] = {0,0,0,0,2,2,2,2,2,2,2,2};
int colour&#91;105]&#91;105], money&#91;105]&#91;105], M, N;

struct node {
    int x, y, c, m;
    bool operator&lt;(const node&amp; b) const {
        return m > b.m;
    }
    // 如此重载运算符是因为priority_queue是大根堆，每次取出的是全局最大的节点，因此在进行比较的时候要让成本低的节点大于成本高的节点。
};
priority_queue&lt;node> q;

void bfs() {
    node next;
    while(!q.empty()) {
        node now = q.top();
        q.pop();
        for(int i = 0; i &lt; 12; i++) {
            next.x = now.x + arr&#91;i]&#91;0], next.y = now.y + arr&#91;i]&#91;1], next.m = now.m + cost&#91;i];
            if(next.x &lt;= 0 || next.x > M || next.y &lt;= 0 || next.y > M) continue;
            next.c = colour&#91;next.x]&#91;next.y];
            if(!next.c) continue;
            // 如果这个节点没有颜色，就跳过
            if(next.c != now.c) next.m++;
            // 转换颜色，代价+1
            if(money&#91;next.x]&#91;next.y] > next.m) {
                money&#91;next.x]&#91;next.y] = next.m;
                q.push(next);
            }
            // 如果这个节点的总花费小于其他路径的花费，就将它压入队中重新处理
        }
    }
}

int main() {
    cin >> M >> N;
    for(int i = 1; i &lt;= M; i++) {
        for(int j = 1; j &lt;= M; j++) {
            colour&#91;i]&#91;j] = 0;
            money&#91;i]&#91;j] = INF;
            // 将初始代价设为一个竭尽全力无法到达的数
        }
    }
    for(int i = 1; i &lt;= N; i++) {
        int x, y, c;
        cin >> x >> y >> c;
        colour&#91;x]&#91;y] = c + 1;
        // 因为没有颜色的设为0，所以另外两种颜色+1
    }
    money&#91;1]&#91;1] = 0;
    q.push({1,1,colour&#91;1]&#91;1], money&#91;1]&#91;1]});
    bfs();
    if(!colour&#91;M]&#91;M]) {
    // 这里是处理终点没有颜色的情况。bfs中只将所有有颜色的点处理好，如果终点没有颜色，那么他的上一步必然为其上方或左侧的节点，那么就取他们两个点最小值再+2
        money&#91;M]&#91;M] = min(money&#91;M-1]&#91;M], money&#91;M]&#91;M-1]) + 2;
        if(money&#91;M]&#91;M] == INF + 2) cout &lt;&lt; -1;
        // 如果上方或左侧的节点也没被访问到，那就输出-1
        else cout &lt;&lt; money&#91;M]&#91;M];
    }else {
        if(money&#91;M]&#91;M] == INF) cout &lt;&lt; -1;
        // 处理本身有颜色且没被访问到的情况
        else cout &lt;&lt; money&#91;M]&#91;M];
    }
    return 0;
}</code></pre>
<!-- /wp:code -->