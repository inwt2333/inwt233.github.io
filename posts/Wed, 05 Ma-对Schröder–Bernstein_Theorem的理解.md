---
title: 对Schröder–Bernstein Theorem的理解
date: Wed, 05 Ma
summary:   定义 Def:    If there exist injective functions f : A → B and g : B → A between the se...
---

<!-- wp:heading -->
<h2 class="wp-block-heading">定义 Def:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If there exist injective functions <em>f</em> : <em>A</em> → <em>B</em> and <em>g</em> : <em>B</em> → <em>A</em> between the sets <em>A</em> and <em>B</em>, then there exists a bijection function <em>h</em> : <em>A</em> → <em>B</em>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如果在集合A和集合B之间存在单射：<em>f: A </em>→ <em>B</em> 和 <em>g</em> : <em>B</em> → <em>A</em>，那么存在一个双射 <em>h</em> : <em>A</em> → <em>B</em>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In terms of the&nbsp;cardinality&nbsp;of the two sets, this classically implies that if&nbsp;|<em>A</em>| ≤ |<em>B</em>|&nbsp;and&nbsp;|<em>B</em>| ≤ |<em>A</em>|, then&nbsp;|<em>A</em>| = |<em>B</em>|; that is,&nbsp;<em>A</em>&nbsp;and&nbsp;<em>B</em> are&nbsp;equipotent.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>从势的角度来看, 这意味着如果 |<em>A</em>| ≤ |<em>B</em>| 并且 |<em>B</em>| ≤ |<em>A</em>|，则 |<em>A</em>| = |<em>B</em>|，即<em>A</em>与<em>B</em>等势。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">证明 Proof：</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let $C_{0}=\{a\in A|\forall b\in B,G(b)\neq a\}$, $D_{0}=\{f(a)|a\in C_{0}\}$, $C_{1}=\{a\in A/C_{0}|\forall b\in B/D_{0},G(b)\neq a\}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(1) If $ a\in C_{1}$, then $a\notin C_{0}$. Thus, there exists $b\in B$, s.t. $G(b)=a$. By <em>def</em> of $C_{1}$, $b \in D_{0}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>(2) If $b\in D_{0}$, $G(b) \notin C_{0}$, Because G is an injection, there is no $b` \neq b$, s.t. $G(b`) = G(b)$. So $G(b) \in C_{1}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By (1) and (2), $C_{1} = \{ G(b)|b\in D_{0}\}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let $D_{1} = \{F(a)|a\in C_{1}\}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>......</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$C_{n+1} = { a\in A \setminus \bigcup_{i=0}^{n} C_{i}|\forall b\in B \setminus \bigcup_{i=0}^{n}D_{i},G(b)\neq a}$, $D_{n+1} = \{F(a)|a\in C_{n+1}\}$.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let <img class="wp-image-84" style="width: 200px;" src="http://47.101.155.71/wp-content/uploads/2025/03/QianJianTec1741181488458-scaled.jpg" alt="H(a)"> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So H(a) is a bijection between A and B. $Q.E.D.$</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">怎样理解？ How to understand?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>听完这个证明之后，我仍然一头雾水。<a href="https://youtu.be/IkoKttTDuxE?si=7_o-JPw3Jns4o8Wa">油管博主blargoner</a>将该定理与希尔伯特酒店相类比的思考过程启发了我，下面就来谈谈我的理解。</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":88,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="http://47.101.155.71/wp-content/uploads/2025/03/IMG_FD24C6D07B2A-1-1024x389.jpeg" alt="" class="wp-image-88"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>将此图与上述证明过程结合起来看：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$C_{0}$：$G(B)$映射不到的地方；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$D_{0}$：$F(C_{0})$映射到的地方；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$C_{1}$：除了$C_{0}$以外$G(B\setminus D_{0})$映射不到的地方；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$D_{1}$：$F(C_{1})$映射到的地方；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>下面来证明$C_{1}=G(D_{0})$：除了C<sub>0</sub>以外的地方本来都是可以由G(B)映射到的，但是把D<sub>0</sub>刨出去之后C<sub>1</sub>这个地方就神奇地没法被映射到了，证明C<sub>1</sub>应该本来是由被刨出去的D<sub>0</sub>映射到的，即$C_{1}=G(D_{0})$。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>接下来令<img class="wp-image-84" style="width: 200px;" src="http://47.101.155.71/wp-content/uploads/2025/03/QianJianTec1741181488458-scaled.jpg" alt="">。下面需要证明这坨函数是个双射。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>首先证明他是个单射。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$\bigcup_{n=0}^{+\infty} C_{n}$在图中是所有蓝色的部分，而$\bigcup_{n=0}^{+\infty} D_{n}$在图中是所有红色的部分。A中蓝色区域能够通过F这个函数映射到B中的红色区域，而B中的红色区域能够通过G这个函数映射到A中的下一个蓝色区域。即所有红色区域都是蓝色区域映射过来的，所有蓝色区域，除了$C_{0}$以外，都是由红色区域映射过来的，而$C_{0}$是B上所有元素都映射不到的盲区。H(a)这个函数想表达的就是，如果你在蓝色区域内，就通过F函数映射到B中的红色区域，而如果你不在蓝色区域内，你就要通过G<sup>-1</sup>映射回B中。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>要想证明单射，那么就证明A中不存在两个相同的元素x和y，使得x和y映射到B中的同一个点。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如果x和y都在蓝色的区域内，那么x和y都要通过F这个函数映射到B上去。因为F是单射，所以F(x)一定不等于F(y)。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如果x和y都在蓝色的区域以外，那么x和y都要通过G的逆函数映射到B上去。因为G是单射，那么G<sup>-1</sup>也是单射，G<sup>-1</sup>(x)也一定不等于G<sup>-1</sup>(y)。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如果x在蓝色的区域里，y在蓝色的区域外，那么我们知道H(x)一定在红色区域内，而假如H(x)=H(y)，根据定义可以知道，因为y不在蓝色的区域内，所以他需要调用G<sup>-1</sup>这个函数映射到B，也就是G<sup>-1</sup>(y)=H(x), y = G(H(x)). 但是因为H(x)在红色的区域内，G(H(x))一定在蓝色的区域内，也就是y应该也在蓝色的区域内，因此推出矛盾，这种情况不成立。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>因此，H(x)应该是一个单射。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>下面证明H(x)是满射，即任意在B当中找一个y，我们都能在A中找到一个x，从而H(x)=y。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当y在红色的区域内，则说明存在一个n，使得$y\in D_{n}$. 由$D_{n}$的定义，$D_{n}$中的所有元素都是$C_{n}$里的所有元素通过F映射过来的，所以我们可以找到一个$x=F^{-1}(y)$（那x一定就在蓝色区域内了）, 使得y=F(x), 即y=H(x)，</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当y在红色的区域外，因为y不在红色区域内，那么我们可以找到一个x=G(y)，x可以被刨出所有红色区域的B映射到，根据定义，x就不在蓝色区域内，这时候H(x)调用的是第二行，$y=G^{-1}(x)$，即y=H(x)。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>综上，H(x)也是个满射。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>H(x)既单又满，所以H(x)是个双射。</p>
<!-- /wp:paragraph -->