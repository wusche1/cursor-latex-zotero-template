## Appendix E Theoretical results

Lemma E.1 (A policy is optimal iff it induces an optimal visit distribution at every state) . Let γ ∈ (0 , 1) and let R be a reward function. π ∈ Π ∗ ( R,γ ) iff π induces an optimal visit distribution at every state.

Proof. By definition, a policy π is optimal iff π induces the maximal on-policy value at each state, which is true iff π induces an optimal visit distribution at every state (by the dual formulation of optimal value functions).

Definition E.2 (Transition matrix induced by a policy) . T π is the transition matrix induced by policy π ∈ Π , where T π e s := T ( s, π ( s )) . ( T π ) t e s gives the probability distribution over the states visited at time step t , after following π for t steps from s .

Proposition E.3 (Properties of visit distribution functions) . Let s, s ′ ∈ S , f π,s ∈ F ( s ) .

1. f π,s ( γ ) is element-wise non-negative and element-wise monotonically increasing on γ ∈ [0 , 1) .
2. ∀ γ ∈ [0 , 1) : ∥ ∥ f π,s ( γ ) ∥ ∥ 1 = 1 1 -γ .

Proof. Item 1: by examination of definition 3.3, f π,s = ∑ ∞ t =0 ( γ T π ) t e s . Since each ( T π ) t is left stochastic and e s is the standard unit vector, each entry in each summand is non-negative. Therefore, ∀ γ ∈ [0 , 1) : f π,s ( γ ) glyph[latticetop] e s ′ ≥ 0 , and this function monotonically increases on γ .

Item 2:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (7) follows because all entries in each ( T π ) t e s are non-negative by item 1. Equation (8) follows because each ( T π ) t is left stochastic and e s is a stochastic vector, and so ∥ ∥ ∥ ( T π ) t e s ∥ ∥ ∥ 1 = 1 .

Lemma E.4 ( f ∈ F ( s ) is multivariate rational on γ ) . f π ∈ F ( s ) is a multivariate rational function on γ ∈ [0 , 1) .

Proof. Let r ∈ R |S| and consider f π ∈ F ( s ) . Let v π R be the V ∗ R ( s, γ ) function in column vector form, with one entry per state value.

By the Bellman equations, v π R = ( I -γ T π ) -1 r . Let A γ := ( I -γ T π ) -1 , and for state s , form A s,γ by replacing A γ 's column for state s with r . As noted by Lippman [1968], by Cramer's rule, V π R ( s, γ ) = det A s,γ det A γ is a rational function with numerator and denominator having degree at most |S| .

In particular, for each state indicator reward function e s i , V π s i ( s, γ ) = f π,s ( γ ) glyph[latticetop] e s i is a rational function of γ whose numerator and denominator each have degree at most |S| . This implies that f π ( γ ) is multivariate rational on γ ∈ [0 , 1) .

Corollary E.5 (On-policy value is rational on γ ) . Let π ∈ Π and R be any reward function. V π R ( s, γ ) is rational on γ ∈ [0 , 1) .

Proof. V π R ( s, γ ) = f π,s ( γ ) glyph[latticetop] r , and f is a multivariate rational function of γ by lemma E.4. Therefore, for fixed r , f π,s ( γ ) glyph[latticetop] r is a rational function of γ .