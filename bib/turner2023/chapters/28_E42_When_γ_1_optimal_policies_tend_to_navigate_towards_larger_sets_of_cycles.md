## E.4.2 When γ = 1 , optimal policies tend to navigate towards 'larger' sets of cycles

Lemma E.51 (POWER identity when γ = 1 ) .

<!-- formula-not-decoded -->

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (200) follows by lemma E.45. Equation (201) follows by the definition of RSD ( s ) (definition 6.10). Equation (202) follows because for all r ∈ R |S| , corollary E.11 shows that max d ∈ RSD ( s ) d glyph[latticetop] r = max d ∈ ND ( RSD ( s ) ) d glyph[latticetop] r =: max d ∈ RSDnd ( s ) d glyph[latticetop] r .

Proposition 6.12 (When γ = 1 , RSDs control POWER) . If RSD ( s ) contains a copy of RSDnd ( s ′ ) via φ , then POWER D bound ( s, 1) ≥ most POWER D bound ( s ′ , 1 ) . If RSDnd ( s ) \ φ · RSDnd ( s ′ ) is non-empty, then the converse ≤ most statement does not hold.

Proof. Suppose RSDnd ( s ′ ) is similar to D ⊆ RSD ( s ) via involution φ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (203) and eq. (205) follow from lemma E.51. By applying lemma E.24 with A := RSD ( s ′ ) , B ′ := D,B := RSD ( s ) and g the identity function, eq. (204) follows.

Suppose RSDnd ( s ) \ D is non-empty. By the same result, eq. (204) is a strict inequality for all D X -IID ∈ D C/B/IID , and we conclude that POWER D bound ( s ′ , 1 ) glyph[negationslash]≥ most: D bound POWER D bound ( s, 1) .

Theorem 6.13 (Average-optimal policies tend to end up in 'larger' sets of RSDs) . Let D,D ′ ⊆ RSD ( s ) . Suppose that D contains a copy of D ′ via φ , and that the sets D ∪ D ′ and RSDnd ( s ) \ ( D ′ ∪ D ) have pairwise orthogonal vector elements ( i . e . pairwise disjoint vector support). Then P D any ( D, average ) ≥ most P D any ( D ′ , average ) . If RSDnd ( s ) ∩ ( D \ φ · D ′ ) is non-empty, the converse ≤ most statement does not hold.

Proof. Let D sub := φ · D ′ , where D sub ⊆ D by assumption. Let X := { s i ∈ S | max d ∈ D ′ ∪ D d glyph[latticetop] e s i &gt; 0 } . Define

<!-- formula-not-decoded -->

Since φ is an involution, φ ′ is also an involution. Furthermore, by the definition of X , φ ′ · D ′ = D sub and φ ′ · D sub = D ′ (because we assumed that both equalities hold for φ ).

Let D ∗ := D ′ ∪ D sub ∪ ( RSDnd ( s ) \ ( D ′ ∪ D ) ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In eq. (209), we know that φ ′ · D ′ = D sub and φ ′ · D sub = D ′ . We just need to show that φ ′ · ( RSDnd ( s ) \ ( D ′ ∪ D ) ) = RSDnd ( s ) \ ( D ′ ∪ D ) .

Suppose ∃ s i ∈ X, d ′ ∈ RSDnd ( s ) \ ( D ′ ∪ D ) : d ′glyph[latticetop] e s i &gt; 0 . By the definition of X , ∃ d ∈ D ′ ∪ D : d glyph[latticetop] e s i &gt; 0 . Then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (211) follows from the definitions of the dot and Hadamard products. Equation (212) follows because d and d ′ have non-negative entries. Equation (215) follows because d glyph[latticetop] e s i and d ′glyph[latticetop] e s i are both positive. But eq. (215) shows that d glyph[latticetop] d ′ &gt; 0 , contradicting our assumption that d and d ′ are orthogonal.

Therefore, such an s i cannot exist, and X ′ := { s ′ i ∈ S | max d ′ ∈ RSDnd ( s ) \ ( D ′ ∪ D ) d ′glyph[latticetop] e s i &gt; 0 } ⊆ ( S \ X ) . By eq. (206), ∀ s ′ i ∈ X ′ : φ ′ ( s ′ i ) = s ′ i . Thus, φ ′ · ( RSDnd ( s ) \ ( D ′ ∪ D ) ) = RSDnd ( s ) \ ( D ′ ∪ D ) , and eq. (209) follows. We conclude that φ ′ · D ∗ = D ∗ .

Consider Z := ( RSDnd ( s ) \ ( D ′ ∪ D ) ) ∪ D ∪ D ′ . First, Z ⊆ RSD ( s ) by definition. Second, RSDnd ( s ) = RSDnd ( s ) \ ( D ′ ∪ D ) ∪ ( RSDnd ( s ) ∩ D ′ ) ∪ ( RSDnd ( s ) ∩ D ) ⊆ Z . Note that D ∗ = Z \ ( D \ D sub ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since φ · D ′ ⊆ D and ND ( D ′ ) ⊆ D ′ , φ · ND ( D ′ ) ⊆ D . Then eq. (217) holds by applying lemma E.28 with A := D ′ , B ′ := D sub , B := D,C := RSD ( s ) , and the previously defined Z which we showed satisfies ND ( C ) ⊆ Z ⊆ C . Furthermore, involution φ ′ satisfies φ ′ · B ∗ = φ ′ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) = B ∗ by eq. (210).

When RSDnd ( s ) ∩ ( D \ D sub ) is non-empty, since B ′ ⊆ C by assumption, lemma E.28 also shows that eq. (217) is strict for all D X -IID ∈ D C/B/IID , and that P D any ( D ′ , average ) glyph[negationslash]≥ most: D any P D any ( D, average ) .

Proposition E.52 (RSD properties) . Let d ∈ RSD ( s ) . d is element-wise non-negative and ‖ d ‖ 1 = 1 .

Proof. d has non-negative elements because it equals the limit of lim γ → 1 (1 -γ ) f ( γ ) , whose elements are non-negative by proposition E.3 item 1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (219) follows because the definition of RSDs (definition 6.10) ensures that ∃ f ∈ F ( s ) : lim γ → 1 (1 -γ ) f ( γ ) = d . Equation (220) follows because ‖·‖ 1 is a continuous function. Equation (221) follows because ∥ ∥ f ( γ ) ∥ ∥ 1 = 1 1 -γ by proposition E.3 item 2.

Lemma E.53 (When reachable with probability 1, 1-cycles induce non-dominated RSDs) . If e s ′ ∈ RSD ( s ) , then e s ′ ∈ RSDnd ( s ) .

Proof. If d ∈ RSD ( s ) is distinct from e s ′ , then ‖ d ‖ 1 = 1 and d has non-negative entries by proposition E.52. Since d is distinct from e s ′ , then its entry for index s ′ must be strictly less than 1: d glyph[latticetop] e s ′ &lt; 1 = e glyph[latticetop] s ′ e s ′ . Therefore, e s ′ ∈ RSD ( s ) is strictly optimal for the reward function r := e s ′ , and so e s ′ ∈ RSDnd ( s ) .

Corollary 6.14 (Average-optimal policies tend not to end up in any given 1-cycle) . Suppose e s x , e s ′ ∈ RSD ( s ) are distinct. Then P D any ( RSD ( s ) \ { e s x } , average ) ≥ most P D any ( { e s x } , average ) . If there is a third e s ′′ ∈ RSD ( s ) , the converse ≤ most statement does not hold.

glyph[negationslash]

Proof. Suppose e s x , e s ′ ∈ RSD ( s ) are distinct. Let φ := ( s x s ′ ) , D ′ := { e s x } , D := RSD ( s ) \ { e s x } . φ · D ′ = { e s ′ } ⊆ RSD ( s ) \{ e s x } =: D since s x = s ′ . D ′ ∪ D = RSD ( s ) and RSDnd ( s ) \ ( D ′ ∪ D ) = RSDnd ( s ) \ RSD ( s ) = ∅ trivially have pairwise orthogonal vector elements. Then apply theorem 6.13 to conclude that P D any ( { e s x } , average ) ≤ most: D any P D any ( RSD ( s ) \ { e s x } , average ) .

Suppose there exists another e s ′′ ∈ RSD ( s ) . By lemma E.53, e s ′′ ∈ RSDnd ( s ) . Furthermore, since s ′′ glyph[negationslash]∈ { s ′ , s x } , e s ′′ ∈ ( RSD ( s ) \ { e s x } ) \ { e s ′ } = D \ φ · D ′ . Therefore, e s ′′ ∈ RSDnd ( s ) ∩ ( D \ φ · D ′ ) . Then apply the second condition of theorem 6.13 to conclude that P D any ( { e s x } , average ) glyph[negationslash]≥ most: D bound P D any ( RSD ( s ) \ { e s x } , average ) .