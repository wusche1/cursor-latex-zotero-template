## 6 Certain environmental symmetries produce power-seeking tendencies

Proposition 6.6 proves that for all γ ∈ [0 , 1] and for most distributions D , POWER D ( glyph[lscript] ↙ , γ ) ≤ POWER D ( r ↘ , γ ) . But first, we explore why this must be true.

F ( glyph[lscript] ↙ ) = { 1 1 -γ e glyph[lscript] ↙ , 1 1 -γ 2 ( e glyph[lscript] ↙ + γ e glyph[lscript] ↖ ) } and F ( r ↘ ) = { 1 1 -γ e r ↘ , 1 1 -γ 2 ( e r ↘ + γ e r ↗ ) , e r ↘ + γ 1 -γ e r ↗ } . These two sets look awfully similar. F ( glyph[lscript] ↙ ) is a 'subset' of F ( r ↘ ) , only with 'different states.' Figure 4 demonstrates a state permutation φ which embeds F ( glyph[lscript] ↙ ) into F ( r ↘ ) .

<!-- image -->

Figure 4: Intuitively, the agent can do more starting from r ↘ than from glyph[lscript] ↙ . By definition 6.1, F ( r ↘ ) contains a copy of F ( glyph[lscript] ↙ ) :

Definition 6.1 (Similarity of vector sets) . Consider state permutation φ ∈ S |S| inducing an |S| × |S| permutation matrix P φ in row representation: ( P φ ) ij = 1 if i = φ ( j ) and 0 otherwise. For X ⊆ R |S| , φ · X := { P φ x | x ∈ X } . X ′ ⊆ R |S| is similar to X when ∃ φ : φ · X ′ = X . φ is an involution if φ = φ -1 (it either transposes states, or fixes them in place). X contains a copy of X ′ when X ′ is similar to a subset of X via an involution φ .

<!-- formula-not-decoded -->

Definition 6.2 (Similarity of vector function sets) . Let I ⊆ R . If F, F ′ are sets of functions I ↦→ R |S| , F is (pointwise) similar to F ′ when ∃ φ : ∀ γ ∈ I : { P φ f ( γ ) | f ∈ F } = { f ′ ( γ ) | f ′ ∈ F ′ } .

Consider a reward function R ′ assigning 1 reward to glyph[lscript] ↙ and glyph[lscript] ↖ and 0 elsewhere. R ′ assigns more optimal value to glyph[lscript] ↙ than to r ↘ : V ∗ R ′ ( glyph[lscript] ↙ , γ ) = 1 1 -γ &gt; 0 = V ∗ R ′ ( r ↘ , γ ) . Considering φ from fig. 4, φ · R ′ assigns 1 reward to r ↘ and r ↗ and 0 elsewhere. Therefore, φ · R ′ assigns more optimal value to r ↘ than to glyph[lscript] ↙ : V ∗ φ · R ′ ( glyph[lscript] ↙ , γ ) = 0 &lt; 1 1 -γ = V ∗ φ · R ′ ( r ↘ , γ ) . Remarkably, this φ has the property that for any R which assigns glyph[lscript] ↙ greater optimal value than r ↘ ( i . e . V ∗ R ( glyph[lscript] ↙ , γ ) &gt; V ∗ R ( r ↘ , γ ) ), the opposite holds for the permuted φ · R : V ∗ φ · R ( glyph[lscript] ↙ , γ ) &lt; V ∗ φ · R ( r ↘ , γ ) .

We can permute reward functions, but we can also permute reward function distributions. Permuted distributions simply permute which states get which rewards.

Figure 5: A permutation of a reward function swaps which states get which rewards. We will show that in certain situations, for any reward function R , power-seeking is optimal for most of the permutations of R . The orbit of a reward function is the set of its permutations. We can also consider the orbit of a distribution over reward functions. This figure shows the probability density plots of the Gaussian distributions D and D ′ over R 2 . The symmetric group S 2 contains the identity permutation φ id and the reflection permutation φ swap (switching the y and x values). The orbit of D consists of φ id · D = D and φ swap · D = D ′ .

<!-- image -->

Definition 6.3 (Pushforward distribution of a permutation) . Let φ ∈ S |S| . φ · D any is the pushforward distribution induced by applying the random vector f ( r ) := P φ r to D any .

Definition 6.4 (Orbit of a probability distribution) . The orbit of D any under the symmetric group S |S| is S |S| · D any := { φ · D any | φ ∈ S |S| } .

For example, the orbit of a degenerate state indicator distribution D s is S |S| · D s = {D s ′ | s ′ ∈ S} , and fig. 5 shows the orbit of a 2D Gaussian distribution.

Consider again the involution φ of fig. 4. For every D bound for which glyph[lscript] ↙ has more POWER D bound than r ↘ , glyph[lscript] ↙ has less POWER φ ·D bound than r ↘ . This fact is not obvious-it is shown by the proof of lemma E.24.

Imagine D bound's orbit elements 'voting' whether glyph[lscript] ↙ or r ↘ has strictly more POWER. Proposition 6.6 will show that r ↘ can't lose the 'vote' for the orbit of any bounded reward function distribution. Definition 6.5 formalizes this 'voting' notion. 4

Definition 6.5 (Inequalities which hold for most probability distributions) . Let f 1 , f 2 : ∆( R |S| ) → R be functions from reward function distributions to real numbers and let D ⊆ ∆( R |S| ) be closed under permutation. We write f 1 ( D ) ≥ most: D f 2 ( D ) 5 when, for all D ∈ D , the following cardinality inequality holds:

<!-- formula-not-decoded -->

Proposition 6.6 (States with 'more options' have more POWER) . If F ( s ) contains a copy of F nd ( s ′ ) via φ , then ∀ γ ∈ [0 , 1] : POWER D bound ( s, γ ) ≥ most POWER D bound ( s ′ , γ ) . If F nd ( s ) \ φ · F nd ( s ′ ) is non-empty, then for all γ ∈ (0 , 1) , the converse ≤ most statement does not hold.

Proposition 6.6 proves that for all γ ∈ [0 , 1] , POWER D bound ( r ↘ , γ ) ≥ most POWER D bound ( glyph[lscript] ↙ , γ ) via s ′ := glyph[lscript] ↙ , s := r ↘ , and the involution φ shown in fig. 4. In fact, because ( 1 1 -γ e r ↗ ) ∈ F nd ( r ↘ ) \ φ · F nd ( glyph[lscript] ↙ ) , r ↘ has 'strictly more options' and therefore fulfills proposition 6.6's stronger condition.

Proposition 6.6 is shown using the fact that φ injectively maps D under which r ↘ has less POWER D , to distributions φ · D which agree with the intuition that r ↘ offers more control. Therefore, at least half of each orbit must agree, and r ↘ never 'loses the POWER vote' against glyph[lscript] ↙ . 6