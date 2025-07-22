## 3 State visit distribution functions quantify the agent's available options

<!-- image -->

Figure 1: glyph[lscript] ↙ is a 1-cycle, and ∅ is a terminal state. Arrows represent deterministic transitions induced by taking some action a ∈ A . Since the right subgraph contains a copy of the left subgraph, proposition 6.9 will prove that more reward functions have optimal policies which go right than which go left at state glyph[star] , and that such policies seek power-both intuitively, and in a reasonable formal sense.

We clarify the power-seeking discussion by proving what optimal policies usually look like in a given environment. We illustrate our results with a simple case study, before explaining how to reason

about a wide range of MDPs. Appendix D.1 lists MDP theory contributions of independent interest, appendix D lists definitions and theorems, and appendix E contains the proofs.

Definition 3.1 (Rewardless MDP) . 〈S , A , T 〉 is a rewardless MDP with finite state and action spaces S and A , and stochastic transition function T : S × A → ∆( S ) . We treat the discount rate γ as a variable with domain [0 , 1] .

Definition 3.2 (1-cycle states) . Let e s ∈ R |S| be the standard basis vector for state s , such that there is a 1 in the entry for state s and 0 elsewhere. State s is a 1-cycle if ∃ a ∈ A : T ( s, a ) = e s . State s is a terminal state if ∀ a ∈ A : T ( s, a ) = e s .

Our theorems apply to stochastic environments, but we present a deterministic case study for clarity. The environment of fig. 1 is small, but its structure is rich. For example, the agent has more 'options' at glyph[star] than at the terminal state ∅ . Formally, glyph[star] has more visit distribution functions than ∅ does.

Definition 3.3 (State visit distribution [Sutton and Barto, 1998]) . Π := A S , the set of stationary deterministic policies. The visit distribution induced by following policy π from state s at discount rate γ ∈ [0 , 1) is f π,s ( γ ) := ∑ ∞ t =0 γ t E s t ∼ π | s [ e s t ] . f π,s is a visit distribution function ; F ( s ) := { f π,s | π ∈ Π } .

In fig. 1, starting from glyph[lscript] ↙ , the agent can stay at glyph[lscript] ↙ or alternate between glyph[lscript] ↙ and glyph[lscript] ↖ , and so F ( glyph[lscript] ↙ ) = { 1 1 -γ e glyph[lscript] ↙ , 1 1 -γ 2 ( e glyph[lscript] ↙ + γ e glyph[lscript] ↖ ) } . In contrast, at ∅ , all policies π map to visit distribution function 1 1 -γ e ∅ .

Before moving on, we introduce two important concepts used in our main results. First, we sometimes restrict our attention to visit distributions which take certain actions (fig. 2).

<!-- image -->

Figure 2: The subgraph corresponding to F ( glyph[star] | π ( glyph[star] ) = right ) . Some trajectories cannot be strictly optimal for any reward function, and so our results can ignore them. Gray dotted actions are only taken by the policies of dominated f π ∈ F ( glyph[star] ) \ F nd ( glyph[star] ) .

Definition 3.4 ( F single-state restriction) . Considering only visit distribution functions induced by policies taking action a at state s ′ , F ( s | π ( s ′ ) = a ) := { f ∈ F ( s ) | ∃ π ∈ Π : π ( s ′ ) = a, f π,s = f } .

Second, some f ∈ F ( s ) are 'unimportant.' Consider an agent optimizing reward function e r ↘ (1 reward when at r ↘ , 0 otherwise) at e . g . γ = 1 2 . Its optimal policies navigate to r ↘ and stay there. Similarly, for reward function e r ↗ , optimal policies navigate to r ↗ and stay there. However, for no reward function is it uniquely optimal to alternate between r ↗ and r ↘ . Only dominated visit distribution functions alternate between r ↗ and r ↘ (definition 3.6).

Definition 3.5 (Value function) . Let π ∈ Π . For any reward function R ∈ R S over the state space, the on-policy value at state s and discount rate γ ∈ [0 , 1) is V π R ( s, γ ) := f π,s ( γ ) glyph[latticetop] r , where r ∈ R |S| is R expressed as a column vector (one entry per state). The optimal value is V ∗ R ( s, γ ) := max π ∈ Π V π R ( s, γ ) .

Definition 3.6 (Non-domination) .

<!-- formula-not-decoded -->

For any reward function R and discount rate γ , f π ∈ F ( s ) is (weakly) dominated by f π ′ ∈ F ( s ) if V π R ( s, γ ) ≤ V π ′ R ( s, γ ) . f π ∈ F nd ( s ) is non-dominated if there exist R and γ at which f π is not dominated by any other f π ′ .