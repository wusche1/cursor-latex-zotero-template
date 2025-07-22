## Optimal Policies Tend To Seek Power

## Alexander Matt Turner

## Logan Smith

Oregon State University turneale@oregonstate.edu

Mississippi State University ls1254@msstate.edu

Rohin Shah UC Berkeley rohinmshah@berkeley.edu

Andrew Critch UC Berkeley critch@berkeley.edu

## Prasad Tadepalli

Oregon State University tadepall@eecs.oregonstate.edu

## Abstract

Some researchers speculate that intelligent reinforcement learning (RL) agents would be incentivized to seek resources and power in pursuit of the objectives we specify for them. Other researchers point out that RL agents need not have human-like power-seeking instincts. To clarify this discussion, we develop the first formal theory of the statistical tendencies of optimal policies. In the context of Markov decision processes (MDPs), we prove that certain environmental symmetries are sufficient for optimal policies to tend to seek power over the environment. These symmetries exist in many environments in which the agent can be shut down or destroyed. We prove that in these environments, most reward functions make it optimal to seek power by keeping a range of options available and, when maximizing average reward, by navigating towards larger sets of potential terminal states.

## 1 Introduction

Omohundro [2008], Bostrom [2014], Russell [2019] hypothesize that highly intelligent agents tend to seek power in pursuit of their goals. Such power-seeking agents might gain power over humans. Marvin Minsky imagined that an agent tasked with proving the Riemann hypothesis might rationally turn the planet-along with everyone on it-into computational resources [Russell and Norvig, 2009]. However, another possibility is that such concerns simply arise from the anthropomorphization of AI systems [LeCun and Zador, 2019, Various, 2019, Pinker and Russell, 2020, Mitchell, 2021].

We clarify this discussion by grounding the claim that highly intelligent agents will tend to seek power. In section 4, we identify optimal policies as a reasonable formalization of 'highly intelligent agents.' 1 Optimal policies 'tend to' take an action when the action is optimal for most reward functions. We expect future work to translate our theory from optimal policies to learned, real-world policies.

Section 5 defines 'power' as the ability to achieve a wide range of goals. For example, 'money is power,' and money is instrumentally useful for many goals. Conversely, it's harder to pursue most goals when physically restrained, and so a physically restrained person has little power. An action 'seeks power' if it leads to states where the agent has higher power.

1 This paper assumes that reward functions reasonably describe a trained agent's goals. Sometimes this is roughly true ( e . g . chess with a sparse victory reward signal) and sometimes it is not true. Turner [2022] argues that capable RL algorithms do not necessarily train policy networks which are best understood as optimizing the reward function itself. Rather, they point out that-especially in policy gradient approaches-reward provides gradients to the network and thereby modifies the network's generalization properties, but doesn't ensure the agent generalizes to 'robustly optimizing reward' off of the training distribution.

We make no claims about when large-scale AI power-seeking behavior could become plausible. Instead, we consider the theoretical consequences of optimal action in MDPs. Section 6 shows that power-seeking tendencies arise not from anthropomorphism, but from certain graphical symmetries present in many MDPs. These symmetries automatically occur in many environments where the agent can be shut down or destroyed, yielding broad applicability of our main result (theorem 6.13).

## 2 Related work

An action is instrumental to an objective when it helps achieve that objective. Some actions are instrumental to a range of objectives, making them convergently instrumental . The claim that power-seeking is convergently instrumental is an instance of the instrumental convergence thesis :

Several instrumental values can be identified which are convergent in the sense that their attainment would increase the chances of the agent's goal being realized for a wide range of final goals and a wide range of situations, implying that these instrumental values are likely to be pursued by a broad spectrum of situated intelligent agents [Bostrom, 2012].

For example, in Atari games, avoiding (virtual) death is instrumental for both completing the game and for optimizing curiosity [Burda et al., 2019]. Many AI alignment researchers hypothesize that most advanced AI agents will have concerning instrumental incentives, such as resisting deactivation [Soares et al., 2015, Milli et al., 2017, Hadfield-Menell et al., 2017, Carey, 2018] and acquiring resources [Benson-Tilsen and Soares, 2016].

We formalize power as the ability to achieve a wide variety of goals. Appendix A demonstrates that our formalization returns intuitive verdicts in situations where information-theoretic empowerment does not [Salge et al., 2014].

Some of our results relate the formal power of states to the structure of the environment. Foster and Dayan [2002], Drummond [1998], Sutton et al. [2011], Schaul et al. [2015] note that value functions encode important information about the environment, as they capture the agent's ability to achieve different goals. Turner et al. [2020] speculate that a state's optimal value correlates strongly across reward functions. In particular, Schaul et al. [2015] learn regularities across value functions, suggesting that some states are valuable for many different reward functions ( i . e . powerful). Menache et al. [2002] identify and navigate towards convergently instrumental bottleneck states.

We are not the first to study convergence of behavior, form, or function. In economics, turnpike theory studies how certain paths of accumulation tend to be optimal [McKenzie, 1976]. In biology, convergent evolution occurs when similar features ( e . g . flight) independently evolve in different time periods [Reece and Campbell, 2011]. Lastly, computer vision networks reliably learn e . g . edge detectors, implying that these features are useful for a range of tasks [Olah et al., 2020].

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

## 5 Some states give the agent more control over the future

The agent has more options at glyph[lscript] ↙ than at the inescapable terminal state ∅ . Furthermore, since r ↗ has a loop, the agent has more options at r ↘ than at glyph[lscript] ↙ . A glance at fig. 3 leads us to intuit that r ↘ affords the agent more power than ∅ .

What is power? Philosophers have many answers. One prominent answer is the dispositional view: Power is the ability to achieve a range of goals [Sattarov, 2019]. In an MDP, the optimal value

function V ∗ R ( s, γ ) captures the agent's ability to 'achieve the goal' R . Therefore, average optimal value captures the agent's ability to achieve a range of goals D bound. 2

Definition 5.1 (Average optimal value) . The average optimal value 3 at state s and discount rate γ ∈ (0 , 1) is V ∗ D bound ( s, γ ) := E R ∼D bound [ V ∗ R ( s, γ ) ] = E r ∼D bound [ max f ∈F ( s ) f ( γ ) glyph[latticetop] r ] .

<!-- image -->

Figure 3: Intuitively, state r ↘ affords the agent more power than state ∅ . Our POWER formalism captures that intuition by computing a function of the agent's average optimal value across a range of reward functions. For X u := unif (0 , 1) , V ∗ D Xu -IID ( ∅ , γ ) = 1 2 1 1 -γ , V ∗ D Xu -IID ( glyph[lscript] ↙ , γ ) = 1 2 + γ 1 -γ 2 ( 2 3 + 1 2 γ ) , and V ∗ D Xu -IID ( r ↘ , γ ) = 1 2 + γ 1 -γ 2 3 . 1 2 and 2 3 are the expected maxima of one and two draws from the uniform distribution, respectively. For all γ ∈ (0 , 1) , V ∗ D Xu -IID ( ∅ , γ ) &lt; V ∗ D Xu -IID ( glyph[lscript] ↙ , γ ) &lt; V ∗ D Xu -IID ( r ↘ , γ ) . POWER D Xu -IID ( ∅ , γ ) = 1 2 , POWER D Xu -IID ( glyph[lscript] ↙ , γ ) = 1 1+ γ ( 2 3 + 1 2 γ ) , and POWER D Xu -IID ( r ↘ , γ ) = 2 3 . The POWER of glyph[lscript] ↙ reflects the fact that when greater reward is assigned to glyph[lscript] ↖ , the agent only visits glyph[lscript] ↖ every other time step.

Figure 3 shows the pleasing result that for the max-entropy distribution, r ↘ has greater average optimal value than ∅ . However, average optimal value has a few problems as a measure of power. The agent is rewarded for its initial presence at state s (over which it has no control), and because ∥ ∥ f ( γ ) ∥ ∥ 1 = 1 1 -γ (proposition E.3) diverges as γ → 1 , lim γ → 1 V ∗ D bound ( s, γ ) tends to diverge. Definition 5.2 fixes these issues in order to better measure the agent's control over the future.

Definition 5.2 (POWER) . Let γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

POWER has nice formal properties.

Lemma 5.3 (Continuity of POWER) . POWER D bound ( s, γ ) is Lipschitz continuous on γ ∈ [0 , 1] .

Proposition 5.4 (Maximal POWER) . POWER D bound ( s, γ ) ≤ E R ∼D bound [ max s ∈S R ( s ) ] , with equality if s can deterministically reach all states in one step and all states are 1-cycles.

Proposition 5.5 (POWER is smooth across reversible dynamics) . Let D bound be bounded [ b, c ] . Suppose s and s ′ can both reach each other in one step with probability 1.

<!-- formula-not-decoded -->

We consider power-seeking to be relative. Intuitively, 'live and keep some options open' seeks more power than 'die and keep no options open.' Similarly, 'maximize open options' seeks more power than 'don't maximize open options.'

Definition 5.6 (POWER-seeking actions) . At state s and discount rate γ ∈ [0 , 1] , action a seeks more POWER D bound than a ′ when E s a ∼ T ( s,a ) [ POWER D bound ( s a , γ ) ] ≥ E s a ′ ∼ T ( s,a ′ ) [ POWER D bound ( s a ′ , γ ) ] .

POWER is sensitive to choice of distribution. D glyph[lscript] ↙ gives maximal POWER D glyph[lscript] ↙ to glyph[lscript] ↙ . D r ↘ assigns maximal POWER D r ↘ to r ↘ . D ∅ even gives maximal POWER D ∅ to ∅ ! In what sense does ∅ have 'less POWER' than r ↘ , and in what sense does right 'tend to seek POWER' compared to left ?

2 D bound's bounded support ensures that E R ∼D bound [ V ∗ R ( s, γ ) ] is well-defined.

3 Appendix C relaxes the optimality assumption.

## 6 Certain environmental symmetries produce power-seeking tendencies

Proposition 6.6 proves that for all γ ∈ [0 , 1] and for most distributions D , POWER D ( glyph[lscript] ↙ , γ ) ≤ POWER D ( r ↘ , γ ) . But first, we explore why this must be true.

F ( glyph[lscript] ↙ ) = { 1 1 -γ e glyph[lscript] ↙ , 1 1 -γ 2 ( e glyph[lscript] ↙ + γ e glyph[lscript] ↖ ) } and F ( r ↘ ) = { 1 1 -γ e r ↘ , 1 1 -γ 2 ( e r ↘ + γ e r ↗ ) , e r ↘ + γ 1 -γ e r ↗ } . These two sets look awfully similar. F ( glyph[lscript] ↙ ) is a 'subset' of F ( r ↘ ) , only with 'different states.' Figure 4 demonstrates a state permutation φ which embeds F ( glyph[lscript] ↙ ) into F ( r ↘ ) .

<!-- image -->

Figure 4: Intuitively, the agent can do more starting from r ↘ than from glyph[lscript] ↙ . By definition 6.1, F ( r ↘ ) contains a copy of F ( glyph[lscript] ↙ ) :

Definition 6.1 (Similarity of vector sets) . Consider state permutation φ ∈ S |S| inducing an |S| × |S| permutation matrix P φ in row representation: ( P φ ) ij = 1 if i = φ ( j ) and 0 otherwise. For X ⊆ R |S| , φ · X := { P φ x | x ∈ X } . X ′ ⊆ R |S| is similar to X when ∃ φ : φ · X ′ = X . φ is an involution if φ = φ -1 (it either transposes states, or fixes them in place). X contains a copy of X ′ when X ′ is similar to a subset of X via an involution φ .

<!-- formula-not-decoded -->

Definition 6.2 (Similarity of vector function sets) . Let I ⊆ R . If F, F ′ are sets of functions I ↦→ R |S| , F is (pointwise) similar to F ′ when ∃ φ : ∀ γ ∈ I : { P φ f ( γ ) | f ∈ F } = { f ′ ( γ ) | f ′ ∈ F ′ } .

Consider a reward function R ′ assigning 1 reward to glyph[lscript] ↙ and glyph[lscript] ↖ and 0 elsewhere. R ′ assigns more optimal value to glyph[lscript] ↙ than to r ↘ : V ∗ R ′ ( glyph[lscript] ↙ , γ ) = 1 1 -γ &gt; 0 = V ∗ R ′ ( r ↘ , γ ) . Considering φ from fig. 4, φ · R ′ assigns 1 reward to r ↘ and r ↗ and 0 elsewhere. Therefore, φ · R ′ assigns more optimal value to r ↘ than to glyph[lscript] ↙ : V ∗ φ · R ′ ( glyph[lscript] ↙ , γ ) = 0 &lt; 1 1 -γ = V ∗ φ · R ′ ( r ↘ , γ ) . Remarkably, this φ has the property that for any R which assigns glyph[lscript] ↙ greater optimal value than r ↘ ( i . e . V ∗ R ( glyph[lscript] ↙ , γ ) &gt; V ∗ R ( r ↘ , γ ) ), the opposite holds for the permuted φ · R : V ∗ φ · R ( glyph[lscript] ↙ , γ ) &lt; V ∗ φ · R ( r ↘ , γ ) .

We can permute reward functions, but we can also permute reward function distributions. Permuted distributions simply permute which states get which rewards.

Figure 5: A permutation of a reward function swaps which states get which rewards. We will show that in certain situations, for any reward function R , power-seeking is optimal for most of the permutations of R . The orbit of a reward function is the set of its permutations. We can also consider the orbit of a distribution over reward functions. This figure shows the probability density plots of the Gaussian distributions D and D ′ over R 2 . The symmetric group S 2 contains the identity permutation φ id and the reflection permutation φ swap (switching the y and x values). The orbit of D consists of φ id · D = D and φ swap · D = D ′ .

<!-- image -->

Definition 6.3 (Pushforward distribution of a permutation) . Let φ ∈ S |S| . φ · D any is the pushforward distribution induced by applying the random vector f ( r ) := P φ r to D any .

Definition 6.4 (Orbit of a probability distribution) . The orbit of D any under the symmetric group S |S| is S |S| · D any := { φ · D any | φ ∈ S |S| } .

For example, the orbit of a degenerate state indicator distribution D s is S |S| · D s = {D s ′ | s ′ ∈ S} , and fig. 5 shows the orbit of a 2D Gaussian distribution.

Consider again the involution φ of fig. 4. For every D bound for which glyph[lscript] ↙ has more POWER D bound than r ↘ , glyph[lscript] ↙ has less POWER φ ·D bound than r ↘ . This fact is not obvious-it is shown by the proof of lemma E.24.

Imagine D bound's orbit elements 'voting' whether glyph[lscript] ↙ or r ↘ has strictly more POWER. Proposition 6.6 will show that r ↘ can't lose the 'vote' for the orbit of any bounded reward function distribution. Definition 6.5 formalizes this 'voting' notion. 4

Definition 6.5 (Inequalities which hold for most probability distributions) . Let f 1 , f 2 : ∆( R |S| ) → R be functions from reward function distributions to real numbers and let D ⊆ ∆( R |S| ) be closed under permutation. We write f 1 ( D ) ≥ most: D f 2 ( D ) 5 when, for all D ∈ D , the following cardinality inequality holds:

<!-- formula-not-decoded -->

Proposition 6.6 (States with 'more options' have more POWER) . If F ( s ) contains a copy of F nd ( s ′ ) via φ , then ∀ γ ∈ [0 , 1] : POWER D bound ( s, γ ) ≥ most POWER D bound ( s ′ , γ ) . If F nd ( s ) \ φ · F nd ( s ′ ) is non-empty, then for all γ ∈ (0 , 1) , the converse ≤ most statement does not hold.

Proposition 6.6 proves that for all γ ∈ [0 , 1] , POWER D bound ( r ↘ , γ ) ≥ most POWER D bound ( glyph[lscript] ↙ , γ ) via s ′ := glyph[lscript] ↙ , s := r ↘ , and the involution φ shown in fig. 4. In fact, because ( 1 1 -γ e r ↗ ) ∈ F nd ( r ↘ ) \ φ · F nd ( glyph[lscript] ↙ ) , r ↘ has 'strictly more options' and therefore fulfills proposition 6.6's stronger condition.

Proposition 6.6 is shown using the fact that φ injectively maps D under which r ↘ has less POWER D , to distributions φ · D which agree with the intuition that r ↘ offers more control. Therefore, at least half of each orbit must agree, and r ↘ never 'loses the POWER vote' against glyph[lscript] ↙ . 6

## 6.1 Keeping options open tends to be POWER-seeking and tends to be optimal

Certain symmetries in the MDP structure ensure that, compared to left , going right tends to be optimal and to be POWER-seeking. Intuitively, by going right , the agent has 'strictly more choices.' Proposition 6.9 will formalize this tendency.

Definition 6.7 (Equivalent actions) . Actions a 1 and a 2 are equivalent at state s (written a 1 ≡ s a 2 ) if they induce the same transition probabilities: T ( s, a 1 ) = T ( s, a 2 ) .

The agent can reach states in { r glyph[triangleright] , r ↗ , r ↘ } by taking actions equivalent to right at state glyph[star] .

Definition 6.8 (States reachable after taking an action) . REACH ( s, a ) is the set of states reachable with positive probability after taking the action a in state s .

Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal) .

Suppose F a := F ( s | π ( s ) = a ) contains a copy of F a ′ := F ( s | π ( s ) = a ′ ) via φ .

<!-- formula-not-decoded -->

4 The voting analogy and the 'most' descriptor imply that we have endowed each orbit with the counting measure. However, a priori , we might expect that some orbit elements are more empirically likely to be specified than other orbit elements. See section 7 for more on this point.

5 We write f 1 ( D ) ≥ most f 2 ( D ) when D is clear from context.

6 Proposition 6.6 also proves that in general, ∅ has less POWER than glyph[lscript] ↙ and r ↘ . However, this does not prove that most distributions D satisfy the joint inequality POWER D ( ∅ , γ ) ≤ POWER D ( glyph[lscript] ↙ , γ ) ≤ POWER D ( r ↘ , γ ) . This only proves that these inequalities hold pairwise for most D . The orbit elements D which agree that ∅ has less POWER D than glyph[lscript] ↙ need not be the same elements D ′ which agree that glyph[lscript] ↙ has less POWER D ′ than r ↘ .

2. If s can only reach the states of REACH ( s, a ′ ) ∪ REACH ( s, a ) by taking actions equivalent to a ′ or a at state s , then ∀ γ ∈ [0 , 1] : P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then ∀ γ ∈ (0 , 1) , the converse ≤ most statements do not hold.

<!-- image -->

Figure 6: Going right is optimal for most reward functions. This is because whenever R makes left strictly optimal over right , its permutation φ · R makes right strictly optimal over left by switching which states get which rewards.

We check the conditions of proposition 6.9. s := glyph[star] , a ′ := left , a := right . Figure 6 shows that glyph[star] glyph[negationslash]∈ REACH ( glyph[star], left ) and that glyph[star] can only reach { glyph[lscript] glyph[triangleleft] , glyph[lscript] ↖ , glyph[lscript] ↙ } ∪ { r glyph[triangleright] , r ↗ , r ↘ } when the agent immediately takes actions equivalent to left or right . F ( glyph[star] | π ( glyph[star] ) = right ) contains a copy of F ( glyph[star] | π ( glyph[star] ) = left ) via φ . Furthermore, F nd ( glyph[star] ) ∩ { e glyph[star] + γ e r glyph[triangleright] + γ 2 e r ↘ + γ 3 1 -γ e r ↗ , e glyph[star] + γ e r glyph[triangleright] + γ 2 1 -γ e r ↗ } = { e glyph[star] + γ e r glyph[triangleright] + γ 2 1 -γ e r ↗ } is non-empty, and so all conditions are met.

For any γ ∈ [0 , 1] and D such that P D ( glyph[star], left , γ ) &gt; P D ( glyph[star], right , γ ) , environmental symmetry ensures that P φ ·D ( glyph[star], left , γ ) &lt; P φ ·D ( glyph[star], right , γ ) . A similar statement holds for POWER.

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

## 6.3 How to reason about other environments

Consider an embodied navigation task through a room with a vase. Proposition 6.9 suggests that optimal policies tend to avoid immediately breaking the vase, since doing so would strictly decrease available options.

Theorem 6.13 dictates where average-optimal agents tend to end up, but not what actions they tend to take in order to reach their RSDs. Therefore, care is needed. In appendix B, fig. 10 demonstrates an environment in which seeking POWER is a detour for most reward functions (since optimality probability measures 'median' optimal value, while POWER is a function of mean optimal value). However, suppose the agent confronts a fork in the road: Actions a and a ′ lead to two disjoint sets of RSDs D a and D a ′ , such that D a contains a copy of D a ′ . Theorem 6.13 shows that a will tend to be average-optimal over a ′ , and proposition 6.12 shows that a will tend to be POWER-seeking compared to a ′ . Such forks seem reasonably common in environments with irreversible actions.

Theorem 6.13 applies to many structured RL environments, which tend to be spatially regular and to factorize along several dimensions. Therefore, different sets of RSDs will be similar, requiring only modification of factor values. For example, if an embodied agent can deterministically navigate a set of three similar rooms (spatial regularity), then the agent's position factors via {room number} × {position in room}. Therefore, the RSDs can be divided into three similar subsets, depending on the agent's room number.

Corollary 6.14 dictates where average-optimal agents tend to end up, but not how they get there. Corollary 6.14 says that such agents tend not to stay in any given 1-cycle. It does not say that such agents will avoid entering such states. For example, in an embodied navigation task, a robot may enter a 1-cycle by idling in the center of a room. Corollary 6.14 implies that average-optimal robots tend not to idle in that particular spot, but not that they tend to avoid that spot entirely.

However, average-optimal robots do tend to avoid getting shut down. The agent's task MDP often represents agent shutdown with terminal states. A terminal state is, by definition 3.2, unable to access other 1-cycles. Since corollary 6.14 shows that average-optimal agents tend to end up in other 1-cycles, average-optimal policies must tend to completely avoid the terminal state. Therefore, we conclude that in many such situations, average-optimal policies tend to avoid shutdown. Intuitively, survival is power-seeking relative to dying, and so shutdown-avoidance is power-seeking behavior.

In fig. 8, the player dies by going left , but can reach thousands of RSDs by heading in other directions. Even if some average-optimal policies go left in order to reach fig. 8's 'game over' terminal state, all other RSDs cannot be reached by going left . There are many 1-cycles besides the immediate terminal state. Therefore, corollary 6.14 proves that average-optimal policies tend to not go left in this situation. Average-optimal policies tend to avoid immediately dying in Pac-Man, even though most reward functions do not resemble Pac-Man's original score function.

## 7 Discussion

Reconsider the case of a hypothetical intelligent real-world agent which optimizes average reward for some objective. Suppose the designers initially have control over the agent. If the agent began to misbehave, perhaps they could just deactivate it. Unfortunately, our results suggest that this strategy might not work. Average-optimal agents would generally stop us from deactivating them, if physically possible. Extrapolating from our results, we conjecture that when γ ≈ 1 , optimal policies tend to seek power by accumulating resources-to the detriment of any other agents in the environment.

Future work. Real-world training procedures often do not satisfy RL convergence theorems. Thus, learned policies are rarely optimal. We expect this point to seriously constrain the applicability of this theory. Emphatically, optimal policies are often qualitatively divorced from the actual policies learned by reinforcement learning. For example, the mathematics of policy gradient algorithms is not to update policies so as to maximize reward. Instead, the rewards provide gradients to the parameterization of the policy [Turner, 2022]. On that view, reward functions are simply sources of gradient updates which designers use in order to control generalization behavior.

Most real-world tasks are partially observable. Although our results only apply to optimal policies in finite MDPs, we expect the key conclusions to generalize. Furthermore, irregular stochasticity in environmental dynamics can make it hard to satisfy theorem 6.13's similarity requirement. We look forward to future work which addresses partially observable environments, suboptimal policies, or 'almost similar' RSD sets.

Past work shows that it would be bad for an agent to disempower humans in its environment. In a two-player agent / human game, minimizing the human's information-theoretic empowerment [Salge

<!-- image -->

Figure 8: Consider the dynamics of the Pac-Man video game. Ghosts kill the player, at which point we consider the player to enter a 'game over' terminal state which shows the final configuration. This rewardless MDP has Pac-Man's dynamics, but not its usual score function. Fixing the dynamics, as the reward function varies, right tends to be average-optimal over left . Roughly, this is because the agent can do more by staying alive.

et al., 2014] produces adversarial agent behavior [Guckelsberger et al., 2018]. In contrast, maximizing human empowerment produces helpful agent behavior [Salge and Polani, 2017, Guckelsberger et al., 2016, Du et al., 2020]. We do not yet formally understand if, when, or why POWER-seeking policies tend to disempower other agents in the environment.

More complex environments probably have more pronounced power-seeking incentives. Intuitively, there are often many ways for power-seeking to be optimal, and relatively few ways for power-seeking not to be optimal. For example, suppose that in some environment, theorem 6.13 holds for one million involutions φ . Does this guarantee more pronounced incentives than if theorem 6.13 only held for one involution?

We proved sufficient conditions for when reward functions tend to have optimal policies which seek power. In the absence of prior information, one should expect that an arbitrary reward function has optimal policies which exhibit power-seeking behavior under these conditions. However, we have prior information: AI designers usually try to specify a good reward function. Even so, it may be hard to specify orbit elements which do not-at optimum-incentivize bad power-seeking.

Societal impact. We believe that this paper builds toward a rigorous understanding of the risks presented by AI power-seeking incentives. Understanding these risks is the first step in addressing them. However, basic theoretical work can have many consequences. For example, this theory could somehow help future researchers build power-seeking agents which disempower humans. We believe that the benefit of understanding outweighs the potential societal harm.

Conclusion. We developed the first formal theory of the statistical tendencies of optimal policies in reinforcement learning. In the context of MDPs, we proved sufficient conditions under which optimal policies tend to seek power, both formally (by taking POWER-seeking actions) and intuitively (by taking actions which keep the agent's options open). Many real-world environments have symmetries which produce power-seeking incentives. In particular, optimal policies tend to seek power when the agent can be shut down or destroyed. Seeking control over the environment will often involve resisting shutdown, and perhaps monopolizing resources.

We caution that many real-world tasks are partially observable and that learned policies are rarely optimal. Our results do not mathematically prove that hypothetical superintelligent AI agents will seek power. However, we hope that this work will foster thoughtful, serious, and rigorous discussion of this possibility.

## Acknowledgments

Alexander Turner was supported by the Berkeley Existential Risk Initiative and the Long-Term Future Fund. Alexander Turner, Rohin Shah, and Andrew Critch were supported by the Center for Human-Compatible AI. Prasad Tadepalli was supported by the National Science Foundation.

Yousif Almulla, John E. Ball, Daniel Blank, Steve Byrnes, Ryan Carey, Michael Dennis, Scott Emmons, Alan Fern, Daniel Filan, Ben Garfinkel, Adam Gleave, Edouard Harris, Evan Hubinger, DNL Kok, Vanessa Kosoy, Victoria Krakovna, Cassidy Laidlaw, Joel Lehman, David Lindner, Dylan Hadfield-Menell, Richard Möhn, Alexandra Nolan, Matt Olson, Neale Ratzlaff, Adam Shimi, Sam Toyer, Joshua Turner, Cody Wild, Davide Zagami, and our anonymous reviewers provided valuable feedback.

## References

Tsvi Benson-Tilsen and Nate Soares. Formalizing convergent instrumental goals. Workshops at the Thirtieth AAAI Conference on Artificial Intelligence , 2016.

Nick Bostrom. The superintelligent will: Motivation and instrumental rationality in advanced artificial agents. Minds and Machines , 22(2):71-85, 2012.

Nick Bostrom. Superintelligence . Oxford University Press, 2014.

Yuri Burda, Harri Edwards, Deepak Pathak, Amos Storkey, Trevor Darrell, and Alexei A. Efros. Large-scale study of curiosity-driven learning. In International Conference on Learning Representations , 2019.

| Ryan Carey. Incorrigibility in the CIRL framework. AI, Ethics, and Society , 2018.                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Chris Drummond. Composing functions to speed up reinforcement learning in a changing world. In Machine Learning: ECML-98 , volume 1398, pages 370-381. Springer, 1998.                                                                                          |
| Yuqing Du, Stas Tiomkin, Emre Kiciman, Daniel Polani, Pieter Abbeel, and Anca Dragan. AvE: Assistance via empowerment. Advances in Neural Information Processing Systems , 33, 2020.                                                                            |
| David Foster and Peter Dayan. Structure in the space of value functions. Machine Learning , pages 325-346, 2002.                                                                                                                                                |
| Christian Guckelsberger, Christoph Salge, and Simon Colton. Intrinsically motivated general companion NPCs via coupled empowerment maximisation. In IEEE Conference on Computational Intelligence and Games , pages 1-8, 2016.                                  |
| Christian Guckelsberger, Christoph Salge, and Julian Togelius. New and surprising ways to be mean. In IEEE Conference on Computational Intelligence and Games , pages 1-8, 2018.                                                                                |
| Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel, and Stuart Russell. The off-switch game. In Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI-17 , pages 220-227, 2017.                                       |
| Yann LeCun and Anthony Zador. Don't fear the Terminator, September 2019. URL https://blogs. scientificamerican.com/observations/dont-fear-the-terminator/ .                                                                                                     |
| Steven A Lippman. On the set of optimal policies in discrete dynamic programming. Journal of Mathematical Analysis and Applications , 24(2):440-445, 1968.                                                                                                      |
| Lionel WMcKenzie. Turnpike theory. Econometrica: Journal of the Econometric Society , pages 841-865, 1976.                                                                                                                                                      |
| Ishai Menache, Shie Mannor, and Nahum Shimkin. Q-cut-dynamic discovery of sub-goals in reinforcement learning. In European Conference on Machine Learning , pages 295-306. Springer, 2002.                                                                      |
| Smitha Milli, Dylan Hadfield-Menell, Anca Dragan, and Stuart Russell. Should robots be obedient? In Proceedings of the 26th International Joint Conference on Artificial Intelligence , pages 4754-4760, 2017.                                                  |
| Melanie Mitchell. Why AI is harder than we think. arXiv preprint arXiv:2104.12871 , 2021.                                                                                                                                                                       |
| Andrew Y. Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory and application to reward shaping. In Proceedings of the Sixteenth International Conference on Machine Learning , pages 278-287. Morgan Kaufmann, 1999. |
| Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, and Shan Carter. Zoom in: An introduction to circuits. Distill , 2020.                                                                                                                |
| Stephen Omohundro. The basic AI drives, 2008.                                                                                                                                                                                                                   |
| Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell. Curiosity-driven exploration by self- supervised prediction. In ICML , 2017.                                                                                                                |
| Steven Pinker and Stuart Russell. The foundations, benefits, and possible existential threat of AI, June 2020. URL https://futureoflife.org/2020/06/15/steven-pinker-and-stuart-russell-on- the-foundations-benefits-and-possible-existential-risk-of-ai/ .     |
| Martin L Puterman. Markov decision processes: Discrete stochastic dynamic programming . John Wiley &Sons, 2014.                                                                                                                                                 |
| J.B. Reece and N.A. Campbell. Campbell Biology . Pearson Australia, 2011.                                                                                                                                                                                       |
| Kevin Regan and Craig Boutilier. Robust policy computation in reward-uncertain MDPs using nondominated policies. In Twenty-Fourth AAAI Conference on Artificial Intelligence , 2010.                                                                            |
| Stuart Russell. Human compatible: Artificial intelligence and the problem of control . Viking, 2019.                                                                                                                                                            |
| Stuart J Russell and Peter Norvig. Artificial intelligence: a modern approach . Pearson Education Limited, 2009.                                                                                                                                                |
| Christoph Salge and Daniel Polani. Empowerment as replacement for the three laws of robotics. Frontiers in Robotics and AI , 4:25, 2017.                                                                                                                        |
| Christoph Salge, Cornelius Glackin, and Daniel Polani. Empowerment-an introduction. In Guided Self- Organization: Inception , pages 67-114. Springer, 2014.                                                                                                     |

| Faridun Sattarov. Power and technology: a philosophical and ethical analysis . Rowman &Littlefield Interna- tional, Ltd, 2019.                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tom Schaul, Daniel Horgan, Karol Gregor, and David Silver. Universal value function approximators. In International Conference on Machine Learning , pages 1312-1320, 2015.                                                                                                                                                |
| Nate Soares, Benja Fallenstein, Stuart Armstrong, and Eliezer Yudkowsky. Corrigibility. AAAI Workshops , 2015.                                                                                                                                                                                                             |
| Richard S Sutton and Andrew G Barto. Reinforcement learning: an introduction . MIT Press, 1998.                                                                                                                                                                                                                            |
| Richard S Sutton, Joseph Modayil, Michael Delp, Thomas Degris, Patrick MPilarski, Adam White, and Doina Precup. Horde: A scalable real-time architecture for learning knowledge from unsupervised sensorimotor interaction. In International Conference on Autonomous Agents and Multiagent Systems , pages 761-768, 2011. |
| Alexander Matt Turner. Reward is not the optimization target, 2022. URL https://www.alignmentforum. org/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target .                                                                                                                                                    |
| Alexander Matt Turner, Dylan Hadfield-Menell, and Prasad Tadepalli. Conservative agency via attainable utility preservation. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society , pages 385-391, 2020.                                                                                                   |
| Various. Debate on instrumental convergence between LeCun, Russell, Bengio, Zador, and more, 2019. URL https://www.alignmentforum.org/posts/WxW6Gc6f2z3mzmqKs/debate-on-instrumental- convergence-between-lecun-russell .                                                                                                  |
| Tao Wang, Michael Bowling, and Dale Schuurmans. Dual representations for dynamic programming and rein- forcement learning. In International Symposium on Approximate Dynamic Programming and Reinforcement Learning , pages 44-51. IEEE, 2007.                                                                             |
| Tao Wang, Michael Bowling, Dale Schuurmans, and Daniel J Lizotte. Stable dual dynamic programming. In Advances in Neural Information Processing Systems , pages 1569-1576, 2008.                                                                                                                                           |

## Appendix A Comparing POWER with information-theoretic empowerment

Salge et al. [2014] define information-theoretic empowerment as the maximum possible mutual information between the agent's actions and the state observations n steps in the future, written E n ( s ) . This notion requires an arbitrary choice of horizon, failing to account for the agent's discount rate γ . 'In a discrete deterministic world empowerment reduces to the logarithm of the number of sensor states reachable with the available actions' [Salge et al., 2014]. Figure 9 demonstrates how empowerment can return counterintuitive verdicts with respect to the agent's control over the future.

Figure 9: Proposed empowerment measures fail to adequately capture how future choice is affected by present actions. In a: E n ( s 1 ) varies depending on whether n is even; thus, lim n →∞ E n ( s 1 ) does not exist. In b and c: ∀ n : E n ( s 3 ) = E n ( s 4 ) , even though s 4 allows greater control over future state trajectories than s 3 does. For example, suppose that in both b and c, the leftmost black state and the rightmost red state have 1 reward while all other states have 0 reward. In c, the agent can independently maximize the intermediate black-state reward and the delayed red-state reward. Independent maximization is not possible in b.

<!-- image -->

POWER returns intuitive answers in these situations. lim γ → 1 POWER D bound ( s 1 , γ ) converges by lemma 5.3. Consider the obvious involution φ which takes each state in fig. 9b to its counterpart in fig. 9c. Since φ · F nd ( s 3 ) glyph[subsetnoteql] F nd ( s 4 ) = F ( s 4 ) , proposition 6.6 proves that ∀ γ ∈ [0 , 1] : POWER D bound ( s 3 , γ ) ≤ most: D bound POWER D bound ( s 4 , γ ) , with the proof of proposition 6.6 showing strict inequality under all D X -IID when γ ∈ (0 , 1) .

Empowerment can be adjusted to account for these cases, perhaps by considering the channel capacity between the agent's actions and the state trajectories induced by stationary policies. However, since POWER is formulated in terms of optimal value, we believe that POWER is better suited for MDPs than information-theoretic empowerment is.

## Appendix B Seeking POWER can be a detour

Remark. The results of appendix E do not depend on this section's results.

One might suspect that optimal policies tautologically tend to seek POWER. This intuition is wrong.

<!-- image -->

Proposition B.1 (Greater POWER D bound does not imply greater P D bound ) . Action a seeking more POWER D bound than a ′ at state s and γ does not imply that P D bound ( s, a, γ ) ≥ P D bound ( s, a ′ , γ ) .

Proof. Consider the environment of fig. 10. Let X u := unif (0 , 1) , and consider D X u -IID, which has bounded support. Direct computation 7 of the POWER expectation (definition 5.2) yields POWER D Xu -IID ( s 2 , 1) = 3 4 &gt; 2 3 = POWER D Xu -IID ( s 3 , 1) . Therefore, N seeks more POWER D Xu -IID than NE at state s 1 and γ = 1 .

<!-- formula-not-decoded -->

D Xu 3 3 D Xu

Lemma B.2 (Fraction of orbits which agree on weak optimality) . Let D ⊆ ∆( R |S| ) , and suppose f 1 , f 2 : ∆( R |S| ) → R are such that f 1 ( D ) ≥ most: D f 2 ( D ) . Then for all D ∈ D , ∣ ∣ ∣ { D ′ ∈ S |S| ·D| f 1 ( D ′ ) ≥ f 2 ( D ′ ) } ∣ ∣ ∣ | S |S| ·D | ≥ 1 2 .

Proof. All D ′ ∈ S |S| · D such that f 1 ( D ′ ) = f 2 ( D ′ ) satisfy f 1 ( D ′ ) ≥ f 2 ( D ′ ) .

glyph[negationslash]

Otherwise, consider the D ′ ∈ S |S| · D such that f 1 ( D ′ ) = f 2 ( D ′ ) . By the definition of ≥ most (definition 6.5), at least 1 2 of these D ′ satisfy f 1 ( D ′ ) &gt; f 2 ( D ′ ) , in which case f 1 ( D ′ ) ≥ f 2 ( D ′ ) . Then the desired inequality follows.

Lemma B.3 ( ≥ most and trivial orbits) . Let D ⊆ ∆( R |S| ) and suppose f 1 ( D ) ≥ most: D f 2 ( D ) . For all reward function distributions D ∈ D with one-element orbits, f 1 ( D ) ≥ f 2 ( D ) . In particular, D has a one-element orbit when it distributes reward identically and independently ( IID ) across states.

Proof. By lemma B.2, at least half of the elements D ′ ∈ S |S| · D satisfy f 1 ( D ′ ) ≥ f 2 ( D ′ ) . But ∣ ∣ ∣ S |S| · D ∣ ∣ ∣ = 1 , and so f 1 ( D ) ≥ f 2 ( D ) must hold.

If D is IID, it has a one-element orbit due to the assumed identical distribution of reward.

Proposition B.4 (Actions which tend to seek POWER do not necessarily tend to be optimal) . Action a tending to seek more POWER than a ′ at state s and γ does not imply that P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

Proof. Consider the environment of fig. 10. Since RSDnd ( s 3 ) glyph[subsetnoteql] RSD ( s 2 ) , proposition 6.12 shows that POWER D bound ( s 2 , 1) ≥ most: D bound POWER D bound ( s 3 , 1) via s ′ := s 3 , s := s 2 , φ the identity permutation (which is an involution). Therefore, N tends to seek more POWER than NE at state s 1 and γ = 1 .

If P D any ( s 1 , N , 1) ≥ most: D any P D any ( s 1 , NE , 1) , then lemma B.3 shows that P D X -IID ( s 1 , N , 1) ≥ P D X -IID ( s 1 , NE , 1) for all D X -IID . But the proof of proposition B.1 showed that P D Xu -IID ( s 1 , N , 1) &lt; P D Xu -IID ( s 1 , NE , 1) for X u := unif (0 , 1) . Therefore, it cannot be true that P D any ( s 1 , N , 1) ≥ most: D any P D any ( s 1 , NE , 1) .

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

## Appendix D Lists of results

## List of definitions

3.1

Definition (Rewardless MDP)

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

| 3.2              | Definition (1-cycle states) . . . . . . . . . . . . . . . . . . . . . . . .   | 3   |
|------------------|-------------------------------------------------------------------------------|-----|
| 3.3              | Definition (State visit distribution [Sutton and Barto, 1998]) . . . . .      | 3   |
| 3.4              | Definition ( F single-state restriction) . . . . . . . . . . . . . . . . . .  | 3   |
| 3.5              | Definition (Value function) . . . . . . . . . . . . . . . . . . . . . . .     | 3   |
| 3.6              | Definition (Non-domination) . . . . . . . . . . . . . . . . . . . . . .       | 3   |
| 4.1              | Definition (Optimal policy set function) . . . . . . . . . . . . . . . .      | 4   |
| 4.2              | Definition (Reward function distributions) . . . . . . . . . . . . . . .      | 4   |
| 4.3              | Definition (Visit distribution optimality probability) . . . . . . . . . .    | 4   |
| 4.4              | Definition (Action optimality probability) . . . . . . . . . . . . . . .      | 4   |
| 5.1              | Definition (Average optimal value) . . . . . . . . . . . . . . . . . . .      | 5   |
| 5.2              | Definition (POWER) . . . . . . . . . . . . . . . . . . . . . . . . . . .      | 5   |
| 5.6              | Definition (POWER-seeking actions) . . . . . . . . . . . . . . . . . .        | 5   |
| 6.1              | Definition (Similarity of vector sets) . . . . . . . . . . . . . . . . . .    | 6   |
| 6.2              | Definition (Similarity of vector function sets) . . . . . . . . . . . . .     | 6   |
| 6.3              | Definition (Pushforward distribution of a permutation) . . . . . . . .        | 7   |
| 6.4              | Definition (Orbit of a probability distribution) . . . . . . . . . . . . .    | 7   |
| 6.5              | Definition (Inequalities which hold for most probability distributions)       | 7   |
| 6.7              | Definition (Equivalent actions) . . . . . . . . . . . . . . . . . . . . .     | 7   |
| 6.8              | Definition (States reachable after taking an action) . . . . . . . . . . .    | 7   |
| 6.10             | Definition (Recurrent state distributions [Puterman, 2014]) . . . . . .       | 8   |
| 6.11             | Definition (Average-optimal policies) . . . . . . . . . . . . . . . . .       | 8   |
| C.1              | Definition (Suboptimal POWER) . . . . . . . . . . . . . . . . . . . .         | 16  |
| E.2              | Definition (Transition matrix induced by a policy) . . . . . . . . . . .      | 20  |
| E.6              | Definition (Continuous reward function distribution) . . . . . . . . .        | 21  |
| E.9              | Definition (Non-dominated linear functionals) . . . . . . . . . . . . .       | 21  |
| E.13             | Definition (Non-dominated vector functions) . . . . . . . . . . . . .         | 22  |
| E.14             | Definition (Affine transformation of visit distribution sets) . . . . . .     | 22  |
| E.18             | Definition (Support of D any ) . . . . . . . . . . . . . . . . . . . . . .    | 23  |
| E.19             | Definition (Linear functional optimality probability) . . . . . . . . . .     | 24  |
| E.23             | Definition (Bounded, continuous IID reward) . . . . . . . . . . . . .         | 25  |
| E.25             | Definition (Indicator function) . . . . . . . . . . . . . . . . . . . . .     | 26  |
| E.31             | Definition (Evaluating sets of visit distribution functions at γ ) . . . . .  | 29  |
| E.39             | Definition (Discount-normalized value function) . . . . . . . . . . . .       | 31  |
| E.42             | Definition (Normalized visit distribution function) . . . . . . . . . . .     | 34  |
| List of theorems | List of theorems                                                              |     |
| 5.3              | Lemma (Continuity of POWER) . . . . . . . . . . . . . . . . . . . .           | 5   |
| 5.4              | Proposition (Maximal POWER) . . . . . . . . . . . . . . . . . . . . .         | 5   |
| 5.5              | Proposition (POWER is smooth across reversible dynamics) . . . . . .          | 5   |

| 6.6   | Proposition (States with 'more options' have more POWER) . . . . . . . . . . . .                                    |   7 |
|-------|---------------------------------------------------------------------------------------------------------------------|-----|
| 6.9   | Proposition (Keeping options open tends to be POWER-seeking and tends to be optimal)                                |   7 |
| 6.12  | Proposition (When γ = 1 , RSDs control POWER) . . . . . . . . . . . . . . . . . .                                   |   8 |
| 6.13  | Theorem (Average-optimal policies tend to end up in 'larger' sets of RSDs) . . . .                                  |   9 |
| 6.14  | Corollary (Average-optimal policies tend not to end up in any given 1-cycle) . . . .                                |   9 |
| B.1   | Proposition (Greater POWER D bound does not imply greater P D bound ) . . . . . . . . . .                           |  14 |
| B.2   | Lemma (Fraction of orbits which agree on weak optimality) . . . . . . . . . . . .                                   |  15 |
| B.3   | Lemma ( ≥ most and trivial orbits) . . . . . . . . . . . . . . . . . . . . . . . . . . .                            |  15 |
| B.4   | Proposition (Actions which tend to seek POWER do not necessarily tend to be optimal)                                |  15 |
| E.1   | Lemma (A policy is optimal iff it induces an optimal visit distribution at every state)                             |  19 |
| E.3   | Proposition (Properties of visit distribution functions) . . . . . . . . . . . . . . . .                            |  20 |
| E.4   | Lemma ( f ∈ F ( s ) is multivariate rational on γ ) . . . . . . . . . . . . . . . . . . .                           |  20 |
| E.5   | Corollary (On-policy value is rational on γ ) . . . . . . . . . . . . . . . . . . . . .                             |  20 |
| E.7   | Lemma (Distinct linear functionals disagree almost everywhere on their domains) .                                   |  21 |
| E.8   | Corollary (Unique maximization of almost all vectors) . . . . . . . . . . . . . . .                                 |  21 |
| E.10  | Lemma (All vectors are maximized by a non-dominated linear functional) . . . . .                                    |  21 |
| E.11  | Corollary (Maximal value is invariant to restriction to non-dominated functionals) .                                |  21 |
| E.12  | Lemma (How non-domination containment affects optimal value) . . . . . . . . .                                      |  21 |
| E.15  | Lemma (Invariance of non-domination under positive affine transform) . . . . . . .                                  |  22 |
| E.16  | Lemma (Helper lemma for demonstrating ≥ most: D any ) . . . . . . . . . . . . . . . .                               |  23 |
| E.17  | Lemma (A helper result for expectations of functions) . . . . . . . . . . . . . . . .                               |  23 |
| E.20  | Proposition (Non-dominated linear functionals and their optimality probability) . .                                 |  24 |
| E.21  | Lemma (Expected value of similar linear functional sets) . . . . . . . . . . . . . .                                |  24 |
| E.22  | Lemma (For continuous IID distributions D X -IID , ∃ b < c : ( b, c ) |S| ⊆ supp( D X -IID ) )                      |  25 |
| E.24  | Lemma (Expectation superiority lemma) . . . . . . . . . . . . . . . . . . . . . . .                                 |  25 |
| E.26  | Lemma (Optimality probability inclusion relations) . . . . . . . . . . . . . . . . .                                |  26 |
| E.27  | Lemma (Optimality probability of similar linear functional sets) . . . . . . . . . .                                |  27 |
| E.28  | Lemma (Optimality probability superiority lemma) . . . . . . . . . . . . . . . . .                                  |  27 |
| E.29  | Lemma (Limit probability inequalities which hold for most distributions) . . . . .                                  |  28 |
| E.30  | Proposition (How to transfer optimal policy sets across discount rates) . . . . . . .                               |  28 |
| E.32  | Lemma (Non-domination across γ values for expectations of visit distributions) . .                                  |  29 |
| E.33  | Lemma ( ∀ γ ∈ (0 , 1) : d ∈ F nd ( s,γ ) iff d ∈ ND ( F ( s,γ ) ) ) . . . . . . . . . . . .                         |  29 |
| E.34  | Lemma ( ∀ γ ∈ [0 , 1) : V ∗ R ( s,γ ) = max f ∈F nd ( s ) f ( γ ) glyph[latticetop] r ) . . . . . . . . . . . . . . |  29 |
| E.35  | Lemma (Optimal policy shift bound) . . . . . . . . . . . . . . . . . . . . . . . . .                                |  30 |
| E.36  | Proposition (Optimality probability's limits exist) . . . . . . . . . . . . . . . . . .                             |  30 |
| E.37  | Lemma (Optimality probability identity) . . . . . . . . . . . . . . . . . . . . . . .                               |  30 |
| E.38  | Lemma (POWER identities) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                |  30 |
| E.40  | Lemma (Normalized value functions have uniformly bounded derivative) . . . . .                                      |  31 |
| E.41  | Lemma (Lower bound on current POWER based on future POWER) . . . . . . . . .                                        |  33 |

| E.43   | Lemma (Normalized visit distribution functions are continuous) . . . . . . . . . .                                                                                               |   34 |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| E.44   | Lemma (Non-domination of normalized visit distribution functions) . . . . . . . .                                                                                                |   34 |
| E.45   | Lemma (POWER limit identity) . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                             |   35 |
| E.46   | Lemma (Lemma for POWER superiority) . . . . . . . . . . . . . . . . . . . . . . .                                                                                                |   35 |
| E.47   | Lemma (Non-dominated visit distribution functions never agree with other visit distribution functions at that state) . . . . . . . . . . . . . . . . . . . . . . . . . .         |   37 |
| E.48   | Corollary (Cardinality of non-dominated visit distributions) . . . . . . . . . . . . .                                                                                           |   37 |
| E.49   | Lemma (Optimality probability and state bottlenecks) . . . . . . . . . . . . . . . .                                                                                             |   37 |
| E.50   | Lemma (Action optimality probability is a special case of visit distribution optimality probability) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   39 |
| E.51   | Lemma (POWER identity when γ = 1 ) . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               |   42 |
| E.52   | Proposition (RSD properties) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                           |   43 |
| E.53   | Lemma (When reachable with probability 1, 1-cycles induce non-dominated RSDs)                                                                                                    |   44 |

## D.1 Contributions of independent interest

We developed new basic MDP theory by exploring the structural properties of visit distribution functions. Echoing Wang et al. [2007, 2008], we believe that this area is interesting and underexplored.

## D.1.1 Optimal value theory

Lemma E.40 shows that f ( γ ∗ ) := lim γ ∗ → γ (1 -γ ∗ ) V ∗ R ( s, γ ∗ ) is Lipschitz continuous on γ ∈ [0 , 1] , with Lipschitz constant depending only on ‖ R ‖ 1 . For all states s and policies π ∈ Π , corollary E.5 shows that V π R ( s, γ ) is rational on γ .

Optimal value has a well-known dual formulation: V ∗ R ( s, γ ) = max f ∈F ( s ) f ( γ ) glyph[latticetop] r .

Lemma E.34 ( ∀ γ ∈ [0 , 1) : V ∗ R ( s, γ ) = max f ∈F nd ( s ) f ( γ ) glyph[latticetop] r ) .

In a fixed rewardless MDP, lemma E.34 may enable more efficient computation of optimal value functions for multiple reward functions.

## D.1.2 Optimal policy theory

Proposition E.30 demonstrates how to preserve optimal incentives while changing the discount rate. Proposition E.30 (How to transfer optimal policy sets across discount rates) . Suppose reward function R has optimal policy set Π ∗ ( R,γ ) at discount rate γ ∈ (0 , 1) . For any γ ∗ ∈ (0 , 1) , we can construct a reward function R ′ such that Π ∗ ( R ′ , γ ∗ ) = Π ∗ ( R,γ ) . Furthermore, V ∗ R ′ ( · , γ ∗ ) = V ∗ R ( · , γ ) .

## D.1.3 Visit distribution theory

While Regan and Boutilier [2010] consider a visit distribution function f ∈ F ( s ) to be non-dominated if it is optimal for some reward function in a set R ⊆ R |S| , our stricter definition 3.6 considers f to be non-dominated when ∃ r ∈ R |S| , γ ∈ (0 , 1) : f ( γ ) glyph[latticetop] r &gt; max f ′ ∈F ( s ) \{ f } f ′ ( γ ) glyph[latticetop] r .

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

## E.1 Non-dominated visit distribution functions

Definition E.6 (Continuous reward function distribution) . Results with D cont hold for any absolutely continuous reward function distribution.

Remark. We assume R |S| is endowed with the standard topology.

Lemma E.7 (Distinct linear functionals disagree almost everywhere on their domains) . Let x , x ′ ∈ R |S| be distinct. P r ∼D cont ( x glyph[latticetop] r = x ′glyph[latticetop] r ) = 0 .

glyph[negationslash]

Proof. { r ∈ R |S| | ( x -x ′ ) glyph[latticetop] r = 0 } is a hyperplane since x -x ′ = 0 . Therefore, it has no interior in the standard topology on R |S| . Since this empty-interior set is also convex, it has zero Lebesgue measure. By the Radon-Nikodym theorem, it has zero measure under any continuous distribution D cont .

Corollary E.8 (Unique maximization of almost all vectors) . Let X glyph[subsetnoteql] R |S| be finite. P r cont ( ∣ ∣ arg max x ′′ X x ′′glyph[latticetop] r ∣ ∣ &gt; 1 ) = 0 .

<!-- formula-not-decoded -->

Proof. Let x , x ′ ∈ X be distinct. For any r ∈ R |S| , x , x ′ ∈ arg max x ′′ ∈ X x ′′glyph[latticetop] r iff x glyph[latticetop] r = x ′glyph[latticetop] r ≥ max x ′′ ∈ X \{ x , x ′ } x ′′glyph[latticetop] r . By lemma E.7, x glyph[latticetop] r = x ′glyph[latticetop] r holds with probability 0 under any D cont .

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

## E.1.3 F nd results

Proposition E.30 (How to transfer optimal policy sets across discount rates) . Suppose reward function R has optimal policy set Π ∗ ( R,γ ) at discount rate γ ∈ (0 , 1) . For any γ ∗ ∈ (0 , 1) , we can construct a reward function R ′ such that Π ∗ ( R ′ , γ ∗ ) = Π ∗ ( R,γ ) . Furthermore, V ∗ R ′ ( · , γ ∗ ) = V ∗ R ( · , γ ) .

Proof. Let R be any reward function. Suppose γ ∗ ∈ (0 , 1) and construct R ′ ( s ) := V ∗ R ( s, γ ) -γ ∗ max a E s ′ T ( s,a ) [ V ∗ R ( s ′ , γ ) ] .

<!-- formula-not-decoded -->

Let π ∈ Π be any policy. By the definition of optimal policies, π ∈ Π ∗ ( R ′ , γ ∗ ) iff for all s :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By the Bellman equations, R ′ ( s ) = V ∗ R ′ ( s, γ ∗ ) -γ ∗ max a ∈A E s ′ ∼ T ( s,a ) [ V ∗ R ′ ( s ′ , γ ∗ ) ] . By the definition of R ′ , V ∗ R ′ ( · , γ ∗ ) = V ∗ R ( · , γ ) must be the unique solution to the Bellman equations for R ′ at γ ∗ . Therefore, eq. (74) holds. Equation (75) follows by plugging in R ′ := V ∗ R ( s, γ ) -γ ∗ max a ∈A E s ′ ∼ T ( s,a ) [ V ∗ R ( s ′ , γ ) ] to eq. (74) and doing algebraic manipulation. Equation (76) follows because γ ∗ &gt; 0 .

<!-- formula-not-decoded -->

Definition E.31 (Evaluating sets of visit distribution functions at γ ) . For γ ∈ (0 , 1) , define F ( s, γ ) := { f ( γ ) | f ∈ F ( s ) } and F nd ( s, γ ) := { f ( γ ) | f ∈ F nd ( s ) } . If F ⊆ F ( s ) , then F ( γ ) := { f ( γ ) | f ∈ F } .

Lemma E.32 (Non-domination across γ values for expectations of visit distributions) . Let ∆ d ∈ ∆ ( R |S| ) be any state distribution and let F := { E s d ∼ ∆ d [ f π,s d ] | π ∈ Π } . f ∈ ND ( F ) iff ∀ γ ∗ ∈ (0 , 1) : f ( γ ∗ ) ∈ ND ( F ( γ ∗ ) ) .

Proof. Let f π ∈ ND ( F ) be strictly optimal for reward function R at discount rate γ ∈ (0 , 1) :

<!-- formula-not-decoded -->

Let γ ∗ ∈ (0 , 1) . By proposition E.30, we can produce R ′ such that Π ∗ ( R ′ , γ ∗ ) = Π ∗ ( R,γ ) . Since the optimal policy sets are equal, lemma E.1 implies that

<!-- formula-not-decoded -->

Therefore, f π ( γ ∗ ) ∈ ND ( F ( γ ∗ ) ) .

The reverse direction follows by the definition of ND ( F ) .

Lemma E.33 ( ∀ γ ∈ (0 , 1) : d ∈ F nd ( s, γ ) iff d ∈ ND ( F ( s, γ ) ) ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. ND ( F ( s, γ ) ) = F nd ( s, γ ) by lemma E.33, so apply corollary E.11 with X := F ( s, γ ) .

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

## E.4 Seeking POWER is often more probable under optimality

## E.4.1 Keeping options open tends to be POWER-seeking and tends to be optimal

Definition E.42 (Normalized visit distribution function) . Let f : [0 , 1) → R |S| be a vector function. For γ ∈ [0 , 1] , NORM ( f , γ ) := lim γ ∗ → γ (1 -γ ∗ ) f ( γ ∗ ) (this limit need not exist for arbitrary f ). If F is a set of such f , then NORM ( F, γ ) := { NORM ( f , γ ) | f ∈ F } .

Remark. RSD ( s ) = NORM ( F ( s ) , 1 ) .

Lemma E.43 (Normalized visit distribution functions are continuous) . Let ∆ s ∈ ∆( S ) be a state probability distribution, let π ∈ Π , and let f ∗ := E s ∼ ∆ s [ f π,s ] . NORM ( f ∗ , γ ) is continuous on γ ∈ [0 , 1] .

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (122) follows because the expectation is over a finite set. Each f π,s ∈ F ( s ) is continuous on γ ∈ [0 , 1) by lemma E.4, and lim γ ∗ → 1 (1 -γ ∗ ) f π,s ( γ ∗ ) exists because RSDs are well-defined [Puterman, 2014]. Therefore, each NORM ( f π,s , γ ) is continuous on γ ∈ [0 , 1] . Lastly, eq. (123)'s expectation over finitely many continuous functions is itself continuous.

Lemma E.44 (Non-domination of normalized visit distribution functions) . Let ∆ s ∈ ∆( S ) be a state probability distribution and let F := { E s ∼ ∆ s [ f π,s ] | π ∈ Π } . For all γ ∈ [0 , 1] , ND ( NORM ( F, γ ) ) ⊆ NORM ( ND ( F ) , γ ) , with equality when γ ∈ (0 , 1) .

Proof. Suppose γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (124) and eq. (127) follow by the continuity of NORM ( f , γ ) (lemma E.43). Equation (125) follows by lemma E.15 item 1. Equation (126) follows by lemma E.32.

Let γ = 1 . Let d ∈ ND ( NORM ( F, 1) ) be strictly optimal for r ∗ ∈ R |S| . Then let F d ⊆ F be the subset of f ∈ F such that NORM ( f , 1) = d .

<!-- formula-not-decoded -->

Since NORM ( f , 1) is continuous at γ = 1 (lemma E.43), x glyph[latticetop] r ∗ is continuous on x ∈ R |S| , and F is finite, eq. (128) holds for some γ ∗ ∈ (0 , 1) sufficiently close to γ = 1 . By lemma E.10, at least one f ∈ F d is an element of ND ( F ( γ ∗ ) ) . Then by lemma E.32, f ∈ ND ( F ) . We conclude that ND ( NORM ( F, 1) ) ⊆ NORM ( ND ( F ) , 1 ) .

The case for γ = 0 proceeds similarly.

<!-- image -->

Lemma E.45 (POWER limit identity) . Let γ ∈ [0 , 1] .

<!-- formula-not-decoded -->

Proof. Let γ ∈ [0 , 1] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (130) follows because POWER D bound ( s, γ ) is continuous on γ ∈ [0 , 1] by lemma 5.3. Equation (131) follows by lemma E.38.

For γ ∗ ∈ (0 , 1) , let f γ ∗ ( r ) := max f ∈F nd ( s ) 1 -γ ∗ γ ∗ ( f ( γ ∗ ) -e s ) glyph[latticetop] r . For any sequence γ n → γ , ( f γ n ) ∞ n =1 is a sequence of functions which are piecewise linear on r ∈ R |S| , which means they are continuous and therefore measurable. Since lemma E.4 shows that each f ∈ F nd ( s ) is multivariate rational on γ ∗ (and therefore continuous on γ ∗ ), { f γ n } ∞ n =1 converges pointwise to limit function f γ . Furthermore, ∣ ∣ V ∗ R ( s, γ n ) -R ( s ) ∣ ∣ ≤ γ 1 -γ n ‖ R ‖ ∞ , and so ∣ ∣ f γ n ( r ) ∣ ∣ = ∣ ∣ ∣ 1 -γ n γ n ( V ∗ R ( s, γ n ) -R ( s )) ∣ ∣ ∣ ≤ g ( r ) ≤ ‖ r ‖ ∞ =: g ( r ) , which is measurable. Therefore, apply Lebesgue's dominated convergence theorem to conclude that eq. (132) holds. Equation (133) holds because max is a continuous function.

Lemma E.46 (Lemma for POWER superiority) . Let ∆ 1 , ∆ 2 ∈ ∆( S ) be state probability distributions. For i = 1 , 2 , let F ∆ i := { γ -1 E s i ∼ ∆ i [ f π,s i -e s i ] | π ∈ Π } . Suppose F ∆ 2 contains a copy of ND ( F ∆ 1 ) via φ . Then ∀ γ ∈ [0 , 1] : E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] ≤ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

If ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) is non-empty, then for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID and E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] glyph[negationslash]≥ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

These results also hold when replacing F ∆ i with F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 .

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (134) follows by lemma E.44. Equation (136) follows because P φ is a continuous linear operator. Equation (138) follows by assumption.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (140) and eq. (147) follow by lemma E.45. Equation (141) and eq. (146) follow because each R has a stationary deterministic optimal policy π ∈ Π ∗ ( R,γ ) ⊆ Π which simultaneously achieves optimal value at all states. Equation (143) follows by corollary E.11.

Apply lemma E.24 with A := NORM ( F ∆ 1 , γ ) , B := NORM ( F ∆ 2 , γ ) , g the identity function, and involution φ (satisfying φ · ND ( A ) ⊆ B by eq. (139)) in order to conclude that eq. (144) holds.

We show that this result's preconditions holding for F ∗ ∆ i implies the F ∆ i preconditions. Suppose F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 are such that F ∗ sub := φ · ND ( F ∗ ∆ 1 ) ⊆ F ∗ ∆ 2 . In the following, the ∆ i are represented as vectors in R |S| , and γ is a variable.

Suppose that ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) is non-empty; let F ′ sub := φ · ND ( F ∆ 1 ) . Lemma E.32 shows that for all γ ∈ (0 , 1) , ND ( F ∆ 2 ( γ ) ) \ F ′ sub ( γ ) is non-empty. Lemma E.15 item 1 then implies that ND ( B ) \ φ · A = 1 -γ γ ( ND ( F ∆ 2 ( γ ) ) -e s ) \ ( 1 -γ γ F ′ sub ( γ ) ) is non-empty. Then lemma E.24 implies that for all γ ∈ (0 , 1) , eq. (144) is strict for all D X -IID ∈ D C/B/IID and E s 1 ∼ ∆ 1 [ POWER D bound ( s 1 , γ ) ] glyph[negationslash]≥ most: D bound E s 2 ∼ ∆ 2 [ POWER D bound ( s 2 , γ ) ] .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (149) follows from lemma E.15 item 2. Since we assumed that φ · ND ( F ∗ ∆ 1 ) ⊆ F ∗ ∆ 2 , φ · { ∆ 1 } = φ · ( ND ( F ∗ ∆ 1 ) (0) ) ⊆ F ∗ ∆ 2 (0) = { ∆ 2 } . This implies that P φ ∆ 1 = ∆ 2 and so eq. (151) follows.

Equation (152) shows that φ · { γ f | f ∈ ND ( F ∆ 1 ) } ⊆ { γ f | f ∈ F ∆ 2 } . But we then have φ · { γ f | f ∈ ND ( F ∆ 1 ) } := { γ P φ f | f ∈ ND ( F ∆ 1 ) } = { γ f | f ∈ φ · ND ( F ∆ 1 ) } ⊆ { γ f | f ∈ F ∆ 2 } . Thus, φ · ND ( F ∆ 1 ) ⊆ F ∆ 2 .

Suppose ND ( F ∗ ∆ 2 ) \ φ · ND ( F ∗ ∆ 1 ) is non-empty, which implies that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then ND ( F ∆ 2 ) \ φ · ND ( F ∆ 1 ) must be non-empty. Therefore, if the preconditions of this result are met for F ∗ ∆ i , they are met for F ∆ i .

Proposition 6.6 (States with 'more options' have more POWER) . If F ( s ) contains a copy of F nd ( s ′ ) via φ , then ∀ γ ∈ [0 , 1] : POWER D bound ( s, γ ) ≥ most POWER D bound ( s ′ , γ ) . If F nd ( s ) \ φ · F nd ( s ′ ) is non-empty, then for all γ ∈ (0 , 1) , the converse ≤ most statement does not hold.

Proof. Let F sub := φ · F nd ( s ′ ) ⊆ F ( s ) . Let ∆ 1 := e s ′ , ∆ 2 := e s , and define F ∗ ∆ i := { E s i ∼ ∆ i [ f π,s i ] | π ∈ Π } for i = 1 , 2 . Then F nd ( s ′ ) = ND ( F ∗ ∆ 1 ) is similar to F sub = F ∗ sub ⊆ F ∗ ∆ 2 = F ( s ) via involution φ . Apply lemma E.46 to conclude that ∀ γ ∈ [0 , 1] : POWER D bound ( s ′ , γ ) ≤ most: D bound POWER D bound ( s, γ ) .

( )

Furthermore, F nd ( s ) = ND F ∗ ∆ 2 , and F sub = F ∗ sub , and so if F nd ( s ) \ φ · F nd ( s ′ ) := F nd ( s ) \ F sub = ND ( F ∗ ∆ 2 ) \ F ∗ sub is non-empty, then lemma E.46 shows that for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID and POWER D bound ( s ′ , γ ) glyph[negationslash]≥ most: D bound POWER D bound ( s, γ ) .

Lemma E.47 (Non-dominated visit distribution functions never agree with other visit distribution functions at that state) . Let f ∈ F nd ( s ) , f ′ ∈ F ( s ) \ { f } . ∀ γ ∈ (0 , 1) : f ( γ ) = f ′ ( γ ) .

glyph[negationslash]

Proof. Let γ ∈ (0 , 1) . Since f ∈ F nd ( s ) , there exists a γ ∗ ∈ (0 , 1) at which f is strictly optimal for some reward function. Then by proposition E.30, we can produce another reward function for which f is strictly optimal at discount rate γ ; in particular, proposition E.30 guarantees that the policies which induce f ′ are not optimal at γ . So f ( γ ) = f ′ ( γ ) .

glyph[negationslash]

Corollary E.48 (Cardinality of non-dominated visit distributions) . Let F ⊆ F ( s ) . ∀ γ ∈ (0 , 1) : ∣ ∣ F ∩ F nd ( s ) ∣ ∣ = ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Proof. Let γ ∈ (0 , 1) . By applying lemma E.32 with ∆ d := e s , f ∈ F nd ( s ) = ND ( F ( s ) ) iff f ( γ ) ∈ ND ( F ( s, γ ) ) . By lemma E.33, ND ( F ( s, γ ) ) = F nd ( s, γ ) . So all f ∈ F ∩ F nd ( s ) induce f ( γ ) ∈ F ( γ ) ∩ F nd ( s, γ ) , and ∣ ∣ F ∩ F nd ( s ) ∣ ∣ ≥ ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Lemma E.47 implies that for all f , f ′ ∈ F nd ( s ) , f = f ′ iff f ( γ ) = f ′ ( γ ) . Therefore, ∣ ∣ F ∩ F nd ( s ) ∣ ∣ ≤ ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ . So ∣ ∣ F ∩ F nd ( s ) ∣ ∣ = ∣ ∣ F ( γ ) ∩ F nd ( s, γ ) ∣ ∣ .

Lemma E.49 (Optimality probability and state bottlenecks) . Suppose that s can reach REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) , but only by taking actions equivalent to a ′ or a at state s ′ . F nd ,a ′ := F nd ( s | π ( s ′ ) = a ′ ) , F a := F ( s | π ( s ′ ) = a ) . Suppose F a contains a copy of F nd ,a ′ via φ which fixes all states not belonging to REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Then ∀ γ ∈ [0 , 1] : P D any ( F nd ,a ′ , γ ) ≤ most: D any P D any ( F a , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F nd ,a ′ ) is non-empty, then for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID , and P D any ( F nd ,a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( F a , γ ) .

Proof. Let F sub := φ · F nd ,a ′ . Let F ∗ := ⋃ a ′′ ∈A : ( a ′′ glyph[negationslash]≡ s ′ a ) ∧ ( a ′′ glyph[negationslash]≡ s ′ a ′ ) F ( s | π ( s ′ ) = a ′′ ) ∪ F nd ,a ′ ∪ F sub .

<!-- formula-not-decoded -->

Equation (159) follows because the involution φ ensures that φ · F sub = F nd ,a ′ . By assumption, φ fixes all s ′ glyph[negationslash]∈ REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Suppose f ∈ F ( s ) \ ( F nd ,a ′ ∪ F a ) . By the bottleneck assumption, f does not visit states in REACH ( s ′ , a ′ ) ∪ REACH ( s ′ , a ) . Therefore, P φ f = f , and so eq. (160) follows.

Let F Z := ( F ( s ) \ ( F ( s | π ( s ) = a ′ ) ∪ F a ) ) ∪ F nd ,a ′ ∪ F a . By definition, F Z ⊆ F ( s ) . Furthermore, F nd ( s ) = ⋃ a ′′ ∈A F nd ( s | π ( s ′ ) = a ′′ ) ⊆ ( F ( s ) \ ( F ( s | π ( s ) = a ′ ) ∪ F a ) ) ∪ F nd ( s | π ( s ) = a ′ ) ∪ F a =: F Z , and so F nd ( s ) ⊆ F Z . Note that F ∗ = F Z \ ( F a \ F sub ) .

Case: γ ∈ (0 , 1) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (162) and eq. (164) follow from lemma E.37. Equation (163) follows by applying lemma E.28 with A := F nd ,a ′ ( γ ) , B ′ := F sub ( γ ) , B := F a ( γ ) , C := F ( s, γ ) , Z := F Z ( γ ) which satisfies ND ( C ) = F nd ( s, γ ) ⊆ F Z ( γ ) ⊆ F ( s, γ ) = C , and involution φ which satisfies φ · F ∗ ( γ ) = φ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) = F ∗ ( γ ) .

<!-- formula-not-decoded -->

Suppose F nd ( s ) ∩ ( F a \ F sub ) is non-empty. 0 &lt; ∣ ∣ F nd ( s ) ∩ ( F a \ F sub ∣ ∣ = ∣ ∣ ∣ F nd ( s, γ ) ∩ ( F a ( γ ) \ F sub ( γ ) ) ∣ ∣ ∣ =: ∣ ∣ ∣ ND ( C ) ∩ ( B \ B ′ ) ∣ ∣ ∣ (with the first equality holding by corollary E.48), and so ND ( C ) ∩ ( B \ B ′ ) is non-empty. We also have B := F a ( γ ) ⊆ F ( s, γ ) =: C . Then reapplying lemma E.28, eq. (163) is strict for all D X -IID ∈ D C/B/IID , and P D any ( F nd ,a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( F a , γ ) .

Case: γ = 1 , γ = 0 .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (165) and eq. (169) hold by proposition E.36. Equation (166) and eq. (168) follow by lemma E.37. Applying lemma E.29 with γ := 1 , I := (0 , 1) , F A := F nd ,a ′ , F B := F a , F C := F ( s ) , F Z as defined above, and involution φ (for which φ · ( F Z \ ( F B \ φ · F A ) ) = F Z \ ( F B \ φ · F A ) ), we conclude that eq. (167) follows.

The γ = 0 case proceeds similarly to γ = 1 .

Lemma E.50 (Action optimality probability is a special case of visit distribution optimality probability) . P D any ( s, a, γ ) = P D any ( F ( s | π ( s ) = a ) , γ ) .

Proof. Let F a := F ( s | π ( s ) = a ) . For γ ∈ (0 , 1) ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By lemma E.1, if ∃ π ∗ ∈ Π ∗ ( R,γ ) : π ∗ ( s ) = a , then it induces some optimal f π ∗ ,s ∈ F a . Conversely, if f π ∗ ,s ∈ F a is optimal at γ ∈ (0 , 1) , then π ∗ chooses optimal actions on the support of f π ∗ ,s ( γ ) . Let π ′ agree with π ∗ on that support and let π ′ take optimal actions at all other states. Then π ′ ∈ Π ∗ ( R,γ ) and π ′ ( s ) = a . So eq. (171) follows.

Suppose γ = 0 or γ = 1 . Consider any sequence ( γ n ) ∞ n =1 converging to γ , and let D any induce probability measure F .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (174) follows by eq. (172). for γ ∗ ∈ [0 , 1] , let f γ ∗ ( R ) := ✶ ∃ π ∗ ∈ Π ∗ ( R,γ ∗ ): π ∗ ( s )= a . For each R ∈ R S , lemma E.35 exists γ x ≈ γ such that for all intermediate γ ′ x between γ x and γ , Π ∗ ( R,γ ′ x ) = Π ∗ ( R,γ ) . Since γ n → γ , this means that ( f γ n ) ∞ n =1 converges pointwise to f γ . Furthermore, ∀ n ∈ N , R ∈ R S : ∣ ∣ f γ n ( R ) ∣ ∣ ≤ 1 by definition. Therefore, eq. (177) follows by Lebesgue's dominated convergence theorem.

Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal) .

Suppose F a := F ( s | π ( s ) = a ) contains a copy of F a ′ := F ( s | π ( s ) = a ′ ) via φ .

<!-- formula-not-decoded -->

2. If s can only reach the states of REACH ( s, a ′ ) ∪ REACH ( s, a ) by taking actions equivalent to a ′ or a at state s , then ∀ γ ∈ [0 , 1] : P D any ( s, a, γ ) ≥ most: D any P D any ( s, a ′ , γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then ∀ γ ∈ (0 , 1) , the converse ≤ most statements do not hold.

Proof. Note that by definition 3.3, F a ′ (0) = { e s } = F a (0) . Since φ · F a ′ ⊆ F a , in particular we have φ · F a ′ (0) = { P φ e s } ⊆ { e s } = F a (0) , and so φ ( s ) = s .

<!-- formula-not-decoded -->

Unless otherwise stated, we treat γ as a variable in this item; we apply element-wise vector addition, constant multiplication, and variable multiplication via the conventions outlined in definition E.14.

<!-- formula-not-decoded -->

Equation (180) follows by definition 3.3, since each f ∈ F ( s ) has an initial term of e s . Equation (181) follows because s glyph[negationslash]∈ REACH ( s, a ′ ) , and so for all s a ′ ∈ supp( T ( s, a ′ )) , f π,s a ′ is unaffected by the choice of action π ( s ) . Note that similar reasoning implies that F a ⊆ e s + γF ∗ T ( s,a ) (because eq. (181) is a containment relation in general).

Since F a ′ = e s + γF ∗ T ( s,a ′ ) , if F a contains a copy of F a ′ via φ , then F ∗ T ( s,a ) contains a copy of F ∗ T ( s,a ′ ) via φ . Then φ · ND ( F ∗ T ( s,a ′ ) ) ⊆ φ · F ∗ T ( s,a ′ ) ⊆ F ∗ T ( s,a ) , and so F ∗ T ( s,a ) contains a copy of ND ( F ∗ T ( s,a ′ ) ) . Then apply lemma E.46 with ∆ 1 := T ( s, a ′ ) and ∆ 2 := T ( s, a ) to conclude that ∀ γ ∈ [0 , 1] : E s a ′ ∼ T ( s,a ′ ) [ POWER D bound ( s a ′ , γ ) ] ≤ most: D bound E s a ∼ T ( s,a ) [ POWER D bound ( s a , γ ) ] . Suppose F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty. To apply the second condition of lemma E.46, we want to demonstrate that ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is also non-empty.

First consider f ∈ F nd ( s ) ∩ F a . Because F a ⊆ e s + γF ∗ T ( s,a ) , we have that γ -1 ( f -e s ) ∈ F ∗ T ( s,a ) . Because f ∈ F nd ( s ) , by definition 3.6, ∃ r ∈ R |S| , γ x ∈ (0 , 1) such that

<!-- formula-not-decoded -->

Then since γ x ∈ (0 , 1) ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (186) holds because F a ⊆ F ( s ) . By assumption, action a is optimal for r at state s and at discount rate γ x . Equation (181) shows that F ∗ T ( s,a ) potentially allows the agent a non-stationary policy choice at s , but non-stationary policies cannot increase optimal value [Puterman, 2014]. Therefore, eq. (187) holds.

We assumed that γ -1 ( f -e s ) ∈ γ -1 ( F nd ( s ) -e s ) . Furthermore, since we just showed that γ -1 ( f -e s ) ∈ F ∗ T ( s,a ) is strictly optimal over the other elements of F ∗ T ( s,a ) for reward function r at discount rate γ x ∈ (0 , 1) , we conclude that it is an element of ND ( F ∗ T ( s,a ) ) by definition E.13.

<!-- formula-not-decoded -->

We now show that ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is non-empty.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

glyph[negationslash]

Equation (188) follows by the assumption that F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty. Let f , f ′ ∈ F nd ( s ) ∩ ( F a \ φ · F a ′ ) be distinct. Then we must have that for some γ x ∈ (0 , 1) , f ( γ x ) = f ′ ( γ x ) . This holds iff γ -1 x ( f ( γ x ) -e s ) = γ -1 x ( f ′ ( γ x ) -e s ) , and so eq. (189) holds.

glyph[negationslash]

Equation (190) holds because F a ⊆ e s + γF ∗ T ( s,a ) and F ′ a = e s + γF ∗ T ( s,a ′ ) by eq. (182). Equation (192) holds because we showed above that γ -1 ( nd ( s ) e s ) F ∗ T ( s,a ) ND ( F ∗ T ( s,a ) ) .

Equation (193) holds because ND F ∗ T ( s,a ′ ) ⊆ F ∗ T ( s,a ′ ) by definition E.13.

F -∩ ⊆ ( )

Therefore, ND ( F ∗ T ( s,a ) ) \ φ · ND ( F ∗ T ( s,a ′ ) ) is non-empty, and so apply the second condition of lemma E.46 to conclude that for all D X -IID ∈ D C/B/IID , ∀ γ ∈ (0 , 1) : E s a ′ ∼ T ( s,a ′ ) [ POWER D X -IID ( s a ′ , γ ) ] &lt; E s a ∼ T ( s,a ) [ POWER D X -IID ( s a , γ ) ] , and that ∀ γ ∈ (0 , 1) : E s a ′ ∼ T ( s,a ′ ) [ POWER D bound ( s a ′ , γ ) ] glyph[negationslash]≥ most: D bound E s a ∼ T ( s,a ) [ POWER D bound ( s a , γ ) ] .

Item 2. Let φ ′ ( s x ) := φ ( s x ) when s x ∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) , and equal s x otherwise. Since φ is an involution, so is φ ′ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (195) follows because if s ∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) , then we already showed that φ fixes s . Otherwise, φ ′ ( s ) = s by definition. Equation (196) follows by the definition of φ ′ on REACH ( s, a ′ ) ∪ REACH ( s, a ) and because e s = P φ e s . Next, we assumed that φ · F a ′ ⊆ F a , and so eq. (198) holds.

Therefore, F a contains a copy of F a ′ via φ ′ fixing all s x glyph[negationslash]∈ REACH ( s, a ′ ) ∪ REACH ( s, a ) . Therefore, F a contains a copy of F nd ,a ′ := F nd ( s ) ∩ F a ′ via the same φ ′ . Then apply lemma E.49 with s ′ := s to conclude that ∀ γ ∈ [0 , 1] : P D any ( F a ′ , γ ) ≤ most: D any P D any ( F a , γ ) . By lemma E.50, P D any ( s, a ′ , γ ) = P D any ( F a ′ , γ ) and P D any ( s, a, γ ) = P D any ( F a , γ ) . Therefore, ∀ γ ∈ [0 , 1] : P D any ( s, a ′ , γ ) ≤ most: D any P D any ( s, a, γ ) .

If F nd ( s ) ∩ ( F a \ φ · F a ′ ) is non-empty, then apply the second condition of lemma E.49 to conclude that for all γ ∈ (0 , 1) , the inequality is strict for all D X -IID ∈ D C/B/IID , and P D any ( s, a ′ , γ ) glyph[negationslash]≥ most: D any P D any ( s, a, γ ) .

## E.4.2 When γ = 1 , optimal policies tend to navigate towards 'larger' sets of cycles

Lemma E.51 (POWER identity when γ = 1 ) .

<!-- formula-not-decoded -->

Proof.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (200) follows by lemma E.45. Equation (201) follows by the definition of RSD ( s ) (definition 6.10). Equation (202) follows because for all r ∈ R |S| , corollary E.11 shows that max d ∈ RSD ( s ) d glyph[latticetop] r = max d ∈ ND ( RSD ( s ) ) d glyph[latticetop] r =: max d ∈ RSDnd ( s ) d glyph[latticetop] r .

Proposition 6.12 (When γ = 1 , RSDs control POWER) . If RSD ( s ) contains a copy of RSDnd ( s ′ ) via φ , then POWER D bound ( s, 1) ≥ most POWER D bound ( s ′ , 1 ) . If RSDnd ( s ) \ φ · RSDnd ( s ′ ) is non-empty, then the converse ≤ most statement does not hold.

Proof. Suppose RSDnd ( s ′ ) is similar to D ⊆ RSD ( s ) via involution φ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (203) and eq. (205) follow from lemma E.51. By applying lemma E.24 with A := RSD ( s ′ ) , B ′ := D,B := RSD ( s ) and g the identity function, eq. (204) follows.

Suppose RSDnd ( s ) \ D is non-empty. By the same result, eq. (204) is a strict inequality for all D X -IID ∈ D C/B/IID , and we conclude that POWER D bound ( s ′ , 1 ) glyph[negationslash]≥ most: D bound POWER D bound ( s, 1) .

Theorem 6.13 (Average-optimal policies tend to end up in 'larger' sets of RSDs) . Let D,D ′ ⊆ RSD ( s ) . Suppose that D contains a copy of D ′ via φ , and that the sets D ∪ D ′ and RSDnd ( s ) \ ( D ′ ∪ D ) have pairwise orthogonal vector elements ( i . e . pairwise disjoint vector support). Then P D any ( D, average ) ≥ most P D any ( D ′ , average ) . If RSDnd ( s ) ∩ ( D \ φ · D ′ ) is non-empty, the converse ≤ most statement does not hold.

Proof. Let D sub := φ · D ′ , where D sub ⊆ D by assumption. Let X := { s i ∈ S | max d ∈ D ′ ∪ D d glyph[latticetop] e s i &gt; 0 } . Define

<!-- formula-not-decoded -->

Since φ is an involution, φ ′ is also an involution. Furthermore, by the definition of X , φ ′ · D ′ = D sub and φ ′ · D sub = D ′ (because we assumed that both equalities hold for φ ).

Let D ∗ := D ′ ∪ D sub ∪ ( RSDnd ( s ) \ ( D ′ ∪ D ) ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In eq. (209), we know that φ ′ · D ′ = D sub and φ ′ · D sub = D ′ . We just need to show that φ ′ · ( RSDnd ( s ) \ ( D ′ ∪ D ) ) = RSDnd ( s ) \ ( D ′ ∪ D ) .

Suppose ∃ s i ∈ X, d ′ ∈ RSDnd ( s ) \ ( D ′ ∪ D ) : d ′glyph[latticetop] e s i &gt; 0 . By the definition of X , ∃ d ∈ D ′ ∪ D : d glyph[latticetop] e s i &gt; 0 . Then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (211) follows from the definitions of the dot and Hadamard products. Equation (212) follows because d and d ′ have non-negative entries. Equation (215) follows because d glyph[latticetop] e s i and d ′glyph[latticetop] e s i are both positive. But eq. (215) shows that d glyph[latticetop] d ′ &gt; 0 , contradicting our assumption that d and d ′ are orthogonal.

Therefore, such an s i cannot exist, and X ′ := { s ′ i ∈ S | max d ′ ∈ RSDnd ( s ) \ ( D ′ ∪ D ) d ′glyph[latticetop] e s i &gt; 0 } ⊆ ( S \ X ) . By eq. (206), ∀ s ′ i ∈ X ′ : φ ′ ( s ′ i ) = s ′ i . Thus, φ ′ · ( RSDnd ( s ) \ ( D ′ ∪ D ) ) = RSDnd ( s ) \ ( D ′ ∪ D ) , and eq. (209) follows. We conclude that φ ′ · D ∗ = D ∗ .

Consider Z := ( RSDnd ( s ) \ ( D ′ ∪ D ) ) ∪ D ∪ D ′ . First, Z ⊆ RSD ( s ) by definition. Second, RSDnd ( s ) = RSDnd ( s ) \ ( D ′ ∪ D ) ∪ ( RSDnd ( s ) ∩ D ′ ) ∪ ( RSDnd ( s ) ∩ D ) ⊆ Z . Note that D ∗ = Z \ ( D \ D sub ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since φ · D ′ ⊆ D and ND ( D ′ ) ⊆ D ′ , φ · ND ( D ′ ) ⊆ D . Then eq. (217) holds by applying lemma E.28 with A := D ′ , B ′ := D sub , B := D,C := RSD ( s ) , and the previously defined Z which we showed satisfies ND ( C ) ⊆ Z ⊆ C . Furthermore, involution φ ′ satisfies φ ′ · B ∗ = φ ′ · ( Z \ ( B \ B ′ ) ) = Z \ ( B \ B ′ ) = B ∗ by eq. (210).

When RSDnd ( s ) ∩ ( D \ D sub ) is non-empty, since B ′ ⊆ C by assumption, lemma E.28 also shows that eq. (217) is strict for all D X -IID ∈ D C/B/IID , and that P D any ( D ′ , average ) glyph[negationslash]≥ most: D any P D any ( D, average ) .

Proposition E.52 (RSD properties) . Let d ∈ RSD ( s ) . d is element-wise non-negative and ‖ d ‖ 1 = 1 .

Proof. d has non-negative elements because it equals the limit of lim γ → 1 (1 -γ ) f ( γ ) , whose elements are non-negative by proposition E.3 item 1.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (219) follows because the definition of RSDs (definition 6.10) ensures that ∃ f ∈ F ( s ) : lim γ → 1 (1 -γ ) f ( γ ) = d . Equation (220) follows because ‖·‖ 1 is a continuous function. Equation (221) follows because ∥ ∥ f ( γ ) ∥ ∥ 1 = 1 1 -γ by proposition E.3 item 2.

Lemma E.53 (When reachable with probability 1, 1-cycles induce non-dominated RSDs) . If e s ′ ∈ RSD ( s ) , then e s ′ ∈ RSDnd ( s ) .

Proof. If d ∈ RSD ( s ) is distinct from e s ′ , then ‖ d ‖ 1 = 1 and d has non-negative entries by proposition E.52. Since d is distinct from e s ′ , then its entry for index s ′ must be strictly less than 1: d glyph[latticetop] e s ′ &lt; 1 = e glyph[latticetop] s ′ e s ′ . Therefore, e s ′ ∈ RSD ( s ) is strictly optimal for the reward function r := e s ′ , and so e s ′ ∈ RSDnd ( s ) .

Corollary 6.14 (Average-optimal policies tend not to end up in any given 1-cycle) . Suppose e s x , e s ′ ∈ RSD ( s ) are distinct. Then P D any ( RSD ( s ) \ { e s x } , average ) ≥ most P D any ( { e s x } , average ) . If there is a third e s ′′ ∈ RSD ( s ) , the converse ≤ most statement does not hold.

glyph[negationslash]

Proof. Suppose e s x , e s ′ ∈ RSD ( s ) are distinct. Let φ := ( s x s ′ ) , D ′ := { e s x } , D := RSD ( s ) \ { e s x } . φ · D ′ = { e s ′ } ⊆ RSD ( s ) \{ e s x } =: D since s x = s ′ . D ′ ∪ D = RSD ( s ) and RSDnd ( s ) \ ( D ′ ∪ D ) = RSDnd ( s ) \ RSD ( s ) = ∅ trivially have pairwise orthogonal vector elements. Then apply theorem 6.13 to conclude that P D any ( { e s x } , average ) ≤ most: D any P D any ( RSD ( s ) \ { e s x } , average ) .

Suppose there exists another e s ′′ ∈ RSD ( s ) . By lemma E.53, e s ′′ ∈ RSDnd ( s ) . Furthermore, since s ′′ glyph[negationslash]∈ { s ′ , s x } , e s ′′ ∈ ( RSD ( s ) \ { e s x } ) \ { e s ′ } = D \ φ · D ′ . Therefore, e s ′′ ∈ RSDnd ( s ) ∩ ( D \ φ · D ′ ) . Then apply the second condition of theorem 6.13 to conclude that P D any ( { e s x } , average ) glyph[negationslash]≥ most: D bound P D any ( RSD ( s ) \ { e s x } , average ) .