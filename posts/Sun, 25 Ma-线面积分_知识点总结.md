---
title: 线面积分 知识点总结
date: Sun, 25 Ma
summary:      第一类线面积分    第一类曲线积分    方向性：第一类曲线积分与曲线方向无关。若曲线C为AB，则$\int_{AB}f(x,y)ds=\int_{BA}f(x,y)...
---

<!-- wp:paragraph -->
<p>[latexpage]</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">第一类线面积分</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">第一类曲线积分</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>方向性</strong>：第一类曲线积分与曲线方向无关。若曲线C为AB，则$\int_{AB}f(x,y)ds=\int_{BA}f(x,y)ds$.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">如何计算？</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设函数f(x,y)在光滑曲线C上连续，C的参数方程为$\left{\begin{matrix}x=x(t),\\y=y(t),\end{matrix}\right.\quad t\in[\alpha,\beta]$，则<br>$$<br>\int_Cf(x,y)ds=\int_\alpha^\beta f(x(t),y(t))\sqrt{x'^2(t)+y'^2(t)}dt<br>$$<br><strong>注意⚠️</strong>：由于ds是弧长，取正值，故定积分限应$\alpha\le\beta$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当曲线C形式为$y=y(x),x\in[a,b]$时，<br>$$<br>\int_Cf(x,y)ds=\int_a^bf(x,y(x))\sqrt{1+y'^2(x)}dx<br>$$<br>在极坐标系$r=r(\theta)$中，$ds=\sqrt{r^2+r'^2}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>同理，对于空间曲线$L:x=x(t),y=y(t),z=z(t),\quad t\in[\alpha,\beta]$,<br>$$<br>\int_Lf(x,y,z)=\int_\alpha^\beta f(x(t),y(t),z(t))\sqrt{x'^2(t)+y'^2(t)+z'^2(t)}dt.<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">第一类曲面积分</h3>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">曲面面积</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设曲面$S:z=f(x,y),\quad (x,y)\in D$，则<br>$$<br>dS=\sqrt{1+z_x^2+z_y^2}dxdy, \quad S=\iint_D\sqrt{1+z_x^2+z_y^2}dxdy<br>$$<br>若S为双参数方程$\left{\begin{matrix}x=x(u,v),\y=y(u,v),\z=z(u,v),\end{matrix}\right.\quad(u,v)\in D$，则<br>$$<br>\mathbf{n}=(x_u,y_u,z_u)\times(x_v,y_v,z_v)=(\begin{vmatrix}y_u&amp;z_u\\y_v&amp;z_v\end{vmatrix},\begin{vmatrix}z_u&amp;x_u\\z_v&amp;x_v\end{vmatrix},\begin{vmatrix}x_u&amp;y_u\\x_v&amp;y_v\end{vmatrix})\overset{\text{def}}{=}(A,B,C)<br>$$<br>于是：<br>$$<br>dS=\frac{\sqrt{A^2+B^2+C^2}}{|C|}dxdy<br>$$<br>由于$dxdy=|C|dudv$，得到<br>$$<br>dS=\sqrt{A^2+B^2+C^2}dudv,\quad S=\iint_D\sqrt{A^2+B^2+C^2}dudv<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">曲面积分的计算</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>若曲面S为显式方程$z=z(x,y), \quad(x,y)\in D$，则有<br>$$<br>\iint_Sf(x,y,z)dS=\iint_Df(x,y,z(x,y))\sqrt{1+z_x^2+z_y^2}dxdy<br>$$<br>若曲面S为双参数方程$\left{\begin{matrix}x=x(u,v),\y=y(u,v),\z=z(u,v),\end{matrix}\right.\quad(u,v)\in D$，则<br>$$<br>\iint_Sf(x,y,z)dS=\iint_Df[x(u,v),y(u,v),z(u,v)]\sqrt{A^2+B^2+C^2}dudv<br>$$<br>其中<br>$$<br>A=\frac{\partial(y,z)}{\partial(u,v)},\quad B=\frac{\partial(z,x)}{\partial(u,v)}, \quad C=\frac{\partial(x,y)}{\partial(u,v)}<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">第二类曲线和曲面积分</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">第二类曲线积分</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设曲线L的端点为A,B，规定其一为起点，这样的曲线为<strong>定向曲线</strong>，起点为A，终点为B的定向曲线记为$L_{AB}$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对简单闭曲线$L\subset xOy$面，通常规定逆时针方向为其正向，记为$L^+$，顺时针方向为负向，记为$L^-$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>设D为平面区域，若D内对任意一条闭曲线所围区域都落在D内，则称D为<strong>单连通</strong>的，否则称其为<strong>复联通</strong>的。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>人话：单连通区域中间没有孔，复连通区域中间有孔。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>当点沿区域D边界朝一个方向前进时，D总在其左手侧，规定此方向为区域D诱导的<strong>边界正向</strong>，记为$\partial D^+$。与$\partial D^+$相反的方向称为D的<strong>边界负向</strong>，记为$\partial D^-$。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>人话：对于最外侧的边界，总体上逆时针为正向；针对复连通区域里面的孔，总体上顺时针是正向。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">如何计算？</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>设L为定向曲线，向量场$\mathbf{F}=(P,Q)$在L上的第二类曲线积分<br>$$<br>\int_L\mathbf{F}\cdot d\mathbf{r}=\int_L\mathbf{F}\cdot\mathbf{e}_\tau ds=\int_L(P\cos\alpha+Q\cos\beta)ds=\int_LPdx+Qdy<br>$$ </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>方向性</strong>：第二类曲线积分与曲线的方向有关，且 $$ \int_{L_{BA}}Pdx+Qdy=-\int_{L_{AB}}Pdx+Qdy<br>$$<br>若定向曲线L为$\left{\begin{matrix}x=x(t),\y=y(t),\end{matrix}\right.\quad t:\alpha\to\beta$，则<br>$$<br>\int_LPdx+Qdy=\int_\alpha^\beta[P(x(t),y(t))x'(t)+Q(x(t),y(t))y'(t)]dt<br>$$<br>特例：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>若曲线L的方程为$y=y(x),x:a\to b$，则<br>$$<br>\int_LPdx+Qdy=\int_a^b[P(x,y(x))+Q(x,y(x))y'(x)]dx<br>$$<br>若L为平行x轴的定向线段，则$\int_L Qdy=0$。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">第二类曲面积分</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>双侧曲面</strong>：设S为光滑曲面，指定其上点P处点法向量$\mathbf{n}$。当点P沿S上任意连续闭曲线不越过S的边界回到起始位置时，法向量$\mathbf{n}$始终保持原来指向。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>定侧曲面</strong>：双侧曲面的S的侧向由其<strong>法向量组</strong>确定。选定S的一侧为正侧，记为$S^+$，则另一侧为负侧，记为$S^-$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>约定：若曲面S的方程为：$z=z(x,y),\quad (x,y)\in D$，则其<strong>单位法向量</strong><br>$$<br>\mathbf{n}^\circ=\pm\frac{(-z_x,-z_y,1)}{\sqrt{1+z_x^2+z_y^2}}<br>$$<br>选“+”号时，则$\mathbf{n}^\circ=(\cos\alpha,\cos\beta,\cos\gamma)$，其中$cos\gamma=\frac{1}{\sqrt{1+z_x^2+z_y^2}}&gt;0$，故$\mathbf{n}^\circ$与z轴正向夹角$\gamma&lt;90^\circ$，指向<strong>上侧</strong>，规定为S的<strong>正侧</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>注：封闭曲面规定其<strong>外侧</strong>为<strong>正侧</strong>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>设S为定侧曲面，向量场$\mathbf{v}=(P,Q,R)$在S上的第二类曲面积分<br>$$<br>\iint_S\mathbf{v}\cdot d\mathbf{S}\overset{\text{def}}{=}\iint_S(\mathbf{v\cdot n^\circ})dS=\iint_SPdydz+Qdzdx+Rdxdy<br>$$<br><strong>侧向性</strong>：第二类曲面积分与曲面的侧向有关，且<br>$$<br>\iint_{S^-}Pdydz+Qdzdx+Rdxdy=-\iint_{S^+}Pdydz+Qdzdx+Rdxdy<br>$$<br>若定侧光滑曲面S为$x=x(u,v),y=y(u,v),z=z(u,v),\quad (u,v)\in D$，则<br>$$<br>\iint_SPdydz+Qdzdx+Rdxdy=\pm\iint_D(PA+QB+RC)dudv<br>$$<br>其中$\pm$号选择由S指定侧的法向量确定。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>特例：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>若曲面S的方程为$z=z(x,y),\quad(x,y)\in D$​，则<br>$$<br>\iint_SPdydz+Qdzdx+Rdxdy=\pm\iint_D(-Pz_x-Qz_y+R)dxdy<br>$$<br>当P=Q=0，曲面S为$z=z(x,y),\quad (x,y)\in D$时，<br>$$<br>\iint_SR(x,y,z)dxdy=\pm\iint_DR(x,y,z(x,y))dxdy<br>$$<br>当曲面S指定上侧时，选+号，指定下侧时，选-号。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当曲面S为母线平行于z轴的柱面时，<br>$$<br>\iint_SR(x,y,z)dxdy=0<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Green公式</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：设$\mathbf{v}=(P,Q)$为平面有界闭域D上的<strong>光滑向量场</strong>，D的边界<strong>分段光滑</strong>，则有<br>$$<br>\oint_{\partial D^+}Pdx+Qdy=\iint_D(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dxdy<br>$$<br>推论：设平面有界闭域D的边界分段光滑，则其面积<br>$$<br>S=\frac{1}{2}\oint_{\partial D^+}xdy-ydx<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>定理(Green)</strong>：设$\mathbf{v}=(P(x,y),Q(x,y))$是单连通区域D内的光滑向量场，则下面四条等价：</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>在D的任一条分段光滑<strong>闭曲线</strong>L上，$\oint_L Pdx+Qdy=0$。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>在D内曲线积分$\int_LPdx+Qdx$<strong>与路径无关</strong>。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>$Pdx+Qdy$是某函数$\varphi(x,y)$的<strong>全微分</strong>，即$\exist\varphi$似的$d\varphi=Pdx+Qdy$，此时称$\varphi$为$Pdx+Qdy$​的<strong>原函数</strong>。 $\varphi(x,y)=\int_{(x_0,y_0)}^{(x,y)}Pdx+Qdy$</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>在D内恒成立$\frac{\partial Q}{\partial x}\equiv\frac{\partial P}{\partial y}$。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Gauss公式</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：设$\mathbf{v}(P,Q,R)$为空间有界闭域$\Omega$上的<strong>光滑向量场</strong>，$\partial\Omega$是分片光滑闭曲面，则有<br>$$<br>\backslash oiint_{\partial\Omega^+}Pdydz+Qdzdx+dxdy=\iiint_\Omega(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z})<br>$$<br>推论：设空间有界闭域$\Omega$的边界分片光滑，则其体积$V(\Omega)=\frac{1}{3}\backslash oiint_{\partial\Omega^+}xdydz+ydzdx+zdxdy$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>注：不知道为什么这里渲染不出来环路二重积分（见下图）符号，因此我用\oiint指代环路二重积分。</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":292,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="http://inwt233.cn/wp-content/uploads/2025/05/image.png" alt="" class="wp-image-292"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">散度</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：向量场$\mathbf{v}=(P,Q,R)$的<strong>散度</strong>定义为<br>$$<br>\mathrm{div}\,\mathbf{v}\overset{\text{def}}{=}\grad\cdot\mathbf{v}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}<br>$$<br>故有：<br>$$<br>\backslash oiint_{\partial\Omega^+}\mathbf{v}\cdot \mathrm{d}\mathbf S = \iiint_\Omega\grad\cdot\mathbf{v}\,\mathrm{d}V=\iiint_\Omega\mathrm{div}\,\mathbf{v}\,\mathrm{d}V<br>$$</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Stokes公式</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定理：设$\mathbf{v}=(P,Q,R)$为空间光滑曲面S上的<strong>光滑向量场</strong>，$\partial S$是<strong>分段光滑闭曲线</strong>，则有<br>$$<br>\oint_{\partial S}Pdx+Qdy+Rdz=\iint_S(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z})dydz+(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x})dzdx+(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dxdy<br>$$<br>其中$\partial S$的方向与S的侧向按右手法则联系。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>借助行列式，Stokes公式可以记为</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$$<br>\oint_{\partial S}Pdx+Qdy+Rdz=\iint_S \begin{vmatrix}dydz&amp;dzdx&amp;dxdy\\ \frac{\partial}{\partial x}&amp;\frac{\partial}{\partial y}&amp;\frac{\partial}{\partial z}\\P&amp;Q&amp;R\end{vmatrix}=\iint_S \begin{vmatrix}\cos\alpha&amp;\cos\beta&amp;\cos\gamma\\ \frac{\partial}{\partial x}&amp;\frac{\partial}{\partial y}&amp;\frac{\partial}{\partial z}\\P&amp;Q&amp;R\end{vmatrix}dS<br>$$<br>其中$\partial S$定向与$(\cos\alpha,\cos\beta,\cos\gamma)$按右手法则联系，这里的$(\cos\alpha,\cos\beta,\cos\gamma)$为定侧曲面的单位法向量。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">旋度</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>定义：向量场$\mathbf{v}=(P,Q,R)$的<strong>旋度</strong>定义为：<br>$$<br>\mathrm{rot}\,\mathbf{v}\overset{\text{def}}{=}\grad\times\mathbf{v}=\begin{vmatrix}i&amp;j&amp;k\\ \frac{\partial}{\partial x}&amp;\frac{\partial}{\partial y}&amp;\frac{\partial}{\partial z}\\P&amp;Q&amp;R\end{vmatrix}=(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})<br>$$<br>记$\mathbf{r}=(x,y,z)$，则$\mathrm{d}\mathbf{r}=(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$​则Stokes公式可以写成<br>$$<br>\oint_{\partial S}\mathbf{v}\cdot\mathrm{d}\mathbf{r}=\iint_S\mathrm{rot}\,\mathbf{v}\cdot\mathrm{d}\mathbf{S}=\iint_S\mathrm{rot}\,\mathbf{v\cdot n^\circ}\mathrm{d}S<br>$$<br>其中$\partial S$的定向与S的定侧$(\mathbf{n}^\circ)$满足右手法则。</p>
<!-- /wp:paragraph -->