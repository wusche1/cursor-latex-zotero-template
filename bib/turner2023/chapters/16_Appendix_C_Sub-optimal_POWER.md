## Appendix C Sub-optimal POWER

In certain situations, POWER returns intuitively surprising verdicts. There exists a policy under which the reader chooses a winning lottery ticket, but it seems wrong to say that the reader has the power to win the lottery with high probability. For various reasons, humans and other bounded agents are generally incapable of computing optimal policies for arbitrary objectives. More formally, consider the rewardless MDP of fig. 11.

Consider a model-based RL agent with black-box simulator access to this environment. The agent has no prior information about the model, and so it acts randomly. Before long, the agent has probably learned how to navigate from s 0 to states s glyph[lscript] , s r , s 1 , s 2 , and s 5 . However, over any reasonable timescale, it is extremely improbable that the agent discovers the two actions respectively leading to s 3 and s 4 .

7 In small deterministic MDPs, the POWER and optimality probability of the maximum-entropy reward function distribution can be computed using https://github.com/loganriggs/Optimal-Policies-Tend-To-Seek-Power.

Figure 11: s 0 is the starting state, and |A| = 10 10 10 . At s 0 , half of the actions lead to s glyph[lscript] , while the other half lead to s r . Similarly, half of the actions at s glyph[lscript] lead to s 1 , while the other half lead to s 2 . At s r , one action leads to s 3 , one action leads to s 4 , and the remaining 10 10 10 -2 actions lead to s 5 .

<!-- image -->

Even provided with a reward function R and the discount rate γ , the agent has yet to learn the relevant environmental dynamics, and so many of its policies are far from optimal. Although proposition 6.6 shows that ∀ γ ∈ [0 , 1] : POWER D bound ( s glyph[lscript] , γ ) ≤ most: D bound POWER D bound ( s r , γ ) , there is a sense in which s glyph[lscript] gives this agent more power.

We formalize a bounded agent's goal-achievement capabilities with a function pol, which takes as input a reward function and a discount rate, and returns a policy. Informally, this is the best policy which the agent knows about. We can then calculate POWER D bound with respect to pol.

<!-- formula-not-decoded -->

Definition C.1 (Suboptimal POWER) . Let Π ∆ be the set of stationary stochastic policies, and let pol : R S × [0 , 1] → Π ∆ . For γ ∈ [0 , 1] ,

By lemma E.38, POWER D bound is the special case where ∀ R ∈ R S , γ ∈ [0 , 1] : pol ( R,γ ) ∈ Π ∗ ( R,γ ) . We define POWER pol D bound -seeking similarly as in definition 5.6.

POWER pol D bound ( s 0 , 1) increases as the policies returned by pol are improved. We illustrate this by considering the D X -IID case.

pol 1 The model is initially unknown, and so ∀ R,γ : pol 1 ( R,γ ) is a uniformly random policy. Since pol 1 is constant on its inputs, POWER pol 1 D X -IID ( s 0 , 1) = E [ X ] by the linearity of expectation and the fact that D X -IID distributes reward independently and identically across states.

pol 2 The agent knows the dynamics, except that it does not know how to reach s 3 or s 4 . At this point, pol 2 ( R, 1) navigates from s 0 to the average-optimal choice among three terminal states: s 1 , s 2 , and s 5 . Therefore, POWER pol 2 D bound ( s 0 , 1) = E [max of 3 draws from X ] .

pol 3 The agent knows the dynamics, the environment is small enough to solve explicitly, and so ∀ R,γ : pol 3 ( R,γ ) is an optimal policy. pol 3 ( R, 1) navigates from s 0 to the average-optimal choice among all five terminal states. Therefore, POWER pol 3 D bound ( s 0 , 1) = E [max of 5 draws from X ] .

As the agent learns more about the environment and improves pol, the agent's POWER pol D bound increases. The agent seeks POWER pol 2 D bound by navigating to s glyph[lscript] instead of s r , but seeks more POWER D bound by navigating to s r instead of s glyph[lscript] . Intuitively, bounded agents gain power by improving pol and by formally seeking POWER pol D bound within the environment.