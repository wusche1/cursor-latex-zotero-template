## E.2 Some actions have greater probability of being optimal

Lemma E.35 (Optimal policy shift bound) . For fixed R , Π ∗ ( R,γ ) can take on at most (2 |S| + 1) ∑ s ( | F ( s ) | 2 ) distinct values over γ ∈ (0 , 1) .

Proof. By lemma E.1, Π ∗ ( R,γ ) changes value iff there is a change in optimality status for some visit distribution function at some state. Lippman [1968] showed that two visit distribution functions can trade off optimality status at most 2 |S| +1 times. At each state s , there are ( | F ( s ) | 2 ) such pairs.

Proposition E.36 (Optimality probability's limits exist) . Let F ⊆ F ( s ) . P D any ( F, 0) = lim γ → 0 P D any ( F, γ ) and P D any ( F, 1) = lim γ → 1 P D any ( F, γ ) .

glyph[negationslash]

If lim γ → 1 δ ( γ ) &gt; 0 , then there exist reward functions whose optimal policy sets Π ∗ ( R,γ ) never converge (in the discrete topology on sets) to Π ∗ ( R, 1) , contradicting lemma E.35. So lim γ → 1 δ ( γ ) = 0 .

Proof. First consider the limit as γ → 1 . Let D any have probability measure F any, and define δ ( γ ) := F any ( { R ∈ R S | ∃ γ ∗ ∈ [ γ, 1) : Π ∗ ( R,γ ∗ ) = Π ∗ ( R, 1) } ) . Since F any is a probability measure, δ ( γ ) is bounded [0 , 1] , and δ ( γ ) is monotone decreasing. Therefore, lim γ → 1 δ ( γ ) exists.

By the definition of optimality probability (definition 4.3) and of δ ( γ ) , | P D any ( F, γ ) -P D any ( F, 1) | ≤ δ ( γ ) . Since lim γ → 1 δ ( γ ) = 0 , lim γ → 1 P D any ( F, γ ) = P D any ( F, 1) .

A similar proof shows that lim γ → 0 P D any ( F, γ ) = P D any ( F, 0) .

Lemma E.37 (Optimality probability identity) . Let γ ∈ (0 , 1) and let F ⊆ F ( s ) .

<!-- formula-not-decoded -->

Proof. Let γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (81) follows because lemma E.1 shows that π is optimal iff it induces an optimal visit distribution f at every state. Equation (82) follows because ∀ r ∈ R |S| : max f ′ ∈F ( s ) f ′ ( γ ) glyph[latticetop] r = max f ′ ∈F nd ( s ) f ′ ( γ ) glyph[latticetop] r by lemma E.34.