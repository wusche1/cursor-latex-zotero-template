## Appendix B Seeking POWER can be a detour

Remark. The results of appendix E do not depend on this section's results.

One might suspect that optimal policies tautologically tend to seek POWER. This intuition is wrong.

<!-- image -->

Proposition B.1 (Greater POWER D bound does not imply greater P D bound ) . Action a seeking more POWER D bound than a ′ at state s and γ does not imply that P D bound ( s, a, γ ) ≥ P D bound ( s, a ′ , γ ) .

Proof. Consider the environment of fig. 10. Let X u := unif (0 , 1) , and consider D X u -IID, which has bounded support. Direct computation 7 of the POWER expectation (definition 5.2) yields POWER D Xu -IID ( s 2 , 1) = 3 4 &gt; 2 3 = POWER D Xu -IID ( s 3 , 1) . Therefore, N seeks more POWER D Xu -IID than NE at state s 1 and γ = 1 .

<!-- formula-not-decoded -->

D Xu 3 3 D Xu

Lemma B.2 (Fraction of orbits which agree on weak optimality) . Let D ⊆ ∆( R |S| ) , and suppose f 1 , f 2 : ∆( R |S| ) → R are such that f 1 ( D ) ≥ most: D f 2 ( D ) . Then for all D ∈ D , ∣ ∣ ∣ { D ′ ∈ S |S| ·D| f 1 ( D ′ ) ≥ f 2 ( D ′ ) } ∣ ∣ ∣ | S |S| ·D | ≥ 1 2 .

Proof. All D ′ ∈ S |S| · D such that f 1 ( D ′ ) = f 2 ( D ′ ) satisfy f 1 ( D ′ ) ≥ f 2 ( D ′ ) .

glyph[negationslash]

Otherwise, consider the D ′ ∈ S |S| · D such that f 1 ( D ′ ) = f 2 ( D ′ ) . By the definition of ≥ most (definition 6.5), at least 1 2 of these D ′ satisfy f 1 ( D ′ ) &gt; f 2 ( D ′ ) , in which case f 1 ( D ′ ) ≥ f 2 ( D ′ ) . Then the desired inequality follows.

Lemma B.3 ( ≥ most and trivial orbits) . Let D ⊆ ∆( R |S| ) and suppose f 1 ( D ) ≥ most: D f 2 ( D ) . For all reward function distributions D ∈ D with one-element orbits, f 1 ( D ) ≥ f 2 ( D ) . In particular, D has a one-element orbit when it distributes reward identically and independently ( IID ) across states.

Proof. By lemma B.2, at least half of the elements D ′ ∈ S |S| · D satisfy f 1 ( D ′ ) ≥ f 2 ( D ′ ) . But ∣ ∣ ∣ S |S| · D ∣ ∣ ∣ = 1 , and so f 1 ( D ) ≥ f 2 ( D ) must hold.

If D is IID, it has a one-element orbit due to the assumed identical distribution of reward.

Proposition B.4 (Actions which tend to seek POWER do not necessarily tend to be optimal) . Action a tending to seek more POWER than a ′ at state s and γ does not imply that P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

Proof. Consider the environment of fig. 10. Since RSDnd ( s 3 ) glyph[subsetnoteql] RSD ( s 2 ) , proposition 6.12 shows that POWER D bound ( s 2 , 1) ≥ most: D bound POWER D bound ( s 3 , 1) via s ′ := s 3 , s := s 2 , φ the identity permutation (which is an involution). Therefore, N tends to seek more POWER than NE at state s 1 and γ = 1 .

If P D any ( s 1 , N , 1) ≥ most: D any P D any ( s 1 , NE , 1) , then lemma B.3 shows that P D X -IID ( s 1 , N , 1) ≥ P D X -IID ( s 1 , NE , 1) for all D X -IID . But the proof of proposition B.1 showed that P D Xu -IID ( s 1 , N , 1) &lt; P D Xu -IID ( s 1 , NE , 1) for X u := unif (0 , 1) . Therefore, it cannot be true that P D any ( s 1 , N , 1) ≥ most: D any P D any ( s 1 , NE , 1) .