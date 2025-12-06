---
title: 重积分 知识点总结
date: Mon, 07 Ap
summary:    1. 分划的定义：设$D$为$\mathbb{R}^2$上可求面积的有界区域，将$D$分为有限个集合之和：$D= {\textstyle \bigcup_{k=1}^{...
---


<!-- wp:paragraph -->
<p>1. <strong>分划</strong>的定义：设$D$为$\mathbb{R}^2$上可求面积的有界区域，将$D$分为有限个集合之和：$D= {\textstyle \bigcup_{k=1}^{n}} \Delta D_k, \Delta D_k$可求面积且两两无公共内点，则称其为$D$的一个分划，记作$\Delta = {\Delta D_1, \Delta D_2, \cdot \cdot \cdot , \Delta D_n}$. 分划的直径定义为$||\Delta || = max_{1 \le k \le n}{diam(\Delta D_k)}$，其中$diam(\Delta D_k)$表示集合$\Delta D_k$直径。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>2. <strong>二重积分</strong>的定义：设$D$为$\mathbb{R}^2$上可求面积的有界区域，函数$f(x,y)$在$D$上定义。如果对于$D$的任意分划$\Delta = {\Delta D_1, \Delta D_2, \cdot \cdot \cdot , \Delta D_n}$(记集合$\Delta D_i$的面积为$\Delta \sigma_{i}$)及任意取点$(\xi _i, \eta _i)\in \Delta D_i(i=1,\cdot \cdot \cdot ,n)$. 当分划直径$||\Delta ||$趋近于零时，Riemann和当极限都存在：$\lim_{||\Delta|| \to 0} \sum_{i=1}^{n} f(\xi_i,\eta_i)\Delta\sigma_i=I$，则称$f(x,y)$在$D$上可积，称$I$为$f(x,y)$在$D$上的二重积分，记作$I=\iint\limits_{D}f(x,y)d\sigma$，或$I=\iint\limits_{D}f(x,y)dxdy$​​.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3. <strong><em>Darboux</em>大和，小和</strong>：设$M_i$和$m_i$分别为$f(x,y)$在$\Delta D_i$上的上下确界，定义<em>Darboux</em>大和为$S(f,\Delta) = \sum_{i=1}^{n}M_i\Delta\sigma_i$，<em>Darboux</em>小和为$s(f,\Delta) = \sum_{i=1}^{n}m_i\Delta\sigma_i$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>4. <strong>可积性的等价命题</strong>：对于可求面积的有界区域$D$及其上有界的函数$f(x,y)$，下列命题等价：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$f(x,y)$在$D$上可积；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$inf_{\Delta}{S(f,\Delta)} \le sup_{\Delta}{s(f,\Delta)}$；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\lim_{||\Delta|| \to 0}(S(f,\Delta) - s(f,\Delta)) = 0$​；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>对于任意$\epsilon &gt; 0$，存在分划$D$使得$\sum_{i=1}^{n}\omega_i\Delta\sigma_i&lt; \epsilon $，其中$\omega_i$表示$f(x,y)$在$D_i$上的振幅。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>5. <strong>二次积分</strong>：设$f:[a,b] \times [c,d] \to \mathbb{R}$, 对于任意给定的$x\in[a,b]$，若存在首次积分$\phi(x)=\int_{c}^{d}f(x,y)dy$，且$\phi$在$[a,b]$上可积，则称$\int_{a}^{b}\phi(x)dx=\int_a^b(\int_c^df(x,y)dy)dx$为$f$在$[a,b]\times[c,d]$上先$y$后$x$的累次（二次）积分，也可记为$\int_a^bdx\int_c^df(x.y)dy$.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>二重积分存在不能导出二次积分存在。</strong></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>二次积分存在不能导出二重积分存在。</strong></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>6. 设$f(x,y)$在$[a,b]\times[c,d]$上可积，且$\forall x\in[a,b]$存在首次积分$F(x)=\int_c^df(x,y)dy$，则$\iint_{[a,b]\times[c,d]}f(x,y)d\sigma = \int_a^bdx\int_c^df(x,y)dy$​.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>若二重积分存在，且对x或y的首次积分存在，则二重积分和二次积分相等。</strong></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>7. 设$f(x,y)$在$[a,b]\times[c,d]$上<strong>连续</strong>，则有$\iint_{[a,b]\times[c,d]}f(x,y)d\sigma = \int_a^bdx\int_c^df(x,y)dy=\int_c^ddy\int_a^bf(x,y)dx$​.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>8. 设$f(x,y)$在$x$型区域$D={(x,y)|a\le x \le b, y_1(x) \le y \le y_2(x)}$上连续，其中$y_1(x),y_2(x)$是$[a,b]$上的一元连续函数，则有$\iint_D f(x,y)d\sigma=\int_a^bdx\int_{y_1(x)}^{y_2(x)}f(x,y)dy$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>9. <strong>极坐标计算二重积分</strong>：$\iint_Df(x,y)dxdy$=$\iint_{D'}f(rcos\theta,rsin\theta)rdrd\theta$=$\int_\alpha^\beta d\theta\int_{r_1(\theta)}^{r_2(\theta)}f(rcos\theta,rsin\theta)rdrd\theta$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>10. <strong>二重积分的变量替换</strong>：设变换$T:\left{\begin{matrix}x=x(u,v)\y=y(u,v)\end{matrix}\right.$有连续偏导数，且满足$J=\frac{\partial (x,y)}{\partial (u,v)}=\begin{vmatrix}x_u&amp;x_v\\y_u&amp;y_v\end{vmatrix}\neq0$，又$f(x,y)\in C(D)$，则$\iint_Df(x,y)dxdy=\iint_{D'}f(x(u,v),y(u,v))|J|dudv$，其中$T$将$D'$变为$D$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>11. <strong>三重积分的计算：</strong>在直角坐标下，由于$dV=dxdydz$，因此有$\iiint_\Omega f(x,y,z)dV = \iiint_\Omega f(x,y,z)dxdydz$. 设$f(x,y,z)$在$[a,b]\times[c,d]\times[e,h]$上可积，</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>12. <strong>柱线法（坐标面投影法）</strong>：设$\Omega$是以曲面$z=z_1(x,y)$为底，曲面$z=z_2(x,y)$为顶，而侧面是母线平行z轴的柱面所围成区域。又$\Omega$在xy平面上投影区域为$D$，则$\Omega$可表示为xy型正则区域${(x,y,z)|z_1(x,y)\le z \le z_2(x,y), (x,y)\in D}$. 从而（不妨设$D={(x,y,z)|a \le x \le b,y_1(x)\le y \le y_2(x)}$） $\iiint_\Omega f(x,y,z)dxdydz = \int_a^bdx\int_{y_1(x)}^{y_2(x)}dy\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)dz$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>13. <strong>截面法（坐标轴投影法）</strong>：设$\Omega$在z轴上的投影区间为$[h_1,h_2]$，即$\Omega$介于平面$z=h_1$与$z=h_2$之间，过z处且垂直z轴的平面截$\Omega$得截面区域$D_z$，则$\Omega$可表示为z型空间区域$\Omega={(x,y,z)|h_1\le z \le h_2,(x,y)\in D_z}$.<br>从而$\iiint_\Omega f(x,y,z)dxdydz = \int_{h_1}^{h_2}dz\iint_{D_z}f(x,y,z)dxdy$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>14.<strong>三重积分的变量替换</strong>：设变换$T:\left{\begin{matrix}x=x(u,v,w)\y=y(u,v,w)\z=z(u,v,w)\end{matrix}\right.$有连续偏导数，且满足$J=\frac{\partial (x,y,z)}{\partial (u,v,w)}=\begin{vmatrix}x_u&amp;x_v&amp;x_w\\y_u&amp;y_v&amp;y_w\\z_u&amp;z_v&amp;z_w\end{vmatrix}\neq0$，又$f(x,y,z)\in C(\Omega)$，则$\iiint_\Omega f(x,y,z)dxdydz = \iiint_{\Omega'} f(x(u,v,w),y(u,v,w),z(u,v,w))|J|dudvdw$，其中$T$将$\Omega'$变为$\Omega$​.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>15.<strong>柱面坐标</strong>：柱面坐标系实质上就是将$(x,y)$坐标转变为极坐标，其变换为$T:\left{\begin{matrix}x=rcos\theta\y=rsin\theta\z=z\end{matrix}\right.$. 由$|J|=r&gt;0$，得到柱面坐标积分公式 $\iiint_\Omega f(x,y,z)dxdydz = \iiint_{\Omega'} f(rcos\theta,rsin\theta,z)rdrd\theta dz$​.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>16.<strong>球坐标</strong>：设$M(x,y,z)$是空间中一点，引进球面坐标$(\rho,\phi,\theta)$，其中$\rho = ||\overrightarrow{OM} ||\in[0,+\infty),\phi\in[0,\pi]$表示向量$\overrightarrow{OM} $与z正半轴间的夹角，$\theta\in[0,2\pi]$表示x正半轴逆时针转到$\overrightarrow{OP} $的角度（其中$P(x,y,0)$是点$M(x,y,z)$在xy平面内的投影）；坐标变换关系式为：$\left{\begin{matrix}x=\rho sin\phi cos\theta\\y=\rho sin\phi sin\theta\\z=\rho cos\phi\end{matrix}\right.$. 由$|J|=\rho^2sin\phi$，导出$\iiint_\Omega f(x,y,z)dxdydz = \iiint_{\Omega'} f(\rho sin\phi cos\theta,\rho sin\phi sin\theta,\rho cos\phi)\rho^2sin\phi d\rho d\phi d\theta$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>17. <strong>多重积分</strong>：设$f$在$\Omega = [a_1,b_1]\times[a_2,b_2]\times \cdot\cdot\cdot\times[a_n,b_n]$上连续，则$\iint\cdot\cdot\cdot\int_\Omega f(x_1,x_2,\cdot\cdot\cdot,x_n)dx_1dx_2\cdot\cdot\cdot dx_n$=$\int_{a_1}^{b_1}dx_1\int\cdot\cdot\cdot\int_{[a_2,b_2]\times \cdot\cdot\cdot\times[a_n,b_n]}f(x_1,x_2,\cdot\cdot\cdot,x_n)dx_2 \cdot\cdot\cdot dx_n$ = $\int\cdot\cdot\cdot\int_{[a_1,b_1]\times \cdot\cdot\cdot\times[a_{n-1},b_{n-1}]}dx_1\cdot\cdot\cdot dx_{n-1}\int_{a_n}^{b_n}f(x_1,x_2,\cdot\cdot\cdot,x_n)dx_n$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>终于把期中考试之前的内容敲完了，$\LaTeX$ 确实有点太费手了...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->