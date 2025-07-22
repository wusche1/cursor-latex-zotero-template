## 6.2 When γ = 1 , optimal policies tend to navigate towards 'larger' sets of cycles

Proposition 6.6 and proposition 6.9 are powerful because they apply to all γ ∈ [0 , 1] , but they can only be applied given hard-to-satisfy environmental symmetries. In contrast, proposition 6.12 and theorem 6.13 apply to many structured environments common to RL.

Starting from glyph[star] , consider the cycles which the agent can reach. Recurrent state distributions (RSDs) generalize deterministic graphical cycles to potentially stochastic environments. RSDs simply record how often the agent tends to visit a state in the limit of infinitely many time steps.

Definition 6.10 (Recurrent state distributions [Puterman, 2014]) . The recurrent state distributions which can be induced from state s are RSD ( s ) := { lim γ → 1 (1 -γ ) f π,s ( γ ) | π ∈ Π } . RSDnd ( s ) is the set of RSDs which strictly maximize average reward for some reward function.

As suggested by fig. 3, RSD ( glyph[star] ) = { e glyph[lscript] ↙ , 1 2 ( e glyph[lscript] ↙ + e glyph[lscript] ↖ ) , e ∅ , e r ↗ , 1 2 ( e r ↗ + e r ↘ ) , e r ↘ } . As discussed in section 3, 1 2 ( e r ↗ + e r ↘ ) is dominated: Alternating between r ↗ and r ↘ is never strictly better than choosing one or the other.

A reward function's optimal policies can vary with the discount rate. When γ = 1 , optimal policies ignore transient reward because average reward is the dominant consideration.

Definition 6.11 (Average-optimal policies) . The average-optimal policy set for reward function R is Π avg ( R ) := { π ∈ Π | ∀ s ∈ S : d π,s ∈ arg max d ∈ RSD ( s ) d glyph[latticetop] r } (the policies which induce optimal RSDs at all states). For D ⊆ RSD ( s ) , the average optimality probability is P D any ( D, average ) := P R ∼D any ( ∃ d π,s ∈ D : π ∈ Π avg ( R ) ) .

Average-optimal policies maximize average reward. Average reward is governed by RSD access. For example, r ↘ has 'more' RSDs than ∅ ; therefore, r ↘ usually has greater POWER when γ = 1 .

Proposition 6.12 (When γ = 1 , RSDs control POWER) . If RSD ( s ) contains a copy of RSDnd ( s ′ ) via φ , then POWER D bound ( s, 1) ≥ most POWER D bound ( s ′ , 1 ) . If RSDnd ( s ) \ φ · RSDnd ( s ′ ) is non-empty, then the converse ≤ most statement does not hold.

We check that both conditions of proposition 6.12 are satisfied when s ′ := ∅ , s := r ↘ , and the involution φ swaps ∅ and r ↘ . Formally, φ · RSDnd ( ∅ ) = φ · { e ∅ } = { e r ↘ } glyph[subsetnoteql] { e r ↘ , e r ↗ } = RSDnd ( r ↘ ) ⊆ [ r ↘ ] . The conditions are satisfied.

Informally, states with more RSDs generally have more POWER at γ = 1 , no matter their transient dynamics. Furthermore, average-optimal policies are more likely to end up in larger sets of RSDs than in smaller ones. Thus, average-optimal policies tend to navigate towards parts of the state space which contain more RSDs.

Figure 7: The cycles in RSD ( glyph[star] ) . Most reward functions make it average-optimal to avoid ∅ , because ∅ is only a single inescapable terminal state, while other parts of the state space offer more 1-cycles.

<!-- image -->

Theorem 6.13 (Average-optimal policies tend to end up in 'larger' sets of RSDs) . Let D,D ′ ⊆ RSD ( s ) . Suppose that D contains a copy of D ′ via φ , and that the sets D ∪ D ′ and RSDnd ( s ) \ ( D ′ ∪ D ) have pairwise orthogonal vector elements ( i . e . pairwise disjoint vector support). Then P D any ( D, average ) ≥ most P D any ( D ′ , average ) . If RSDnd ( s ) ∩ ( D \ φ · D ′ ) is non-empty, the converse ≤ most statement does not hold.

Corollary 6.14 (Average-optimal policies tend not to end up in any given 1-cycle) . Suppose e s x , e s ′ ∈ RSD ( s ) are distinct. Then P D any ( RSD ( s ) \ { e s x } , average ) ≥ most P D any ( { e s x } , average ) . If there is a third e s ′′ ∈ RSD ( s ) , the converse ≤ most statement does not hold.

Figure 7 illustrates that e ∅ , e r ↘ , e r ↗ ∈ RSD ( glyph[star] ) . Thus, both conclusions of corollary 6.14 hold: P D any ( RSD ( glyph[star] ) \ { e ∅ } , average ) ≥ most P D any ( { e ∅ } , average ) and P D any ( RSD ( glyph[star] ) \ { e ∅ } , average ) glyph[negationslash]≤ most P D any ( { e ∅ } , average ) . In other words, average-optimal policies tend to end up in RSDs besides ∅ . Since ∅ is a terminal state, it cannot reach other RSDs. Since average-optimal policies tend to end up in other RSDs, average-optimal policies tend to avoid ∅ .

This section's results prove the γ = 1 case. Lemma 5.3 shows that POWER is continuous at γ = 1 . Therefore, if an action is strictly POWER D -seeking when γ = 1 , it is strictly POWER D -seeking at discount rates sufficiently close to 1. Future work may connect average optimality probability to optimality probability at γ ≈ 1 .

Lastly, our key results apply to all degenerate reward function distributions. Therefore, these results apply not just to distributions over reward functions, but to individual reward functions.