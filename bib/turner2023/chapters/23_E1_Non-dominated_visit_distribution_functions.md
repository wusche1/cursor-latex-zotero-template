## E.1 Non-dominated visit distribution functions

Definition E.6 (Continuous reward function distribution) . Results with D cont hold for any absolutely continuous reward function distribution.

Remark. We assume R |S| is endowed with the standard topology.

Lemma E.7 (Distinct linear functionals disagree almost everywhere on their domains) . Let x , x ′ ∈ R |S| be distinct. P r ∼D cont ( x glyph[latticetop] r = x ′glyph[latticetop] r ) = 0 .

glyph[negationslash]

Proof. { r ∈ R |S| | ( x -x ′ ) glyph[latticetop] r = 0 } is a hyperplane since x -x ′ = 0 . Therefore, it has no interior in the standard topology on R |S| . Since this empty-interior set is also convex, it has zero Lebesgue measure. By the Radon-Nikodym theorem, it has zero measure under any continuous distribution D cont .

Corollary E.8 (Unique maximization of almost all vectors) . Let X glyph[subsetnoteql] R |S| be finite. P r cont ( ∣ ∣ arg max x ′′ X x ′′glyph[latticetop] r ∣ ∣ &gt; 1 ) = 0 .

<!-- formula-not-decoded -->

Proof. Let x , x ′ ∈ X be distinct. For any r ∈ R |S| , x , x ′ ∈ arg max x ′′ ∈ X x ′′glyph[latticetop] r iff x glyph[latticetop] r = x ′glyph[latticetop] r ≥ max x ′′ ∈ X \{ x , x ′ } x ′′glyph[latticetop] r . By lemma E.7, x glyph[latticetop] r = x ′glyph[latticetop] r holds with probability 0 under any D cont .