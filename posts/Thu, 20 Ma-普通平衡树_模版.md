---
title: 普通平衡树 模版
date: Thu, 20 Ma
summary:  题源：P3369 【模板】普通平衡树    简单来说，就是要求实现以下几个功能：     向 M 中插入一个数 x。    从 M 中删除一个数 x（若有多个相同的数，应只删除一个）。    查询 ...
---

<!-- wp:paragraph -->
<p>题源：<a href="https://www.luogu.com.cn/problem/P3369">P3369 【模板】普通平衡树</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>简单来说，就是要求实现以下几个功能：</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>向 <em>M</em> 中插入一个数 <em>x</em>。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>从 <em>M</em> 中删除一个数 <em>x</em>（若有多个相同的数，应只删除一个）。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>查询 <em>M</em> 中有多少个数比 <em>x</em> 小，并且将得到的答案加一。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>查询如果将 <em>M</em> 从小到大排列后，排名位于第 <em>x</em> 位的数。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>查询 <em>M</em> 中 <em>x</em> 的前驱（前驱定义为小于 <em>x</em>，且最大的数）。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>查询 <em>M</em> 中 <em>x</em> 的后继（后继定义为大于 <em>x</em>，且最小的数）。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>对于操作 3,5,6，<strong>不保证</strong>当前可重集中存在数 <em>x</em>。这就需要我们针对这些情况进行特殊处理。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>直接上代码：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include&lt;iostream>
#include&lt;cstdio>
using namespace std;

const int maxn = 1000019, INF = 1e9;
int child&#91;maxn]&#91;2];  // 左右子节点索引
int val&#91;maxn], dat&#91;maxn]; // 节点值和优先级
int large&#91;maxn], cnt&#91;maxn]; // 子树大小和相同键值的副本数
int total = 0, root; // 总节点数和根节点索引

// 平衡树,利用BST(Binary Search Tree, 二叉搜索树)性质查询和修改,利用随机和堆优先级来保持平衡,把树的深度控制在log N,保证了操作效率
// 基本平衡树有以下几个比较重要的函数：新建(New),插入(insert),删除,旋转
// 节点的基本属性有val(值),dat(随机出来的优先级
// 通过增加属性,结合BST的性质可以达到一些效果,如large(子树大小,查询排名),cnt(每个节点包含的相同键值的副本数)等

int New(int value) {   // 新增节点
    val&#91;++total] = value;   // 为节点赋值
    dat&#91;total] = rand(); // 随机优先级
    large&#91;total] = 1;     // 初始子树大小为1
    cnt&#91;total] = 1;     // 初始副本数为1
    return total;    // total即该新增节点在val中的索引
}

void pushup(int id) {   // 更新子树大小
    large&#91;id] = large&#91;child&#91;id]&#91;0]] + large&#91;child&#91;id]&#91;1]] + cnt&#91;id];
    // 本节点子树大小 = 左儿子子树大小 + 右儿子子树大小 + 本节点副本数
}

void build() {  // 初始化Treap
    root = New(-INF);   // 根节点的val为-INF
    child&#91;root]&#91;1] = New(INF);   // 根的右子节点的val为INF
    pushup(root);   // 更新根的子树大小
}

void Rotate(int &amp;id, int d) {    // 实现旋转操作
    // id是引用传递,引用的是一个节点在val数组里面的索引,d(direction)为旋转方向
    // Rotate和insert里面的id为什么要采用引用传递？因为我们要将id最后成为存这个value的索引,所以在一层递归中如果修改,全局的id都要改变
    int temp = child&#91;id]&#91;d ^ 1];     // d=0左旋,将右子树提升为父节点；d=1右旋,将左子树提升为父节点
    // d ^ 1 为异或操作,作用是将1改成0,将0改成1,此处是将要旋转的另外一个方向变为父节点
    child&#91;id]&#91;d ^ 1] = child&#91;temp]&#91;d];  // 将temp的d方向子节点赋给id的d^1方向
    child&#91;temp]&#91;d] = id;     // 将原父节点id变成temp的d方向子节点
    id = temp;    // temp成为新父节点
    pushup(child&#91;id]&#91;d]);     // 先更新原子节点
    pushup(id);     // 再更新新父节点
}

void insert(int &amp;id, int value) {  // 插入节点
    // 初始时传入的id为root,id为节点在val数组里面的索引,value是插入节点的值
    if (!id) {   // 如果搜索完成之后发现这个索引不存在(即上一个点的左/右子树索引为0)
        id = New(value); // 则新建一个节点
        return;
    }
    if (value == val&#91;id]) {   // 如果找到了value所对应的索引,证明值为value的节点已经存在,不需要重新创建
        cnt&#91;id]++;    // 增加副本数
    } else { // 如果还没找到,就继续往下找
        int d = (value &lt; val&#91;id]) ? 0 : 1;   // 确定查找方向,小于本节点则向左查找,大于则向右查找
        insert(child&#91;id]&#91;d], value);        // 在左子树或右子树里继续递归搜索
        if (dat&#91;id] &lt; dat&#91;child&#91;id]&#91;d]]) {   // 若子节点优先级更高
            Rotate(id, d ^ 1);     // 自下而上旋转以维持堆性质
        }
    }
    pushup(id); // 更新当前节点大小
}

void Remove(int &amp;id, int v) {
    if (!id) return;   // 若未找到节点(即节点的索引不存在),直接返回
    if (v == val&#91;id]) {   // 如果找到了值为value的节点的索引
        if (cnt&#91;id] > 1) {   // 如果这样的节点个数超过一个
            cnt&#91;id]--;       // 只需要减少副本数
            pushup(id);      // 更新该节点子树大小
            return;
        }
        // 只有一个副本且有子节点, delete之后这个树的结构会发生改变
        if (child&#91;id]&#91;0] || child&#91;id]&#91;1]) {
            // 选择优先级高的子节点旋转
            if (!child&#91;id]&#91;1] || dat&#91;child&#91;id]&#91;0]] > dat&#91;child&#91;id]&#91;1]]) {
                // 如果右子树为空,或者左子树的优先级大于右子树的优先级
                Rotate(id, 1); // 右旋
                Remove(child&#91;id]&#91;1], v); // 这时候值为value的节点被旋转到了原来的右子树上,因此递归删除右子树
            } else {
                Rotate(id, 0); // 左旋
                Remove(child&#91;id]&#91;0], v); // 这时候值为value的节点被旋转到了原来的左子树上,因此递归删除左子树
            }
            pushup(id); // 更新原节点(此时这个节点的val不再是要找的value了)子树的高度
        } else {
            id = 0; // 无子节点,或者多次旋转递归把该节点旋转到最底下了,那就直接删除这个节点
        }
        return;
    }
    v &lt; val&#91;id] ? Remove(child&#91;id]&#91;0], v) : Remove(child&#91;id]&#91;1], v);
    // 如果还没找到这个节点,那就往左/往右继续找
    pushup(id);
}

int get_rank(int id, int v) { // 查找某一个节点的排名(即树中所有比他小的元素个数 + 1)
    if (!id) return 1; // 如果不存在这个节点,则返回1
    if (v == val&#91;id]) { // 如果找到了这个节点的索引
        return large&#91;child&#91;id]&#91;0]]; // 左子树大小 + 1（当前节点）- 1 (排除-INF哨兵)
    } else if (v &lt; val&#91;id]) {
        return get_rank(child&#91;id]&#91;0], v); // 递归左子树
    } else {
        // 左子树大小 + 当前副本数 + 右子树中的排名
        return large&#91;child&#91;id]&#91;0]] + cnt&#91;id] + get_rank(child&#91;id]&#91;1], v);
        // 因为小于某个节点的元素个数 = 这个节点的左子树大小 + 在寻找这个节点的路径上在某点处向右走时,左边的大小与节点大小的和,所以向右走时要这样处理
    }
}

int get_val(int id, int rank) { // 获取排名为rank的节点的val
    if (!id) return INF; // 如果排名比元素总个数还要多
    if (rank &lt;= large&#91;child&#91;id]&#91;0]]) { // 排名比左子树大小要小,说明排名所对应的元素应该比该节点小,所以递归向左子树查找
        return get_val(child&#91;id]&#91;0], rank);
    } else if (rank &lt;= large&#91;child&#91;id]&#91;0]] + cnt&#91;id]) { // 比左子树大,比 左子树 + 当前节点cnt 要小
        return val&#91;id]; // 在当前节点
    } else {
        // 排名比 左子树 + 当前节点cnt 还要大,说明在右子树里,递归向右子树搜索
        // 递归时要注意,原来的排名在右子树里的新排名应为 原排名 - 左子树大小 - 当前节点cnt
        return get_val(child&#91;id]&#91;1], rank - large&#91;child&#91;id]&#91;0]] - cnt&#91;id]);
    }
}

int get_pre(int value) { // 获取比某一值value小的上一个节点(不是父节点)
    int id = root, pre = -INF;
    while (id) { // 在搜索到尽头之前
        if (val&#91;id] &lt; value) { // 如果该节点的val比value要小,说明他确实在value之前
            pre = val&#91;id];     // 更新前驱
            id = child&#91;id]&#91;1];    // 向右寻找更大的前驱
        } else {
            id = child&#91;id]&#91;0];    // 向左寻找
        }
    }
    return pre;
}

int get_next(int v) { // 获取比某一值value大的下一个节点(不是子节点)
    int id = root, next = INF;
    while (id) {
        if (val&#91;id] > v) {
            next = val&#91;id];    // 更新后继
            id = child&#91;id]&#91;0];    // 向左寻找更小的后继
        } else {
            id = child&#91;id]&#91;1];    // 向右寻找
        }
    }
    return next;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>未给出main函数，可根据实际需要进行编写。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->