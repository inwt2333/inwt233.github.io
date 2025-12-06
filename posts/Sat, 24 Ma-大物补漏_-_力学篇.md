---
title: 大物补漏 - 力学篇
date: Sat, 24 Ma
summary:    质点运动学    切向与法向加速度    切向加速度：与速度方向平行（沿切线），改变速度的大小。$\overrightarrow{a_t}=\frac{dv}{dt}\...
---

<!-- wp:heading -->
<h2 class="wp-block-heading">质点运动学</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">切向与法向加速度</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>切向加速度</strong>：与速度方向平行（沿切线），改变速度的大小。$\overrightarrow{a_t}=\frac{dv}{dt}\hat{e_t}$<br><strong>法向加速度</strong>：与速度方向垂直，指向（曲率）圆心，改变速度的方向。$\overrightarrow{a_n}=\frac{v^2}{\rho}\hat{e_n}$​</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">极坐标系</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>在极坐标系中，<br>$$<br>d\overrightarrow{e_r} =d\theta\overrightarrow{e_\theta},d\overrightarrow{e_\theta}=d\theta(-\overrightarrow{e_r})<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">抛体运动</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设初速度与地面夹角为$\theta_0$，则抛体运动的轨道方程为<br>$$<br>y=x\tan\theta_0-\frac{gx^2}{2v_0^2\cos^2\theta_0}<br>$$<br>射程为<br>$$<br>R=\frac{v_0^2}{g}\sin2\theta_0,R_{max}=\frac{v_0^2}{g}\iff\theta_0=\frac{\pi}{4}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">科里奥利力</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>在圆盘参考系中观察，质点从圆盘中心沿径向做匀速直线运动，速度为$\overrightarrow{u}$.<br>在地面参考系上看（极坐标），<br>$$<br>\overrightarrow{a}=-r\omega^2\hat{r} + 2u\omega\hat{\theta}<br>$$<br>在圆盘参考系上，惯性离心力/科里奥利力为<br>$$<br>\overrightarrow{F_{in}} = m\omega^2\overrightarrow{r} + 2m\overrightarrow{u}\times\overrightarrow{\omega}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">狭义相对论</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">从S系到S'系：</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>x'=\frac{x-ut}{\sqrt{1-\frac{u^2}{c^2}}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>t'=\frac{t-\frac{u}{c^2}x}{\sqrt{1-\frac{u^2}{c^2}}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">从S'系到S系：</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>x=\frac{x'+ut'}{\sqrt{1-\frac{u^2}{c^2}}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>t=\frac{t'+\frac{u}{c^2}x'}{\sqrt{1-\frac{u^2}{c^2}}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">速度的洛伦兹变换</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>令<br>$$<br>\gamma = \frac{1}{\sqrt{1-\frac{u^2}{c^2}}}<br>$$<br>在S'系中的速度定义为$dx'/dt'$,化简之后可以得到<br>$$<br>v'_x=\frac{dx'}{dt'}=\frac{\gamma(dx-udt)}{\gamma(dt-udx/c^2)}=\frac{v_x-u}{1-uv_x/c^2}<br>$$<br>在y和z方向上由于$y'=y,z'=z$，因此速度相比于$v'_x$来说分母不变，分子变成$v_y$和$v_z$​。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">钟慢尺短</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>\Delta x' =\frac{\Delta x}{\gamma}, \Delta t'=\frac{\Delta t}{\gamma}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由于$\gamma &gt; 1$，因此变换到另外一个参考系之后，$\Delta x' &lt; \Delta x, \Delta t'&lt;\Delta t$，所以会造成钟慢尺短。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">质量与速度的关系</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>m(v)=\frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}=\gamma m_0<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">功与能量</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>有心力一定是保守力。<br>内力做功与参考系无关。如果改变参考系导致机械能守恒不成立，那么是谁由于外力对体系所做的功不同。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">势能与力的关系</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>F=-\frac{dV(x)}{dx},\overrightarrow{F}=-\grad V<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">能量与质量的关系</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>dK=v^2dm+mvdv<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>mc^2 = E = K + m_0c^2<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">能量与动量的关系：</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>E^2=p^2c^2+m_0^2c^2<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>用$p=mv,m=\gamma m_0$​代入就能推出来。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">动量和角动量</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">动量定理的推广形式：</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>{\mathord{ \buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over F} } = \frac{dm}{dt} {\mathord{ \buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over v} } + m\frac{d {\mathord{ \buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over v} } }{dt}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$m$是指某一时刻t，该系统的瞬时质量；<br>$\overrightarrow{v}$是指在t时刻，系统质心的速度，$\frac{d\overrightarrow{v}}{dt}$指质心的加速度；<br>$\overrightarrow{F}$是指系统所受的合外力；<br>$\frac{dm}{dt}$​是指系统质量随时间的变化率；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">质心</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>在动量守恒的过程中，质心的位置矢量是不变的。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于两个质量的孤立系统，质心的位置矢量：<br>$$<br>\overrightarrow{r_c}=\frac{m_1\overrightarrow{r_1}+m_2\overrightarrow{r_2}}{m_1+m_2}<br>$$<br>如果拓展为n个质点的孤立系统，则质心的位置矢量：<br>$$<br>\overrightarrow{r_c}=\frac{\sum_{i=1}^{n}m_i\overrightarrow{r_i}}{\sum_{i=1}^nm_i}<br>$$<br>对于一个质量连续分布的物体，质心的位置矢量为：<br>$$<br>\overrightarrow{r_c}=\frac{\int\overrightarrow{r}dm}{\int dm}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">角动量</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>\overrightarrow{L}=\overrightarrow{r}\times m\overrightarrow{v}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">力矩</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>\overrightarrow{M} = \overrightarrow{r}\times\overrightarrow{F}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">角动量定理</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>d\overrightarrow{L}=\overrightarrow{M}dt, \overrightarrow{L_2}-\overrightarrow{L_1}=\int_{t_1}^{t_2}\overrightarrow{M}dt,\overrightarrow{M}=\frac{d\overrightarrow{L}}{dt}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">刚体运动学</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">转动惯量</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>若刚体是由n个质量为$m_1,m_2,… m_i, … m_n$的质点组成：<br>$$<br>J=\sum_{i=1}^{n}r_i^2m_i<br>$$<br>若刚体的质量连续分布：<br>$$<br>J=\int r^2dm<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>对于一维物体，$dm=\lambda dx = \frac{m}{l}dx$, 其中$\lambda=\frac{m}{l}$​为线密度</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>对于二维物体，$dm=\sigma dS = \frac{m}{\pi R^2}2\pi rdr$,其中$\sigma = \frac{m}{\pi R^2}$​为面密度</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">刚体定轴转动的角动量</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>刚体对转轴z对角动量为：<br>$$<br>L_z=J\omega<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">平行轴定理:</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>J_A = J_C + md^2<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$J_A$为刚体对某轴A的转动惯量；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$J_C$是刚体对通过质心C且与轴A平行的轴C的转动惯量；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>d为两平行轴之间的垂直距离。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">刚体定轴转动定理</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>\overrightarrow{M}=J\overrightarrow{\alpha}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由(22),(25)两式联立可以得到。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">刚体定轴转动的转动动能</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>K=\frac{1}{2}J\omega^2<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定轴转动刚体，若M=0，则$L=J\omega=不变量$。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">陀螺的进动</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>\Omega = \frac{M}{L\sin\theta}=\frac{M}{J\omega\sin\theta}= \frac{mgr_c}{J\omega}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>$\Omega$是陀螺绕中心转轴的角速度；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\overrightarrow{M}=\overrightarrow{r_c}\times m\overrightarrow{g}, M=mgr_c\sin\theta$​为重力相对于中心转轴的力矩；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$r_c$是陀螺质心距陀螺与地面接触点O的距离；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\omega$​是陀螺高速自转的角速度；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$\theta$是陀螺自转轴和中心轴的夹角。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">振动力学基础</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>振动方程满足通式：<br>$$<br>\frac{d^2x}{dt^2}+\omega^2x=0<br>$$<br>如果是摆动方程的话，$x$可以替换为$\theta$。比如复摆中，$\frac{d^2\theta}{dt^2}+\frac{mgh}{J}\theta=0,\omega^2=\frac{mgh}{J}$，其中h为转轴到质心的距离</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>若振动方程为$y=A\cos(\omega t+\varphi)$，若已知当t=0时，$x=x_0,v=v_0$，则$A=\sqrt{x_0^2+\frac{v_0^2}{\omega^2}}.\tan\varphi=-\frac{v_0}{\omega x_0}$.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">阻尼振动</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>-kx-b\frac{dx}{dt}=m\frac{d^2x}{dt^2}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中b为阻力系数.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>令$\omega_0^2=\frac{k}{m},2\alpha=\frac{b}{m}（\alpha为阻尼因子）$，得$\frac{d^2x}{dt^2}+2\alpha\frac{dx}{dt}+\omega_0^2x=0$​，解得<br>$$<br>x=Ae^{-\alpha t}\cos(\sqrt{w_0^2-\alpha^2}t+\varphi)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">受迫振动</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>令驱动力为$F=F_0cos\omega t$，则有<br>$$<br>-kx-b\frac{dx}{dt}+F=m\frac{d^2x}{dt^2}<br>$$<br>令$\omega_0^2=\frac{k}{m},2\alpha=\frac{b}{m}（\alpha为阻尼因子）,f_0=\frac{F_0}{m}$，得$\frac{d^2x}{dt^2}+2\alpha\frac{dx}{dt}+\omega_0^2x=f_0\cos\omega t$​，解得<br>$$<br>x=A_0e^{-\alpha t}cos(\sqrt{w_0^2-\alpha^2}t+\varphi_0)+Acos(wt+\varphi)<br>$$<br>其中第一项为暂态项（齐次解），第二项为定态项（特解）。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>暂态项是由初始状态引起的自由振动，在$t&gt;\frac{5}{\alpha}$之后可忽略。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>定态项是驱动力持续作用的响应，在定态项中，<br>$$<br>A=\frac{f_0}{\sqrt{(\omega_0^2-\omega^2)^2+4\alpha^2\omega^2}}=\frac{F_0}{\sqrt{m^2(\omega^2-\omega_0^2)^2+b^2\omega^2}},\tan\varphi=-\frac{2\alpha\omega}{\omega_0^2-\omega^2}<br>$$<br>当$\omega=\sqrt{\omega_0^2-2\alpha^2}$时，$A_{max}=\frac{f_0}{2\alpha\sqrt{\omega_0^2-\alpha^2}}$，此时的$\omega$为共振频率。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">机械波</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">机械波的波速</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>v=\frac{\omega}{k}=\frac{\lambda}{T}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中$\omega=\frac{2\pi}{T}$为角频率，$k=\frac{2\pi}{\lambda}$​​为角波数。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">在弦或绳上的恒波波速</h5>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>v=\sqrt{\frac{T}{\mu}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中T为弦两端的张力，$\mu$为弦的线密度。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">在细棒中的纵波波速</h5>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>v=\sqrt{\frac{Y}{\rho}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中Y为杨氏模量，$\rho$为体密度。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">固体中的横波波速</h5>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>v=\sqrt{\frac{G}{\rho}}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>其中G为切变模量，$\rho$为体密度。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">平面简谐波的能量密度</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>$$<br>动能dK=\frac{1}{2}\mu dx(\frac{\partial y}{\partial t})^2=\frac{1}{2}\mu dx\omega^2A^2\sin^2(\omega t-kx)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>势能dU=T{[(dx)^2+(dy)^2]^{\frac{1}{2}}-dx}=\frac{1}{2}Tdx(\frac{\partial y}{\partial x})^2=\frac{1}{2}Tdxk^2A^2\sin^2(\omega t-kx)<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由于$v=\frac{\omega}{k}=\sqrt{\frac{T}{\mu}}$，得到$dK=dU$，于是<br>$$<br>dE=\mu dx\omega^2A^2\sin^2(\omega t-kx), \lang dE\rang=\frac{\int_0^{2\pi}dEdx}{2\pi}=\frac{1}{2}\mu dx\omega^2A^2<br>$$<br>若考察的为弹性杆中的纵波，则将$\mu$替换为$\rho S$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>设弦的横截面积为S,则$\mu=\rho S$，得<br>$$<br>能量密度w=\frac{dE}{Sdx}=\rho\omega^2A^2\sin^2(\omega t-kx),\lang w\rang=\frac{1}{T}\int_0^Twdt=\frac{1}{2}\rho\omega^2A^2<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">机械波的能流密度</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>能流密度为单位时间内通过垂直于波的传播方向上的单位面积的机械波的能量$\overrightarrow{S}=w\overrightarrow{v}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>机械波的强度（平均能流密度）为<br>$$<br>I=\lang S\rang = \frac{1}{T}\int_0^TSdt = \frac{v}{T}\int_0^Twdt=v\lang w\rang=\frac{1}{2}\rho \omega^2vA^2<br>$$<br>对无吸收介质，利用上式和能量守恒可以证明：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>球面波：$Ar=const. A\propto \frac{1}{r}$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>平面波：$A=const.$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>柱面波：$A\sqrt{r}=const.A\propto\frac{1}{\sqrt{r}}$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">波的反射</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>当波从<strong>波疏介质</strong>传递到与<strong>波密介质</strong>的交界处，反射时会发生相位突变$\pi$，称为半波损失，反之则没有半波损失。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">驻波</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>两列<strong>振幅相同</strong>的<strong>相干波</strong>在同一直线上<strong>沿相反方向</strong>传播时叠加。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>假设$y_1=A\cos(\omega t-kx), y_2=A\cos(\omega t+kx)$，则驻波方程为<br>$$<br>y=y_1+y_2=2A\cos kx\cos \omega t=2A\cos\frac{2\pi x}{\lambda}\cos \omega t<br>$$<br>驻波实际上是一种振动，不再是振动状态的传播，因此总平均能流密度为0.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">简正模</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>两段固定的张紧的长为L的弦，有$n\cdot\frac{\lambda}{2}=L$，则<br>$$<br>f_n=\frac{v}{\lambda}=\frac{n}{2L}\sqrt{\frac{F_T}{\mu}}<br>$$<br>上述各种允许频率所对应的驻波，称为弦的简正模，相应的频率$f_n$被称为弦的简正频率。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对弦来说，在两段固定的情况下，可以有多个不同的简正频率（指n可以取遍所有正整数），每个简正频率对应一个简正模。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于弦上发生的任何可能的一般运动，总可以看成是一系列简正模的线性叠加。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">多普勒效应</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>假设在介质参考系中机械波的波速为$\overrightarrow{u}$，由介质的性质确定，T为振动周期，f为振动频率。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>观测者以速度$v_r$相对于介质运动，波相对于观测者的波速变为$u\pm v_r\cos\theta_r$。其中$\theta_r$为$\overrightarrow{v_r}$和观测者与波源连线的夹角.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>波源以速度$v_s$相对于介质运动，波长变为$uT\mp v_s\cos\theta_sT$，其中$\theta_s$为$\overrightarrow{v_s}$和观测者与波源连线的夹角。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>因此得到频率：<br>$$<br>f_r=\frac{u\pm v_r\cos\theta_r}{uT \mp v_sT\cos\theta_s}=\frac{u\pm v_r\cos\theta_r}{u\mp v_s\cos\theta_s}f<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":5} -->
<h5 class="wp-block-heading">电磁波的多普勒效应</h5>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>由于电磁波的传播不需要介质，设v为在r所在的参考系中波源s的运动速度，$\theta$为$\overrightarrow{v}$与s和r连线的夹角，有<br>$$<br>f_r=\frac{\sqrt{1-\frac{v^2}{c^2}}}{1-\frac{v\cos\theta}{c}}f<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>纵向多普勒效应：$\theta=\frac{\pi}{2},f_r=\frac{\sqrt{1-\frac{v^2}{c^2}}}{1-\frac{v}{c}}f=\sqrt{\frac{c+v}{c-v}}f$；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>横向多普勒效应：$\theta=0,f_r=\sqrt{1-\frac{v^2}{c^2}}f$</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->