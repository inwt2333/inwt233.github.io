---
title: 多元函数微分学 知识点总结
date: Tue, 01 Ap
summary:  1. 若函数$f$在点$(x_{0},y_{0})$处可微，则$f$在点$(x_{0},y_{0})$处连续。（可微必连续）  2. 可微必可偏导，不可偏导必不可微。  若偏...
---

1. 若函数$f$在点$(x_{0},y_{0})$处可微，则$f$在点$(x_{0},y_{0})$处连续。（<strong>可微必连续</strong>）

2. <strong>可微必可偏导</strong>，不可偏导必不可微。

若偏导数在$(x_{0},y_{0})$处连续，则$f$在点$(x_{0},y_{0})$处可微分，

即验证$\lim_{\rho \to 0} \frac{\Delta f - [f_{x}(x_{0},y_{0}) \Delta x + f_{y}(x_{0},y_{0}) \Delta y]}{\rho}=0$​<strong>是否成立</strong>。

3. <strong>方向导数</strong>的定义：设函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$的邻域内有定义，$l$为非零向量，其方向余弦为$cos\alpha ,cos\beta$，若极限$\lim_{t \to 0} \frac{f(x_{0}+tcos\alpha,y_{0}+tcos\beta)-f(x_0,y_0)}{t}=0$存在，则称此极限值为函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$处沿$l$的方向导数，记作$\frac{\partial f}{\partial l} \bigg|_{(x_{0},y_0)}$​，或$\frac{\partial z}{\partial l} \bigg|_{(x_{0},y_0)}$.

Thm: 若函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$处可微，$l$的方向余弦为$cos\alpha ,cos\beta$，则函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$处沿$l$的方向导数存在，且$\frac{\partial z}{\partial l} \bigg|_{(x_{0},y_0)} = f_x(x_0,y_0)cos\alpha + f_y(x_0,y_0)cos\beta$.

4.<strong> 梯度</strong>：若函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$处可微，则称向量$(f_x(x_0,y_0),f_y(x_0,y_0))$为函数$z=f(x,y)$在点$P_{0}(x_{0},y_{0})$处的梯度，记为$\textbf{grad}f\bigg|_{(x_0,y_0)},\textbf{grad}f(x_0,y_0),\grad f\bigg|_{(x_0,y_0)}或\grad f(x_0,y_0)$.

这里$\grad=(\frac{\partial}{\partial x},\frac{\partial}{\partial y} )$是一个算子，称为<strong>向量微分算子</strong>或<strong>Hamilton算子</strong>，读作Nabla.

<strong>方向导数最大的方向，即为梯度的方向。</strong>

5. 多元函数的混合高阶偏导数<strong>连续</strong>，则他们与求偏导数的<strong>次序无关</strong>。

6. <strong>隐函数存在定理</strong>：设函数$F(x,y)$在$(x_{0},y{_0})$的邻域内具有连续偏导数，且$F(x_0,y_0) = 0, {F_y(x_0,y_0)\neq0}$，则方程$F(x,y)=0$在$(x_{0},y{_0})$的某邻域内可确定唯一的隐函数$y=y(x)$，满足$F(x,y(x)) \equiv 0, y_0 = y(x_0)$，且有连续导数$\frac{dy}{dx}=-\frac{F_x(x,y)}{F_y(x,y)}$.

<strong>注意</strong>：如果确定的隐函数是$x=x(y)$，那么就要保证${F_x(x_0,y_0)\neq0}$​​，即**哪个在分母上哪个不为零**。

<strong>理解</strong>：对于一个曲面与xOy平面的交线，隐函数存在定理可以求出这条交线某一点处y对x（或x对y）的导数。所以要求分母不为0是为了保证该点处导数存在。

7. <strong>隐映射存在定理</strong>：设函数$F(x,y,u,v),G(x,y,u,v)$满足如下条件：
<ul>
 	<li>在$(x_0,y_0,u_0,v_0)$的某一邻域内，$F,G$具有连续偏导数；</li>
 	<li>$F(x_0,y_0,u_0,v_0) = 0, G(x_0,y_0,u_0,v_0) = 0$;</li>
 	<li>行列式$J_0=\begin{vmatrix}F_u &amp;F_v \\G_u&amp;G_v\end{vmatrix}_{(x_0,y_0,u_0,v_0)}\neq0$​</li>
</ul>
那么：
<ul>
 	<li>在$(x_0,y_0,u_0,v_0)$的某一邻域内，方程组$\left\{\begin{matrix}F(x,y,u,v)=0\\G(x,y,u,v)=0\end{matrix}\right.$可确定唯一隐映射$\begin{pmatrix}u\\v\end{pmatrix}=\begin{pmatrix}u(x,y) \\v(x,y)\end{pmatrix}$，满足$\left\{\begin{matrix}F(x,y,u(x,y),v(x,y))=0,\\G(x,y,u(x,y),v(x,y))=0\end{matrix}\right.$​且$\left\{\begin{matrix}u_0=u(x_0,y_0)\\v_0=v(x_0,y_0)\end{matrix}\right.$;</li>
 	<li>该隐映射在$(x_0,y_0,u_0,v_0)$的某一邻域内连续；</li>
 	<li>该隐映射在$(x_0,y_0,u_0,v_0)$的某一邻域内具有连续偏导数，且$\begin{bmatrix}u_x&amp;u_y\\v_x&amp;v_y\end{bmatrix}=-\frac{\begin{bmatrix}F_x&amp;F_y\\G_x&amp;G_y\end{bmatrix}}{\begin{bmatrix}F_u&amp;F_v\\G_u&amp;G_v\end{bmatrix}}$.</li>
</ul>
记$J=\begin{vmatrix}F_u &amp; F_v\\G_u&amp;G_v \end{vmatrix}=\frac{\partial (F,G) }{\partial(u,v)}$，并称之为F，G关于u，v的<strong>Jacobi行列式</strong>，则上式可分解成：

$u_x = -\frac{1}{J}\frac{\partial (F,G) }{\partial(x,v)},u_y = -\frac{1}{J}\frac{\partial (F,G) }{\partial(y,v)},v_x = -\frac{1}{J}\frac{\partial (F,G) }{\partial(u,x)},v_y = -\frac{1}{J}\frac{\partial (F,G) }{\partial(u,y)}$​
<ul>
 	<li><strong>记忆</strong>：Jacobi行列式放分母上，上面是Jacobi行列式中将出现的字母换成另一个出现的字母，别忘加负号。</li>
 	<li><strong>理解</strong>：类似于换元，将x和y通过某种规则换元成u和v，但是这个规则是以隐函数的形式出现的，即$x,y,u,v$交杂在一起没办法分开，这个时候隐映射存在定理就能够求出来u, v关于x, y的偏导。</li>
</ul>
8. <strong>逆映射存在性</strong>：设映射$f$在区域$D\subset R^2$内有连续偏导数，$(x_0,y_0)\in D$. 记$u_0=u(x_0,y_0),v_0=v(x_0,y_0)$，且Jacobi行列式$J_0=\frac{\partial (u,v) }{\partial(x,y)}\bigg|_{(x_0,y_0)}\neq 0$，则存在$(u_0,v_0)$的某邻域$U(u_0,v_0)\subset D'$，在该邻域内存在$f$具有连续偏导数的映射$f^{-1}$. 若设其坐标分量函数为$\left\{\begin{matrix}x=x(u,v)\\y=y(u,v)\end{matrix}\right.$，则满足$\left\{\begin{matrix}x_0=x(u_0,v_0)\\y_0=y(u_0,v_0)\end{matrix}\right.$，且有$\frac{\partial x}{\partial u} =\frac{1}{J}\frac{\partial v}{\partial y},\frac{\partial y}{\partial u} =-\frac{1}{J}\frac{\partial v}{\partial x},\frac{\partial x}{\partial v} =-\frac{1}{J}\frac{\partial u}{\partial y},\frac{\partial y}{\partial v} =\frac{1}{J}\frac{\partial u}{\partial x}$.
<ul>
 	<li><strong>记忆</strong>：原来u, v可以用x, y表示，现在想要让x, y用u, v表示，那么还是底下先放一个Jacobi行列式，将x, y互换，u, v互换，然后分子分母上下颠倒，如果一侧在同一列（即x与u，y与v）则不用加负号，否则前面填负号。）</li>
</ul>
9. 对于<strong>空间曲线</strong>$\Gamma$：
<ul>
 	<li>若$\Gamma$的参数方程为$x=x(t),y=y(t),z=z(t)$，其中$x(t),y(t),z(t)$具有连续的导数，则曲线$\Gamma$在点$M_0(x_0,y_0,z_0)$处的<strong>切向量</strong>$\tau =(x'(t),y'(t),z'(t))$.</li>
 	<li>若空间曲线$\Gamma$以一般式方程$\left\{\begin{matrix}F(x,y,z)=0\\G(x,y,z)=0\end{matrix}\right.$给出，并满足隐映射定理的条件，则曲线$\Gamma$在点$M_0(x_0,y_0,z_0)$处的<strong>切向量</strong>$\tau=(\frac{\partial (F,G)}{\partial (y,z)},\frac{\partial (F,G)}{\partial (z,x)},\frac{\partial (F,G)}{\partial (x,y)})$。</li>
 	<li>已知曲线$\Gamma$在点$M_0(x_0,y_0,z_0)$处的切向量$\tau = (a,b,c)$，则曲线在$M_0$处的<strong>切线方程</strong>为$\frac{x-x_0}{a}=\frac{y-y_0}{b}=\frac{z-z_0}{c}$，<strong>法平面</strong>方程为$a(x-x_0)+b(y-y_0)+c(z-z_0)=0$.</li>
</ul>
10. 对于<strong>空间曲面</strong>$S$：设曲面的一般式方程为$F(x,y,z)=0$，其中偏导数$F_x,F_y,F_z$​连续，则在点$M_0(x_0,y_0,z_0)$处：
<ul>
 	<li>曲面$S$在点$M_0$处的<strong>法向量</strong>可取为$\grad F(M_0) = (F_x(M_0),F_y(M_0),F_z(M_0))$;</li>
 	<li>曲面$S$在点$M_0$处的<strong>切平面</strong>方程为$F_x(M_0)(x-x_0)+F_y(M_0)(y-y_0)+F_z(M_0)(z-z_0)=0$​；</li>
 	<li>曲面$S$在点$M_0$处的<strong>法线</strong>方程为$\frac{x-x_0}{F_x(M_0)}=\frac{y-y_0}{F_y(M_0)}=\frac{z-z_0}{F_z(M_0)}$​.</li>
</ul>
11. 若空间曲线$\Gamma$是曲线$S_1:F(x,y,z)=0$和$S_2:G(x,y,z)=0$的<strong>交线</strong>，它在其上一点$M_0$处的<strong>切线同时落在$S_1$和$S_2$在点$M_0$处的切平面上</strong>，所以曲线$\Gamma$在点$M_0$处的<strong>切线</strong>就是$S_1$和$S_2$在点$M_0$处的<strong>切平面的交线</strong>。若$S_1$和$S_2$在点$M_0$处的<strong>法向量</strong>分别为$n_1$和$n_2$，那么$n_1\times n_2$就是$\Gamma$在$M_0$处的<strong>切向量</strong>。

12. <strong>平面曲线的切线</strong>：设<strong>平面曲线</strong>$C$的一般式方程为$F(x,y)=0$，其中偏导数$F_x,F_y$连续，且$F_x^2+F_y^2\neq 0$. 设点$M_0(x_0,y_0)$在$C$上，且$F_y(x_0,y_0)\neq 0$，则根据<strong>一元隐函数存在定理</strong>，方程$F(x,y)=0$在$M_0$的某邻域可确定唯一的满足$y(x_0)=y_0$的隐函数$y=y(x)$，且有$y'(x_0)=-\frac{F_x(x_0,y_0)}{F_y(x_0,y_0)}$,由此可得曲线$C$在$M_0$处的<strong>切线方程</strong>为$F_x(x_0,y_0)(x-x_0)+F_y(x_0,y_0)(y-y_0)=0$，曲线$C$在$M_0$处的<strong>法向量</strong>为$\textbf{n}=\grad F(M_0)=(F_x(x_0,y_0),F_y(x_0,y_0))$​.

13. <strong>微分中值定理</strong>：设函数$f(x,y)$在凸区域$D$内可微，则对$D$中任意两点$P(a,b),Q(a+h,b+k)$，存在$\theta \in (0,1)$使得$f(a+h,b+k)-f(a,b)=f_x(a+\theta h, b + \theta k)h + f_y(a+\theta h, b + \theta k)k$.
<ul>
 	<li><strong>记忆</strong>：与一元函数的微分中值定理$f(x+\Delta x) - f(x)=f'(x+\theta \Delta x) \Delta x$​类比记忆.</li>
</ul>
14. <strong>Taylor公式</strong>：设函数$f(x,y)$在点$(x_0,y_0)$的邻域内<strong>有n+1阶连续偏导数</strong>，则对该邻域内任一点$(x_0+h,y_0+k)$，存在$\theta \in (0,1)$,使得$f(x_0+h,y_0+k)=\sum_{m=0}^{n} \frac{1}{m!}(\frac{\partial}{\partial x}h+\frac{\partial}{\partial y}k)^{m}f(x_0,y_0)+R_n$，其中$R_n=\frac{1}{(n+1)!}(\frac{\partial}{\partial x}h+\frac{\partial}{\partial y}k)^{n+1}f(x_0+\theta h,y_0+\theta k)$.
<ul>
 	<li><strong>记忆</strong>：与一元函数的Taylor公式$f(x_0+\Delta x)=\sum_{m=0}^{n} \frac{1}{m!}(\frac{d}{dx})^{m}f(x_0)+R_n$,其中$R_n=ac{1}{(n+1)!}(\frac{d}{dx})^{n+1}f(x_0+\theta \Delta x)$类比记忆.</li>
</ul>
或者我们也可以将Lagrange余项$R_n$换成<strong>Peano余项</strong>$o(\rho ^n)$，其中$\rho = \sqrt{h^2+k^2}$.

15. （<strong>极值点的必要条件</strong>）若函数$f(x,y)$在点$P_0(x_0,y_0)$处可偏导，且在$P_0$点取极值，则有$f_x(x_0,y_0)=0,f_y(x_0,y_0)=0$. 函数的一阶偏导数都为零的点称为<strong>驻点</strong>。
<ul>
 	<li><strong>极值点不一定是驻点</strong>：有可能函数在极值点$P_0$处不可偏导，例如$f(x,y)=\sqrt{x^2+y^2}$有极小值点$(0,0)$，但由于$f(x,y)$在$(0,0)$的偏导数不存在，故$(0,0)$不是$f(x,y)$​的驻点。</li>
 	<li><strong>驻点不一定是极值点</strong>：例如$f(x,y)=xy$有驻点$(0,0)$，但根据极值点的定义易知$(0,0)$不是$f(x,y)$的极值点。</li>
</ul>
16. （<strong>极值点的充分条件</strong>）设函数$f(x,y)$在点$P_0(x_0,y_0)$某邻域内有二阶连续的偏导数，且$f_x(x_0,y_0)=0,f_y(x_0,y_0)=0$,记<strong>Hesse矩阵</strong>$H=\begin{bmatrix}f_{xx}&amp;f_{xy}\\f_{yx}&amp;f_{yy}\end{bmatrix}_{P_{0}}$​
<ul>
 	<li>若$H$为正定矩阵，则$f(x_0,y_0)$为严格极小值；若$H$为负定矩阵，则$f(x_0,y_0)$为严格极大值。</li>
 	<li>若$H$为不定矩阵，则$f(x_0,y_0)$非极值。</li>
</ul>
17. <strong>条件极值</strong>：若想要求目标函数$u=f(x,y,z)$在约束条件$\varphi (x,y,z)=0$下的极值：
<ul>
 	<li><strong>直接法</strong>：从约束条件$\varphi (x,y,z)=0$中接触一个变量，比如$z=z(x,y)$，然后代入目标函数中得$u=f(x,y,z(x,y))$，再求此二元函数的无条件极值；</li>
 	<li><strong>Lagrange乘数法</strong>：引入辅助函数$L(x,y,z,\lambda)=f(x,y,z)+\lambda \varphi (x,y,z)$，从其无条件极值的必要条件$\left\{\begin{matrix}L_x=f_x+\lambda \varphi_x=0\\L_y=f_y+\lambda \varphi_y=0\\L_z=f_z+\lambda \varphi_z=0\\L_\lambda=\varphi(x,y,z)=0\end{matrix}\right.$求出的驻点$(x_0,y_0,z_0)$是可能的条件极值点。</li>
</ul>
18.<strong>最值问题的原则</strong>：有界闭区域上的可微函数的最值在<strong>内部驻点</strong>或<strong>边界点</strong>取到。实际问题中，若最值必在<strong>区域内部</strong>取得又<strong>驻点唯一</strong>，则此驻点就是最值点。

&nbsp;