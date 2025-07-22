## E.4 Seeking POWER is often more probable under optimality

## E.4.1 Keeping options open tends to be POWER-seeking and tends to be optimal

Definition E.42 (Normalized visit distribution function) . Let f : [0 , 1) → R |S| be a vector function. For γ ∈ [0 , 1] , NORM ( f , γ ) := lim γ ∗ → γ (1 -γ ∗ ) f ( γ ∗ ) (this limit need not exist for arbitrary f ). If F is a set of such f , then NORM ( F, γ ) := { NORM ( f , γ ) | f ∈ F } .

Remark. RSD ( s ) = NORM ( F ( s ) , 1 ) .

Lemma E.43 (Normalized visit distribution functions are continuous) . Let ∆ s ∈ ∆( S ) be a state probability distribution, let π ∈ Π , and let f ∗ := E s ∼ ∆ s [ f π,s ] . NORM ( f ∗ , γ ) is continuous on γ ∈ [0 , 1] .

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (122) follows because the expectation is over a finite set. Each f π,s ∈ F ( s ) is continuous on γ ∈ [0 , 1) by lemma E.4, and lim γ ∗ → 1 (1 -γ ∗ ) f π,s ( γ ∗ ) exists because RSDs are well-defined [Puterman, 2014]. Therefore, each NORM ( f π,s , γ ) is continuous on γ ∈ [0 , 1] . Lastly, eq. (123)'s expectation over finitely many continuous functions is itself continuous.

Lemma E.44 (Non-domination of normalized visit distribution functions) . Let ∆ s ∈ ∆( S ) be a state probability distribution and let F := { E s ∼ ∆ s [ f π,s ] | π ∈ Π } . For all γ ∈ [0 , 1] , ND ( NORM ( F, γ ) ) ⊆ NORM ( ND ( F ) , γ ) , with equality when γ ∈ (0 , 1) .

Proof. Suppose γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (124) and eq. (127) follow by the continuity of NORM ( f , γ ) (lemma E.43). Equation (125) follows by lemma E.15 item 1. Equation (126) follows by lemma E.32.

Let γ = 1 . Let d ∈ ND ( NORM ( F, 1) ) be strictly optimal for r ∗ ∈ R |S| . Then let F d ⊆ F be the subset of f ∈ F such that NORM ( f , 1) = d .

<!-- formula-not-decoded -->

Since NORM ( f , 1) is continuous at γ = 1 (lemma E.43), x glyph[latticetop] r ∗ is continuous on x ∈ R |S| , and F is finite, eq. (128) holds for some γ ∗ ∈ (0 , 1) sufficiently close to γ = 1 . By lemma E.10, at least one f ∈ F d is an element of ND ( F ( γ ∗ ) ) . Then by lemma E.32, f ∈ ND ( F ) . We conclude that ND ( NORM ( F, 1) ) ⊆ NORM ( ND ( F ) , 1 ) .

The case for γ = 0 proceeds similarly.

<!-- image -->

Lemma E.45 (POWER limit identity) . Let γ ∈ [0 , 1] .

<!-- formula-not-decoded -->

Proof. Let γ ∈ [0 , 1] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (130) follows because POWER D bound ( s, γ ) is continuous on γ ∈ [0 , 1] by lemma 5.3. Equation (131) follows by lemma E.38.

For γ ∗ ∈ (0 , 1) , let f γ ∗ ( r ) := max f ∈F nd ( s ) 1 -γ ∗ γ ∗ ( f ( γ ∗ ) -e s ) glyph[latticetop] r . For any sequence γ n → γ , ( f γ n ) ∞ n =1 is a sequence of functions which are piecewise linear on r ∈ R |S| , which means they are continuous and therefore measurable. Since lemma E.4 shows that each f ∈ F nd ( s ) is multivariate rational on γ ∗ (and therefore continuous on γ ∗ ), { f γ n } ∞ n =1 converges pointwise to limit function f γ . Furthermore, ∣ ∣ V ∗ R ( s, γ n ) -R ( s ) ∣ ∣ ≤ γ 1 -γ n ‖ R ‖ ∞ , and so ∣ ∣ f γ n ( r ) ∣ ∣ = ∣ ∣ ∣ 1 -γ n γ n ( V ∗ R ( s, γ n ) -R ( s )) ∣ ∣ ∣ ≤ g ( r ) ≤ ‖ r ‖ ∞ =: g ( r ) , which is measurable. Therefore, apply Lebesgue's dominated convergence theorem to conclude that eq. (132) holds. Equation (133) holds because max is a continuous function.

Lemma E.46 (Lemma for POWER superiority) . Let ∆ 1 , ∆ 2 ∈ ∆( S ) be state probability distributions. For i = 1 , 2 , let F ∆ i := { γ -1 E s i ∼ ∆ i [ f π,s i -e s i ] | π ∈ Π } . Suppose F ∆ 2 contains a copy of ND ( F ∆ 1 ) via φ . Then ∀ γ ∈ [0 , 1] : E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] ≤ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

If ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) is non-empty, then for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID and E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] glyph[negationslash]≥ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

These results also hold when replacing F ∆ i with F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 .

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (134) follows by lemma E.44. Equation (136) follows because P φ is a continuous linear operator. Equation (138) follows by assumption.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (140) and eq. (147) follow by lemma E.45. Equation (141) and eq. (146) follow because each R has a stationary deterministic optimal policy π ∈ Π ∗ ( R,γ ) ⊆ Π which simultaneously achieves optimal value at all states. Equation (143) follows by corollary E.11.

Apply lemma E.24 with A := NORM ( F ∆ 1 , γ ) , B := NORM ( F ∆ 2 , γ ) , g the identity function, and involution φ (satisfying φ · ND ( A ) ⊆ B by eq. (139)) in order to conclude that eq. (144) holds.

We show that this result's preconditions holding for F ∗ ∆ i implies the F ∆ i preconditions. Suppose F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 are such that F ∗ sub := φ · ND ( F ∗ ∆ 1 ) ⊆ F ∗ ∆ 2 . In the following, the ∆ i are represented as vectors in R |S| , and γ is a variable.

Suppose that ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) is non-empty; let F ′ sub := φ · ND ( F ∆ 1 ) . Lemma E.32 shows that for all γ ∈ (0 , 1) , ND ( F ∆ 2 ( γ ) ) \ F ′ sub ( γ ) is non-empty. Lemma E.15 item 1 then implies that ND ( B ) \ φ · A = 1 -γ γ ( ND ( F ∆ 2 ( γ ) ) -e s ) \ ( 1 -γ γ F ′ sub ( γ ) ) is non-empty. Then lemma E.24 implies that for all γ ∈ (0 , 1) , eq. (144) is strict for all D X -IID ∈ D C/B/IID and E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] glyph[negationslash]≥ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (149) follows from lemma E.15 item 2. Since we assumed that φ · ND ( F ∗ ∆ 1 ) ⊆ F ∗ ∆ 2 , φ · { ∆ 1 } = φ · ( ND ( F ∗ ∆ 1 ) (0) ) ⊆ F ∗ ∆ 2 (0) = { ∆ 2 } . This implies that P φ ∆ 1 = ∆ 2 and so eq. (151) follows.

Equation (152) shows that φ · { γ f | f ∈ ND ( F ∆ 1 ) } ⊆ { γ f | f ∈ F ∆ 2 } . But we then have φ · { γ f | f ∈ ND ( F ∆ 1 ) } := { γ P φ f | f ∈ ND ( F ∆ 1 ) } = { γ f | f ∈ φ · ND ( F ∆ 1 ) } ⊆ { γ f | f ∈ F ∆ 2 } . Thus, φ · ND ( F ∆ 1 ) ⊆ F ∆ 2 .

Suppose ND ( F ∗ ∆ 2 ) \ φ · ND ( F ∗ ∆ 1 ) is non-empty, which implies that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) must be non-empty. Therefore, if the preconditions of this result are met for F ∗ ∆ i , they are met for F ∆ i .

Proposition 6.6 (States with 'more options' have more POWER) . If F ( s ) contains a copy of F nd ( s ′ ) via φ , then ∀ γ ∈ [0 , 1] : POWER D bound ( s, γ ) ≥ most POWER D bound ( s ′ , γ ) . If F nd ( s ) \ φ · F nd ( s ′ ) is non-empty, then for all γ ∈ (0 , 1) , the converse ≤ most statement does not hold.

Proof. Let F sub := φ · F nd ( s ′ ) ⊆ F ( s ) . Let ∆ 1 := e s ′ , ∆ 2 := e s , and define F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 . Then F nd ( s ′ ) = ND ( F ∗ ∆ 1 ) is similar to F sub = F ∗ sub ⊆ F ∗ ∆ 2 = F ( s ) via involution φ . Apply lemma E.46 to conclude that ∀ γ ∈ [0 , 1] : POWER D bound ( s ′ , γ ) ≤ most: D bound POWER D bound ( s, γ ) .

( )

Furthermore, F nd ( s ) = ND F ∗ ∆ 2 , and F sub = F ∗ sub , and so if F nd ( s ) \ φ · F nd ( s ′ ) := F nd ( s ) \ F sub = ND ( F ∗ ∆ 2 ) \ F ∗ sub is non-empty, then lemma E.46 shows that for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID and POWER D bound ( s ′ , γ ) glyph[negationslash]≥ most: D bound POWER D bound ( s, γ ) .

Lemma E.47 (Non-dominated visit distribution functions never agree with other visit distribution functions at that state) . Let f ∈ F nd ( s ) , f ′ ∈ F ( s ) \ { f } . ∀ γ ∈ (0 , 1) : f ( γ ) = f ′ ( γ ) .

glyph[negationslash]

Proof. Let γ ∈ (0 , 1) . Since f ∈ F nd ( s ) , there exists a γ ∗ ∈ (0 , 1) at which f is strictly optimal for some reward function. Then by proposition E.30, we can produce another reward function for which f is strictly optimal at discount rate γ ; in particular, proposition E.30 guarantees that the policies which induce f ′ are not optimal at γ . So f ( γ ) = f ′ ( γ ) .

glyph[negationslash]

Corollary E.48 (Cardinality of non-dominated visit distributions) . Let F ⊆ F ( s ) . ∀ γ ∈ (0 , 1) : ∣ ∣ F ∩ F nd ( s ) ∣ ∣ = ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Proof. Let γ ∈ (0 , 1) . By applying lemma E.32 with ∆ d := e s , f ∈ F nd ( s ) = ND ( F ( s ) ) iff f ( γ ) ∈ ND ( F ( s, γ ) ) . By lemma E.33, ND ( F ( s, γ ) ) = F nd ( s, γ ) . So all f ∈ F ∩ F nd ( s ) induce f ( γ ) ∈ F ( γ ) ∩ F nd ( s, γ ) , and ∣ ∣ F ∩ F nd ( s ) ∣ ∣ ≥ ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Lemma E.47 implies that for all f , f ′ ∈ F nd ( s ) , f = f ′ iff f ( γ ) = f ′ ( γ ) . Therefore, ∣ ∣ F ∩ F nd ( s ) ∣ ∣ ≤ ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ . So ∣ ∣ F ∩ F nd ( s ) ∣ ∣ = ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Lemma E.49 (Optimality probability and state bottlenecks) . Suppose that s can reach REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) , but only by taking actions equivalent to a ′ or a at state s ′ . F nd ,a ′ := F nd ( s | π ( s ′ ) = a ′ ) , F a := F ( s | π ( s ′ ) = a ) . Suppose F a contains a copy of F nd ,a ′ via φ which fixes all states not belonging to REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Then ∀ γ ∈ [0 , 1] : P D any ( F nd ,a ′ , γ ) ≤ most: D any P D any ( F a , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F nd ,a ′ ) is non-empty, then for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID , and P D any ( F nd ,a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( F a , γ ) .

Proof. Let F sub := φ · F nd ,a ′ . Let F ∗ := ⋃ a ′′ ∈A : ( a ′′ glyph[negationslash]≡ s ′ a ) ∧ ( a ′′ glyph[negationslash]≡ s ′ a ′ ) F ( s | π ( s ′ ) = a ′′ ) ∪ F nd ,a ′ ∪ F sub .

<!-- formula-not-decoded -->

Equation (159) follows because the involution φ ensures that φ · F sub = F nd ,a ′ . By assumption, φ fixes all s ′ glyph[negationslash]∈ REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Suppose f ∈ F ( s ) \ ( F nd ,a ′ ∪ F a ) . By the bottleneck assumption, f does not visit states in REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Therefore, P φ f = f , and so eq. (160) follows.

Let F Z := ( F ( s ) \ ( F ( s | π ( s ) = a ′ ) ∪ F a ) ) ∪ F nd ,a ′ ∪ F a . By definition, F Z ⊆ F ( s ) . Furthermore, F nd ( s ) = ⋃ a ′′ ∈A F nd ( s | π ( s ′ ) = a ′′ ) ⊆ ( F ( s ) \ ( F ( s | π ( s ) = a ′ ) ∪ F a ) ) ∪ F nd ( s | π ( s ) = a ′ ) ∪ F a =: F Z , and so F nd ( s ) ⊆ F Z . Note that F ∗ = F Z \ ( F a \ F sub ) .

Case: γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (162) and eq. (164) follow from lemma E.37. Equation (163) follows by applying lemma E.28 with A := F nd ,a ′ ( γ ) , B ′ := F sub ( γ ) , B := F a ( γ ) , C := F ( s, γ ) , Z := F Z ( γ ) which satisfies ND ( C ) = F nd ( s, γ ) ⊆ F Z ( γ ) ⊆ F ( s, γ ) = C , and involution φ which satisfies φ · F ∗ ( γ ) = φ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) = F ∗ ( γ ) .

<!-- formula-not-decoded -->

Suppose F nd ( s ) ∩ ( F a \ F sub ) is non-empty. 0 &lt; ∣ ∣ F nd ( s ) ∩ ( F a \ F sub ∣ ∣ = ∣ ∣ ∣ F nd ( s, γ ) ∩ ( F a ( γ ) \ F sub ( γ ) ) ∣ ∣ ∣ =: ∣ ∣ ∣ ND ( C ) ∩ ( B \ B ′ ) ∣ ∣ ∣ (with the first equality holding by corollary E.48), and so ND ( C ) ∩ ( B \ B ′ ) is non-empty. We also have B := F a ( γ ) ⊆ F ( s, γ ) =: C . Then reapplying lemma E.28, eq. (163) is strict for all D X -IID ∈ D C/B/IID , and P D any ( F nd ,a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( F a , γ ) .

Case: γ = 1 , γ = 0 .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (165) and eq. (169) hold by proposition E.36. Equation (166) and eq. (168) follow by lemma E.37. Applying lemma E.29 with γ := 1 , I := (0 , 1) , F A := F nd ,a ′ , F B := F a , F C := F ( s ) , F Z as defined above, and involution φ (for which φ · ( F Z \ ( F B \ φ · F A ) ) = F Z \ ( F B \ φ · F A ) ), we conclude that eq. (167) follows.

The γ = 0 case proceeds similarly to γ = 1 .

Lemma E.50 (Action optimality probability is a special case of visit distribution optimality probability) . P D any ( s, a, γ ) = P D any ( F ( s | π ( s ) = a ) , γ ) .

Proof. Let F a := F ( s | π ( s ) = a ) . For γ ∈ (0 , 1) ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By lemma E.1, if ∃ π ∗ ∈ Π ∗ ( R,γ ) : π ∗ ( s ) = a , then it induces some optimal f π ∗ ,s ∈ F a . Conversely, if f π ∗ ,s ∈ F a is optimal at γ ∈ (0 , 1) , then π ∗ chooses optimal actions on the support of f π ∗ ,s ( γ ) . Let π ′ agree with π ∗ on that support and let π ′ take optimal actions at all other states. Then π ′ ∈ Π ∗ ( R,γ ) and π ′ ( s ) = a . So eq. (171) follows.

Suppose γ = 0 or γ = 1 . Consider any sequence ( γ n ) ∞ n =1 converging to γ , and let D any induce probability measure F .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (174) follows by eq. (172). for γ ∗ ∈ [0 , 1] , let f γ ∗ ( R ) := ✶ ∃ π ∗ ∈ Π ∗ ( R,γ ∗ ): π ∗ ( s )= a . For each R ∈ R S , lemma E.35 exists γ x ≈ γ such that for all intermediate γ ′ x between γ x and γ , Π ∗ ( R,γ ′ x ) = Π ∗ ( R,γ ) . Since γ n → γ , this means that ( f γ n ) ∞ n =1 converges pointwise to f γ . Furthermore, ∀ n ∈ N , R ∈ R S : ∣ ∣ f γ n ( R ) ∣ ∣ ≤ 1 by definition. Therefore, eq. (177) follows by Lebesgue's dominated convergence theorem.

Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal) .

Suppose F a := F ( s | π ( s ) = a ) contains a copy of F a ′ := F ( s | π ( s ) = a ′ ) via φ .

<!-- formula-not-decoded -->

2. If s can only reach the states of REACH ( s, a ′ ) ∪ REACH ( s, a ) by taking actions equivalent to a ′ or a at state s , then ∀ γ ∈ [0 , 1] : P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then ∀ γ ∈ (0 , 1) , the converse ≤ most statements do not hold.

Proof. Note that by definition 3.3, F a ′ (0) = { e s } = F a (0) . Since φ · F a ′ ⊆ F a , in particular we have φ · F a ′ (0) = { P φ e s } ⊆ { e s } = F a (0) , and so φ ( s ) = s .

<!-- formula-not-decoded -->

Unless otherwise stated, we treat γ as a variable in this item; we apply element-wise vector addition, constant multiplication, and variable multiplication via the conventions outlined in definition E.14.

<!-- formula-not-decoded -->

Equation (180) follows by definition 3.3, since each f ∈ F ( s ) has an initial term of e s . Equation (181) follows because s glyph[negationslash]∈ REACH ( s, a ′ ) , and so for all s a ′ ∈ supp( T ( s, a ′ )) , f π,s a ′ is unaffected by the choice of action π ( s ) . Note that similar reasoning implies that F a ⊆ e s + γF ∗ T ( s,a ) (because eq. (181) is a containment relation in general).

Since F a ′ = e s + γF ∗ T ( s,a ′ ) , if F a contains a copy of F a ′ via φ , then F ∗ T ( s,a ) contains a copy of F ∗ T ( s,a ′ ) via φ . Then φ · ND ( F ∗ T ( s,a ′ ) ) ⊆ φ · F ∗ T ( s,a ′ ) ⊆ F ∗ T ( s,a ) , and so F ∗ T ( s,a ) contains a copy of ND ( F ∗ T ( s,a ′ ) ) . Then apply lemma E.46 with ∆ 1 := T ( s, a ′ ) and ∆ 2 := T ( s, a ) to conclude that ∀ γ ∈ [0 , 1] : E s a ′ ∼ T ( s,a ′ ) [ POWER D bound ( s a ′ , γ ) ] ≤ most: D bound E s a ∼ T ( s,a ) [ POWER D bound ( s a , γ ) ] . Suppose F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty. To apply the second condition of lemma E.46, we want to demonstrate that ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is also non-empty.

First consider f ∈ F nd ( s ) ∩ F a . Because F a ⊆ e s + γF ∗ T ( s,a ) , we have that γ -1 ( f -e s ) ∈ F ∗ T ( s,a ) . Because f ∈ F nd ( s ) , by definition 3.6, ∃ r ∈ R |S| , γ x ∈ (0 , 1) such that

<!-- formula-not-decoded -->

Then since γ x ∈ (0 , 1) ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (186) holds because F a ⊆ F ( s ) . By assumption, action a is optimal for r at state s and at discount rate γ x . Equation (181) shows that F ∗ T ( s,a ) potentially allows the agent a non-stationary policy choice at s , but non-stationary policies cannot increase optimal value [Puterman, 2014]. Therefore, eq. (187) holds.

We assumed that γ -1 ( f -e s ) ∈ γ -1 ( F nd ( s ) -e s ) . Furthermore, since we just showed that γ -1 ( f -e s ) ∈ F ∗ T ( s,a ) is strictly optimal over the other elements of F ∗ T ( s,a ) for reward function r at discount rate γ x ∈ (0 , 1) , we conclude that it is an element of ND ( F ∗ T ( s,a ) ) by definition E.13.

<!-- formula-not-decoded -->

We now show that ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is non-empty.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

glyph[negationslash]

Equation (188) follows by the assumption that F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty. Let f , f ′ ∈ F nd ( s ) ∩ ( F a \ φ · F a ′ ) be distinct. Then we must have that for some γ x ∈ (0 , 1) , f ( γ x ) = f ′ ( γ x ) . This holds iff γ -1 x ( f ( γ x ) -e s ) = γ -1 x ( f ′ ( γ x ) -e s ) , and so eq. (189) holds.

glyph[negationslash]

Equation (190) holds because F a ⊆ e s + γF ∗ T ( s,a ) and F ′ a = e s + γF ∗ T ( s,a ′ ) by eq. (182). Equation (192) holds because we showed above that γ -1 ( nd ( s ) e s ) F ∗ T ( s,a ) ND ( F ∗ T ( s,a ) ) .

Equation (193) holds because ND F ∗ T ( s,a ′ ) ⊆ F ∗ T ( s,a ′ ) by definition E.13.

F -∩ ⊆ ( )

Therefore, ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is non-empty, and so apply the second condition of lemma E.46 to conclude that for all D X -IID ∈ D C/B/IID , ∀ γ ∈ (0 , 1) : E s a ′ ∼ T ( s,a ′ ) [ POWER D X -IID ( s a ′ , γ ) ] &lt; E s a ∼ T ( s,a ) [ POWER D X -IID ( s a , γ ) ] , and that ∀ γ ∈ (0 , 1) : E s a ′ ∼ T ( s,a ′ ) [ POWER D bound ( s a ′ , γ ) ] glyph[negationslash]≥ most: D bound E s a ∼ T ( s,a ) [ POWER D bound ( s a , γ ) ] .

Item 2. Let φ ′ ( s x ) := φ ( s x ) when s x ∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) , and equal s x otherwise. Since φ is an involution, so is φ ′ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (195) follows because if s ∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) , then we already showed that φ fixes s . Otherwise, φ ′ ( s ) = s by definition. Equation (196) follows by the definition of φ ′ on REACH ( s, a ′ ) ∪ REACH ( s, a ) and because e s = P φ e s . Next, we assumed that φ · F a ′ ⊆ F a , and so eq. (198) holds.

Therefore, F a contains a copy of F a ′ via φ ′ fixing all s x glyph[negationslash]∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) . Therefore, F a contains a copy of F nd ,a ′ := F nd ( s ) ∩ F a ′ via the same φ ′ . Then apply lemma E.49 with s ′ := s to conclude that ∀ γ ∈ [0 , 1] : P D any ( F a ′ , γ ) ≤ most: D any P D any ( F a , γ ) . By lemma E.50, P D any ( s, a ′ , γ ) = P D any ( F a ′ , γ ) and P D any ( s, a, γ ) = P D any ( F a , γ ) . Therefore, ∀ γ ∈ [0 , 1] : P D any ( s, a ′ , γ ) ≤ most: D any P D any ( s, a, γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then apply the second condition of lemma E.49 to conclude that for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID , and P D any ( s, a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( s, a, γ ) .