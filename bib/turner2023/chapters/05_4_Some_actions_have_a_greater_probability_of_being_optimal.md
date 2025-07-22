## 4 Some actions have a greater probability of being optimal

We claim that optimal policies 'tend' to take certain actions in certain situations. We first consider the probability that certain actions are optimal.

Reconsider the reward function e r ↘ , optimized at γ = 1 2 . Starting from glyph[star] , the optimal trajectory goes right to r glyph[triangleright] to r ↘ , where the agent remains. The right action is optimal at glyph[star] under these incentives. Optimal policy sets capture the behavior incentivized by a reward function and a discount rate.

Definition 4.1 (Optimal policy set function) . Π ∗ ( R,γ ) is the optimal policy set for reward function R at γ ∈ (0 , 1) . All R have at least one optimal policy π ∈ Π [Puterman, 2014]. Π ∗ ( R, 0) := lim γ → 0 Π ∗ ( R,γ ) and Π ∗ ( R, 1) := lim γ → 1 Π ∗ ( R,γ ) exist by lemma E.35 (taking the limits with respect to the discrete topology over policy sets).

We may be unsure which reward function an agent will optimize. We may expect to deploy a system in a known environment, without knowing the exact form of e . g . the reward shaping [Ng et al., 1999] or intrinsic motivation [Pathak et al., 2017]. Alternatively, one might attempt to reason about future RL agents, whose details are unknown. Our power-seeking results do not hinge on such uncertainty, as they also apply to degenerate distributions ( i . e . we know what reward function will be optimized).

Definition 4.2 (Reward function distributions) . Different results make different distributional assumptions. Results with D any ∈ D any := ∆( R |S| ) hold for any probability distribution over R |S| . D bound is the set of bounded-support probability distributions D bound. For any distribution X over R , D X -IID := X |S| . For example, when X u := unif (0 , 1) , D X u -IID is the maximum-entropy distribution. D s is the degenerate distribution on the state indicator reward function e s , which assigns 1 reward to s and 0 elsewhere.

With D any representing our prior beliefs about the agent's reward function, what behavior should we expect from its optimal policies? Perhaps we want to reason about the probability that it's optimal to go from glyph[star] to ∅ , or to go to r glyph[triangleright] and then stay at r ↗ . In this case, we quantify the optimality probability of F := { e glyph[star] + γ 1 -γ e ∅ , e glyph[star] + γ e r glyph[triangleright] + γ 2 1 -γ e r ↗ } .

Definition 4.3 (Visit distribution optimality probability) . Let F ⊆ F ( s ) , γ ∈ [0 , 1] . P D any ( F, γ ) := P R ∼D any ( ∃ f π ∈ F : π ∈ Π ∗ ( R,γ ) ) .

Alternatively, perhaps we're interested in the probability that right is optimal at glyph[star] .

Definition 4.4 (Action optimality probability) . At discount rate γ and at state s , the optimality probability of action a is P D any ( s, a, γ ) := P R ∼D any ( ∃ π ∗ ∈ Π ∗ ( R,γ ) : π ∗ ( s ) = a ) .

Optimality probability may seem hard to reason about. It's hard enough to compute an optimal policy for a single reward function, let alone for uncountably many! But consider any D X -IID distributing reward independently and identically across states. When γ = 0 , optimal policies greedily maximize next-state reward. At glyph[star] , identically distributed reward means glyph[lscript] glyph[triangleleft] and r glyph[triangleright] have an equal probability of having maximal next-state reward. Therefore, P D X -IID ( glyph[star], left , 0) = P D X -IID ( glyph[star], right , 0) . This is not a proof, but such statements are provable.

With D glyph[lscript] glyph[triangleleft] being the degenerate distribution on reward function e glyph[lscript] glyph[triangleleft] , P D glyph[lscript] glyph[triangleleft] ( glyph[star], left , 1 2 ) = 1 &gt; 0 = P D glyph[lscript] glyph[triangleleft] ( glyph[star], right , 1 2 ) . Similarly, P D rglyph[triangleright] ( glyph[star], left , 1 2 ) = 0 &lt; 1 = P D rglyph[triangleright] ( glyph[star], right , 1 2 ) . Therefore, 'what do optimal policies 'tend' to look like?' seems to depend on one's prior beliefs. But in fig. 1, we claimed that left is optimal for fewer reward functions than right is. The claim is meaningful and true, but we will return to it in section 6.