## E.3 Basic properties of POWER

Lemma E.38 (POWER identities) . Let γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (89) follows from lemma E.34. Equation (91) follows from the dual formulation of optimal value functions. Equation (92) holds by the definition of V ∗ D bound ( s, γ ) (definition 5.1). Equation (93) holds because f π,s ( γ ) = e s + γ E s ′ ∼ T ( s,π ( s ) ) [ f π,s ′ ( γ ) ] by the definition of a visit distribution function (definition 3.3).

Definition E.39 (Discount-normalized value function) . Let π be a policy, R a reward function, and s a state. For γ ∈ [0 , 1] , V π R, norm ( s, γ ) := lim γ ∗ → γ (1 -γ ∗ ) V π R ( s, γ ∗ ) .

Lemma E.40 (Normalized value functions have uniformly bounded derivative) . There exists K ≥ 0 such that for all reward functions r ∈ R |S| , sup s ∈S ,π ∈ Π ,γ ∈ [0 , 1] ∣ ∣ ∣ d dγ V π R, norm ( s, γ ) ∣ ∣ ∣ ≤ K ‖ r ‖ 1 .

Proof. Let π be any policy, s a state, and R a reward function. Since V π R, norm ( s, γ ) = lim γ ∗ → γ (1 -γ ∗ ) f π,s ( γ ∗ ) glyph[latticetop] r , d dγ V π R, norm ( s, γ ) is controlled by the behavior of lim γ ∗ → γ (1 -γ ∗ ) f π,s ( γ ∗ ) . We show that this function's gradient is bounded in infinity norm.

glyph[negationslash]

glyph[negationslash]

By lemma E.4, f π,s ( γ ) is a multivariate rational function on γ . Therefore, for any state s ′ , f π,s ( γ ) glyph[latticetop] e s ′ = P ( γ ) Q ( γ ) in reduced form. By proposition E.3, 0 ≤ f π,s ( γ ) glyph[latticetop] e s ′ ≤ 1 1 -γ . Thus, Q may only have a root of multiplicity 1 at γ = 1 , and Q ( γ ) = 0 for γ ∈ [0 , 1) . Let f s ′ ( γ ) := (1 -γ ) f π,s ( γ ) glyph[latticetop] e s ′ .

If Q (1) = 0 , then the derivative f ′ s ′ ( γ ) is bounded on γ ∈ [0 , 1) because the polynomial (1 -γ ) P ( γ ) cannot diverge on a bounded domain.

If Q (1) = 0 , then factor out the root as Q ( γ ) = (1 -γ ) Q ∗ ( γ ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since Q ∗ ( γ ) is a polynomial with no roots on γ ∈ [0 , 1] , f ′ s ′ ( γ ) is bounded on γ ∈ [0 , 1) .

Therefore, whether or not Q ( γ ) has a root at γ = 1 , f ′ s ′ ( γ ) is bounded on γ ∈ [0 , 1) . Furthermore, sup γ ∈ [0 , 1) ∥ ∥ ∇ (1 -γ ) f π,s ( γ ) ∥ ∥ ∞ = sup γ ∈ [0 , 1) max s ′ ∈S ∣ ∣ f ′ s ′ ( γ ) ∣ ∣ is finite since there are only finitely many states.

There are finitely many π ∈ Π , and finitely many states s , and so there exists some K ′ such that sup s ∈S , π ∈ Π ,γ ∈ [0 , 1) ∥ ∥ ∇ (1 -γ ) f π,s ( γ ) ∥ ∥ ∞ ≤ K ′ . Then ∥ ∥ ∇ (1 -γ ) f π,s ( γ ) ∥ ∥ 1 ≤ |S| K ′ =: K .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (99) holds because V π R ( s, γ ) is continuous on γ ∈ [0 , 1) by corollary E.5. Equation (101) holds by the Cauchy-Schwarz inequality.

<!-- formula-not-decoded -->

Lemma 5.3 (Continuity of POWER) . POWER D bound ( s, γ ) is Lipschitz continuous on γ ∈ [0 , 1] .

Proof. Let b, c be such that supp( D bound ) ⊆ [ b, c ] |S| . For any r ∈ supp( D bound ) and π ∈ Π , V π R, norm ( s, γ ) has Lipschitz constant K ‖ r ‖ 1 ≤ K |S| ‖ r ‖ ∞ ≤ K |S| max( | c | , | b | ) on γ ∈ (0 , 1) by lemma E.40.

<!-- formula-not-decoded -->

eq. (94). The expectation of the maximum of a set of functions which share a Lipschitz constant, also shares the Lipschitz constant. This shows that POWER D bound ( s, γ ) is Lipschitz continuous on γ ∈ (0 , 1) . Thus, its limits are well-defined as γ → 0 and γ → 1 . So it is Lipschitz continuous on the closed unit interval.

Proposition 5.4 (Maximal POWER) . POWER D bound ( s, γ ) ≤ E R ∼D bound [ max s ∈S R ( s ) ] , with equality if s can deterministically reach all states in one step and all states are 1-cycles.

Proof. Let γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

Equation (103) follows from lemma E.38. Equation (104) follows because V ∗ R ( s ′ , γ ) ≤ max s ′′ ∈S R ( s ′′ ) 1 -γ , as no policy can do better than achieving maximal reward at each time step. Taking limits, the inequality holds for all γ ∈ [0 , 1] .

Suppose that s can deterministically reach all states in one step and all states are 1-cycles. Then eq. (104) is an equality for all γ ∈ (0 , 1) , since for each R , the agent can select an action which

deterministically transitions to a state with maximal reward. Thus the equality holds for all γ ∈ [0 , 1] .

Lemma E.41 (Lower bound on current POWER based on future POWER) .

<!-- formula-not-decoded -->

Proof. Let γ ∈ (0 , 1) and let a ∗ ∈ arg max a E s ′ ∼ T ( s,a ) [ POWER D bound ( s ′ , γ ) ] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (108) holds by lemma E.38. Equation (109) follows because E x ∼ X [ max a f ( a, x ) ] ≥ max a E x ∼ X [ f ( a, x ) ] by Jensen's inequality, and eq. (111) follows by lemma E.38.

The inequality also holds when we take the limits γ → 0 or γ → 1 .

Proposition 5.5 (POWER is smooth across reversible dynamics) . Let D bound be bounded [ b, c ] . Suppose s and s ′ can both reach each other in one step with probability 1.

<!-- formula-not-decoded -->

Proof. Suppose γ ∈ [0 , 1] . First consider the case where POWER D bound ( s, γ ) ≥ POWER D bound ( s ′ , γ ) .

<!-- formula-not-decoded -->

(114)

<!-- formula-not-decoded -->

Equation (114) follows by lemma E.41. Equation (115) follows because reward is lower-bounded by b and because s ′ can reach s in one step with probability 1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (116) follows because POWER D bound ( s, γ ) ≥ POWER D bound ( s ′ , γ ) . Equation (117) follows by eq. (115). Equation (119) follows by proposition 5.4. Equation (120) follows because reward under D bound is upper-bounded by c .

The case where POWER D bound ( s, γ ) ≤ POWER D bound ( s ′ , γ ) is similar, leveraging the fact that s can also reach s ′ in one step with probability 1.