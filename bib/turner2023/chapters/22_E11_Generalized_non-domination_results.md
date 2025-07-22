## E.1.1 Generalized non-domination results

Our formalism includes both F nd ( s ) and RSDnd ( s ) ; we therefore prove results that are applicable to both.

Definition E.9 (Non-dominated linear functionals) . Let X glyph[subsetnoteql] R |S| be finite. ND ( X ) := { x ∈ X | ∃ r ∈ R |S| : x glyph[latticetop] r &gt; max x ′ ∈ X \{ x } x ′glyph[latticetop] r } .

Lemma E.10 (All vectors are maximized by a non-dominated linear functional) . Let r ∈ R |S| and let X glyph[subsetnoteql] R |S| be finite and non-empty. ∃ x ∗ ∈ ND ( X ) : x ∗glyph[latticetop] r = max x ∈ X x glyph[latticetop] r .

<!-- formula-not-decoded -->

In eq. (10), each x glyph[latticetop] r expression is linear on r . The max is piecewise linear on r since it is the maximum of a finite set of linear functionals. In particular, all expressions in eq. (10) are continuous on r , and so we can find some δ &gt; 0 neighborhood B ( r , δ ) such that ∀ r ′ ∈ B ( r , δ ) : max x i ∈ A ( r | X ) x glyph[latticetop] i r ′ &gt; max x ′ ∈ X \ A ( r | X ) x ′glyph[latticetop] r ′ .

But almost all r ′ ∈ B ( r , δ ) are maximized by a unique functional x ∗ by corollary E.8; in particular, at least one such r ′′ exists. Formally, ∃ r ′′ ∈ B ( r , δ ) : x ∗glyph[latticetop] r ′′ &gt; max x ′ ∈ X \{ x ∗ } x ′glyph[latticetop] r ′′ . Therefore, x ∗ ∈ ND ( X ) by definition E.9.

x ∗glyph[latticetop] r ′ ≥ max x i ∈ A ( r | X ) x glyph[latticetop] i r ′ &gt; max x ′ ∈ X \ A ( r | X ) x ′glyph[latticetop] r ′ , with the strict inequality following because r ′′ ∈ B ( r , δ ) . These inequalities imply that x ∗ ∈ A ( r | X ) .

Corollary E.11 (Maximal value is invariant to restriction to non-dominated functionals) . Let r ∈ R |S| and let X glyph[subsetnoteql] R |S| be finite. max x ∈ X x glyph[latticetop] r = max x ∈ ND ( X ) x glyph[latticetop] r .

<!-- formula-not-decoded -->

Lemma E.12 (How non-domination containment affects optimal value) . Let r ∈ R |S| and let X,X ′ glyph[subsetnoteql] R |S| be finite.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. Item 1:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (11) follows by corollary E.11. Equation (12) follows because ND ( X ) ⊆ X ′ .

Item 2: by item 1, max x ∈ X x glyph[latticetop] r ≤ max x ′ ∈ X ′ x ′glyph[latticetop] r . Since X ′ ⊆ X , we also have max x ∈ X x glyph[latticetop] r ≥ max x ′ ∈ X ′ x ′glyph[latticetop] r , and so equality must hold.

Definition E.13 (Non-dominated vector functions) . Let I ⊆ R and let F glyph[subsetnoteql] ( R |S| ) I be a finite set of vector-valued functions on I . ND ( F ) := { f ∈ F | ∃ γ ∈ I, r ∈ R |S| : f ( γ ) glyph[latticetop] r &gt; max f ′ ∈ F \{ f } f ′ ( γ ) glyph[latticetop] r } .

Remark. F nd ( s ) = ND ( F ( s ) ) by definition 3.6.

Definition E.14 (Affine transformation of visit distribution sets) . For notational convenience, we define set-scalar multiplication and set-vector addition on X ⊆ R |S| : for c ∈ R , cX := { c x | x ∈ X } . For a ∈ R |S| , X + a := { x + a | x ∈ X } . Similar operations hold when X is a set of vector functions R ↦→ R |S| .

Lemma E.15 (Invariance of non-domination under positive affine transform) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. Item 1: Suppose x ∈ ND ( X ) is strictly optimal for r ∈ R |S| . Then let c &gt; 0 , a ∈ R |S| be arbitrary, and define b := a glyph[latticetop] r .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (14) follows because c &gt; 0 . Equation (15) follows by the definition of b .

Item 2: If f ∈ ND ( F ) , then by definition E.13, there exist γ ∈ I, r ∈ R |S| such that

<!-- formula-not-decoded -->

Apply item 1 to conclude

<!-- formula-not-decoded -->

Therefore, ( c f + a ) ∈ ND ( cF + a ) .