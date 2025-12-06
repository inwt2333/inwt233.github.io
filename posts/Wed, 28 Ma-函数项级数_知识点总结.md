---
title: 函数项级数 知识点总结
date: Wed, 28 Ma
summary:  一致收敛性    点态收敛    对函数列$\{f_n(x)\},x\in X$，若$\{f_n(x_0)\}$收敛，则称$x_0$为收敛点，否则称之为发散点。收敛点的...
---


<!-- wp:heading -->
<h2 class="wp-block-heading">一致收敛性</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">点态收敛</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>对函数列$\{f_n(x)\},x\in X$，若$\{f_n(x_0)\}$收敛，则称$x_0$为<strong>收敛点</strong>，否则称之为<strong>发散点</strong>。收敛点的全体D称为<strong>收敛域</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定义：设$\{f_n(x)\}$的收敛域为D，且$\forall x\in D:\quad \underset{n\to\infty}\lim f_n(x) = f(x)$，则称$\{f_n(x)\}$在D上<strong>（点态）收敛</strong>，f(x)称为极限函数，记为$f_n(x)\overset{D}\longrightarrow f(x)$​。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$\epsilon -N$叙述：$f_n(x)\overset{D}\longrightarrow f(x)$即<br>$$<br>\forall x\in D,\forall \epsilon>0,\exist N=N(x,\epsilon)\in\mathbb{N},\forall n>N:|f_n(x)-f(x)|&lt;\epsilon<br>$$<br>定义：设$\{u_n(x)\}$为函数列，称$\sum_{n=1}^{\infty}u_n(x)=u_1(x)+u_2(x)+\cdots+u_n(x)+\cdots$为<strong>函数项级数</strong>，$S_n(x)=\sum_{k=1}^nu_k(x)$称为其<strong>部分和函数</strong>。若$S_n(x)\overset{D}\longrightarrow S(x)$，则称$\sum_{n=1}^{\infty}u_n(x)$在D上<strong>（点态）收敛</strong>，$S(x)$称为和函数，记为$\sum_{n=1}^{\infty}u_n(x)=S(x)$。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">一致收敛性</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：设${f_n(x)}$为函数列，若存在f(x)使$\forall \epsilon&gt;0,\exist N= N(\epsilon)\in\mathbb{N},\forall x\in D: |f_n(x)-f(x)|&lt;\epsilon$，则称${f_n(x)}$在D上<strong>一致收敛</strong>于f(x)，记为<br>$$<br>f_n(x)\overset{D}\rightrightarrows f(x)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>若$f_n(x)\overset{D}\rightrightarrows f(x)$，则$f_n(x)\overset{D}\longrightarrow f(x)$，反之不然；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>若$f_n(x)\overset{D}\rightrightarrows f(x)$，则$\forall D_1\subset D：f_n(x)\overset{D_1}\rightrightarrows f(x)$。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>不一致收敛判别法：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>或者$\{f_n(x)\}$在D上不点态收敛；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>或者虽$f_n(x)\overset{D}\longrightarrow f(x)$，但$f_n(x)$上总有一个点不趋近于$f(x)$，即$\exist \epsilon_0>0,\exist{n_k}\subset\mathbb{N},\exist x_k\in D:|f_{n_k}(x_k)-f(x_k)|>\epsilon_0$​​。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">一致收敛的判别充要条件</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理<strong>(Cauchy一致收敛准则)</strong>：<br>$$<br>f_n(x)\overset{D}\rightrightarrows f(x)\iff \forall\epsilon&gt;0,\exist N\in\mathbb{N},\forall n&gt;N,\forall p\in\mathbb{N},\forall x\in D:|f_{n+p}(x)-f_n(x)|&lt;\epsilon<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>\sum_{n=1}^\infty u_n(x)\overset{D}\rightrightarrows S(x)\iff \forall\epsilon&gt;0,\exist N\in\mathbb{N},\forall n&gt;N,\forall p\in\mathbb{N},\forall x\in D:|\sum_{k=n+1}^{n+p}u_k(x)|&lt;\epsilon<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>结论：若$\sum_{n=1}^\infty u_n(x)\overset{D}\rightrightarrows S(x)$，则$u_n(x)\overset{D}\rightrightarrows 0$​。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（确界极限）</strong>：<br>$$<br>f_n(x)\overset{D}\rightrightarrows f(x)\iff \underset{n\to\infty}\lim\underset{x\in D}\sup|f_n(x)-f(x)|=0<br>$$<br>实际应用中，为了找到上确界，通常应用求导的方式来解出f(x)在D上的最大值。如果这个最大值趋向于0，那么就证明一致收敛。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（点列极限）</strong>：<br>$$<br>f_n(x)\overset{D}\rightrightarrows f(x)\iff\forall{x_n}\subset D:\underset{n\to\infty}\lim|f_n(x_n)-f(x_n)|=0<br>$$<br>注：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>当极限函数（和函数）难以确定的时候，常用<strong>Cauchy准则</strong>；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>当极限函数（和函数）易计算时，常用<strong>定义</strong>或<strong>确界极限</strong>；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>判断不一致收敛的时候，常用<strong>点列极限</strong>。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>命题：设$u_n(x)\in C[a,b]$，且$\sum_{n=1}^{\infty}u_n(x)$在(a,b)内一致收敛，则$\sum_{n=1}^{\infty}u_n(a),\sum_{n=1}^{\infty}u_n(b)$收敛，且$\sum_{n=1}^\infty u_n(x)$在[a,b]上一致收敛。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>闭区间内连续 + 开区间内一致收敛 = 端点收敛 + 闭区间内一致收敛</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>若$u_n(x)\in C[a,b)$，且$\sum_{n=1}^\infty u_n(a)$发散，则$\sum_{n=1}^\infty u_n(a)$​在(a,b)内非一致收敛。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">内闭一致收敛</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：设D为区间，若对于任意闭区间$I\subset D$，$\{f_n(x)\}$总在$I$上一致收敛，则称$\{f_n(x)\}$​在D上<strong>内闭一致收敛</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>结论：设$\{f_n(x)\}$在(a,b)内闭一致收敛，则$\{f_n(x)\}$在(a,b)点态收敛，但是$\{f_n(x)\}$在(a,b)不一定一致收敛。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Weierstrass判别法</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：设对$\forall n\in N, \forall x\in D$有$|u_n(x)|\le M_n$，且$\sum_{n=1}^\infty M_n$（被称为<strong>优级数</strong>）收敛，则$\sum_{n=1}^\infty u_n(x)$在D上一致收敛。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$\sum_{n=1}^\infty u_n(x)$<strong>绝对一致收敛</strong>：$\sum_{n=1}^\infty |u_n(x)|$一致收敛。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">A-D判别法</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：设$\{u_n(x)\},\{v_n(x)\}$满足下列的两组条件之一，则$\sum_{n=1}^\infty u_n(x)v_n(x)$在D上一致收敛：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>（Abel）</strong>：$\forall x \in D, {v_n(x)}$单调，且在D上<strong>一致有界</strong>，$\sum_{n=1}^\infty u_n(x)$在D上<strong>一致收敛</strong>；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>（Dirichlet）</strong>：$\forall x \in D, {v_n(x)}$单调，且在D上<strong>一致趋向于0</strong>，$\sum_{n=1}^\infty u_n(x)$的部分和${S_n(x)}$在D上一致有界。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>定理<strong>（连续性）</strong>：设$f_n(x)\in C(D)$，且$f_n(x)\overset{D}\rightrightarrows f(x)$，则$f(x)\in C(D)$.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>等价形式：$\underset{x\to x_0}\lim(\underset{n\to \infty}\lim f_n(x)) = \underset{n \to \infty}\lim(\underset{x\to x_0}\lim f_n(x))$​</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>推论：若$u_n(x)\in C(D)$，且$\sum_{n=1}^\infty u_n(x)$一致收敛（或内闭一致收敛）于S(x)，则$S(x)\in C(D)$。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>逆否命题：若$f_n(x)\in C(D)$，且$f_n(x)\overset{D}\longrightarrow f(x)$，但$f(x) \notin C(D)$，则$\{f_n(x)\}$在D上不一致收敛。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>定理<strong>（Dini）</strong>：设${f_n(x)}$满足：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$f_n(x)\in C[a,b]$;</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\forall x\in [a,b], {f_n(x)}$关于n单调；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$f_n(x)\overset{[a,b]}\longrightarrow f(x)$，且$f(x)\in C[a,b]$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>则$f_n(x)\overset{D}\rightrightarrows f(x)$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（积分号下取极限）</strong>：设$f_n(x)\in C[a,b]$，且$f_n(x)\overset{D}\rightrightarrows f(x)$，则有<br>$$<br>\underset{n\to\infty}\lim\int_a^bf_n(x)\mathrm{d} x=\int_a^b(\underset{n\to\infty}\lim f_n(x))\mathrm{d} x = \int_a^bf(x)dx<br>$$<br>注：条件$f_n(x)\in C[a,b]$可减弱为$f_n(x)\in R[a,b]$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>推论<strong>（逐项可积性）</strong>：设$u_n(x)\in C[a,b]$，且$\sum_{n=1}^\infty u_n(x)$​在[a,b]上一致收敛，则<br>$$<br>\int_a^b(\sum_{n=1}^\infty u_n(x))\mathrm{d} x=\sum_{n=1}^\infty\int_a^bu_n(x)\mathrm{d} x<br>$$<br>定理<strong>（微分号下取极限）</strong>：设$f_n(x)\overset{[a,b]}\longrightarrow f(x)$，又$f_n'(x)\in C[a,b]$，且$\{f_n'(x)\}$一致收敛，则$f'(x)\in C[a,b]$<br>$$<br>\underset{n\to\infty}\lim f_n'(x)=(\underset{n\to\infty}\lim f_n(x))'=f'(x)<br>$$<br>推论<strong>（逐项可微性）</strong>：设$\sum_{n=1}^\infty u_n(x)$满足：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$\sum_{n=1}^\infty u_n(x)=S(x)$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$u_n'(x)\in C[a,b]$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\sum_{n=1}^\infty u'_n(x)$在[a,b]上一致收敛，则$S'(x)\in C[a,b]$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>$$<br>S'(x)=(\sum_{n=1}^\infty u_n(x))'=\sum_{n=1}^\infty u'_n(x)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">幂级数</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：形如$\sum_{n=0}^\infty a_n(x-x_0^n)$的函数项级数称为<strong>幂级数</strong>，其中$x_0\in\mathbb{R},a_i$称为系数。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>定理(Cauchy-Hadamard)</strong>：设$\rho=\underset{\text{n}\to\infty}\varlimsup \sqrt[n]{|a_n|}$，则</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>当$0&lt;\rho&lt;+\infty$时，$\sum_{n=0}^\infty a_nx^n$在$(-\frac{1}{\rho},\frac{1}{\rho})$内绝对收敛，在$|x|>\frac{1}{rho}$发散；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>当$\rho=0$时，$\sum_{n=0}^\infty a_nx^n$在$(-\infty,+\infty)$内绝对收敛；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>当$\rho=+\infty$时，$\sum_{n=0}^\infty a_nx^n$仅在$x=0$处收敛。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>收敛半径：$r=\frac{1}{\rho}$；收敛区间：$(-r,r)$​。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>另：若$\underset{n\to\infty}\lim\frac{|a_{n+1}|}{|a_n|}$存在广义极限，则$r=\underset{n\to\infty}\lim\frac{|a_n|}{|a_{n+1}|}$​</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Abel定理</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Abel第一定理</strong>：设$\sum_{n=0}^\infty a_nx^n$在$x_1\ne 0$处收敛，则$|x|&lt;|x_1|$时绝对收敛；若$\sum_{n=0}^\infty a_nx^n$在$x_2$处发散，则$|x|&gt;|x_2|$时发散。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>结论：幂级数的条件收敛点（若存在）到中心的距离即为收敛半径。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Abel第二定理</strong>：设$\sum_{n=0}^\infty a_nx^n$收敛半径为r(&gt;0)，则它在$(-r,r)$内闭一致收敛；若$x=r$时收敛，则它在$[0,r]$一致收敛，从而在$(-r,r]$内闭一致收敛。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>注：内闭一致收敛性是幂级数的特性，一般函数项级数未必具有。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">幂级数的分析性质</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：幂级数$\sum_{n=0}^\infty a_nx^n$与其<strong>导数级数</strong>$\sum_{n=1}^{\infty}na_nx^{n-1}$和<strong>积分级数</strong>$\sum_{n=0}^\infty \frac{a_n}{n+1}x^{n+1}$的收敛半径相等。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>注意⚠️：</strong>三个级数在端点处的收敛性未必相同</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>定理：设$f(x)=\sum_{n=0}^\infty a_nx^n,\quad x\in(-r,r)$​，则</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$f(x)\in C(-r,r)$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$f(x) \in D(-r,r)$，且可逐项求导，即$\forall x\in(-r,r):f'(x)=(\sum_{n=0}^\infty a_nx^n)'=\sum_{n=0}^\infty(a_nx^n)'=\sum_{n=1}^\infty na_nx^{n-1}$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>可逐项积分，即$\forall x\in(-r,r):\int_0^xf(t)\mathrm{d} t=\int_0^x(\sum_{n=0}^\infty a_nt^n)\mathrm{d} t =\sum_{n=0}^\infty\int_0^xa_nt^n\mathrm{d} t=\sum_{n=0}^\infty\frac{a_n}{n+1}x^{n+1}$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Abel第三定理</strong>：设$f(x)=\sum_{n=0}^{\infty}a_nx^n\quad x\in(-r,r]$，则f(x)在x=r处<strong>左连续</strong>，即<br>$$<br>\underset{x\to r^-}\lim \sum_{n=0}^\infty a_nx^n=\sum_{n=0}^\infty a_nr^n<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">函数的幂级数展开</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Taylor级数</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：设$f(x)$在$x_0$处无穷次可导，则称f(x)在$x_0$处的<strong>Taylor级数</strong>为<br>$$<br>f(x)\sim\sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n<br>$$<br>$x_0=0$时称为<strong>Maclaurin</strong>级数。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>为什么用～而不是用=？是因为我们不知道其到底收不收敛，如果不收敛则不能认为其相等，那么如何判断其是否收敛？</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理：设$f\in C^{(\infty)}(I)$，且$\forall n\in \mathbb{N}, \forall x\in I:|f^{(n)}(x)|\le M$，则$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n\quad(\forall x\in I)$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（唯一性）</strong>：若$f(x)=\sum_{n=0}^\infty a_n(x-x_0)^n,\quad x\in(x_0-r,x_0+r)$（此时称f(x)在$x_0$处<strong>可展开为幂级数</strong>)，则必有$a_n=\frac{f^{(n)}(x_0)}{n!}$.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Stirling公式</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理<strong>（Stirling公式）</strong><br>$$<br>n!=\sqrt{2n\pi}(\frac{n}{e})^ne^{\frac{\theta_n}{12n}}\quad(0&lt;\theta_n&lt;1)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Fourier级数</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设在$[-\pi,\pi]$上函数f(x)可展开为三角级数，即<br>$$<br>f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)<br>$$<br>利用正交性，可以得到<br>$$<br>\left{\begin{matrix}a_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos nx\mathrm{d} x\b_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin nx\mathrm{d} x\a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\mathrm{d}x\end{matrix}\right.<br>$$<br><strong>可积与绝对可积</strong>：函数f满足下两条件之一：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$f\in R[-\pi,\pi]$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>瑕积分$\int_{-\pi}^\pi f(x)\mathrm{d}x$绝对收敛</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>定义：设f(x)以$2\pi$为周期，且在$[-\pi,\pi]$上可积与绝对可积，以f的Fourier系数$a_n,b_n$为系数的三角级数称为f(x)的<strong>Fourier级数（F氏级数）</strong>，记为<br>$$<br>f(x)\sim\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">正弦和余弦级数</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设f(x)在$[-\pi,\pi]$上可积与绝对可积，且为<strong>奇函数</strong>，则其Fourier级数中$a_n=0$，<br>$$<br>b_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin nx\mathrm{d}x=\frac{2}{\pi}\int_0^\pi f(x)\sin nx\mathrm{d}x<br>$$<br>其Fourier级数$f(x)\sim\sum_{n=1}^\infty b_n\sin nx$称为<strong>正弦级数</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>同理，设f(x)在$[-\pi,\pi]$上可积与绝对可积，且为<strong>偶函数</strong>，则其Fourier级数中$b_n=0$​，<br>$$<br>a_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos nx\mathrm{d} x=\frac{2}{\pi}\int_0^\pi f(x)\cos nx\mathrm{d}x,\quad a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\mathrm{d}x = \frac{2}{\pi}\int_0^\pi f(x)dx<br>$$<br>其Fourier级数$f(x)\sim\frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos nx$​称为<strong>余弦级数</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>约定：若f仅在$[0,\pi]$（或$[-\pi,0]$）上可积或绝对可积，对f作<strong>奇延拓</strong>后所得函数$f_0$的F氏（正弦）级数也称为f的<strong>正弦级数</strong>，此时<br>$$<br>b_n=\frac{2}{\pi}\int_0^\pi f(x)\sin nx\mathrm{d}x<br>$$<br>同理，对对f作<strong>偶延拓</strong>后所得函数$f_0$的F氏（余弦）级数也称为f的<strong>余弦级数</strong>，此时<br>$$<br>a_n=\frac{2}{\pi}\int_0^\pi f(x)\cos nx\mathrm{d}x,\quad a_0=\frac{2}{\pi}\int_0^\pi f(x)dx<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Fourier级数的收敛性</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Fourier级数的部分和函数<br>$$<br>S_n(f,x)=\frac{a_0}{2}+\sum_{k=1}^n(a_k\cos kx+b_k\sin kx)<br>$$<br>称为f的n阶<strong>Fourier多项式</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>结论：<br>$$<br>S_n(f,x)=\frac{1}{\pi}\int_{-\pi}^\pi f(x+u)\frac{\sin\frac{2n+1}{2}u}{2\sin\frac{u}{2}}\mathrm{d}u=\frac{1}{\pi}\int_{0}^\pi [f(x+u)+f(x-u)]\frac{\sin\frac{2n+1}{2}u}{2\sin\frac{u}{2}}\mathrm{d}u<br>$$<br>定义<strong>Dirichlet积分核</strong>：<br>$$<br>D_n(u)=\frac{\sin\frac{2n+1}{2}u}{2\sin\frac{u}{2}}<br>$$<br>简单事实：<br>$$<br>\frac{2}{\pi}\int_0^\pi D_n(u)\mathrm{d}u=\frac{2}{\pi}\int_0^\pi (\frac{1}{2}+\sum_{k=1}^n\cos ku)\mathrm{d}u=1<br>$$<br>命题：设S(x)是任一给定函数，则<br>$$<br>\underset{n\to\infty}\lim S_n(f,x)=S(x)\iff\underset{n\to\infty}\lim\frac{1}{\pi}\int_0^\pi[f(x+u)+f(x-u)-2S(x)]D_n(u)\mathrm{d}u=0<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">局部性定理</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Riemann引理</strong>：设f在[a,b]上可积与绝对可积，则<br>$$<br>\underset{p\to\infty}\lim\int_a^bf(u)\sin pu\mathrm{d}u=0=\underset{p\to\infty}\lim\int_a^bf(u)\cos pu\mathrm{d}u<br>$$<br>定理<strong>（局部性）</strong>：设f(x)以$2\pi$为周期，在$[-\pi,\pi]$上可积与绝对可积，则f的F氏级数在x处的收敛性及收敛时的值仅与f在U(x)的值相关。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>推论：同局部性定理假设，则$\forall \delta &gt; 0,$<br>$$<br>\underset{n\to\infty}\lim\frac{1}{\pi}\int_0^\delta\frac{f(x+u)+f(x-u)-2S(x)}{2sin\frac{u}{2}}\cdot\sin\frac{2n+1}{2}u\mathrm{d}u=\underset{n\to\infty}\lim\frac{1}{\pi}\int_0^\delta\frac{f(x+u)+f(x-u)-2S(x)}{u}\cdot\sin\frac{2n+1}{2}u\mathrm{d}u<br>$$<br>推论：<br>$$<br>\int_0^{+\infty}\frac{\sin x}{x}\mathrm{d}x=\frac{\pi}{2}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（Dini）</strong>：设f满足局部性定理条件，且$\exist \delta\in(0,\pi)$使$\frac{f(x+u)+f(x-u)-2S(x)}{u}$在$[0,\delta]$上可积与绝对可积，则$\underset{n\to\infty}\lim S_n(f,x)=S(x)$。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">F氏级数收敛性判别法</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：设$f:[a,b]\to\mathbb{R}$，若可将[a,b]分为有限个子区间，使f在每个开子区间上单调有界，则称f为<strong>分段单调函数</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Dirichlet引理</strong>：设g在[0,h]上<strong>单调或分段单调</strong>，则<br>$$<br>\underset{p\to\infty}\lim\int_0^h\frac{g(u)-g(0+0)}{u}\sin pu\mathrm{d} u=0<br>$$<br>等价形式：<br>$$<br>\underset{p\to\infty}\lim\int_0^hg(u)\frac{\sin pu}{u}\mathrm{d}u=\frac{\pi}{2}g(0+0)<br>$$<br>定理：设f以$2\pi$为周期，在$[-\pi,\pi]$上可积与绝对可积，且满足下面两条件之一，则f的F氏级数在x处收敛于<br>$$<br>\frac{f(x+0)+f(x-0)}{2}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>(Dirichlet-Jordan)</strong>：f在$U(x,\delta]$上分段单调或为分段单调函数之和；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>(Dini-Lipschitz)</strong>：f在x处满足指数为$\alpha\in(0,1]$的Holder条件，即$|f(x\pm u) - |f(x\pm 0)| \le Lu^\alpha$.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>推论：设f以$2\pi$为周期，在$[-\pi,\pi]$上至多有限个第一类间断点，且仅有有限个严格极值点，则<br>$$<br>f(x)\sim\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)=\begin{Bmatrix}f(x),&amp;x\text{ is a continuity point},\\frac{f(x+0)+f(x-0)}{2},&amp;x\text{ is a discontinuity point},\\frac{f(-\pi+0)+f(\pi-0)}{2},&amp;x = \pm \pi.\end{Bmatrix}=S(x)<br>$$<br>定义：f在x处的<strong>拟左、右导数</strong>分别定义为<br>$$<br>\underset{u\to 0^+}\lim\frac{f(x-u)-f(x-0)}{-u},\quad \underset{u\to 0^-}\lim\frac{f(x+u)-f(x+0)}{u}<br>$$<br>推论：设f以$2\pi$为周期，在$[-\pi,\pi]$上可积与绝对可积，且在x处<strong>有左、右导数（或拟左、右导数）</strong>，则f的F氏级数在x处收敛于$\frac{f(x+0)+f(x-0)}{2}$.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Fourier级数的性质</h3>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Fourier级数的分析性质</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>分段连续函数</strong>：f在[a,b]上仅有有限个第一类间断点。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（逐项积分）</strong>：设f在$[-\pi,\pi]$上分段连续（可以减弱为<strong>可积与连续可积</strong>），又$f(x)\sim\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)$，则$\forall x \in[-\pi,\pi]$有：<br>$$<br>\int_0^x f(t)\mathrm{d}t=\frac{a_0}{2}x+\sum_{n=1}^\infty\int_0^x(a_n\cos nt+b_n\sin nt)\mathrm{d}t=\frac{a_0}{2}x+\sum_{n=1}^\infty(\frac{a_n}{n}\sin nx-\frac{b_n}{n}\cos nx+\frac{b_n}{n})<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>推论<strong>（必要条件）</strong>：设f在$[-\pi,\pi]$上可积与绝对可积，又$f(x)\sim\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)$，则$\sum_{n=1}^{\infty}\frac{b_n}{n}$收敛，且<br>$$<br>\sum_{n=1}^{\infty}\frac{b_n}{n}=\frac{1}{2\pi}\int_{-\pi}^\pi(\int_0^xf(t)\mathrm{d}t)\mathrm{d}x<br>$$<br>结论：若$\sum_{n=1}^{\infty}\frac{b_n}{n}$发散，则三角级数$\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx)$必不是F氏级数。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理<strong>（逐项微分）</strong>：设$f\in D[\pi,\pi]$，且$f(-\pi)=f(\pi)$，若$f'(x)$可积与绝对可积，则<br>$$<br>f'(x)\sim \sum_{n=1}^\infty\frac{\mathrm{d}}{\mathrm{d}x}(a_n\cos nx+b_n\sin nx)=\sum_{n=1}^\infty(nb_n\cos nx-na_n\sin nx)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">F氏级数的逼近和Bessel不等式</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>记<strong>n阶三角多项式</strong>集合为<br>$$<br>T=\{T_n(x)|T_n(x)=\frac{\alpha_0}{2}+\sum_{k=1}^N(\alpha_k\cos kx+\beta_k\sin kx)\}<br>$$<br>又记X={ f(x) | f在$[-\pi,\pi]$​上可积与平方可积 }</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定义：函数f和g的<strong>（平方平均偏差）距离</strong>为<br>$$<br>d(f,g)=(\frac{1}\pi\int_{-\pi}^\pi[f(x)-g(x)]^2\mathrm{d}x)^{\frac{1}{2}}<br>$$<br>定理：设$f\in X$，则对$\forall T_n\in T$有<br>$$<br>d(f,S_n(x))\le d(f,T_n(x))<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>推论<strong>（Bessel不等式）</strong>：设$f\in X$，则f的Fourier系数满足<br>$$<br>\frac{a_0^2}{2}+\sum_{n=1}^\infty(a_n^2+b_n^2)\le\frac{1}{\pi}\int_{-\pi}^\pi f^2(x)\mathrm{dx}<br>$$<br>推论：设$f\in X$，则级数$\frac{a_0^2}{2}+\sum_{n=1}^\infty(a_n^2+b_n^2)$收敛，从而<br>$$<br>\underset{n\to\infty}\lim a_n=0=\underset{n\to\infty}\lim b_n<br>$$<br>其中$a_n,b_n$是f的Fourier系数。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>推论：设f在$[-\pi,\pi]$上除有限点外可导，在这有限点处单侧可导，且$f(-\pi)=f(\pi)$，若$f'(x)$可积与绝对可积，则f的F氏级数在$[-\pi,\pi]$上一致收敛于f(x)。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定理：设$f\in X$，则$\{S_n(x)\}$平方平均收敛于f，即<br>$$<br>\underset{n\to\infty}\lim d(f,S_n)=0<br>$$<br>或<strong>Parseval等式</strong>成立，即f的Fourier系数满足<br>$$<br>\frac{a_0^2}{2}+\sum_{n=1}^\infty(a_n^2+b_n^2)=\frac{1}{\pi}\int_{-\pi}^\pi f^2(x)dx<br>$$<br>推论：设$f\in C[-\pi,\pi]$，且f与三角函数系{1,cosx,sinx,…,cosnx,sinnx}中的每一个都正交，则$f\equiv 0$。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>若$f,g\in C[-\pi,\pi]$，且F氏级数相等，则$f(x)\equiv g(x)$。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>推论：设$f,g\in X$，其F氏级数分别为$a_n,b_n$和$\bar{a_n},\bar{b_n}$，则<br>$$<br>\frac{1}{\pi}\int_{-\pi}^\pi f(x)g(x)\mathrm{d}x=\frac{a_0\bar{a_0}}{2}+\sum_{n=1}^\infty(a_n\bar{a_n}+b_n\bar{b_n})<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">一些杂点：</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>含参积分求导：<br>$$<br>\int_{\alpha(x)}^{\beta(x)}f(x,y)\mathrm{d}y=\int_{\alpha(x)}^{\beta(x)}\frac{\partial f}{\partial x}\mathrm{d}y+f(x,\beta(x))\beta'(x)-f(x,\alpha(x))\alpha'(x)<br>$$</p>
<!-- /wp:paragraph -->