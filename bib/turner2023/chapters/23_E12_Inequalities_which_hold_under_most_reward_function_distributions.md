## E.1.2 Inequalities which hold under most reward function distributions

Definition 6.5 (Inequalities which hold for most probability distributions) . Let f 1 , f 2 : ∆( R |S| ) → R be functions from reward function distributions to real numbers and let D ⊆ ∆( R |S| ) be closed under permutation. We write f 1 ( D ) ≥ most: D f 2 ( D ) 8 when, for all D ∈ D , the following cardinality inequality holds:

<!-- formula-not-decoded -->

Lemma E.16 (Helper lemma for demonstrating ≥ most: D any ) . Let D ⊆ ∆( R |S| ) . If ∃ φ ∈ S |S| such that for all D ∈ D , f 1 ( D ) &lt; f 2 ( D ) implies that f 1 ( φ · D ) &gt; f 2 ( φ · D ) , then f 1 ( D ) ≥ most: D f 2 ( D ) .

Proof. Since φ does not belong to the stabilizer of S |S| , φ acts injectively on S |S| · D . By assumption on φ , the image of {D ′ ∈ S |S| · D | f 1 ( D ′ ) &lt; f 2 ( D ′ ) } under φ is a subset of {D ′ ∈ S |S| · D | f 1 ( D ′ ) &gt; f 2 ( D ′ ) } . Since φ is injective, ∣ ∣ ∣ {D ′ ∈ S |S| · D | f 1 ( D ′ ) &lt; f 2 ( D ′ ) } ∣ ∣ ∣ ≤ ∣ ∣ ∣ {D ′ ∈ S |S| · D | f 1 ( D ′ ) &gt; f 2 ( D ′ ) } ∣ ∣ ∣ . f 1 ( D ) ≥ most: D f 2 ( D ) by definition 6.5.

Lemma E.17 (A helper result for expectations of functions) . Let B 1 , . . . , B n glyph[subsetnoteql] R |S| be finite and let D ⊆ ∆( R |S| ) . Suppose f is a function of the form

<!-- formula-not-decoded -->

for some function g , and that f is well-defined for all D ∈ D . Let φ be a state permutation. Then

<!-- formula-not-decoded -->

Proof. Let distribution D have probability measure F , and let φ · D have probability measure F φ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (24) follows by the definition of F φ (definition 6.3). Equation (25) follows by substituting r ′ := P φ r . Equation (26) follows from the fact that all permutation matrices have unitary determinant and are orthogonal (and so ( P -1 φ ) glyph[latticetop] = P φ ).

Definition E.18 (Support of D any ) . Let D any be any reward function distribution. supp( D any ) is the smallest closed subset of R |S| whose complement has measure zero under D any .

8 We write f 1 ( D ) ≥ most f 2 ( D ) when D is clear from context.

Definition E.19 (Linear functional optimality probability) . For finite A,B glyph[subsetnoteql] R |S| , the probability under D any that A is optimal over B is p D any ( A ≥ B ) := P r ∼D any ( max a ∈ A a glyph[latticetop] r ≥ max b ∈ B b glyph[latticetop] r ) .

Proposition E.20 (Non-dominated linear functionals and their optimality probability) . Let A glyph[subsetnoteql] R |S| be finite. If ∃ b &lt; c : [ b, c ] |S| ⊆ supp( D any ) , then a ∈ ND ( A ) implies that a is strictly optimal for a set of reward functions with positive measure under D any .

Proof. Suppose ∃ b &lt; c : [ b, c ] |S| ⊆ supp( D any ) . If a ∈ ND ( A ) , then let r be such that a glyph[latticetop] r &gt; max a ′ ∈ A \{ a } a ′glyph[latticetop] r . For a 1 &gt; 0 , a 2 ∈ R , positively affinely transform r ′ := a 1 r + a 2 1 (where 1 ∈ R |S| is the all-ones vector) so that r ′ ∈ ( b, c ) |S| .

Note that a is still strictly optimal for r ′ :

<!-- formula-not-decoded -->

Furthermore, by the continuity of both terms on the right-hand side of eq. (29), a is strictly optimal for reward functions in some open neighborhood N of r ′ . Let N ′ := N ∩ ( b, c ) |S| . N ′ is still open in R |S| since it is the intersection of two open sets N and ( b, c ) |S| .

D any must assign positive probability measure to all open sets in its support; otherwise, its support would exclude these zero-measure sets by definition E.18. Therefore, D any assigns positive probability to N ′ ⊆ supp( D any ) .

Lemma E.21 (Expected value of similar linear functional sets) . Let A,B glyph[subsetnoteql] R |S| be finite, let A ′ be such that ND ( A ) ⊆ A ′ ⊆ A , and let g : R → R be an increasing function. If B contains a copy B ′ of A ′ via φ , then

<!-- formula-not-decoded -->

If ND ( B ) \ B ′ is empty, then eq. (30) is an equality. If ND ( B ) \ B ′ is non-empty, g is strictly increasing, and ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D bound ) , then eq. (30) is strict.

Proof. Because g : R → R is increasing, it is measurable (as is max ). Therefore, the relevant expectations exist for all D bound.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (31) holds because ∀ r ∈ R |S| : max a ∈ A a glyph[latticetop] r = max a ∈ A ′ a glyph[latticetop] r by lemma E.12's item 2 with X := A , X ′ := A ′ . Equation (32) holds by lemma E.17. Equation (33) holds by the definition of B ′ . Furthermore, our assumption on φ guarantees that B ′ ⊆ B . Therefore, max b ∈ B ′ b glyph[latticetop] r ≤ max b ∈ B b glyph[latticetop] r , and so eq. (34) holds by the fact that g is an increasing function. Then eq. (30) holds.

If ND ( B ) \ B ′ is empty, then ND ( B ) ⊆ B ′ . By assumption, B ′ ⊆ B . Then apply lemma E.12 item 2 with X := B , X ′ := B ′ in order to conclude that eq. (34) is an equality. Then eq. (30) is also an equality.

Suppose that g is strictly increasing, ND ( B ) \ B ′ is non-empty, and ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D bound ) . Let x ∈ ND ( B ) \ B ′ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

x is strictly optimal for a positive-probability subset of supp( D bound ) by proposition E.20. Since g is strictly increasing, eq. (35) is strict. Therefore, we conclude that eq. (30) is strict.

Lemma E.22 (For continuous IID distributions D X -IID , ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D X -IID ) ) .

Proof. D X -IID := X |S| . Since the state reward distribution X is continuous, X must have support on some open interval ( b, c ) . Since D X -IID is IID across states, ( b, c ) |S| ⊆ supp( D X -IID ) .

Definition E.23 (Bounded, continuous IID reward) . D C/B/IID is the set of D X -IID which equal X |S| for some continuous, bounded-support distribution X over R .

Lemma E.24 (Expectation superiority lemma) . Let A,B glyph[subsetnoteql] R |S| be finite and let g : R → R be an increasing function. If B contains a copy B ′ of ND ( A ) via φ , then

<!-- formula-not-decoded -->

Furthermore, if g is strictly increasing and ND ( B ) \ φ · ND ( A ) is non-empty, then eq. (37) is strict for all D X -IID ∈ D C/B/IID . In particular, E r ∼D bound [ g ( max a ∈ A a glyph[latticetop] r ) ] glyph[negationslash]≥ most: D bound E r ∼D bound [ g ( max b ∈ B b glyph[latticetop] r ) ] .

Proof. Because g : R → R is increasing, it is measurable (as is max ). Therefore, the relevant expectations exist for all D bound.

Suppose that D bound is such that E r ∼D bound [ g ( max b ∈ B b glyph[latticetop] r ) ] &lt; E r ∼D bound [ g ( max a ∈ A a glyph[latticetop] r ) ] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (38) follows by applying lemma E.21 with permutation φ and A ′ := ND ( A ) . Equation (39) follows because involutions satisfy φ -1 = φ , and φ 2 is therefore the identity. Equation (40) follows because we assumed that E r ∼D bound [ g ( max b ∈ B b glyph[latticetop] r ) ] &lt; E r ∼D bound [ g ( max a ∈ A a glyph[latticetop] r ) ] . Equation (41) follows by applying lemma E.21 with permutation φ and and A ′ := ND ( A ) . By lemma E.16, eq. (37) holds.

Suppose g is strictly increasing and ND ( B ) \ B ′ is non-empty. Let φ ′ ∈ S |S| .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (42) and eq. (44) hold because D X -IID distributes reward identically across states: ∀ φ x ∈ S |S| : φ x · D X -IID = D X -IID. By lemma E.22, ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D X -IID ) . Therefore, apply lemma E.21 with A ′ := ND ( A ) to conclude that eq. (43) holds.

<!-- formula-not-decoded -->

Definition E.25 (Indicator function) . Let L be a predicate which takes input x . ✶ L ( x ) is the function which returns 1 when L ( x ) is true, and 0 otherwise.

<!-- formula-not-decoded -->

Lemma E.26 (Optimality probability inclusion relations) . Let X,Y glyph[subsetnoteql] R |S| be finite and suppose Y ′ ⊆ Y .

If ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D any ) , X ⊆ Y , and ND ( Y ) ∩ ( Y \ Y ′ ) is non-empty, then the second inequality is strict.

## Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (47) follows because ∀ r ∈ R |S| : ✶ max x ∈ X x glyph[latticetop] r ≥ max y ∈ Y y glyph[latticetop] r ≤ ✶ max x ∈ X x glyph[latticetop] r ≥ max y ∈ Y ′ y glyph[latticetop] r since Y ′ ⊆ Y ; note that eq. (47) equals p D any ( X ≥ Y ′ ) , and so the first inequality of eq. (45) is shown. Equation (48) holds because ∀ r ∈ R |S| : ✶ max x ∈ X x glyph[latticetop] r ≥ max y ∈ Y ′ y glyph[latticetop] r ≤ max x ∈ X ∪ ( Y \ Y ′ ) x glyph[latticetop] r ≥ max y ∈ Y ′ b glyph[latticetop] r .

✶ Suppose ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D any ) , X ⊆ Y , and ND ( Y ) ∩ ( Y \ Y ′ ) is non-empty. Let y ∗ ∈ ND ( Y ) ∩ ( Y \ Y ′ ) . By proposition E.20, y ∗ is strictly optimal on a subset of supp( D any ) with positive measure under D any. In particular, for a set of r ∗ with positive measure under D any, we have y ∗glyph[latticetop] r ∗ &gt; max y ∈ Y ′ y glyph[latticetop] r ∗ .

Then eq. (48) is strict, and therefore the second inequality of eq. (45) is strict as well.

Lemma E.27 (Optimality probability of similar linear functional sets) . Let A,B,C glyph[subsetnoteql] R |S| be finite, and let Z ⊆ R |S| be such that ND ( C ) ⊆ Z ⊆ C . If ND ( A ) is similar to B ′ ⊆ B via φ such that φ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) , then

<!-- formula-not-decoded -->

If B ′ = B , then eq. (52) is an equality. If ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D any ) , B ′ ⊆ C , and ND ( C ) ∩ ( B \ B ′ ) is non-empty, then eq. (52) is strict.

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (53) and eq. (59) follow by lemma E.12's item 2 with X := C , X ′ := Z . Similarly, eq. (54) follows by lemma E.12's item 2 with X := A , X ′ := ND ( A ) . Equation (55) follows by applying the first inequality of lemma E.26 with X := ND ( A ) , Y := Z, Y ′ := Z \ ( B \ B ′ ) . Equation (56) follows by applying lemma E.17 to eq. (53) with permutation φ .

Equation (57) follows by our assumptions on φ . Equation (58) follows because by applying the second inequality of lemma E.26 with X := B ′ , Y := ND ( C ) , Y ′ := ND ( C ) \ ( B \ B ′ ) .

Suppose B ′ = B . Then B \ B ′ = ∅ , and so eq. (55) and eq. (58) are trivially equalities. Then eq. (52) is an equality.

Suppose ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D any ) ; note that ( b, c ) |S| ⊆ supp( φ · D any ) , since such support must be invariant to permutation. Further suppose that B ′ ⊆ C and that ND ( C ) ∩ ( B \ B ′ ) is nonempty. Then letting X := B ′ , Y := Z, Y ′ := Z \ ( B \ B ′ ) and noting that ND ( ND ( Z ) ) = ND ( Z ) , apply lemma E.26 to eq. (58) to conclude that eq. (52) is strict.

Lemma E.28 (Optimality probability superiority lemma) . Let A,B,C glyph[subsetnoteql] R |S| be finite, and let Z satisfy ND ( C ) ⊆ Z ⊆ C . If B contains a copy B ′ of ND ( A ) via φ such that φ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) , then p D any ( A ≥ C ) ≤ most: D any p D any ( B ≥ C ) .

If B ′ ⊆ C and ND ( C ) ∩ ( B \ B ′ ) is non-empty, then the inequality is strict for all D X -IID ∈ D C/B/IID and p D any ( A ≥ C ) glyph[negationslash]≥ most: D any p D any ( B ≥ C ) .

Proof. Suppose D any is such that p D any ( B ≥ C ) &lt; p D any ( A ≥ C ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (60) holds because φ is an involution. Equation (61) and eq. (63) hold by applying lemma E.27 with permutation φ . Equation (62) holds by assumption. Therefore, p D any ( A ≥ C ) ≤ most: D any p D any ( B ≥ C ) by lemma E.16.

Suppose B ′ ⊆ C and ND ( C ) ∩ ( B \ B ′ ) is non-empty, and let D X -IID be any continuous distribution which distributes reward independently and identically across states. Let φ ′ ∈ S |S| .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (64) and eq. (66) hold because D X -IID distributes reward identically across states, ∀ φ x ∈ S |S| : φ x · D X -IID = D X -IID. By lemma E.22, ∃ b &lt; c : ( b, c ) |S| ⊆ supp( D X -IID ) . Therefore, apply lemma E.27 to conclude that eq. (65) holds.

<!-- formula-not-decoded -->

Lemma E.29 (Limit probability inequalities which hold for most distributions) . Let I ⊆ R , let D ⊆ ∆( R |S| ) be closed under permutation, and let F A , F B , F C be finite sets of vector functions I ↦→ R |S| . Let γ be a limit point of I such that f 1 ( D ) := lim γ ∗ → γ p D ( F B ( γ ∗ ) ≥ F C ( γ ∗ ) ) , f 2 ( D ) := lim γ ∗ → γ p D ( F A ( γ ∗ ) ≥ F C ( γ ∗ ) ) are well-defined for all D ∈ D .

Let F Z satisfy ND ( F C ) ⊆ F Z ⊆ F C . Suppose F B contains a copy of F A via φ such that φ · ( F Z \ ( F B \ φ · F A ) ) = F Z \ ( F B \ φ · F A ) . Then f 2 ( D ) ≤ most: D f 1 ( D ) .

Proof. Suppose D ∈ D is such that f 2 ( D ) &gt; f 1 ( D ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By the assumption that D is closed under permutation and f 2 is well-defined for all D ∈ D , f 2 ( φ · D ) is well-defined. Equation (67) follows since φ = φ -1 because φ is an involution. For all γ ∗ ∈ I , let A := F A ( γ ∗ ) , B := F B ( γ ∗ ) , C := F C ( γ ∗ ) , Z := F Z ( γ ∗ ) (by definition E.13, ND ( C ) ⊆ Z ⊆ C ). Since φ · A ⊆ B by assumption, and since ND ( A ) ⊆ A , B also contains a copy of ND ( A ) via φ . Furthermore, φ · ( Z \ ( B \ φ · A ) ) = Z \ ( B \ φ · A ) (by assumption), and so apply lemma E.27 to conclude that p φ -1 ·D ( F A ( γ ∗ ) ≥ F C ( γ ∗ ) ) ≤ p D ( F B ( γ ∗ ) ≥ F C ( γ ∗ ) ) . Therefore, the limit inequality eq. (69) holds. Equation (70) follows because we assumed that f 1 ( D ) &lt; f 2 ( D ) . Equation (71) holds by reasoning similar to that given for eq. (69).

Therefore, f 2 ( D ) &gt; f 1 ( D ) implies that f 2 ( φ · D ) &lt; f 1 ( φ · D ) , and so apply lemma E.16 to conclude that f 2 ( D ) ≤ most: D f 1 ( D ) .