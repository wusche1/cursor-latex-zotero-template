## 6.1 Keeping options open tends to be POWER-seeking and tends to be optimal

Certain symmetries in the MDP structure ensure that, compared to left , going right tends to be optimal and to be POWER-seeking. Intuitively, by going right , the agent has 'strictly more choices.' Proposition 6.9 will formalize this tendency.

Definition 6.7 (Equivalent actions) . Actions a 1 and a 2 are equivalent at state s (written a 1 ≡ s a 2 ) if they induce the same transition probabilities: T ( s, a 1 ) = T ( s, a 2 ) .

The agent can reach states in { r glyph[triangleright] , r ↗ , r ↘ } by taking actions equivalent to right at state glyph[star] .

Definition 6.8 (States reachable after taking an action) . REACH ( s, a ) is the set of states reachable with positive probability after taking the action a in state s .

Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal) .

Suppose F a := F ( s | π ( s ) = a ) contains a copy of F a ′ := F ( s | π ( s ) = a ′ ) via φ .

<!-- formula-not-decoded -->

4 The voting analogy and the 'most' descriptor imply that we have endowed each orbit with the counting measure. However, a priori , we might expect that some orbit elements are more empirically likely to be specified than other orbit elements. See section 7 for more on this point.

5 We write f 1 ( D ) ≥ most f 2 ( D ) when D is clear from context.

6 Proposition 6.6 also proves that in general, ∅ has less POWER than glyph[lscript] ↙ and r ↘ . However, this does not prove that most distributions D satisfy the joint inequality POWER D ( ∅ , γ ) ≤ POWER D ( glyph[lscript] ↙ , γ ) ≤ POWER D ( r ↘ , γ ) . This only proves that these inequalities hold pairwise for most D . The orbit elements D which agree that ∅ has less POWER D than glyph[lscript] ↙ need not be the same elements D ′ which agree that glyph[lscript] ↙ has less POWER D ′ than r ↘ .

2. If s can only reach the states of REACH ( s, a ′ ) ∪ REACH ( s, a ) by taking actions equivalent to a ′ or a at state s , then ∀ γ ∈ [0 , 1] : P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then ∀ γ ∈ (0 , 1) , the converse ≤ most statements do not hold.

<!-- image -->

Figure 6: Going right is optimal for most reward functions. This is because whenever R makes left strictly optimal over right , its permutation φ · R makes right strictly optimal over left by switching which states get which rewards.

We check the conditions of proposition 6.9. s := glyph[star] , a ′ := left , a := right . Figure 6 shows that glyph[star] glyph[negationslash]∈ REACH ( glyph[star], left ) and that glyph[star] can only reach { glyph[lscript] glyph[triangleleft] , glyph[lscript] ↖ , glyph[lscript] ↙ } ∪ { r glyph[triangleright] , r ↗ , r ↘ } when the agent immediately takes actions equivalent to left or right . F ( glyph[star] | π ( glyph[star] ) = right ) contains a copy of F ( glyph[star] | π ( glyph[star] ) = left ) via φ . Furthermore, F nd ( glyph[star] ) ∩ { e glyph[star] + γ e r glyph[triangleright] + γ 2 e r ↘ + γ 3 1 -γ e r ↗ , e glyph[star] + γ e r glyph[triangleright] + γ 2 1 -γ e r ↗ } = { e glyph[star] + γ e r glyph[triangleright] + γ 2 1 -γ e r ↗ } is non-empty, and so all conditions are met.

For any γ ∈ [0 , 1] and D such that P D ( glyph[star], left , γ ) &gt; P D ( glyph[star], right , γ ) , environmental symmetry ensures that P φ ·D ( glyph[star], left , γ ) &lt; P φ ·D ( glyph[star], right , γ ) . A similar statement holds for POWER.