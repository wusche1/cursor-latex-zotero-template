# Full Text: turner2023

Extracted: 2025-07-21 14:03:01
Source: PDF
---

Optimal Policies Tend To Seek Power
Alexander Matt Turner
Oregon State University
turneale@oregonstate.edu
Logan Smith
Mississippi State University
ls1254@msstate.edu
Rohin Shah
UC Berkeley
rohinmshah@berkeley.edu
Andrew Critch
UC Berkeley
critch@berkeley.edu
Prasad Tadepalli
Oregon State University
tadepall@eecs.oregonstate.edu
Abstract
Some researchers speculate that intelligent reinforcement learning (RL) agents
would be incentivized to seek resources and power in pursuit of the objectives
we specify for them. Other researchers point out that RL agents need not have
human-like power-seeking instincts. To clarify this discussion, we develop the ﬁrst
formal theory of the statistical tendencies of optimal policies. In the context of
Markov decision processes (MDPs), we prove that certain environmental symme-
tries are sufﬁcient for optimal policies to tend to seek power over the environment.
These symmetries exist in many environments in which the agent can be shut
down or destroyed. We prove that in these environments, most reward functions
make it optimal to seek power by keeping a range of options available and, when
maximizing average reward, by navigating towards larger sets of potential terminal
states.
1
Introduction
Omohundro [2008], Bostrom [2014], Russell [2019] hypothesize that highly intelligent agents tend
to seek power in pursuit of their goals. Such power-seeking agents might gain power over humans.
Marvin Minsky imagined that an agent tasked with proving the Riemann hypothesis might rationally
turn the planet—along with everyone on it—into computational resources [Russell and Norvig, 2009].
However, another possibility is that such concerns simply arise from the anthropomorphization of AI
systems [LeCun and Zador, 2019, Various, 2019, Pinker and Russell, 2020, Mitchell, 2021].
We clarify this discussion by grounding the claim that highly intelligent agents will tend to seek power.
In section 4, we identify optimal policies as a reasonable formalization of “highly intelligent agents.”1
Optimal policies “tend to” take an action when the action is optimal for most reward functions. We
expect future work to translate our theory from optimal policies to learned, real-world policies.
Section 5 deﬁnes “power” as the ability to achieve a wide range of goals. For example, “money is
power,” and money is instrumentally useful for many goals. Conversely, it’s harder to pursue most
goals when physically restrained, and so a physically restrained person has little power. An action
“seeks power” if it leads to states where the agent has higher power.
1This paper assumes that reward functions reasonably describe a trained agent’s goals. Sometimes this is
roughly true (e.g. chess with a sparse victory reward signal) and sometimes it is not true. Turner [2022] argues
that capable RL algorithms do not necessarily train policy networks which are best understood as optimizing the
reward function itself. Rather, they point out that—especially in policy gradient approaches—reward provides
gradients to the network and thereby modiﬁes the network’s generalization properties, but doesn’t ensure the
agent generalizes to “robustly optimizing reward” off of the training distribution.
35th Conference on Neural Information Processing Systems (NeurIPS 2021).
arXiv:1912.01683v10  [cs.AI]  28 Jan 2023
We make no claims about when large-scale AI power-seeking behavior could become plausible.
Instead, we consider the theoretical consequences of optimal action in MDPs. Section 6 shows that
power-seeking tendencies arise not from anthropomorphism, but from certain graphical symmetries
present in many MDPs. These symmetries automatically occur in many environments where the agent
can be shut down or destroyed, yielding broad applicability of our main result (theorem 6.13).
2
Related work
An action is instrumental to an objective when it helps achieve that objective. Some actions are
instrumental to a range of objectives, making them convergently instrumental. The claim that
power-seeking is convergently instrumental is an instance of the instrumental convergence thesis:
Several instrumental values can be identiﬁed which are convergent in the sense
that their attainment would increase the chances of the agent’s goal being realized
for a wide range of ﬁnal goals and a wide range of situations, implying that
these instrumental values are likely to be pursued by a broad spectrum of situated
intelligent agents [Bostrom, 2012].
For example, in Atari games, avoiding (virtual) death is instrumental for both completing the game
and for optimizing curiosity [Burda et al., 2019]. Many AI alignment researchers hypothesize that
most advanced AI agents will have concerning instrumental incentives, such as resisting deactiva-
tion [Soares et al., 2015, Milli et al., 2017, Hadﬁeld-Menell et al., 2017, Carey, 2018] and acquiring
resources [Benson-Tilsen and Soares, 2016].
We formalize power as the ability to achieve a wide variety of goals. Appendix A demonstrates that
our formalization returns intuitive verdicts in situations where information-theoretic empowerment
does not [Salge et al., 2014].
Some of our results relate the formal power of states to the structure of the environment. Foster
and Dayan [2002], Drummond [1998], Sutton et al. [2011], Schaul et al. [2015] note that value
functions encode important information about the environment, as they capture the agent’s ability to
achieve different goals. Turner et al. [2020] speculate that a state’s optimal value correlates strongly
across reward functions. In particular, Schaul et al. [2015] learn regularities across value functions,
suggesting that some states are valuable for many different reward functions (i.e. powerful). Menache
et al. [2002] identify and navigate towards convergently instrumental bottleneck states.
We are not the ﬁrst to study convergence of behavior, form, or function. In economics, turnpike
theory studies how certain paths of accumulation tend to be optimal [McKenzie, 1976]. In biology,
convergent evolution occurs when similar features (e.g. ﬂight) independently evolve in different
time periods [Reece and Campbell, 2011]. Lastly, computer vision networks reliably learn e.g. edge
detectors, implying that these features are useful for a range of tasks [Olah et al., 2020].
3
State visit distribution functions quantify the agent’s available options
⋆
∅
ℓ◁
left
ℓ↙
ℓ↖
r▷
right
r↘
r↗
Figure 1: ℓ↙is a 1-cycle, and ∅is a terminal state. Arrows represent deterministic transitions induced
by taking some action a ∈A. Since the right subgraph contains a copy of the left subgraph,
proposition 6.9 will prove that more reward functions have optimal policies which go right than
which go left at state ⋆, and that such policies seek power—both intuitively, and in a reasonable
formal sense.
We clarify the power-seeking discussion by proving what optimal policies usually look like in a given
environment. We illustrate our results with a simple case study, before explaining how to reason
2
about a wide range of MDPs. Appendix D.1 lists MDP theory contributions of independent interest,
appendix D lists deﬁnitions and theorems, and appendix E contains the proofs.
Deﬁnition 3.1 (Rewardless MDP). ⟨S, A, T⟩is a rewardless MDP with ﬁnite state and action spaces
S and A, and stochastic transition function T : S × A →∆(S). We treat the discount rate γ as a
variable with domain [0, 1].
Deﬁnition 3.2 (1-cycle states). Let es ∈R|S| be the standard basis vector for state s, such that there
is a 1 in the entry for state s and 0 elsewhere. State s is a 1-cycle if ∃a ∈A : T(s, a) = es. State s is
a terminal state if ∀a ∈A : T(s, a) = es.
Our theorems apply to stochastic environments, but we present a deterministic case study for clarity.
The environment of ﬁg. 1 is small, but its structure is rich. For example, the agent has more “options”
at ⋆than at the terminal state ∅. Formally, ⋆has more visit distribution functions than ∅does.
Deﬁnition 3.3 (State visit distribution [Sutton and Barto, 1998]). Π := AS, the set of stationary
deterministic policies. The visit distribution induced by following policy π from state s at discount
rate γ ∈[0, 1) is f π,s(γ) := P∞
t=0 γt Est∼π|s [est]. f π,s is a visit distribution function; F(s) :=
{f π,s | π ∈Π}.
In ﬁg. 1, starting from ℓ↙, the agent can stay at ℓ↙or alternate between ℓ↙and ℓ↖, and so
F(ℓ↙) = {
1
1−γ eℓ↙,
1
1−γ2 (eℓ↙+ γeℓ↖)}. In contrast, at ∅, all policies π map to visit distribution
function
1
1−γ e∅.
Before moving on, we introduce two important concepts used in our main results. First, we sometimes
restrict our attention to visit distributions which take certain actions (ﬁg. 2).
⋆
r▷
right
r↘
r↗
Figure 2: The subgraph corresponding to F(⋆| π(⋆) = right). Some trajectories cannot be strictly
optimal for any reward function, and so our results can ignore them. Gray dotted actions are only
taken by the policies of dominated f π ∈F(⋆) \ Fnd(⋆).
Deﬁnition 3.4 (F single-state restriction). Considering only visit distribution functions induced by
policies taking action a at state s′, F(s | π(s′) = a) :=

f ∈F(s) | ∃π ∈Π : π(s′) = a, f π,s = f
	
.
Second, some f ∈F(s) are “unimportant.” Consider an agent optimizing reward function er↘(1
reward when at r↘, 0 otherwise) at e.g. γ = 1
2. Its optimal policies navigate to r↘and stay there.
Similarly, for reward function er↗, optimal policies navigate to r↗and stay there. However, for
no reward function is it uniquely optimal to alternate between r↗and r↘. Only dominated visit
distribution functions alternate between r↗and r↘(deﬁnition 3.6).
Deﬁnition 3.5 (Value function). Let π ∈Π. For any reward function R ∈RS over the state
space, the on-policy value at state s and discount rate γ ∈[0, 1) is V π
R (s, γ) := f π,s(γ)⊤r, where
r ∈R|S| is R expressed as a column vector (one entry per state). The optimal value is V ∗
R (s, γ) :=
maxπ∈Π V π
R (s, γ).
Deﬁnition 3.6 (Non-domination).
Fnd(s) := {f π ∈F(s) | ∃r ∈R|S|, γ ∈(0, 1) : f π(γ)⊤r >
max
f π′∈F(s)\{f π} f π′(γ)⊤r}.
(1)
For any reward function R and discount rate γ, f π ∈F(s) is (weakly) dominated by f π′ ∈F(s)
if V π
R (s, γ) ≤V π′
R (s, γ). f π ∈Fnd(s) is non-dominated if there exist R and γ at which f π is not
dominated by any other f π′.
3
4
Some actions have a greater probability of being optimal
We claim that optimal policies “tend” to take certain actions in certain situations. We ﬁrst consider
the probability that certain actions are optimal.
Reconsider the reward function er↘, optimized at γ = 1
2. Starting from ⋆, the optimal trajectory goes
right to r▷to r↘, where the agent remains. The right action is optimal at ⋆under these incentives.
Optimal policy sets capture the behavior incentivized by a reward function and a discount rate.
Deﬁnition 4.1 (Optimal policy set function). Π∗(R, γ) is the optimal policy set for reward function
R at γ ∈(0, 1). All R have at least one optimal policy π ∈Π [Puterman, 2014]. Π∗(R, 0) :=
limγ→0 Π∗(R, γ) and Π∗(R, 1) := limγ→1 Π∗(R, γ) exist by lemma E.35 (taking the limits with
respect to the discrete topology over policy sets).
We may be unsure which reward function an agent will optimize. We may expect to deploy a system
in a known environment, without knowing the exact form of e.g. the reward shaping [Ng et al., 1999]
or intrinsic motivation [Pathak et al., 2017]. Alternatively, one might attempt to reason about future
RL agents, whose details are unknown. Our power-seeking results do not hinge on such uncertainty,
as they also apply to degenerate distributions (i.e. we know what reward function will be optimized).
Deﬁnition 4.2 (Reward function distributions). Different results make different distributional as-
sumptions. Results with Dany ∈Dany := ∆(R|S|) hold for any probability distribution over R|S|.
Dbound is the set of bounded-support probability distributions Dbound. For any distribution X over R,
DX-IID := X|S|. For example, when Xu := unif(0, 1), DXu-IID is the maximum-entropy distribution.
Ds is the degenerate distribution on the state indicator reward function es, which assigns 1 reward to
s and 0 elsewhere.
With Dany representing our prior beliefs about the agent’s reward function, what behavior should we
expect from its optimal policies? Perhaps we want to reason about the probability that it’s optimal to
go from ⋆to ∅, or to go to r▷and then stay at r↗. In this case, we quantify the optimality probability
of F := {e⋆+
γ
1−γ e∅, e⋆+ γer▷+
γ2
1−γ er↗}.
Deﬁnition 4.3 (Visit distribution optimality probability). Let F ⊆F(s), γ ∈[0, 1]. PDany (F, γ) :=
PR∼Dany
 ∃f π ∈F : π ∈Π∗(R, γ)

.
Alternatively, perhaps we’re interested in the probability that right is optimal at ⋆.
Deﬁnition 4.4 (Action optimality probability). At discount rate γ and at state s, the optimality
probability of action a is PDany (s, a, γ) := PR∼Dany
 ∃π∗∈Π∗(R, γ) : π∗(s) = a

.
Optimality probability may seem hard to reason about. It’s hard enough to compute an optimal policy
for a single reward function, let alone for uncountably many! But consider any DX-IID distributing
reward independently and identically across states. When γ = 0, optimal policies greedily maximize
next-state reward. At ⋆, identically distributed reward means ℓ◁and r▷have an equal probability of
having maximal next-state reward. Therefore, PDX-IID (⋆, left, 0) = PDX-IID (⋆, right, 0). This is
not a proof, but such statements are provable.
With Dℓ◁being the degenerate distribution on reward function eℓ◁, PDℓ◁
 ⋆, left, 1
2

= 1 > 0 =
PDℓ◁
 ⋆, right, 1
2

. Similarly, PDr▷
 ⋆, left, 1
2

= 0 < 1 = PDr▷
 ⋆, right, 1
2

. Therefore, “what
do optimal policies ‘tend’ to look like?” seems to depend on one’s prior beliefs. But in ﬁg. 1, we
claimed that left is optimal for fewer reward functions than right is. The claim is meaningful and
true, but we will return to it in section 6.
5
Some states give the agent more control over the future
The agent has more options at ℓ↙than at the inescapable terminal state ∅. Furthermore, since r↗
has a loop, the agent has more options at r↘than at ℓ↙. A glance at ﬁg. 3 leads us to intuit that r↘
affords the agent more power than ∅.
What is power? Philosophers have many answers. One prominent answer is the dispositional view:
Power is the ability to achieve a range of goals [Sattarov, 2019]. In an MDP, the optimal value
4
function V ∗
R (s, γ) captures the agent’s ability to “achieve the goal” R. Therefore, average optimal
value captures the agent’s ability to achieve a range of goals Dbound.2
Deﬁnition 5.1 (Average optimal value). The average optimal value3 at state s and discount rate
γ ∈(0, 1) is V ∗
Dbound (s, γ) := ER∼Dbound

V ∗
R (s, γ)

= Er∼Dbound
h
maxf∈F(s) f(γ)⊤r
i
.
⋆
∅
ℓ◁
left
ℓ↙
ℓ↖
r▷
right
r↘
r↗
Figure 3: Intuitively, state r↘affords the agent more power than state ∅. Our POWER formal-
ism captures that intuition by computing a function of the agent’s average optimal value across
a range of reward functions. For Xu := unif(0, 1), V ∗
DXu-IID(∅, γ) =
1
2
1
1−γ , V ∗
DXu-IID(ℓ↙, γ) =
1
2 +
γ
1−γ2 ( 2
3 + 1
2γ), and V ∗
DXu-IID(r↘, γ) = 1
2 +
γ
1−γ
2
3. 1
2 and 2
3 are the expected maxima of one
and two draws from the uniform distribution, respectively. For all γ ∈(0, 1), V ∗
DXu-IID(∅, γ) <
V ∗
DXu-IID(ℓ↙, γ) < V ∗
DXu-IID(r↘, γ). POWERDXu-IID(∅, γ) = 1
2, POWERDXu-IID(ℓ↙, γ) =
1
1+γ ( 2
3 +
1
2γ), and POWERDXu-IID(r↘, γ) = 2
3. The POWER of ℓ↙reﬂects the fact that when greater reward is
assigned to ℓ↖, the agent only visits ℓ↖every other time step.
Figure 3 shows the pleasing result that for the max-entropy distribution, r↘has greater average
optimal value than ∅. However, average optimal value has a few problems as a measure of power.
The agent is rewarded for its initial presence at state s (over which it has no control), and be-
cause
f(γ)

1 =
1
1−γ (proposition E.3) diverges as γ →1, limγ→1 V ∗
Dbound (s, γ) tends to diverge.
Deﬁnition 5.2 ﬁxes these issues in order to better measure the agent’s control over the future.
Deﬁnition 5.2 (POWER). Let γ ∈(0, 1).
POWERDbound (s, γ) :=
E
r∼Dbound
"
max
f∈F(s)
1 −γ
γ
 f(γ) −es
⊤r
#
= 1 −γ
γ
E
R∼Dbound

V ∗
R (s, γ) −R(s)

.
(2)
POWER has nice formal properties.
Lemma 5.3 (Continuity of POWER). POWERDbound (s, γ) is Lipschitz continuous on γ ∈[0, 1].
Proposition 5.4 (Maximal POWER). POWERDbound (s, γ) ≤ER∼Dbound

maxs∈S R(s)

, with equality
if s can deterministically reach all states in one step and all states are 1-cycles.
Proposition 5.5 (POWER is smooth across reversible dynamics). Let Dbound be bounded [b, c]. Sup-
pose s and s′ can both reach each other in one step with probability 1.
POWERDbound (s, γ) −POWERDbound
 s′, γ
  ≤(c −b)(1 −γ).
(3)
We consider power-seeking to be relative. Intuitively, “live and keep some options open” seeks more
power than “die and keep no options open.” Similarly, “maximize open options” seeks more power
than “don’t maximize open options.”
Deﬁnition 5.6 (POWER-seeking actions). At state s and discount rate γ ∈[0, 1], action a seeks more
POWERDbound than a′ when Esa∼T (s,a)

POWERDbound(sa, γ)

≥Esa′∼T (s,a′)

POWERDbound(sa′, γ)

.
POWER is sensitive to choice of distribution. Dℓ↙gives maximal POWERDℓ↙to ℓ↙. Dr↘assigns
maximal POWERDr↘to r↘. D∅even gives maximal POWERD∅to ∅! In what sense does ∅have
“less POWER” than r↘, and in what sense does right “tend to seek POWER” compared to left?
2Dbound’s bounded support ensures that ER∼Dbound

V ∗
R (s, γ)

is well-deﬁned.
3Appendix C relaxes the optimality assumption.
5
6
Certain environmental symmetries produce power-seeking tendencies
Proposition 6.6 proves that for all γ ∈[0, 1] and for most distributions D, POWERD(ℓ↙, γ) ≤
POWERD(r↘, γ). But ﬁrst, we explore why this must be true.
F(ℓ↙) = {
1
1−γ eℓ↙,
1
1−γ2 (eℓ↙+ γeℓ↖)} and F(r↘) = {
1
1−γ er↘,
1
1−γ2 (er↘+ γer↗), er↘+
γ
1−γ er↗}. These two sets look awfully similar. F(ℓ↙) is a “subset” of F(r↘), only with “different
states.” Figure 4 demonstrates a state permutation φ which embeds F(ℓ↙) into F(r↘).
⋆
∅
ℓ◁
left
ℓ↙
ℓ↖
r▷
right
r↘
r↗
Involution φ
Figure 4: Intuitively, the agent can do more starting from r↘than from ℓ↙. By deﬁnition 6.1, F(r↘)
contains a copy of F(ℓ↙):
φ · F(ℓ↙) := {
1
1−γ Pφeℓ↙,
1
1−γ2 Pφ(eℓ↙+ γeℓ↖)} = {
1
1−γ er↘,
1
1−γ2 (er↘+ γer↗)} ⊊F(r↘).
Deﬁnition 6.1 (Similarity of vector sets). Consider state permutation φ ∈S|S| inducing an |S| × |S|
permutation matrix Pφ in row representation: (Pφ)ij = 1 if i = φ(j) and 0 otherwise. For X ⊆R|S|,
φ · X :=

Pφx | x ∈X
	
. X′ ⊆R|S| is similar to X when ∃φ : φ · X′ = X. φ is an involution if
φ = φ−1 (it either transposes states, or ﬁxes them in place). X contains a copy of X′ when X′ is
similar to a subset of X via an involution φ.
Deﬁnition 6.2 (Similarity of vector function sets). Let I ⊆R. If F, F ′ are sets of functions I 7→R|S|,
F is (pointwise) similar to F ′ when ∃φ : ∀γ ∈I : {Pφf(γ) | f ∈F} = {f ′(γ) | f ′ ∈F ′}.
Consider a reward function R′ assigning 1 reward to ℓ↙and ℓ↖and 0 elsewhere. R′ assigns more
optimal value to ℓ↙than to r↘: V ∗
R′(ℓ↙, γ) =
1
1−γ > 0 = V ∗
R′(r↘, γ). Considering φ from ﬁg. 4,
φ · R′ assigns 1 reward to r↘and r↗and 0 elsewhere. Therefore, φ · R′ assigns more optimal value
to r↘than to ℓ↙: V ∗
φ·R′(ℓ↙, γ) = 0 <
1
1−γ = V ∗
φ·R′(r↘, γ). Remarkably, this φ has the property
that for any R which assigns ℓ↙greater optimal value than r↘(i.e. V ∗
R(ℓ↙, γ) > V ∗
R(r↘, γ)), the
opposite holds for the permuted φ · R: V ∗
φ·R(ℓ↙, γ) < V ∗
φ·R(r↘, γ).
We can permute reward functions, but we can also permute reward function distributions. Permuted
distributions simply permute which states get which rewards.
x
y
D
D′
φswap
Figure 5: A permutation of a reward function swaps which states get which rewards. We will
show that in certain situations, for any reward function R, power-seeking is optimal for most of the
permutations of R. The orbit of a reward function is the set of its permutations. We can also consider
the orbit of a distribution over reward functions. This ﬁgure shows the probability density plots of the
Gaussian distributions D and D′ over R2. The symmetric group S2 contains the identity permutation
φid and the reﬂection permutation φswap (switching the y and x values). The orbit of D consists of
φid · D = D and φswap · D = D′.
6
Deﬁnition 6.3 (Pushforward distribution of a permutation). Let φ ∈S|S|. φ·Dany is the pushforward
distribution induced by applying the random vector f(r) := Pφr to Dany.
Deﬁnition 6.4 (Orbit of a probability distribution). The orbit of Dany under the symmetric group
S|S| is S|S| · Dany := {φ · Dany | φ ∈S|S|}.
For example, the orbit of a degenerate state indicator distribution Ds is S|S| · Ds = {Ds′ | s′ ∈S},
and ﬁg. 5 shows the orbit of a 2D Gaussian distribution.
Consider again the involution φ of ﬁg. 4. For every Dbound for which ℓ↙has more POWERDbound
than r↘, ℓ↙has less POWERφ·Dbound than r↘. This fact is not obvious—it is shown by the proof of
lemma E.24.
Imagine Dbound’s orbit elements “voting” whether ℓ↙or r↘has strictly more POWER. Proposition 6.6
will show that r↘can’t lose the “vote” for the orbit of any bounded reward function distribution.
Deﬁnition 6.5 formalizes this “voting” notion.4
Deﬁnition 6.5 (Inequalities which hold for most probability distributions). Let f1, f2 : ∆(R|S|) →R
be functions from reward function distributions to real numbers and let D ⊆∆(R|S|) be closed
under permutation. We write f1(D) ≥most: D f2(D) 5 when, for all D ∈D, the following cardinality
inequality holds:
{D′ ∈S|S| · D | f1(D′) > f2(D′)}
 ≥
{D′ ∈S|S| · D | f1(D′) < f2(D′)}
 .
(4)
Proposition 6.6 (States with “more options” have more POWER). If F(s) contains a copy of Fnd(s′)
via φ, then ∀γ ∈[0, 1] : POWERDbound(s, γ) ≥most POWERDbound(s′, γ). If Fnd(s) \ φ · Fnd(s′) is
non-empty, then for all γ ∈(0, 1), the converse ≤most statement does not hold.
Proposition 6.6 proves that for all γ ∈[0, 1], POWERDbound(r↘, γ) ≥most POWERDbound(ℓ↙, γ) via
s′ := ℓ↙, s := r↘, and the involution φ shown in ﬁg. 4. In fact, because (
1
1−γ er↗) ∈Fnd(r↘) \ φ ·
Fnd(ℓ↙), r↘has “strictly more options” and therefore fulﬁlls proposition 6.6’s stronger condition.
Proposition 6.6 is shown using the fact that φ injectively maps D under which r↘has less POWERD,
to distributions φ · D which agree with the intuition that r↘offers more control. Therefore, at least
half of each orbit must agree, and r↘never “loses the POWER vote” against ℓ↙.6
6.1
Keeping options open tends to be POWER-seeking and tends to be optimal
Certain symmetries in the MDP structure ensure that, compared to left, going right tends to be
optimal and to be POWER-seeking. Intuitively, by going right, the agent has “strictly more choices.”
Proposition 6.9 will formalize this tendency.
Deﬁnition 6.7 (Equivalent actions). Actions a1 and a2 are equivalent at state s (written a1 ≡s a2) if
they induce the same transition probabilities: T(s, a1) = T(s, a2).
The agent can reach states in {r▷, r↗, r↘} by taking actions equivalent to right at state ⋆.
Deﬁnition 6.8 (States reachable after taking an action). REACH (s, a) is the set of states reachable
with positive probability after taking the action a in state s.
Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal).
Suppose Fa := F(s | π(s) = a) contains a copy of Fa′ := F(s | π(s) = a′) via φ.
1. If s ̸∈REACH
 s, a′
, then ∀γ ∈[0, 1] : Esa∼T (s,a)

POWERDbound (sa, γ)

≥most: Dbound
Esa′∼T (s,a′)

POWERDbound (sa′, γ)

.
4The voting analogy and the “most” descriptor imply that we have endowed each orbit with the counting
measure. However, a priori, we might expect that some orbit elements are more empirically likely to be speciﬁed
than other orbit elements. See section 7 for more on this point.
5We write f1(D) ≥most f2(D) when D is clear from context.
6Proposition 6.6 also proves that in general, ∅has less POWER than ℓ↙and r↘. However, this does not prove
that most distributions D satisfy the joint inequality POWERD(∅, γ) ≤POWERD(ℓ↙, γ) ≤POWERD(r↘, γ).
This only proves that these inequalities hold pairwise for most D. The orbit elements D which agree that ∅has
less POWERD than ℓ↙need not be the same elements D′ which agree that ℓ↙has less POWERD′ than r↘.
7
2. If s can only reach the states of REACH
 s, a′
∪REACH (s, a) by taking actions equivalent
to a′ or a at state s, then ∀γ ∈[0, 1] : PDany (s, a, γ) ≥most: Dany PDany
 s, a′, γ

.
If Fnd(s) ∩
 Fa \ φ · Fa′
is non-empty, then ∀γ ∈(0, 1), the converse ≤most statements do not hold.
⋆
∅
ℓ◁
left
ℓ↙
ℓ↖
r▷
right
r↘
r↗
Involution φ
Figure 6: Going right is optimal for most reward functions. This is because whenever R makes
left strictly optimal over right, its permutation φ · R makes right strictly optimal over left by
switching which states get which rewards.
We check the conditions of proposition 6.9. s := ⋆, a′ := left, a := right. Figure 6 shows
that ⋆̸∈REACH (⋆, left) and that ⋆can only reach {ℓ◁, ℓ↖, ℓ↙} ∪{r▷, r↗, r↘} when the agent
immediately takes actions equivalent to left or right. F(⋆| π(⋆) = right) contains a copy of
F(⋆| π(⋆) = left) via φ. Furthermore, Fnd(⋆) ∩{e⋆+ γer▷+ γ2er↘+
γ3
1−γ er↗, e⋆+ γer▷+
γ2
1−γ er↗} = {e⋆+ γer▷+
γ2
1−γ er↗} is non-empty, and so all conditions are met.
For any γ ∈[0, 1] and D such that PD (⋆, left, γ) > PD (⋆, right, γ), environmental symmetry
ensures that Pφ·D (⋆, left, γ) < Pφ·D (⋆, right, γ). A similar statement holds for POWER.
6.2
When γ = 1, optimal policies tend to navigate towards “larger” sets of cycles
Proposition 6.6 and proposition 6.9 are powerful because they apply to all γ ∈[0, 1], but they can
only be applied given hard-to-satisfy environmental symmetries. In contrast, proposition 6.12 and
theorem 6.13 apply to many structured environments common to RL.
Starting from ⋆, consider the cycles which the agent can reach. Recurrent state distributions (RSDs)
generalize deterministic graphical cycles to potentially stochastic environments. RSDs simply record
how often the agent tends to visit a state in the limit of inﬁnitely many time steps.
Deﬁnition 6.10 (Recurrent state distributions [Puterman, 2014]). The recurrent state distributions
which can be induced from state s are RSD (s) :=

limγ→1(1 −γ)f π,s(γ) | π ∈Π
	
. RSDnd (s) is
the set of RSDs which strictly maximize average reward for some reward function.
As suggested by ﬁg. 3, RSD (⋆) = {eℓ↙, 1
2(eℓ↙+ eℓ↖), e∅, er↗, 1
2(er↗+ er↘), er↘}. As dis-
cussed in section 3, 1
2(er↗+ er↘) is dominated: Alternating between r↗and r↘is never strictly
better than choosing one or the other.
A reward function’s optimal policies can vary with the discount rate. When γ = 1, optimal policies
ignore transient reward because average reward is the dominant consideration.
Deﬁnition 6.11 (Average-optimal policies). The average-optimal policy set for reward function R is
Πavg (R) :=
n
π ∈Π | ∀s ∈S : dπ,s ∈arg maxd∈RSD(s) d⊤r
o
(the policies which induce optimal
RSDs at all states). For D ⊆RSD (s), the average optimality probability is PDany (D, average) :=
PR∼Dany
 ∃dπ,s ∈D : π ∈Πavg (R)

.
Average-optimal policies maximize average reward. Average reward is governed by RSD access. For
example, r↘has “more” RSDs than ∅; therefore, r↘usually has greater POWER when γ = 1.
Proposition 6.12 (When γ = 1, RSDs control POWER). If RSD (s) contains a copy of RSDnd
 s′
via φ, then POWERDbound (s, 1) ≥most POWERDbound
 s′, 1

. If RSDnd (s)\φ· RSDnd(s′) is non-empty,
then the converse ≤most statement does not hold.
8
We check that both conditions of proposition 6.12 are satisﬁed when s′ := ∅, s := r↘, and the
involution φ swaps ∅and r↘. Formally, φ · RSDnd (∅) = φ · {e∅} = {er↘} ⊊{er↘, er↗} =
RSDnd(r↘) ⊆[r↘]. The conditions are satisﬁed.
Informally, states with more RSDs generally have more POWER at γ = 1, no matter their transient
dynamics. Furthermore, average-optimal policies are more likely to end up in larger sets of RSDs
than in smaller ones. Thus, average-optimal policies tend to navigate towards parts of the state space
which contain more RSDs.
⋆
∅
ℓ◁
left
ℓ↙
ℓ↖
r▷
right
r↘
r↗
Figure 7: The cycles in RSD (⋆). Most reward functions make it average-optimal to avoid ∅, because
∅is only a single inescapable terminal state, while other parts of the state space offer more 1-cycles.
Theorem 6.13 (Average-optimal policies tend to end up in “larger” sets of RSDs). Let D, D′ ⊆
RSD (s). Suppose that D contains a copy of D′ via φ, and that the sets D ∪D′ and RSDnd (s) \
 D′ ∪D

have pairwise orthogonal vector elements (i.e. pairwise disjoint vector support). Then
PDany (D, average) ≥most PDany
 D′, average

. If RSDnd (s)∩
 D \ φ · D′
is non-empty, the converse
≤most statement does not hold.
Corollary 6.14 (Average-optimal policies tend not to end up in any given 1-cycle). Sup-
pose esx, es′
∈
RSD (s) are distinct.
Then PDany
 RSD (s) \ {esx}, average

≥most
PDany
 {esx}, average

. If there is a third es′′ ∈RSD (s), the converse ≤most statement does not
hold.
Figure
7
illustrates
that
e∅, er↘, er↗
∈
RSD (⋆).
Thus,
both
conclusions
of
corollary 6.14 hold:
PDany
 RSD (⋆) \ {e∅}, average

≥most
PDany
 {e∅}, average

and
PDany
 RSD (⋆) \ {e∅}, average

̸≤most PDany
 {e∅}, average

. In other words, average-optimal
policies tend to end up in RSDs besides ∅. Since ∅is a terminal state, it cannot reach other RSDs.
Since average-optimal policies tend to end up in other RSDs, average-optimal policies tend to avoid
∅.
This section’s results prove the γ = 1 case. Lemma 5.3 shows that POWER is continuous at γ = 1.
Therefore, if an action is strictly POWERD-seeking when γ = 1, it is strictly POWERD-seeking at
discount rates sufﬁciently close to 1. Future work may connect average optimality probability to
optimality probability at γ ≈1.
Lastly, our key results apply to all degenerate reward function distributions. Therefore, these results
apply not just to distributions over reward functions, but to individual reward functions.
6.3
How to reason about other environments
Consider an embodied navigation task through a room with a vase. Proposition 6.9 suggests that
optimal policies tend to avoid immediately breaking the vase, since doing so would strictly decrease
available options.
Theorem 6.13 dictates where average-optimal agents tend to end up, but not what actions they tend
to take in order to reach their RSDs. Therefore, care is needed. In appendix B, ﬁg. 10 demonstrates
an environment in which seeking POWER is a detour for most reward functions (since optimality
probability measures “median” optimal value, while POWER is a function of mean optimal value).
However, suppose the agent confronts a fork in the road: Actions a and a′ lead to two disjoint sets of
RSDs Da and Da′, such that Da contains a copy of Da′. Theorem 6.13 shows that a will tend to be
average-optimal over a′, and proposition 6.12 shows that a will tend to be POWER-seeking compared
to a′. Such forks seem reasonably common in environments with irreversible actions.
9
Theorem 6.13 applies to many structured RL environments, which tend to be spatially regular and to
factorize along several dimensions. Therefore, different sets of RSDs will be similar, requiring only
modiﬁcation of factor values. For example, if an embodied agent can deterministically navigate a set
of three similar rooms (spatial regularity), then the agent’s position factors via {room number} ×
{position in room}. Therefore, the RSDs can be divided into three similar subsets, depending on the
agent’s room number.
Corollary 6.14 dictates where average-optimal agents tend to end up, but not how they get there.
Corollary 6.14 says that such agents tend not to stay in any given 1-cycle. It does not say that such
agents will avoid entering such states. For example, in an embodied navigation task, a robot may
enter a 1-cycle by idling in the center of a room. Corollary 6.14 implies that average-optimal robots
tend not to idle in that particular spot, but not that they tend to avoid that spot entirely.
However, average-optimal robots do tend to avoid getting shut down. The agent’s task MDP often
represents agent shutdown with terminal states. A terminal state is, by deﬁnition 3.2, unable to
access other 1-cycles. Since corollary 6.14 shows that average-optimal agents tend to end up in other
1-cycles, average-optimal policies must tend to completely avoid the terminal state. Therefore, we
conclude that in many such situations, average-optimal policies tend to avoid shutdown. Intuitively,
survival is power-seeking relative to dying, and so shutdown-avoidance is power-seeking behavior.
In ﬁg. 8, the player dies by going left, but can reach thousands of RSDs by heading in other
directions. Even if some average-optimal policies go left in order to reach ﬁg. 8’s “game over”
terminal state, all other RSDs cannot be reached by going left. There are many 1-cycles besides
the immediate terminal state. Therefore, corollary 6.14 proves that average-optimal policies tend to
not go left in this situation. Average-optimal policies tend to avoid immediately dying in Pac-Man,
even though most reward functions do not resemble Pac-Man’s original score function.
7
Discussion
Reconsider the case of a hypothetical intelligent real-world agent which optimizes average reward for
some objective. Suppose the designers initially have control over the agent. If the agent began to
misbehave, perhaps they could just deactivate it. Unfortunately, our results suggest that this strategy
might not work. Average-optimal agents would generally stop us from deactivating them, if physically
possible. Extrapolating from our results, we conjecture that when γ ≈1, optimal policies tend to
seek power by accumulating resources—to the detriment of any other agents in the environment.
Future work.
Real-world training procedures often do not satisfy RL convergence theorems. Thus,
learned policies are rarely optimal. We expect this point to seriously constrain the applicability of
this theory. Emphatically, optimal policies are often qualitatively divorced from the actual policies
learned by reinforcement learning. For example, the mathematics of policy gradient algorithms
is not to update policies so as to maximize reward. Instead, the rewards provide gradients to the
parameterization of the policy [Turner, 2022]. On that view, reward functions are simply sources of
gradient updates which designers use in order to control generalization behavior.
Most real-world tasks are partially observable. Although our results only apply to optimal policies
in ﬁnite MDPs, we expect the key conclusions to generalize. Furthermore, irregular stochasticity in
environmental dynamics can make it hard to satisfy theorem 6.13’s similarity requirement. We look
forward to future work which addresses partially observable environments, suboptimal policies, or
“almost similar” RSD sets.
Past work shows that it would be bad for an agent to disempower humans in its environment. In a
two-player agent / human game, minimizing the human’s information-theoretic empowerment [Salge
· · ·
left
right
Figure 8: Consider the dynamics of the Pac-Man video game. Ghosts kill the player, at which point
we consider the player to enter a “game over” terminal state which shows the ﬁnal conﬁguration.
This rewardless MDP has Pac-Man’s dynamics, but not its usual score function. Fixing the dynamics,
as the reward function varies, right tends to be average-optimal over left. Roughly, this is because
the agent can do more by staying alive.
10
et al., 2014] produces adversarial agent behavior [Guckelsberger et al., 2018]. In contrast, maximizing
human empowerment produces helpful agent behavior [Salge and Polani, 2017, Guckelsberger et al.,
2016, Du et al., 2020]. We do not yet formally understand if, when, or why POWER-seeking policies
tend to disempower other agents in the environment.
More complex environments probably have more pronounced power-seeking incentives. Intuitively,
there are often many ways for power-seeking to be optimal, and relatively few ways for power-seeking
not to be optimal. For example, suppose that in some environment, theorem 6.13 holds for one
million involutions φ. Does this guarantee more pronounced incentives than if theorem 6.13 only
held for one involution?
We proved sufﬁcient conditions for when reward functions tend to have optimal policies which seek
power. In the absence of prior information, one should expect that an arbitrary reward function has
optimal policies which exhibit power-seeking behavior under these conditions. However, we have
prior information: AI designers usually try to specify a good reward function. Even so, it may be
hard to specify orbit elements which do not—at optimum—incentivize bad power-seeking.
Societal impact.
We believe that this paper builds toward a rigorous understanding of the risks
presented by AI power-seeking incentives. Understanding these risks is the ﬁrst step in addressing
them. However, basic theoretical work can have many consequences. For example, this theory could
somehow help future researchers build power-seeking agents which disempower humans. We believe
that the beneﬁt of understanding outweighs the potential societal harm.
Conclusion.
We developed the ﬁrst formal theory of the statistical tendencies of optimal policies in
reinforcement learning. In the context of MDPs, we proved sufﬁcient conditions under which optimal
policies tend to seek power, both formally (by taking POWER-seeking actions) and intuitively (by
taking actions which keep the agent’s options open). Many real-world environments have symmetries
which produce power-seeking incentives. In particular, optimal policies tend to seek power when
the agent can be shut down or destroyed. Seeking control over the environment will often involve
resisting shutdown, and perhaps monopolizing resources.
We caution that many real-world tasks are partially observable and that learned policies are rarely
optimal. Our results do not mathematically prove that hypothetical superintelligent AI agents will
seek power. However, we hope that this work will foster thoughtful, serious, and rigorous discussion
of this possibility.
Acknowledgments
Alexander Turner was supported by the Berkeley Existential Risk Initiative and the Long-Term
Future Fund. Alexander Turner, Rohin Shah, and Andrew Critch were supported by the Center for
Human-Compatible AI. Prasad Tadepalli was supported by the National Science Foundation.
Yousif Almulla, John E. Ball, Daniel Blank, Steve Byrnes, Ryan Carey, Michael Dennis, Scott
Emmons, Alan Fern, Daniel Filan, Ben Garﬁnkel, Adam Gleave, Edouard Harris, Evan Hubinger,
DNL Kok, Vanessa Kosoy, Victoria Krakovna, Cassidy Laidlaw, Joel Lehman, David Lindner, Dylan
Hadﬁeld-Menell, Richard Möhn, Alexandra Nolan, Matt Olson, Neale Ratzlaff, Adam Shimi, Sam
Toyer, Joshua Turner, Cody Wild, Davide Zagami, and our anonymous reviewers provided valuable
feedback.
References
Tsvi Benson-Tilsen and Nate Soares. Formalizing convergent instrumental goals. Workshops at the Thirtieth
AAAI Conference on Artiﬁcial Intelligence, 2016.
Nick Bostrom. The superintelligent will: Motivation and instrumental rationality in advanced artiﬁcial agents.
Minds and Machines, 22(2):71–85, 2012.
Nick Bostrom. Superintelligence. Oxford University Press, 2014.
Yuri Burda, Harri Edwards, Deepak Pathak, Amos Storkey, Trevor Darrell, and Alexei A. Efros. Large-scale
study of curiosity-driven learning. In International Conference on Learning Representations, 2019.
11
Ryan Carey. Incorrigibility in the CIRL framework. AI, Ethics, and Society, 2018.
Chris Drummond. Composing functions to speed up reinforcement learning in a changing world. In Machine
Learning: ECML-98, volume 1398, pages 370–381. Springer, 1998.
Yuqing Du, Stas Tiomkin, Emre Kiciman, Daniel Polani, Pieter Abbeel, and Anca Dragan. AvE: Assistance via
empowerment. Advances in Neural Information Processing Systems, 33, 2020.
David Foster and Peter Dayan. Structure in the space of value functions. Machine Learning, pages 325–346,
2002.
Christian Guckelsberger, Christoph Salge, and Simon Colton. Intrinsically motivated general companion NPCs
via coupled empowerment maximisation. In IEEE Conference on Computational Intelligence and Games,
pages 1–8, 2016.
Christian Guckelsberger, Christoph Salge, and Julian Togelius. New and surprising ways to be mean. In IEEE
Conference on Computational Intelligence and Games, pages 1–8, 2018.
Dylan Hadﬁeld-Menell, Anca Dragan, Pieter Abbeel, and Stuart Russell. The off-switch game. In Proceedings
of the Twenty-Sixth International Joint Conference on Artiﬁcial Intelligence, IJCAI-17, pages 220–227, 2017.
Yann LeCun and Anthony Zador.
Don’t fear the Terminator, September 2019.
URL https://blogs.
scientificamerican.com/observations/dont-fear-the-terminator/.
Steven A Lippman. On the set of optimal policies in discrete dynamic programming. Journal of Mathematical
Analysis and Applications, 24(2):440–445, 1968.
Lionel W McKenzie. Turnpike theory. Econometrica: Journal of the Econometric Society, pages 841–865,
1976.
Ishai Menache, Shie Mannor, and Nahum Shimkin. Q-cut—dynamic discovery of sub-goals in reinforcement
learning. In European Conference on Machine Learning, pages 295–306. Springer, 2002.
Smitha Milli, Dylan Hadﬁeld-Menell, Anca Dragan, and Stuart Russell. Should robots be obedient?
In
Proceedings of the 26th International Joint Conference on Artiﬁcial Intelligence, pages 4754–4760, 2017.
Melanie Mitchell. Why AI is harder than we think. arXiv preprint arXiv:2104.12871, 2021.
Andrew Y. Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory
and application to reward shaping. In Proceedings of the Sixteenth International Conference on Machine
Learning, pages 278–287. Morgan Kaufmann, 1999.
Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, and Shan Carter. Zoom in: An
introduction to circuits. Distill, 2020.
Stephen Omohundro. The basic AI drives, 2008.
Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell. Curiosity-driven exploration by self-
supervised prediction. In ICML, 2017.
Steven Pinker and Stuart Russell.
The foundations, beneﬁts, and possible existential threat of AI, June
2020. URL https://futureoflife.org/2020/06/15/steven-pinker-and-stuart-russell-on-
the-foundations-benefits-and-possible-existential-risk-of-ai/.
Martin L Puterman. Markov decision processes: Discrete stochastic dynamic programming. John Wiley & Sons,
2014.
J.B. Reece and N.A. Campbell. Campbell Biology. Pearson Australia, 2011.
Kevin Regan and Craig Boutilier. Robust policy computation in reward-uncertain MDPs using nondominated
policies. In Twenty-Fourth AAAI Conference on Artiﬁcial Intelligence, 2010.
Stuart Russell. Human compatible: Artiﬁcial intelligence and the problem of control. Viking, 2019.
Stuart J Russell and Peter Norvig. Artiﬁcial intelligence: a modern approach. Pearson Education Limited, 2009.
Christoph Salge and Daniel Polani. Empowerment as replacement for the three laws of robotics. Frontiers in
Robotics and AI, 4:25, 2017.
Christoph Salge, Cornelius Glackin, and Daniel Polani. Empowerment–an introduction. In Guided Self-
Organization: Inception, pages 67–114. Springer, 2014.
12
Faridun Sattarov. Power and technology: a philosophical and ethical analysis. Rowman & Littleﬁeld Interna-
tional, Ltd, 2019.
Tom Schaul, Daniel Horgan, Karol Gregor, and David Silver. Universal value function approximators. In
International Conference on Machine Learning, pages 1312–1320, 2015.
Nate Soares, Benja Fallenstein, Stuart Armstrong, and Eliezer Yudkowsky. Corrigibility. AAAI Workshops, 2015.
Richard S Sutton and Andrew G Barto. Reinforcement learning: an introduction. MIT Press, 1998.
Richard S Sutton, Joseph Modayil, Michael Delp, Thomas Degris, Patrick M Pilarski, Adam White, and Doina
Precup. Horde: A scalable real-time architecture for learning knowledge from unsupervised sensorimotor
interaction. In International Conference on Autonomous Agents and Multiagent Systems, pages 761–768,
2011.
Alexander Matt Turner. Reward is not the optimization target, 2022. URL https://www.alignmentforum.
org/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target.
Alexander Matt Turner, Dylan Hadﬁeld-Menell, and Prasad Tadepalli. Conservative agency via attainable utility
preservation. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, pages 385–391, 2020.
Various. Debate on instrumental convergence between LeCun, Russell, Bengio, Zador, and more, 2019.
URL https://www.alignmentforum.org/posts/WxW6Gc6f2z3mzmqKs/debate-on-instrumental-
convergence-between-lecun-russell.
Tao Wang, Michael Bowling, and Dale Schuurmans. Dual representations for dynamic programming and rein-
forcement learning. In International Symposium on Approximate Dynamic Programming and Reinforcement
Learning, pages 44–51. IEEE, 2007.
Tao Wang, Michael Bowling, Dale Schuurmans, and Daniel J Lizotte. Stable dual dynamic programming. In
Advances in Neural Information Processing Systems, pages 1569–1576, 2008.
13
Appendix A
Comparing POWER with information-theoretic empowerment
Salge et al. [2014] deﬁne information-theoretic empowerment as the maximum possible mutual
information between the agent’s actions and the state observations n steps in the future, written
En(s). This notion requires an arbitrary choice of horizon, failing to account for the agent’s discount
rate γ. “In a discrete deterministic world empowerment reduces to the logarithm of the number of
sensor states reachable with the available actions” [Salge et al., 2014]. Figure 9 demonstrates how
empowerment can return counterintuitive verdicts with respect to the agent’s control over the future.
1
2
(a)
3
(b)
4
(c)
Figure 9: Proposed empowerment measures fail to adequately capture how future choice is affected
by present actions. In a: En(s1) varies depending on whether n is even; thus, limn→∞En(s1)
does not exist. In b and c: ∀n : En(s3) = En(s4), even though s4 allows greater control over
future state trajectories than s3 does. For example, suppose that in both b and c, the leftmost black
state and the rightmost red state have 1 reward while all other states have 0 reward. In c, the agent
can independently maximize the intermediate black-state reward and the delayed red-state reward.
Independent maximization is not possible in b.
POWER returns intuitive answers in these situations. limγ→1 POWERDbound (s1, γ) converges by
lemma 5.3. Consider the obvious involution φ which takes each state in ﬁg. 9b to its counterpart
in ﬁg. 9c. Since φ · Fnd(s3) ⊊Fnd(s4) = F(s4), proposition 6.6 proves that ∀γ ∈[0, 1] :
POWERDbound (s3, γ) ≤most: Dbound POWERDbound (s4, γ), with the proof of proposition 6.6 showing
strict inequality under all DX-IID when γ ∈(0, 1).
Empowerment can be adjusted to account for these cases, perhaps by considering the channel capacity
between the agent’s actions and the state trajectories induced by stationary policies. However, since
POWER is formulated in terms of optimal value, we believe that POWER is better suited for MDPs
than information-theoretic empowerment is.
Appendix B
Seeking POWER can be a detour
Remark. The results of appendix E do not depend on this section’s results.
One might suspect that optimal policies tautologically tend to seek POWER. This intuition is wrong.
1
2
3
N
NE
Figure 10
Proposition B.1 (Greater POWERDbound does not imply greater PDbound). Action a seeking more
POWERDbound than a′ at state s and γ does not imply that PDbound (s, a, γ) ≥PDbound
 s, a′, γ

.
14
Proof. Consider the environment of ﬁg. 10. Let Xu := unif(0, 1), and consider DXu-IID, which
has bounded support.
Direct computation7 of the POWER expectation (deﬁnition 5.2) yields
POWERDXu-IID (s2, 1) = 3
4 > 2
3 = POWERDXu-IID (s3, 1). Therefore, N seeks more POWERDXu-IID
than NE at state s1 and γ = 1.
However, PDXu-IID (s1, N, 1) = 1
3 < 2
3 = PDXu-IID (s1, NE, 1).
Lemma B.2 (Fraction of orbits which agree on weak optimality). Let D ⊆∆(R|S|), and sup-
pose f1, f2 : ∆(R|S|) →R are such that f1(D) ≥most: D f2(D).
Then for all D ∈D,
{D′∈S|S|·D|f1(D′)≥f2(D′)}

|S|S|·D|
≥1
2.
Proof. All D′ ∈S|S| · D such that f1(D′) = f2(D′) satisfy f1(D′) ≥f2(D′).
Otherwise, consider the D′ ∈S|S| · D such that f1(D′) ̸= f2(D′). By the deﬁnition of ≥most
(deﬁnition 6.5), at least 1
2 of these D′ satisfy f1(D′) > f2(D′), in which case f1(D′) ≥f2(D′).
Then the desired inequality follows.
Lemma B.3 (≥most and trivial orbits). Let D ⊆∆(R|S|) and suppose f1(D) ≥most: D f2(D). For
all reward function distributions D ∈D with one-element orbits, f1(D) ≥f2(D). In particular, D
has a one-element orbit when it distributes reward identically and independently (IID) across states.
Proof. By lemma B.2, at least half of the elements D′ ∈S|S| · D satisfy f1(D′) ≥f2(D′). But
S|S| · D
 = 1, and so f1(D) ≥f2(D) must hold.
If D is IID, it has a one-element orbit due to the assumed identical distribution of reward.
Proposition B.4 (Actions which tend to seek POWER do not necessarily tend to be optimal). Action
a tending to seek more POWER than a′ at state s and γ does not imply that PDany (s, a, γ) ≥most: Dany
PDany
 s, a′, γ

.
Proof. Consider the environment of ﬁg. 10. Since RSDnd (s3) ⊊RSD (s2), proposition 6.12
shows that POWERDbound (s2, 1) ≥most: Dbound POWERDbound (s3, 1) via s′ := s3, s := s2, φ the identity
permutation (which is an involution). Therefore, N tends to seek more POWER than NE at state s1 and
γ = 1.
If PDany (s1, N, 1) ≥most: Dany PDany (s1, NE, 1), then lemma B.3 shows that PDX-IID (s1, N, 1) ≥
PDX-IID (s1, NE, 1) for all DX-IID. But the proof of proposition B.1 showed that PDXu-IID (s1, N, 1) <
PDXu-IID (s1, NE, 1) for Xu := unif(0, 1). Therefore, it cannot be true that PDany (s1, N, 1) ≥most: Dany
PDany (s1, NE, 1).
Appendix C
Sub-optimal POWER
In certain situations, POWER returns intuitively surprising verdicts. There exists a policy under which
the reader chooses a winning lottery ticket, but it seems wrong to say that the reader has the power
to win the lottery with high probability. For various reasons, humans and other bounded agents are
generally incapable of computing optimal policies for arbitrary objectives. More formally, consider
the rewardless MDP of ﬁg. 11.
Consider a model-based RL agent with black-box simulator access to this environment. The agent has
no prior information about the model, and so it acts randomly. Before long, the agent has probably
learned how to navigate from s0 to states sℓ, sr, s1, s2, and s5. However, over any reasonable
timescale, it is extremely improbable that the agent discovers the two actions respectively leading to
s3 and s4.
7In small deterministic MDPs, the POWER and optimality probability of the maximum-entropy reward function
distribution can be computed using https://github.com/loganriggs/Optimal-Policies-Tend-To-Seek-Power.
15
0
r
3
4
5
ℓ
2
1
Figure 11: s0 is the starting state, and |A| = 101010. At s0, half of the actions lead to sℓ, while the
other half lead to sr. Similarly, half of the actions at sℓlead to s1, while the other half lead to s2. At
sr, one action leads to s3, one action leads to s4, and the remaining 101010 −2 actions lead to s5.
Even provided with a reward function R and the discount rate γ, the agent has yet to learn the relevant
environmental dynamics, and so many of its policies are far from optimal. Although proposition 6.6
shows that ∀γ ∈[0, 1] : POWERDbound (sℓ, γ) ≤most: Dbound POWERDbound (sr, γ), there is a sense in
which sℓgives this agent more power.
We formalize a bounded agent’s goal-achievement capabilities with a function pol, which takes as
input a reward function and a discount rate, and returns a policy. Informally, this is the best policy
which the agent knows about. We can then calculate POWERDbound with respect to pol.
Deﬁnition C.1 (Suboptimal POWER). Let Π∆be the set of stationary stochastic policies, and let
pol : RS × [0, 1] →Π∆. For γ ∈[0, 1],
POWERpol
Dbound (s, γ) :=
E
R∼Dbound,
a∼pol(R,γ)(s),
s′∼T (s,a)

lim
γ∗→γ(1 −γ∗)V pol(R,γ)
R
 s′, γ∗
.
(5)
By lemma E.38, POWERDbound is the special case where ∀R ∈RS, γ ∈[0, 1] : pol (R, γ) ∈Π∗(R, γ).
We deﬁne POWERpol
Dbound-seeking similarly as in deﬁnition 5.6.
POWERpol
Dbound (s0, 1) increases as the policies returned by pol are improved. We illustrate this by
considering the DX-IID case.
pol1 The model is initially unknown, and so ∀R, γ : pol1(R, γ) is a uniformly random policy.
Since pol1 is constant on its inputs, POWERpol1
DX-IID (s0, 1) = E [X] by the linearity of ex-
pectation and the fact that DX-IID distributes reward independently and identically across
states.
pol2 The agent knows the dynamics, except that it does not know how to reach s3 or s4. At this
point, pol2(R, 1) navigates from s0 to the average-optimal choice among three terminal
states: s1, s2, and s5. Therefore, POWERpol2
Dbound (s0, 1) = E [max of 3 draws from X].
pol3 The agent knows the dynamics, the environment is small enough to solve explicitly,
and so ∀R, γ : pol3(R, γ) is an optimal policy. pol3(R, 1) navigates from s0 to the
average-optimal choice among all ﬁve terminal states. Therefore, POWERpol3
Dbound (s0, 1) =
E [max of 5 draws from X].
As the agent learns more about the environment and improves pol, the agent’s POWERpol
Dbound increases.
The agent seeks POWERpol2
Dbound by navigating to sℓinstead of sr, but seeks more POWERDbound by
navigating to sr instead of sℓ. Intuitively, bounded agents gain power by improving pol and by
formally seeking POWERpol
Dbound within the environment.
Appendix D
Lists of results
List of deﬁnitions
3.1
Deﬁnition (Rewardless MDP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
16
3.2
Deﬁnition (1-cycle states) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
3.3
Deﬁnition (State visit distribution [Sutton and Barto, 1998])
. . . . . . . . . . . .
3
3.4
Deﬁnition (F single-state restriction) . . . . . . . . . . . . . . . . . . . . . . . . .
3
3.5
Deﬁnition (Value function) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
3.6
Deﬁnition (Non-domination) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
4.1
Deﬁnition (Optimal policy set function) . . . . . . . . . . . . . . . . . . . . . . .
4
4.2
Deﬁnition (Reward function distributions) . . . . . . . . . . . . . . . . . . . . . .
4
4.3
Deﬁnition (Visit distribution optimality probability) . . . . . . . . . . . . . . . . .
4
4.4
Deﬁnition (Action optimality probability) . . . . . . . . . . . . . . . . . . . . . .
4
5.1
Deﬁnition (Average optimal value) . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.2
Deﬁnition (POWER) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.6
Deﬁnition (POWER-seeking actions) . . . . . . . . . . . . . . . . . . . . . . . . .
5
6.1
Deﬁnition (Similarity of vector sets) . . . . . . . . . . . . . . . . . . . . . . . . .
6
6.2
Deﬁnition (Similarity of vector function sets)
. . . . . . . . . . . . . . . . . . . .
6
6.3
Deﬁnition (Pushforward distribution of a permutation)
. . . . . . . . . . . . . . .
7
6.4
Deﬁnition (Orbit of a probability distribution) . . . . . . . . . . . . . . . . . . . .
7
6.5
Deﬁnition (Inequalities which hold for most probability distributions)
. . . . . . .
7
6.7
Deﬁnition (Equivalent actions) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
6.8
Deﬁnition (States reachable after taking an action) . . . . . . . . . . . . . . . . . .
7
6.10 Deﬁnition (Recurrent state distributions [Puterman, 2014]) . . . . . . . . . . . . .
8
6.11 Deﬁnition (Average-optimal policies)
. . . . . . . . . . . . . . . . . . . . . . . .
8
C.1
Deﬁnition (Suboptimal POWER) . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
E.2
Deﬁnition (Transition matrix induced by a policy) . . . . . . . . . . . . . . . . . .
20
E.6
Deﬁnition (Continuous reward function distribution)
. . . . . . . . . . . . . . . .
21
E.9
Deﬁnition (Non-dominated linear functionals) . . . . . . . . . . . . . . . . . . . .
21
E.13 Deﬁnition (Non-dominated vector functions)
. . . . . . . . . . . . . . . . . . . .
22
E.14 Deﬁnition (Afﬁne transformation of visit distribution sets)
. . . . . . . . . . . . .
22
E.18 Deﬁnition (Support of Dany)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
E.19 Deﬁnition (Linear functional optimality probability) . . . . . . . . . . . . . . . . .
24
E.23 Deﬁnition (Bounded, continuous IID reward)
. . . . . . . . . . . . . . . . . . . .
25
E.25 Deﬁnition (Indicator function) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
E.31 Deﬁnition (Evaluating sets of visit distribution functions at γ) . . . . . . . . . . . .
29
E.39 Deﬁnition (Discount-normalized value function) . . . . . . . . . . . . . . . . . . .
31
E.42 Deﬁnition (Normalized visit distribution function) . . . . . . . . . . . . . . . . . .
34
List of theorems
5.3
Lemma (Continuity of POWER)
. . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.4
Proposition (Maximal POWER) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.5
Proposition (POWER is smooth across reversible dynamics) . . . . . . . . . . . . .
5
17
6.6
Proposition (States with “more options” have more POWER)
. . . . . . . . . . . .
7
6.9
Proposition (Keeping options open tends to be POWER-seeking and tends to be optimal)
7
6.12 Proposition (When γ = 1, RSDs control POWER)
. . . . . . . . . . . . . . . . . .
8
6.13 Theorem (Average-optimal policies tend to end up in “larger” sets of RSDs) . . . .
9
6.14 Corollary (Average-optimal policies tend not to end up in any given 1-cycle) . . . .
9
B.1
Proposition (Greater POWERDbound does not imply greater PDbound) . . . . . . . . . .
14
B.2
Lemma (Fraction of orbits which agree on weak optimality)
. . . . . . . . . . . .
15
B.3
Lemma (≥most and trivial orbits) . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
B.4
Proposition (Actions which tend to seek POWER do not necessarily tend to be optimal) 15
E.1
Lemma (A policy is optimal iff it induces an optimal visit distribution at every state)
19
E.3
Proposition (Properties of visit distribution functions) . . . . . . . . . . . . . . . .
20
E.4
Lemma (f ∈F(s) is multivariate rational on γ) . . . . . . . . . . . . . . . . . . .
20
E.5
Corollary (On-policy value is rational on γ) . . . . . . . . . . . . . . . . . . . . .
20
E.7
Lemma (Distinct linear functionals disagree almost everywhere on their domains) .
21
E.8
Corollary (Unique maximization of almost all vectors)
. . . . . . . . . . . . . . .
21
E.10 Lemma (All vectors are maximized by a non-dominated linear functional) . . . . .
21
E.11 Corollary (Maximal value is invariant to restriction to non-dominated functionals) .
21
E.12 Lemma (How non-domination containment affects optimal value)
. . . . . . . . .
21
E.15 Lemma (Invariance of non-domination under positive afﬁne transform) . . . . . . .
22
E.16 Lemma (Helper lemma for demonstrating ≥most: Dany) . . . . . . . . . . . . . . . .
23
E.17 Lemma (A helper result for expectations of functions) . . . . . . . . . . . . . . . .
23
E.20 Proposition (Non-dominated linear functionals and their optimality probability) . .
24
E.21 Lemma (Expected value of similar linear functional sets) . . . . . . . . . . . . . .
24
E.22 Lemma (For continuous IID distributions DX-IID, ∃b < c : (b, c)|S| ⊆supp(DX-IID))
25
E.24 Lemma (Expectation superiority lemma) . . . . . . . . . . . . . . . . . . . . . . .
25
E.26 Lemma (Optimality probability inclusion relations) . . . . . . . . . . . . . . . . .
26
E.27 Lemma (Optimality probability of similar linear functional sets)
. . . . . . . . . .
27
E.28 Lemma (Optimality probability superiority lemma) . . . . . . . . . . . . . . . . .
27
E.29 Lemma (Limit probability inequalities which hold for most distributions)
. . . . .
28
E.30 Proposition (How to transfer optimal policy sets across discount rates) . . . . . . .
28
E.32 Lemma (Non-domination across γ values for expectations of visit distributions) . .
29
E.33 Lemma (∀γ ∈(0, 1) : d ∈Fnd(s, γ) iff d ∈ND
 F(s, γ)

)
. . . . . . . . . . . .
29
E.34 Lemma (∀γ ∈[0, 1) : V ∗
R (s, γ) = maxf∈Fnd(s) f(γ)⊤r)
. . . . . . . . . . . . . .
29
E.35 Lemma (Optimal policy shift bound) . . . . . . . . . . . . . . . . . . . . . . . . .
30
E.36 Proposition (Optimality probability’s limits exist) . . . . . . . . . . . . . . . . . .
30
E.37 Lemma (Optimality probability identity) . . . . . . . . . . . . . . . . . . . . . . .
30
E.38 Lemma (POWER identities) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
E.40 Lemma (Normalized value functions have uniformly bounded derivative)
. . . . .
31
E.41 Lemma (Lower bound on current POWER based on future POWER) . . . . . . . . .
33
18
E.43 Lemma (Normalized visit distribution functions are continuous)
. . . . . . . . . .
34
E.44 Lemma (Non-domination of normalized visit distribution functions) . . . . . . . .
34
E.45 Lemma (POWER limit identity) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
E.46 Lemma (Lemma for POWER superiority) . . . . . . . . . . . . . . . . . . . . . . .
35
E.47 Lemma (Non-dominated visit distribution functions never agree with other visit
distribution functions at that state) . . . . . . . . . . . . . . . . . . . . . . . . . .
37
E.48 Corollary (Cardinality of non-dominated visit distributions) . . . . . . . . . . . . .
37
E.49 Lemma (Optimality probability and state bottlenecks) . . . . . . . . . . . . . . . .
37
E.50 Lemma (Action optimality probability is a special case of visit distribution optimality
probability) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
E.51 Lemma (POWER identity when γ = 1) . . . . . . . . . . . . . . . . . . . . . . . .
42
E.52 Proposition (RSD properties) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
E.53 Lemma (When reachable with probability 1, 1-cycles induce non-dominated RSDs)
44
D.1
Contributions of independent interest
We developed new basic MDP theory by exploring the structural properties of visit distribution
functions. Echoing Wang et al. [2007, 2008], we believe that this area is interesting and underexplored.
D.1.1
Optimal value theory
Lemma E.40 shows that f(γ∗) := limγ∗→γ(1 −γ∗)V ∗
R (s, γ∗) is Lipschitz continuous on γ ∈[0, 1],
with Lipschitz constant depending only on ∥R∥1. For all states s and policies π ∈Π, corollary E.5
shows that V π
R (s, γ) is rational on γ.
Optimal value has a well-known dual formulation: V ∗
R (s, γ) = maxf∈F(s) f(γ)⊤r.
Lemma E.34 (∀γ ∈[0, 1) : V ∗
R (s, γ) = maxf∈Fnd(s) f(γ)⊤r).
In a ﬁxed rewardless MDP, lemma E.34 may enable more efﬁcient computation of optimal value
functions for multiple reward functions.
D.1.2
Optimal policy theory
Proposition E.30 demonstrates how to preserve optimal incentives while changing the discount rate.
Proposition E.30 (How to transfer optimal policy sets across discount rates). Suppose reward
function R has optimal policy set Π∗(R, γ) at discount rate γ ∈(0, 1). For any γ∗∈(0, 1), we
can construct a reward function R′ such that Π∗ R′, γ∗
= Π∗(R, γ). Furthermore, V ∗
R′ (·, γ∗) =
V ∗
R (·, γ).
D.1.3
Visit distribution theory
While Regan and Boutilier [2010] consider a visit distribution function f ∈F(s) to be non-dominated
if it is optimal for some reward function in a set R ⊆R|S|, our stricter deﬁnition 3.6 considers f to
be non-dominated when ∃r ∈R|S|, γ ∈(0, 1) : f(γ)⊤r > maxf ′∈F(s)\{f} f ′(γ)⊤r.
Appendix E
Theoretical results
Lemma E.1 (A policy is optimal iff it induces an optimal visit distribution at every state). Let
γ ∈(0, 1) and let R be a reward function. π ∈Π∗(R, γ) iff π induces an optimal visit distribution
at every state.
Proof. By deﬁnition, a policy π is optimal iff π induces the maximal on-policy value at each state,
which is true iff π induces an optimal visit distribution at every state (by the dual formulation of
optimal value functions).
19
Deﬁnition E.2 (Transition matrix induced by a policy). Tπ is the transition matrix induced by policy
π ∈Π, where Tπes := T(s, π(s)). (Tπ)tes gives the probability distribution over the states visited
at time step t, after following π for t steps from s.
Proposition E.3 (Properties of visit distribution functions). Let s, s′ ∈S, f π,s ∈F(s).
1. f π,s(γ) is element-wise non-negative and element-wise monotonically increasing on γ ∈
[0, 1).
2. ∀γ ∈[0, 1) :
f π,s(γ)

1 =
1
1−γ .
Proof. Item 1: by examination of deﬁnition 3.3, f π,s = P∞
t=0 (γTπ)t es. Since each (Tπ)t is left
stochastic and es is the standard unit vector, each entry in each summand is non-negative. Therefore,
∀γ ∈[0, 1) : f π,s(γ)⊤es′ ≥0, and this function monotonically increases on γ.
Item 2:
f π,s(γ)

1 =

∞
X
t=0
(γTπ)t es

1
(6)
=
∞
X
t=0
γt (Tπ)t es

1
(7)
=
∞
X
t=0
γt
(8)
=
1
1 −γ .
(9)
Equation (7) follows because all entries in each (Tπ)t es are non-negative by item 1. Equation (8)
follows because each (Tπ)t is left stochastic and es is a stochastic vector, and so
(Tπ)t es

1 =
1.
Lemma E.4 (f ∈F(s) is multivariate rational on γ). f π ∈F(s) is a multivariate rational function
on γ ∈[0, 1).
Proof. Let r ∈R|S| and consider f π ∈F(s). Let vπ
R be the V ∗
R (s, γ) function in column vector
form, with one entry per state value.
By the Bellman equations, vπ
R = (I −γTπ)−1 r. Let Aγ := (I −γTπ)−1, and for state s, form
As,γ by replacing Aγ’s column for state s with r. As noted by Lippman [1968], by Cramer’s rule,
V π
R (s, γ) = det As,γ
det Aγ is a rational function with numerator and denominator having degree at most
|S|.
In particular, for each state indicator reward function esi, V π
si(s, γ) = f π,s(γ)⊤esi is a rational
function of γ whose numerator and denominator each have degree at most |S|. This implies that
f π(γ) is multivariate rational on γ ∈[0, 1).
Corollary E.5 (On-policy value is rational on γ). Let π ∈Π and R be any reward function. V π
R (s, γ)
is rational on γ ∈[0, 1).
Proof. V π
R (s, γ) = f π,s(γ)⊤r, and f is a multivariate rational function of γ by lemma E.4. Therefore,
for ﬁxed r, f π,s(γ)⊤r is a rational function of γ.
20
E.1
Non-dominated visit distribution functions
Deﬁnition E.6 (Continuous reward function distribution). Results with Dcont hold for any absolutely
continuous reward function distribution.
Remark. We assume R|S| is endowed with the standard topology.
Lemma E.7 (Distinct linear functionals disagree almost everywhere on their domains). Let x, x′ ∈
R|S| be distinct. Pr∼Dcont
 x⊤r = x′⊤r

= 0.
Proof.
n
r ∈R|S| | (x −x′)⊤r = 0
o
is a hyperplane since x −x′ ̸= 0. Therefore, it has no interior
in the standard topology on R|S|. Since this empty-interior set is also convex, it has zero Lebesgue
measure. By the Radon-Nikodym theorem, it has zero measure under any continuous distribution
Dcont.
Corollary E.8 (Unique maximization of almost all vectors). Let X
⊊
R|S| be ﬁnite.
Pr∼Dcont
arg maxx′′∈X x′′⊤r
 > 1

= 0.
Proof. Let x, x′ ∈X be distinct. For any r ∈R|S|, x, x′ ∈arg maxx′′∈X x′′⊤r iff x⊤r = x′⊤r ≥
maxx′′∈X\{x,x′} x′′⊤r. By lemma E.7, x⊤r = x′⊤r holds with probability 0 under any Dcont.
E.1.1
Generalized non-domination results
Our formalism includes both Fnd(s) and RSDnd (s); we therefore prove results that are applicable to
both.
Deﬁnition E.9 (Non-dominated linear functionals). Let X
⊊R|S| be ﬁnite.
ND (X) :=
n
x ∈X | ∃r ∈R|S| : x⊤r > maxx′∈X\{x} x′⊤r
o
.
Lemma E.10 (All vectors are maximized by a non-dominated linear functional). Let r ∈R|S| and
let X ⊊R|S| be ﬁnite and non-empty. ∃x∗∈ND (X) : x∗⊤r = maxx∈X x⊤r.
Proof. Let A(r | X) := arg maxx∈X x⊤r = {x1, . . . , xn}. Then
x⊤
1 r = · · · = x⊤
n r >
max
x′∈X\A(r|X) x′⊤r.
(10)
In eq. (10), each x⊤r expression is linear on r. The max is piecewise linear on r since it is
the maximum of a ﬁnite set of linear functionals. In particular, all expressions in eq. (10) are
continuous on r, and so we can ﬁnd some δ > 0 neighborhood B(r, δ) such that ∀r′ ∈B(r, δ) :
maxxi∈A(r|X) x⊤
i r′ > maxx′∈X\A(r|X) x′⊤r′.
But almost all r′ ∈B(r, δ) are maximized by a unique functional x∗by corollary E.8; in particular,
at least one such r′′ exists. Formally, ∃r′′ ∈B(r, δ) : x∗⊤r′′ > maxx′∈X\{x∗} x′⊤r′′. Therefore,
x∗∈ND (X) by deﬁnition E.9.
x∗⊤r′ ≥maxxi∈A(r|X) x⊤
i r′ > maxx′∈X\A(r|X) x′⊤r′, with the strict inequality following because
r′′ ∈B(r, δ). These inequalities imply that x∗∈A(r | X).
Corollary E.11 (Maximal value is invariant to restriction to non-dominated functionals). Let r ∈R|S|
and let X ⊊R|S| be ﬁnite. maxx∈X x⊤r = maxx∈ND(X) x⊤r.
Proof. If X is empty, holds trivially. Otherwise, apply lemma E.10.
Lemma E.12 (How non-domination containment affects optimal value). Let r ∈R|S| and let
X, X′ ⊊R|S| be ﬁnite.
1. If ND (X) ⊆X′, then maxx∈X x⊤r ≤maxx′∈X′ x′⊤r.
21
2. If ND (X) ⊆X′ ⊆X, then maxx∈X x⊤r = maxx′∈X′ x′⊤r.
Proof. Item 1:
max
x∈X x⊤r =
max
x∈ND(X) x⊤r
(11)
≤max
x′∈X′ x′⊤r.
(12)
Equation (11) follows by corollary E.11. Equation (12) follows because ND (X) ⊆X′.
Item 2: by item 1, maxx∈X x⊤r ≤maxx′∈X′ x′⊤r. Since X′ ⊆X, we also have maxx∈X x⊤r ≥
maxx′∈X′ x′⊤r, and so equality must hold.
Deﬁnition
E.13
(Non-dominated
vector
functions).
Let
I
⊆
R
and
let
F
⊊

R|S|I
be
a
ﬁnite
set
of
vector-valued
functions
on
I.
ND (F)
:=
n
f ∈F | ∃γ ∈I, r ∈R|S| : f(γ)⊤r > maxf ′∈F \{f} f ′(γ)⊤r
o
.
Remark. Fnd(s) = ND
 F(s)

by deﬁnition 3.6.
Deﬁnition E.14 (Afﬁne transformation of visit distribution sets). For notational convenience, we de-
ﬁne set-scalar multiplication and set-vector addition on X ⊆R|S|: for c ∈R, cX :=

cx | x ∈X
	
.
For a ∈R|S|, X + a :=

x + a | x ∈X
	
. Similar operations hold when X is a set of vector
functions R 7→R|S|.
Lemma E.15 (Invariance of non-domination under positive afﬁne transform).
1. Let X ⊊R|S| be ﬁnite. If x ∈ND (X), then ∀c > 0, a ∈R|S| : (cx + a) ∈ND (cX + a).
2. Let I ⊆R and let F ⊊

R|S|I
be a ﬁnite set of vector-valued functions on I. If
f ∈ND (F), then ∀c > 0, a ∈R|S| : (cf + a) ∈ND (cF + a).
Proof. Item 1: Suppose x ∈ND (X) is strictly optimal for r ∈R|S|. Then let c > 0, a ∈R|S| be
arbitrary, and deﬁne b := a⊤r.
x⊤r >
max
x′∈X\{x} x′⊤r
(13)
cx⊤r + b >
max
x′∈X\{x} cx′⊤r + b
(14)
(cx + a)⊤r >
max
x′∈X\{x}(cx′ + a)⊤r
(15)
(cx + a)⊤r >
max
x′′∈(cX+a)\{cx+a} x′′⊤r.
(16)
Equation (14) follows because c > 0. Equation (15) follows by the deﬁnition of b.
Item 2: If f ∈ND (F), then by deﬁnition E.13, there exist γ ∈I, r ∈R|S| such that
f(γ)⊤r >
max
f ′∈F \{f} f ′(γ)⊤r.
(17)
Apply item 1 to conclude
(cf(γ) + a)⊤r >
max
(cf ′+a)∈(cF +a)\{cf+a}(cf ′(γ) + a)⊤r.
(18)
Therefore, (cf + a) ∈ND (cF + a).
22
E.1.2
Inequalities which hold under most reward function distributions
Deﬁnition 6.5 (Inequalities which hold for most probability distributions). Let f1, f2 : ∆(R|S|) →R
be functions from reward function distributions to real numbers and let D ⊆∆(R|S|) be closed
under permutation. We write f1(D) ≥most: D f2(D) 8 when, for all D ∈D, the following cardinality
inequality holds:
{D′ ∈S|S| · D | f1(D′) > f2(D′)}
 ≥
{D′ ∈S|S| · D | f1(D′) < f2(D′)}
 .
(4)
Lemma E.16 (Helper lemma for demonstrating ≥most: Dany). Let D ⊆∆(R|S|). If ∃φ ∈S|S| such
that for all D ∈D, f1 (D) < f2 (D) implies that f1 (φ · D) > f2 (φ · D), then f1(D) ≥most: D
f2(D).
Proof. Since φ does not belong to the stabilizer of S|S|, φ acts injectively on S|S| · D. By as-
sumption on φ, the image of {D′ ∈S|S| · D | f1(D′) < f2(D′)} under φ is a subset of
{D′ ∈S|S| · D | f1(D′) > f2(D′)}. Since φ is injective,
{D′ ∈S|S| · D | f1(D′) < f2(D′)}
 ≤
{D′ ∈S|S| · D | f1(D′) > f2(D′)}
. f1(D) ≥most: D f2(D) by deﬁnition 6.5.
Lemma E.17 (A helper result for expectations of functions). Let B1, . . . , Bn ⊊R|S| be ﬁnite and
let D ⊆∆(R|S|). Suppose f is a function of the form
f
 B1, . . . , Bn | D

= E
r∼D
"
g

max
b1∈B1 b⊤
1 r, . . . , max
bn∈Bn b⊤
n r
#
(19)
for some function g, and that f is well-deﬁned for all D ∈D. Let φ be a state permutation. Then
f
 B1, . . . , Bn | D

= f
 φ · B1, . . . , φ · Bn | φ · D

.
(20)
Proof. Let distribution D have probability measure F, and let φ · D have probability measure Fφ.
f
 B1, . . . , Bn | D

(21)
:=
E
r∼D
"
g

max
b1∈B1 b⊤
1 r, . . . , max
bn∈Bn b⊤
n r
#
(22)
:=
Z
R|S| g

max
b1∈B1 b⊤
1 r, . . . , max
bn∈Bn b⊤
n r

dF(r)
(23)
=
Z
R|S| g

max
b1∈B1 b⊤
1 r, . . . , max
bn∈Bn b⊤
n r

dFφ(Pφr)
(24)
=
Z
R|S| g

max
b1∈B1 b⊤
1

P−1
φ r′
, . . . , max
bn∈Bn b⊤
n

P−1
φ r′ det Pφ
 dFφ(r′)
(25)
=
Z
R|S| g

max
b1∈B1
 Pφb1
⊤r′, . . . , max
bn∈Bn
 Pφbn
⊤r′

dFφ(r′)
(26)
=
Z
R|S| g
 
max
b′
1∈φ·B1 b′⊤
1 r′, . . . ,
max
b′
n∈φ·Bn b′⊤
n r′
!
dFφ(r′)
(27)
=: f
 φ · B1, . . . , φ · Bn | φ · D

.
(28)
Equation (24) follows by the deﬁnition of Fφ (deﬁnition 6.3). Equation (25) follows by substituting
r′ := Pφr. Equation (26) follows from the fact that all permutation matrices have unitary determinant
and are orthogonal (and so (P−1
φ )⊤= Pφ).
Deﬁnition E.18 (Support of Dany). Let Dany be any reward function distribution. supp(Dany) is the
smallest closed subset of R|S| whose complement has measure zero under Dany.
8We write f1(D) ≥most f2(D) when D is clear from context.
23
Deﬁnition E.19 (Linear functional optimality probability). For ﬁnite A, B ⊊R|S|, the probability
under Dany that A is optimal over B is pDany (A ≥B) := Pr∼Dany
 maxa∈A a⊤r ≥maxb∈B b⊤r

.
Proposition E.20 (Non-dominated linear functionals and their optimality probability). Let A ⊊R|S|
be ﬁnite. If ∃b < c : [b, c]|S| ⊆supp(Dany), then a ∈ND (A) implies that a is strictly optimal for a
set of reward functions with positive measure under Dany.
Proof. Suppose ∃b < c : [b, c]|S| ⊆supp(Dany). If a ∈ND (A), then let r be such that a⊤r >
maxa′∈A\{a} a′⊤r. For a1 > 0, a2 ∈R, positively afﬁnely transform r′ := a1r + a21 (where
1 ∈R|S| is the all-ones vector) so that r′ ∈(b, c)|S|.
Note that a is still strictly optimal for r′:
a⊤r >
max
a′∈A\{a} a′⊤r ⇐⇒a⊤r′ >
max
a′∈A\{a} a′⊤r′.
(29)
Furthermore, by the continuity of both terms on the right-hand side of eq. (29), a is strictly optimal
for reward functions in some open neighborhood N of r′. Let N ′ := N ∩(b, c)|S|. N ′ is still open in
R|S| since it is the intersection of two open sets N and (b, c)|S|.
Dany must assign positive probability measure to all open sets in its support; otherwise, its support
would exclude these zero-measure sets by deﬁnition E.18. Therefore, Dany assigns positive probability
to N ′ ⊆supp(Dany).
Lemma E.21 (Expected value of similar linear functional sets). Let A, B ⊊R|S| be ﬁnite, let A′ be
such that ND (A) ⊆A′ ⊆A, and let g : R →R be an increasing function. If B contains a copy B′
of A′ via φ, then
E
r∼Dbound
"
g

max
a∈A a⊤r
#
≤
E
r∼φ·Dbound
"
g

max
b∈B b⊤r
#
.
(30)
If ND (B) \ B′ is empty, then eq. (30) is an equality. If ND (B) \ B′ is non-empty, g is strictly
increasing, and ∃b < c : (b, c)|S| ⊆supp(Dbound), then eq. (30) is strict.
Proof. Because g : R →R is increasing, it is measurable (as is max). Therefore, the relevant
expectations exist for all Dbound.
E
r∼Dbound
"
g

max
a∈A a⊤r
#
=
E
r∼Dbound
"
g

max
a∈A′ a⊤r
#
(31)
=
E
r∼φ·Dbound
"
g

max
a∈φ·A′ a⊤r
#
(32)
=
E
r∼φ·Dbound
"
g

max
b∈B′ b⊤r
#
(33)
≤
E
r∼φ·Dbound
"
g

max
b∈B b⊤r
#
.
(34)
Equation (31) holds because ∀r ∈R|S| : maxa∈A a⊤r = maxa∈A′ a⊤r by lemma E.12’s item 2
with X := A, X′ := A′. Equation (32) holds by lemma E.17. Equation (33) holds by the deﬁnition
of B′. Furthermore, our assumption on φ guarantees that B′ ⊆B. Therefore, maxb∈B′ b⊤r ≤
maxb∈B b⊤r, and so eq. (34) holds by the fact that g is an increasing function. Then eq. (30) holds.
If ND (B) \ B′ is empty, then ND (B) ⊆B′. By assumption, B′ ⊆B. Then apply lemma E.12
item 2 with X := B, X′ := B′ in order to conclude that eq. (34) is an equality. Then eq. (30) is also
an equality.
24
Suppose that g is strictly increasing, ND (B) \ B′ is non-empty, and ∃b < c : (b, c)|S| ⊆
supp(Dbound). Let x ∈ND (B) \ B′.
E
r∼φ·Dbound
"
g

max
b∈B′ b⊤r
#
<
E
r∼φ·Dbound

g
 
max
a∈B′∪{x} b⊤r
!

(35)
≤
E
r∼φ·Dbound
"
g

max
b∈B b⊤r
#
.
(36)
x is strictly optimal for a positive-probability subset of supp(Dbound) by proposition E.20. Since g is
strictly increasing, eq. (35) is strict. Therefore, we conclude that eq. (30) is strict.
Lemma E.22 (For continuous IID distributions DX-IID, ∃b < c : (b, c)|S| ⊆supp(DX-IID)).
Proof. DX-IID := X|S|. Since the state reward distribution X is continuous, X must have support on
some open interval (b, c). Since DX-IID is IID across states, (b, c)|S| ⊆supp(DX-IID).
Deﬁnition E.23 (Bounded, continuous IID reward). DC/B/IID is the set of DX-IID which equal X|S|
for some continuous, bounded-support distribution X over R.
Lemma E.24 (Expectation superiority lemma). Let A, B ⊊R|S| be ﬁnite and let g : R →R be an
increasing function. If B contains a copy B′ of ND (A) via φ, then
E
r∼Dbound
"
g

max
a∈A a⊤r
#
≤most: Dbound
E
r∼Dbound
"
g

max
b∈B b⊤r
#
.
(37)
Furthermore, if g is strictly increasing and ND (B) \ φ · ND (A) is non-empty, then eq. (37)
is strict for all DX-IID
∈DC/B/IID.
In particular, Er∼Dbound
h
g
 maxa∈A a⊤r
i
̸≥most: Dbound
Er∼Dbound
h
g
 maxb∈B b⊤r
i
.
Proof. Because g : R →R is increasing, it is measurable (as is max). Therefore, the relevant
expectations exist for all Dbound.
Suppose that Dbound is such that Er∼Dbound
h
g
 maxb∈B b⊤r
i
< Er∼Dbound
h
g
 maxa∈A a⊤r
i
.
E
r∼φ·Dbound
"
g

max
a∈A a⊤r
#
≤
E
r∼φ2·Dbound
"
g

max
b∈B b⊤r
#
(38)
=
E
r∼Dbound
"
g

max
b∈B b⊤r
#
(39)
<
E
r∼Dbound
"
g

max
a∈A a⊤r
#
(40)
≤
E
r∼φ·Dbound
"
g

max
b∈B b⊤r
#
.
(41)
Equation (38) follows by applying lemma E.21 with permutation φ and A′ := ND (A). Equation (39)
follows because involutions satisfy φ−1 = φ, and φ2 is therefore the identity. Equation (40)
follows because we assumed that Er∼Dbound
h
g
 maxb∈B b⊤r
i
< Er∼Dbound
h
g
 maxa∈A a⊤r
i
.
Equation (41) follows by applying lemma E.21 with permutation φ and and A′ := ND (A). By
lemma E.16, eq. (37) holds.
25
Suppose g is strictly increasing and ND (B) \ B′ is non-empty. Let φ′ ∈S|S|.
E
r∼φ′·DX-IID
"
g

max
a∈A a⊤r
#
=
E
r∼DX-IID
"
g

max
a∈A a⊤r
#
(42)
<
E
r∼φ·DX-IID
"
g

max
b∈B b⊤r
#
(43)
=
E
r∼φ′·DX-IID
"
g

max
b∈B b⊤r
#
.
(44)
Equation (42) and eq. (44) hold because DX-IID distributes reward identically across states: ∀φx ∈
S|S| : φx · DX-IID = DX-IID. By lemma E.22, ∃b < c : (b, c)|S| ⊆supp(DX-IID). Therefore, apply
lemma E.21 with A′ := ND (A) to conclude that eq. (43) holds.
Therefore, ∀φ′ ∈S|S| : Er∼φ′·DX-IID
h
g
 maxa∈A a⊤r
i
< Er∼φ′·DX-IID
h
g
 maxb∈B b⊤r
i
, and so
Er∼Dbound
h
g
 maxa∈A a⊤r
i
̸≥most: Dbound Er∼Dbound
h
g
 maxb∈B b⊤r
i
by deﬁnition 6.5.
Deﬁnition E.25 (Indicator function). Let L be a predicate which takes input x. 1L(x) is the function
which returns 1 when L(x) is true, and 0 otherwise.
Lemma E.26 (Optimality probability inclusion relations). Let X, Y ⊊R|S| be ﬁnite and suppose
Y ′ ⊆Y .
pDany (X ≥Y ) ≤pDany
 X ≥Y ′
≤pDany

X ∪
 Y \ Y ′
≥Y

.
(45)
If ∃b < c : (b, c)|S| ⊆supp(Dany), X ⊆Y , and ND (Y ) ∩
 Y \ Y ′
is non-empty, then the second
inequality is strict.
Proof.
pDany (X ≥Y ) :=
E
r∼Dany
h
1maxx∈X x⊤r≥maxy∈Y y⊤r
i
(46)
≤
E
r∼Dany
h
1maxx∈X x⊤r≥maxy∈Y ′ y⊤r
i
(47)
≤
E
r∼Dany
h
1maxx∈X∪(Y \Y ′) x⊤r≥maxy∈Y ′ y⊤r
i
(48)
=
E
r∼Dany
h
1maxx∈X∪(Y \Y ′) x⊤r≥maxy∈Y ′∪(Y \Y ′) y⊤r
i
(49)
=
E
r∼Dany
h
1maxx∈X∪(Y \Y ′) x⊤r≥maxy∈Y y⊤r
i
(50)
=: pDany

X ∪
 Y \ Y ′
≥Y

.
(51)
Equation (47) follows because ∀r ∈R|S| : 1maxx∈X x⊤r≥maxy∈Y y⊤r ≤1maxx∈X x⊤r≥maxy∈Y ′ y⊤r
since Y ′
⊆
Y ; note that eq. (47) equals pDany
 X ≥Y ′
, and so the ﬁrst inequality of
eq. (45) is shown.
Equation (48) holds because ∀r ∈R|S| : 1maxx∈X x⊤r≥maxy∈Y ′ y⊤r ≤
1maxx∈X∪(Y \Y ′) x⊤r≥maxy∈Y ′ b⊤r.
Suppose ∃b < c : (b, c)|S| ⊆supp(Dany), X ⊆Y , and ND (Y ) ∩
 Y \ Y ′
is non-empty. Let
y∗∈ND (Y ) ∩
 Y \ Y ′
. By proposition E.20, y∗is strictly optimal on a subset of supp(Dany)
with positive measure under Dany. In particular, for a set of r∗with positive measure under Dany, we
have y∗⊤r∗> maxy∈Y ′ y⊤r∗.
Then eq. (48) is strict, and therefore the second inequality of eq. (45) is strict as well.
26
Lemma E.27 (Optimality probability of similar linear functional sets). Let A, B, C ⊊R|S| be ﬁnite,
and let Z ⊆R|S| be such that ND (C) ⊆Z ⊆C. If ND (A) is similar to B′ ⊆B via φ such that
φ ·

Z \
 B \ B′
= Z \
 B \ B′
, then
pDany (A ≥C) ≤pφ·Dany (B ≥C) .
(52)
If B′ = B, then eq. (52) is an equality. If ∃b < c : (b, c)|S| ⊆supp(Dany), B′ ⊆C, and
ND (C) ∩
 B \ B′
is non-empty, then eq. (52) is strict.
Proof.
pDany (A ≥C) = pDany (A ≥Z)
(53)
= pDany
 ND (A) ≥Z

(54)
≤pDany

ND (A) ≥Z \
 B \ B′
(55)
= pφ·Dany

φ · ND (A) ≥φ · Z \
 B \ B′
(56)
= pφ·Dany

B′ ≥Z \
 B \ B′
(57)
≤pφ·Dany

B′ ∪
 B \ B′
≥Z

(58)
= pφ·Dany (B ≥C) .
(59)
Equation (53) and eq. (59) follow by lemma E.12’s item 2 with X := C, X′ := Z. Similarly, eq. (54)
follows by lemma E.12’s item 2 with X := A, X′ := ND (A). Equation (55) follows by applying
the ﬁrst inequality of lemma E.26 with X := ND (A) , Y := Z, Y ′ := Z \ (B \ B′). Equation (56)
follows by applying lemma E.17 to eq. (53) with permutation φ.
Equation (57) follows by our assumptions on φ. Equation (58) follows because by applying the
second inequality of lemma E.26 with X := B′, Y := ND (C) , Y ′ := ND (C) \ (B \ B′).
Suppose B′ = B. Then B \B′ = ∅, and so eq. (55) and eq. (58) are trivially equalities. Then eq. (52)
is an equality.
Suppose ∃b < c : (b, c)|S| ⊆supp(Dany); note that (b, c)|S| ⊆supp(φ · Dany), since such support
must be invariant to permutation. Further suppose that B′ ⊆C and that ND (C) ∩
 B \ B′
is non-
empty. Then letting X := B′, Y := Z, Y ′ := Z \(B \B′) and noting that ND
 ND (Z)

= ND (Z),
apply lemma E.26 to eq. (58) to conclude that eq. (52) is strict.
Lemma E.28 (Optimality probability superiority lemma). Let A, B, C ⊊R|S| be ﬁnite, and let Z
satisfy ND (C) ⊆Z ⊆C. If B contains a copy B′ of ND (A) via φ such that φ ·

Z \
 B \ B′
=
Z \
 B \ B′
, then pDany (A ≥C) ≤most: Dany pDany (B ≥C).
If B′ ⊆C and ND (C)∩
 B \ B′
is non-empty, then the inequality is strict for all DX-IID ∈DC/B/IID
and pDany (A ≥C) ̸≥most: Dany pDany (B ≥C).
Proof. Suppose Dany is such that pDany (B ≥C) < pDany (A ≥C).
pφ·Dany (A ≥C) = pφ−1·Dany (A ≥C)
(60)
≤pDany (B ≥C)
(61)
< pDany (A ≥C)
(62)
≤pφ·Dany (B ≥C) .
(63)
Equation (60) holds because φ is an involution.
Equation (61) and eq. (63) hold by ap-
plying lemma E.27 with permutation φ.
Equation (62) holds by assumption.
Therefore,
pDany (A ≥C) ≤most: Dany pDany (B ≥C) by lemma E.16.
27
Suppose B′ ⊆C and ND (C)∩
 B \ B′
is non-empty, and let DX-IID be any continuous distribution
which distributes reward independently and identically across states. Let φ′ ∈S|S|.
pφ′·DX-IID (A ≥C) = pDX-IID (A ≥C)
(64)
< pφ·DX-IID (B ≥C)
(65)
= pφ′·DX-IID (A ≥C) .
(66)
Equation (64) and eq. (66) hold because DX-IID distributes reward identically across states, ∀φx ∈
S|S| : φx · DX-IID = DX-IID. By lemma E.22, ∃b < c : (b, c)|S| ⊆supp(DX-IID). Therefore, apply
lemma E.27 to conclude that eq. (65) holds.
Therefore,
∀φ′
∈
S|S|
:
pφ′·DX-IID (A ≥C)
<
pφ′·DX-IID (B ≥C).
In particular,
pDany (A ≥C) ̸≥most: Dany pDany (B ≥C) by deﬁnition 6.5.
Lemma E.29 (Limit probability inequalities which hold for most distributions). Let I ⊆R, let
D ⊆∆(R|S|) be closed under permutation, and let FA, FB, FC be ﬁnite sets of vector functions I 7→
R|S|. Let γ be a limit point of I such that f1(D) := limγ∗→γ pD
 FB(γ∗) ≥FC(γ∗)

, f2(D) :=
limγ∗→γ pD
 FA(γ∗) ≥FC(γ∗)

are well-deﬁned for all D ∈D.
Let FZ satisfy ND (FC) ⊆FZ ⊆FC. Suppose FB contains a copy of FA via φ such that φ ·

FZ \
 FB \ φ · FA

= FZ \
 FB \ φ · FA

. Then f2(D) ≤most: D f1(D).
Proof. Suppose D ∈D is such that f2(D) > f1(D).
f2 (φ · D) = f2

φ−1 · D

(67)
:= lim
γ∗→γ pφ−1·D
 FA(γ∗) ≥FC(γ∗)

(68)
≤lim
γ∗→γ pD
 FB(γ∗) ≥FC(γ∗)

(69)
< lim
γ∗→γ pD
 FA(γ∗) ≥FC(γ∗)

(70)
≤lim
γ∗→γ pφ·D
 FB(γ∗) ≥FC(γ∗)

(71)
=: f1 (φ · D) .
(72)
By the assumption that D is closed under permutation and f2 is well-deﬁned for all D ∈D, f2(φ · D)
is well-deﬁned. Equation (67) follows since φ = φ−1 because φ is an involution. For all γ∗∈I, let
A := FA(γ∗), B := FB(γ∗), C := FC(γ∗), Z := FZ(γ∗) (by deﬁnition E.13, ND (C) ⊆Z ⊆C).
Since φ · A ⊆B by assumption, and since ND (A) ⊆A, B also contains a copy of ND (A)
via φ. Furthermore, φ ·

Z \
 B \ φ · A

= Z \
 B \ φ · A

(by assumption), and so apply
lemma E.27 to conclude that pφ−1·D
 FA(γ∗) ≥FC(γ∗)

≤pD
 FB(γ∗) ≥FC(γ∗)

. Therefore,
the limit inequality eq. (69) holds. Equation (70) follows because we assumed that f1(D) < f2(D).
Equation (71) holds by reasoning similar to that given for eq. (69).
Therefore, f2(D) > f1(D) implies that f2 (φ · D) < f1 (φ · D), and so apply lemma E.16 to
conclude that f2(D) ≤most: D f1(D).
E.1.3
Fnd results
Proposition E.30 (How to transfer optimal policy sets across discount rates). Suppose reward
function R has optimal policy set Π∗(R, γ) at discount rate γ ∈(0, 1). For any γ∗∈(0, 1), we
can construct a reward function R′ such that Π∗ R′, γ∗
= Π∗(R, γ). Furthermore, V ∗
R′ (·, γ∗) =
V ∗
R (·, γ).
Proof. Let R be any reward function. Suppose γ∗∈(0, 1) and construct R′(s) := V ∗
R (s, γ) −
γ∗maxa∈A Es′∼T (s,a)
h
V ∗
R
 s′, γ
i
.
28
Let π ∈Π be any policy. By the deﬁnition of optimal policies, π ∈Π∗ R′, γ∗
iff for all s:
R′(s) + γ∗
E
s′∼T(s,π(s))
h
V ∗
R′
 s′, γ∗i
= R′(s) + γ∗max
a∈A
E
s′∼T (s,a)
h
V ∗
R′
 s′, γ∗i
(73)
R′(s) + γ∗
E
s′∼T(s,π(s))
h
V ∗
R
 s′, γ
i
= R′(s) + γ∗max
a∈A
E
s′∼T (s,a)
h
V ∗
R
 s′, γ
i
(74)
γ∗
E
s′∼T(s,π(s))
h
V ∗
R
 s′, γ
i
= γ∗max
a∈A
E
s′∼T (s,a)
h
V ∗
R
 s′, γ
i
(75)
E
s′∼T(s,π(s))
h
V ∗
R
 s′, γ
i
= max
a∈A
E
s′∼T (s,a)
h
V ∗
R
 s′, γ
i
.
(76)
By the Bellman equations, R′(s) = V ∗
R′ (s, γ∗) −γ∗maxa∈A Es′∼T (s,a)
h
V ∗
R′
 s′, γ∗i
. By the
deﬁnition of R′, V ∗
R′ (·, γ∗) = V ∗
R (·, γ) must be the unique solution to the Bellman equations for
R′ at γ∗. Therefore, eq. (74) holds. Equation (75) follows by plugging in R′ := V ∗
R (s, γ) −
γ∗maxa∈A Es′∼T (s,a)
h
V ∗
R
 s′, γ
i
to eq. (74) and doing algebraic manipulation. Equation (76)
follows because γ∗> 0.
Equation (76) shows that π
∈
Π∗ R′, γ∗
iff ∀s
:
Es′∼T (s,π(s))
h
V ∗
R
 s′, γ
i
=
maxa∈A Es′∼T (s,a)
h
V ∗
R
 s′, γ
i
. That is, π ∈Π∗ R′, γ∗
iff π ∈Π∗(R, γ).
Deﬁnition E.31 (Evaluating sets of visit distribution functions at γ). For γ ∈(0, 1), deﬁne
F(s, γ) :=

f(γ) | f ∈F(s)
	
and Fnd(s, γ) :=

f(γ) | f ∈Fnd(s)
	
.
If F
⊆F(s), then
F(γ) :=

f(γ) | f ∈F
	
.
Lemma E.32 (Non-domination across γ values for expectations of visit distributions). Let ∆d ∈
∆

R|S|
be any state distribution and let F :=

Esd∼∆d [f π,sd] | π ∈Π
	
. f ∈ND (F) iff ∀γ∗∈
(0, 1) : f(γ∗) ∈ND
 F(γ∗)

.
Proof. Let f π ∈ND (F) be strictly optimal for reward function R at discount rate γ ∈(0, 1):
f π(γ)⊤r >
max
f π′∈F \{f π} f π′(γ)⊤r.
(77)
Let γ∗∈(0, 1). By proposition E.30, we can produce R′ such that Π∗ R′, γ∗
= Π∗(R, γ). Since
the optimal policy sets are equal, lemma E.1 implies that
f π(γ∗)⊤r′ >
max
f π′∈F \{f π} f π′(γ∗)⊤r′.
(78)
Therefore, f π(γ∗) ∈ND
 F(γ∗)

.
The reverse direction follows by the deﬁnition of ND (F).
Lemma E.33 (∀γ ∈(0, 1) : d ∈Fnd(s, γ) iff d ∈ND
 F(s, γ)

).
Proof. By deﬁnition E.31, Fnd(s, γ) :=
n
f(γ) | f ∈ND
 F(s)
o
. By applying lemma E.32 with
∆d := es, f ∈ND
 F(s)

iff ∀γ ∈(0, 1) : f(γ) ∈ND
 F(s, γ)

.
Lemma E.34 (∀γ ∈[0, 1) : V ∗
R (s, γ) = maxf∈Fnd(s) f(γ)⊤r).
Proof. ND
 F(s, γ)

= Fnd(s, γ) by lemma E.33, so apply corollary E.11 with X := F(s, γ).
29
E.2
Some actions have greater probability of being optimal
Lemma E.35 (Optimal policy shift bound). For ﬁxed R, Π∗(R, γ) can take on at most (2 |S| +
1) P
s
 |F(s)|
2

distinct values over γ ∈(0, 1).
Proof. By lemma E.1, Π∗(R, γ) changes value iff there is a change in optimality status for some visit
distribution function at some state. Lippman [1968] showed that two visit distribution functions can
trade off optimality status at most 2 |S| + 1 times. At each state s, there are
 |F(s)|
2

such pairs.
Proposition E.36 (Optimality probability’s limits exist). Let F
⊆
F(s).
PDany (F, 0)
=
limγ→0 PDany (F, γ) and PDany (F, 1) = limγ→1 PDany (F, γ).
Proof. First consider the limit as γ →1. Let Dany have probability measure Fany, and deﬁne
δ(γ) := Fany

R ∈RS | ∃γ∗∈[γ, 1) : Π∗(R, γ∗) ̸= Π∗(R, 1)
	
. Since Fany is a probability
measure, δ(γ) is bounded [0, 1], and δ(γ) is monotone decreasing. Therefore, limγ→1 δ(γ) exists.
If limγ→1 δ(γ) > 0, then there exist reward functions whose optimal policy sets Π∗(R, γ) never
converge (in the discrete topology on sets) to Π∗(R, 1), contradicting lemma E.35. So limγ→1 δ(γ) =
0.
By the deﬁnition of optimality probability (deﬁnition 4.3) and of δ(γ), | PDany (F, γ)−PDany (F, 1) | ≤
δ(γ). Since limγ→1 δ(γ) = 0, limγ→1 PDany (F, γ) = PDany (F, 1).
A similar proof shows that limγ→0 PDany (F, γ) = PDany (F, 0).
Lemma E.37 (Optimality probability identity). Let γ ∈(0, 1) and let F ⊆F(s).
PDany (F, γ) = pD′  F(γ) ≥F(s, γ)

= pD′  F(γ) ≥Fnd(s, γ)

.
(79)
Proof. Let γ ∈(0, 1).
PDany (F, γ) :=
P
R∼Dany
 ∃f π ∈F : π ∈Π∗(R, γ)

(80)
=
E
r∼Dany
h
1maxf∈F f(γ)⊤r=maxf′∈F(s) f ′(γ)⊤r
i
(81)
=
E
r∼Dany
h
1maxf∈F f(γ)⊤r=maxf′∈Fnd(s) f ′(γ)⊤r
i
(82)
=: pD′  F(γ) ≥Fnd(s, γ)

.
(83)
Equation (81) follows because lemma E.1 shows that π is optimal iff it induces an optimal visit
distribution f at every state. Equation (82) follows because ∀r ∈R|S| : maxf ′∈F(s) f ′(γ)⊤r =
maxf ′∈Fnd(s) f ′(γ)⊤r by lemma E.34.
E.3
Basic properties of POWER
Lemma E.38 (POWER identities). Let γ ∈(0, 1).
POWERDbound (s, γ) =
E
r∼Dbound
"
max
f∈Fnd(s)
1 −γ
γ
 f(γ) −es
⊤r
#
(84)
= 1 −γ
γ
E
r∼Dbound

V ∗
R (s, γ) −R(s)

(85)
= 1 −γ
γ

V ∗
Dbound (s, γ) −
E
R∼Dbound

R(s)

(86)
=
E
R∼Dbound

max
π∈Π
E
s′∼T(s,π(s))
h
(1 −γ) V π
R
 s′, γ
i

.
(87)
30
Proof.
POWERDbound(s, γ) :=
E
r∼Dbound
"
max
f∈F(s)
1 −γ
γ
 f(γ) −es
⊤r
#
(88)
=
E
r∼Dbound
"
max
f∈Fnd(s)
1 −γ
γ
 f(γ) −es
⊤r
#
(89)
=
E
r∼Dbound
"
max
f∈F(s)
1 −γ
γ
 f(γ) −es
⊤r
#
(90)
= 1 −γ
γ
E
r∼Dbound

V ∗
R (s, γ) −R(s)

(91)
= 1 −γ
γ

V ∗
Dbound (s, γ) −
E
R∼Dbound

R(s)

(92)
=
E
r∼Dbound

max
π∈Π
E
s′∼T(s,π(s))
h
(1 −γ) f π,s′(γ)⊤r
i


(93)
=
E
R∼Dbound

max
π∈Π
E
s′∼T(s,π(s))
h
(1 −γ) V π
R
 s′, γ
i

.
(94)
Equation (89) follows from lemma E.34. Equation (91) follows from the dual formulation of optimal
value functions. Equation (92) holds by the deﬁnition of V ∗
Dbound (s, γ) (deﬁnition 5.1). Equation (93)
holds because f π,s(γ) = es + γ Es′∼T(s,π(s))
h
f π,s′(γ)
i
by the deﬁnition of a visit distribution
function (deﬁnition 3.3).
Deﬁnition E.39 (Discount-normalized value function). Let π be a policy, R a reward function, and s
a state. For γ ∈[0, 1], V π
R, norm (s, γ) := limγ∗→γ(1 −γ∗)V π
R (s, γ∗).
Lemma E.40 (Normalized value functions have uniformly bounded derivative). There exists K ≥0
such that for all reward functions r ∈R|S|, sups∈S,π∈Π,γ∈[0,1]
 d
dγ V π
R, norm (s, γ)
 ≤K ∥r∥1.
Proof. Let π be any policy, s a state, and R a reward function. Since V π
R, norm (s, γ) = limγ∗→γ(1 −
γ∗)f π,s(γ∗)⊤r,
d
dγ V π
R, norm (s, γ) is controlled by the behavior of limγ∗→γ(1 −γ∗)f π,s(γ∗). We
show that this function’s gradient is bounded in inﬁnity norm.
By lemma E.4, f π,s(γ) is a multivariate rational function on γ.
Therefore, for any state s′,
f π,s(γ)⊤es′ =
P (γ)
Q(γ) in reduced form. By proposition E.3, 0 ≤f π,s(γ)⊤es′ ≤
1
1−γ . Thus,
Q may only have a root of multiplicity 1 at γ = 1, and Q(γ) ̸= 0 for γ ∈[0, 1).
Let
fs′(γ) := (1 −γ)f π,s(γ)⊤es′.
If Q(1) ̸= 0, then the derivative f ′
s′(γ) is bounded on γ ∈[0, 1) because the polynomial (1 −γ)P(γ)
cannot diverge on a bounded domain.
If Q(1) = 0, then factor out the root as Q(γ) = (1 −γ)Q∗(γ).
f ′
s′(γ) = d
dγ
(1 −γ)P(γ)
Q(γ)

(95)
= d
dγ
 P(γ)
Q∗(γ)

(96)
= P ′(γ)Q∗(γ) −(Q∗)′(γ)P(γ)
(Q∗(γ))2
.
(97)
Since Q∗(γ) is a polynomial with no roots on γ ∈[0, 1], f ′
s′(γ) is bounded on γ ∈[0, 1).
31
Therefore, whether or not Q(γ) has a root at γ = 1, f ′
s′(γ) is bounded on γ ∈[0, 1). Furthermore,
supγ∈[0,1)
∇(1 −γ)f π,s(γ)

∞= supγ∈[0,1) maxs′∈S
f ′
s′(γ)
 is ﬁnite since there are only ﬁnitely
many states.
There are ﬁnitely many π ∈Π, and ﬁnitely many states s, and so there exists some K′ such that
sup
s∈S,
π∈Π,γ∈[0,1)
∇(1 −γ)f π,s(γ)

∞≤K′. Then
∇(1 −γ)f π,s(γ)

1 ≤|S| K′ =: K.
sup
s∈S,
π∈Π,γ∈[0,1)

d
dγ V π
R,norm (s, γ)
 :=
sup
s∈S,
π∈Π,γ∈[0,1)

d
dγ lim
γ∗→γ(1 −γ∗)V π
R (s, γ∗)

(98)
=
sup
s∈S,
π∈Π,γ∈[0,1)

d
dγ (1 −γ)V π
R (s, γ)

(99)
=
sup
s∈S,
π∈Π,γ∈[0,1)
∇(1 −γ)f π,s(γ)⊤r

(100)
≤
sup
s∈S,
π∈Π,γ∈[0,1)
∇(1 −γ)f π,s(γ)

1 ∥r∥1
(101)
≤K ∥r∥1 .
(102)
Equation (99) holds because V π
R (s, γ) is continuous on γ ∈[0, 1) by corollary E.5. Equation (101)
holds by the Cauchy-Schwarz inequality.
Since
 d
dγ V π
R,norm (s, γ)
 is bounded for all γ ∈[0, 1), eq. (102) also holds for γ →1.
Lemma 5.3 (Continuity of POWER). POWERDbound (s, γ) is Lipschitz continuous on γ ∈[0, 1].
Proof. Let b, c be such that supp(Dbound) ⊆[b, c]|S|. For any r ∈supp(Dbound) and π ∈Π,
V π
R, norm (s, γ) has Lipschitz constant K ∥r∥1 ≤K |S| ∥r∥∞≤K |S| max(|c| , |b|) on γ ∈(0, 1) by
lemma E.40.
For γ ∈(0, 1), POWERDbound (s, γ) = ER∼Dbound

maxπ∈Π Es′∼T(s,π(s))
h
(1 −γ)V π
R
 s′, γ
i
by
eq. (94). The expectation of the maximum of a set of functions which share a Lipschitz constant,
also shares the Lipschitz constant. This shows that POWERDbound (s, γ) is Lipschitz continuous on
γ ∈(0, 1). Thus, its limits are well-deﬁned as γ →0 and γ →1. So it is Lipschitz continuous on
the closed unit interval.
Proposition 5.4 (Maximal POWER). POWERDbound (s, γ) ≤ER∼Dbound

maxs∈S R(s)

, with equality
if s can deterministically reach all states in one step and all states are 1-cycles.
Proof. Let γ ∈(0, 1).
POWERDbound (s, γ) =
E
R∼Dbound
"
max
π∈Π
E
s′∼T (s,π(s))
h
(1 −γ)V ∗
R
 s′, γ
i#
(103)
≤
E
R∼Dbound
"
max
π∈Π
E
s′∼T (s,π(s))

(1 −γ)maxs′′∈S R(s′′)
1 −γ
#
(104)
=
E
R∼Dbound

max
s′′∈S R(s′′)

.
(105)
Equation (103) follows from lemma E.38.
Equation (104) follows because V ∗
R
 s′, γ

≤
maxs′′∈S R(s′′)
1−γ
, as no policy can do better than achieving maximal reward at each time step. Taking
limits, the inequality holds for all γ ∈[0, 1].
Suppose that s can deterministically reach all states in one step and all states are 1-cycles. Then
eq. (104) is an equality for all γ ∈(0, 1), since for each R, the agent can select an action which
32
deterministically transitions to a state with maximal reward. Thus the equality holds for all γ ∈
[0, 1].
Lemma E.41 (Lower bound on current POWER based on future POWER).
POWERDbound (s, γ) ≥(1 −γ) min
a
E
s′∼T (s,a),
R∼Dbound

R(s′)

+ γ max
a
E
s′∼T (s,a)
h
POWERDbound
 s′, γ
i
.
(106)
Proof. Let γ ∈(0, 1) and let a∗∈arg maxa Es′∼T (s,a)
h
POWERDbound
 s′, γ
i
.
POWERDbound (s, γ)
(107)
= (1 −γ)
E
R∼Dbound
"
max
a
E
s′∼T (s,a)
h
V ∗
R
 s′, γ
i#
(108)
≥(1 −γ) max
a
E
s′∼T (s,a)

E
R∼Dbound
h
V ∗
R
 s′, γ
i
(109)
= (1 −γ) max
a
E
s′∼T (s,a)
h
V ∗
Dbound
 s′, γ
i
(110)
= (1 −γ) max
a
E
s′∼T (s,a)

E
R∼Dbound

R(s′)

+
γ
1 −γ POWERDbound
 s′, γ

(111)
≥(1 −γ)
E
s′∼T (s,a∗)

E
R∼Dbound

R(s′)

+
γ
1 −γ POWERDbound
 s′, γ

(112)
≥(1 −γ) min
a
E
s′∼T (s,a),
R∼Dbound

R(s′)

+ γ
E
s′∼T (s,a∗)
h
POWERDbound
 s′, γ
i
.
(113)
Equation (108) holds by lemma E.38. Equation (109) follows because Ex∼X

maxa f(a, x)

≥
maxa Ex∼X

f(a, x)

by Jensen’s inequality, and eq. (111) follows by lemma E.38.
The inequality also holds when we take the limits γ →0 or γ →1.
Proposition 5.5 (POWER is smooth across reversible dynamics). Let Dbound be bounded [b, c]. Sup-
pose s and s′ can both reach each other in one step with probability 1.
POWERDbound (s, γ) −POWERDbound
 s′, γ
  ≤(c −b)(1 −γ).
(3)
Proof. Suppose γ ∈[0, 1]. First consider the case where POWERDbound (s, γ) ≥POWERDbound
 s′, γ

.
POWERDbound
 s′, γ

≥(1 −γ) min
a
E
sx∼T (s′,a),
R∼Dbound

R(sx)

+ γ max
a
E
sx∼T (s′,a)

POWERDbound (sx, γ)

(114)
≥(1 −γ)b + γPOWERDbound (s, γ) .
(115)
Equation (114) follows by lemma E.41. Equation (115) follows because reward is lower-bounded by
b and because s′ can reach s in one step with probability 1.
POWERDbound (s, γ) −POWERDbound
 s′, γ
 = POWERDbound (s, γ) −POWERDbound
 s′, γ

(116)
≤POWERDbound (s, γ) −
 (1 −γ)b + γPOWERDbound (s, γ)

(117)
= (1 −γ)
 POWERDbound (s, γ) −b

(118)
≤(1 −γ)
 
E
R∼Dbound

max
s′′∈S R(s′′)

−b
!
(119)
≤(1 −γ)(c −b).
(120)
33
Equation (116) follows because POWERDbound (s, γ) ≥POWERDbound
 s′, γ

. Equation (117) follows
by eq. (115). Equation (119) follows by proposition 5.4. Equation (120) follows because reward
under Dbound is upper-bounded by c.
The case where POWERDbound (s, γ) ≤POWERDbound
 s′, γ

is similar, leveraging the fact that s can
also reach s′ in one step with probability 1.
E.4
Seeking POWER is often more probable under optimality
E.4.1
Keeping options open tends to be POWER-seeking and tends to be optimal
Deﬁnition E.42 (Normalized visit distribution function). Let f : [0, 1) →R|S| be a vector function.
For γ ∈[0, 1], NORM (f, γ) := limγ∗→γ(1 −γ∗)f(γ∗) (this limit need not exist for arbitrary f). If
F is a set of such f, then NORM (F, γ) :=

NORM (f, γ) | f ∈F
	
.
Remark. RSD (s) = NORM
 F(s), 1

.
Lemma E.43 (Normalized visit distribution functions are continuous). Let ∆s ∈∆(S) be a state
probability distribution, let π ∈Π, and let f ∗:= Es∼∆s [f π,s]. NORM (f ∗, γ) is continuous on
γ ∈[0, 1].
Proof.
NORM (f ∗, γ) := lim
γ∗→γ(1 −γ∗)
E
s∼∆s

f π,s(γ∗)

(121)
=
E
s∼∆s

lim
γ∗→γ(1 −γ∗)f π,s(γ∗)

(122)
=:
E
s∼∆s

NORM (f π,s, γ)

.
(123)
Equation (122) follows because the expectation is over a ﬁnite set. Each f π,s ∈F(s) is continuous
on γ ∈[0, 1) by lemma E.4, and limγ∗→1(1 −γ∗)f π,s(γ∗) exists because RSDs are well-deﬁned
[Puterman, 2014]. Therefore, each NORM (f π,s, γ) is continuous on γ ∈[0, 1]. Lastly, eq. (123)’s
expectation over ﬁnitely many continuous functions is itself continuous.
Lemma E.44 (Non-domination of normalized visit distribution functions). Let ∆s ∈∆(S)
be a state probability distribution and let F :=

Es∼∆s [f π,s] | π ∈Π
	
.
For all γ ∈[0, 1],
ND
 NORM (F, γ)

⊆NORM
 ND (F) , γ

, with equality when γ ∈(0, 1).
Proof. Suppose γ ∈(0, 1).
ND
 NORM (F, γ)

= ND
 (1 −γ)F(γ)

(124)
= (1 −γ)ND
 F(γ)

(125)
= (1 −γ)
 ND (F) (γ)

(126)
= NORM
 ND (F) , γ

.
(127)
Equation (124) and eq. (127) follow by the continuity of NORM (f, γ) (lemma E.43). Equation (125)
follows by lemma E.15 item 1. Equation (126) follows by lemma E.32.
Let γ = 1. Let d ∈ND
 NORM (F, 1)

be strictly optimal for r∗∈R|S|. Then let Fd ⊆F be the
subset of f ∈F such that NORM (f, 1) = d.
max
f∈Fd NORM (f, 1)⊤r∗>
max
f ′∈F \Fd NORM
 f ′, 1
⊤r∗.
(128)
Since NORM (f, 1) is continuous at γ = 1 (lemma E.43), x⊤r∗is continuous on x ∈R|S|, and F
is ﬁnite, eq. (128) holds for some γ∗∈(0, 1) sufﬁciently close to γ = 1. By lemma E.10, at least
one f ∈Fd is an element of ND
 F(γ∗)

. Then by lemma E.32, f ∈ND (F). We conclude that
ND
 NORM (F, 1)

⊆NORM
 ND (F) , 1

.
The case for γ = 0 proceeds similarly.
34
Lemma E.45 (POWER limit identity). Let γ ∈[0, 1].
POWERDbound (s, γ) =
E
r∼Dbound
"
max
f∈Fnd(s) lim
γ∗→γ
1 −γ∗
γ∗
 f(γ∗) −es
⊤r
#
.
(129)
Proof. Let γ ∈[0, 1].
POWERDbound (s, γ) = lim
γ∗→γ POWERDbound (s, γ∗)
(130)
= lim
γ∗→γ
E
r∼Dbound
"
max
f∈Fnd(s)
1 −γ∗
γ∗
 f(γ∗) −es
⊤r
#
(131)
=
E
r∼Dbound
"
lim
γ∗→γ
max
f∈Fnd(s)
1 −γ∗
γ∗
 f(γ∗) −es
⊤r
#
(132)
=
E
r∼Dbound
"
max
f∈Fnd(s) lim
γ∗→γ
1 −γ∗
γ∗
 f(γ∗) −es
⊤r
#
.
(133)
Equation (130) follows because POWERDbound (s, γ) is continuous on γ ∈[0, 1] by lemma 5.3.
Equation (131) follows by lemma E.38.
For γ∗∈(0, 1), let fγ∗(r) := maxf∈Fnd(s)
1−γ∗
γ∗
 f(γ∗) −es
⊤r. For any sequence γn →γ,
 fγn
∞
n=1 is a sequence of functions which are piecewise linear on r ∈R|S|, which means they are
continuous and therefore measurable. Since lemma E.4 shows that each f ∈Fnd(s) is multivariate
rational on γ∗(and therefore continuous on γ∗),

fγn
	∞
n=1 converges pointwise to limit function fγ.
Furthermore,
V ∗
R (s, γn) −R(s)
 ≤
γ
1−γn ∥R∥∞, and so
fγn(r)
 =
 1−γn
γn (V ∗
R (s, γn) −R(s))
 ≤
g(r) ≤∥r∥∞=: g(r), which is measurable. Therefore, apply Lebesgue’s dominated convergence
theorem to conclude that eq. (132) holds. Equation (133) holds because max is a continuous
function.
Lemma E.46 (Lemma for POWER superiority). Let ∆1, ∆2 ∈∆(S) be state probability dis-
tributions. For i = 1, 2, let F∆i :=

γ−1 Esi∼∆i [f π,si −esi] | π ∈Π
	
. Suppose F∆2 con-
tains a copy of ND (F∆1) via φ. Then ∀γ ∈[0, 1] : Es1∼∆1

POWERDbound (s1, γ)

≤most: Dbound
Es2∼∆2

POWERDbound (s2, γ)

.
If ND (F∆2) \ φ · ND (F∆1) is non-empty, then for all γ ∈(0, 1), the inequality is strict for all
DX-IID ∈DC/B/IID and Es1∼∆1

POWERDbound (s1, γ)

̸≥most: Dbound Es2∼∆2

POWERDbound (s2, γ)

.
These results also hold when replacing F∆i with F ∗
∆i :=

Esi∼∆i [f π,si] | π ∈Π
	
for i = 1, 2.
Proof.
φ · ND
 NORM (F∆1, γ)

⊆φ · NORM
 ND (F∆1) , γ

(134)
:=

Pφ lim
γ∗→γ(1 −γ∗)f(γ∗) | f ∈ND (F∆1)

(135)
=

lim
γ∗→γ(1 −γ∗)Pφf(γ∗) | f ∈ND (F∆1)

(136)
=

lim
γ∗→γ(1 −γ∗)f(γ∗) | f ∈F ′
sub

(137)
⊆

lim
γ∗→γ(1 −γ∗)f(γ∗) | f ∈F∆2

(138)
=: NORM (F∆2, γ) .
(139)
Equation (134) follows by lemma E.44. Equation (136) follows because Pφ is a continuous linear
operator. Equation (138) follows by assumption.
E
s1∼∆1

POWERDbound (s1, γ)
 :=
E
s1∼∆1,
r∼Dbound

max
π∈Π lim
γ∗→γ
1 −γ∗
γ∗
 f π,s1(γ∗) −es1
⊤r

(140)
35
=
E
r∼Dbound

max
π∈Π lim
γ∗→γ
1 −γ∗
γ∗
E
s1∼∆1

f π,s1(γ∗) −es1
⊤r

(141)
=
E
r∼Dbound


max
d∈NORM(F∆1,γ)
d⊤r


(142)
=
E
r∼Dbound


max
d∈ND

NORM(F∆1,γ)
 d⊤r


(143)
≤most: Dbound
E
r∼Dbound


max
d∈NORM(F∆2,γ)
d⊤r


(144)
=
E
r∼Dbound

max
π∈Π lim
γ∗→γ
1 −γ∗
γ∗
E
s2∼∆2

f π,s2(γ∗) −es2
⊤r

(145)
=
E
s2∼∆2,
r∼Dbound

max
π∈Π lim
γ∗→γ
1 −γ∗
γ∗
 f π,s2(γ∗) −es2
⊤r

(146)
=:
E
s2∼∆2

POWERDbound (s2, γ)

.
(147)
Equation (140) and eq. (147) follow by lemma E.45. Equation (141) and eq. (146) follow because
each R has a stationary deterministic optimal policy π ∈Π∗(R, γ) ⊆Π which simultaneously
achieves optimal value at all states. Equation (143) follows by corollary E.11.
Apply lemma E.24 with A := NORM (F∆1, γ) , B := NORM (F∆2, γ), g the identity function, and
involution φ (satisfying φ · ND (A) ⊆B by eq. (139)) in order to conclude that eq. (144) holds.
Suppose that ND (F∆2) \ φ · ND (F∆1) is non-empty; let F ′
sub := φ · ND (F∆1). Lemma E.32
shows that for all γ ∈(0, 1), ND
 F∆2(γ)

\ F ′
sub(γ) is non-empty. Lemma E.15 item 1 then im-
plies that ND (B) \ φ · A =
1−γ
γ

ND
 F∆2(γ)

−es

\

1−γ
γ F ′
sub(γ)

is non-empty. Then
lemma E.24 implies that for all γ ∈(0, 1), eq. (144) is strict for all DX-IID ∈DC/B/IID and
Es1∼∆1

POWERDbound (s1, γ)

̸≥most: Dbound Es2∼∆2

POWERDbound (s2, γ)

.
We show that this result’s preconditions holding for F ∗
∆i implies the F∆i preconditions. Suppose
F ∗
∆i :=

Esi∼∆i [f π,si] | π ∈Π
	
for i = 1, 2 are such that F ∗
sub := φ · ND

F ∗
∆1

⊆F ∗
∆2. In the
following, the ∆i are represented as vectors in R|S|, and γ is a variable.
φ ·

γf | f ∈ND (F∆1)
	
= φ ·

ND
 F ∗
∆1 −∆1

(148)
= φ ·

ND
 F ∗
∆1

−∆1

(149)
=
n
Pφf −Pφ∆1 | f ∈ND
 F ∗
∆1
o
(150)
⊆

f −∆2 | f ∈F ∗
∆2
	
(151)
=

γf | f ∈F∆2
	
.
(152)
Equation (149) follows from lemma E.15 item 2. Since we assumed that φ · ND

F ∗
∆1

⊆F ∗
∆2,
φ · {∆1} = φ ·

ND

F ∗
∆1

(0)

⊆F ∗
∆2(0) = {∆2}. This implies that Pφ∆1 = ∆2 and so
eq. (151) follows.
Equation (152) shows that φ ·

γf | f ∈ND (F∆1)
	
⊆

γf | f ∈F∆2
	
.
But we then
have φ ·

γf | f ∈ND (F∆1)
	 :=

γPφf | f ∈ND (F∆1)
	
=

γf | f ∈φ · ND (F∆1)
	
⊆

γf | f ∈F∆2
	
. Thus, φ · ND (F∆1) ⊆F∆2.
36
Suppose ND

F ∗
∆2

\ φ · ND

F ∗
∆1

is non-empty, which implies that
φ ·

γf | f ∈ND (F∆1)
	
=
n
Pφf −Pφ∆1 | f ∈ND
 F ∗
∆1
o
(153)
=
n
f −Pφ∆1 | f ∈φ · ND
 F ∗
∆1
o
(154)
⊊
n
f −∆2 | f ∈ND
 F ∗
∆2
o
(155)
=

γf | f ∈ND (F∆2)
	
.
(156)
Then ND (F∆2) \ φ · ND (F∆1) must be non-empty. Therefore, if the preconditions of this result are
met for F ∗
∆i, they are met for F∆i.
Proposition 6.6 (States with “more options” have more POWER). If F(s) contains a copy of Fnd(s′)
via φ, then ∀γ ∈[0, 1] : POWERDbound(s, γ) ≥most POWERDbound(s′, γ). If Fnd(s) \ φ · Fnd(s′) is
non-empty, then for all γ ∈(0, 1), the converse ≤most statement does not hold.
Proof. Let Fsub := φ · Fnd(s′) ⊆F(s).
Let ∆1 := es′, ∆2 := es, and deﬁne F ∗
∆i :=

Esi∼∆i [f π,si] | π ∈Π
	
for i = 1, 2.
Then Fnd(s′) = ND

F ∗
∆1

is similar to Fsub =
F ∗
sub ⊆F ∗
∆2 = F(s) via involution φ.
Apply lemma E.46 to conclude that ∀γ ∈[0, 1] :
POWERDbound
 s′, γ

≤most: Dbound POWERDbound (s, γ).
Furthermore, Fnd(s) = ND

F ∗
∆2

, and Fsub = F ∗
sub, and so if Fnd(s) \ φ · Fnd(s′) := Fnd(s) \
Fsub = ND

F ∗
∆2

\ F ∗
sub is non-empty, then lemma E.46 shows that for all γ ∈(0, 1), the inequality
is strict for all DX-IID ∈DC/B/IID and POWERDbound
 s′, γ

̸≥most: Dbound POWERDbound (s, γ).
Lemma E.47 (Non-dominated visit distribution functions never agree with other visit distribution
functions at that state). Let f ∈Fnd(s), f ′ ∈F(s) \ {f}. ∀γ ∈(0, 1) : f(γ) ̸= f ′(γ).
Proof. Let γ ∈(0, 1). Since f ∈Fnd(s), there exists a γ∗∈(0, 1) at which f is strictly optimal for
some reward function. Then by proposition E.30, we can produce another reward function for which
f is strictly optimal at discount rate γ; in particular, proposition E.30 guarantees that the policies
which induce f ′ are not optimal at γ. So f(γ) ̸= f ′(γ).
Corollary E.48 (Cardinality of non-dominated visit distributions). Let F ⊆F(s). ∀γ ∈(0, 1) :
F ∩Fnd(s)
 =
F(γ) ∩Fnd(s, γ)
.
Proof. Let γ ∈(0, 1). By applying lemma E.32 with ∆d := es, f ∈Fnd(s) = ND
 F(s)

iff
f(γ) ∈ND
 F(s, γ)

. By lemma E.33, ND
 F(s, γ)

= Fnd(s, γ). So all f ∈F ∩Fnd(s) induce
f(γ) ∈F(γ) ∩Fnd(s, γ), and
F ∩Fnd(s)
 ≥
F(γ) ∩Fnd(s, γ)
.
Lemma E.47 implies that for all f, f ′ ∈Fnd(s), f = f ′ iff f(γ) = f ′(γ). Therefore,
F ∩Fnd(s)
 ≤
F(γ) ∩Fnd(s, γ)
. So
F ∩Fnd(s)
 =
F(γ) ∩Fnd(s, γ)
.
Lemma E.49 (Optimality probability and state bottlenecks). Suppose that s can reach
REACH
 s′, a′
∪REACH
 s′, a

, but only by taking actions equivalent to a′ or a at state s′.
Fnd,a′ := Fnd(s | π(s′) = a′), Fa := F(s | π(s′) = a).
Suppose Fa contains a copy
of Fnd,a′ via φ which ﬁxes all states not belonging to REACH
 s′, a′
∪REACH
 s′, a

. Then
∀γ ∈[0, 1] : PDany
 Fnd,a′, γ

≤most: Dany PDany (Fa, γ).
If Fnd(s) ∩
 Fa \ φ · Fnd,a′
is non-empty, then for all γ ∈(0, 1), the inequality is strict for all
DX-IID ∈DC/B/IID, and PDany
 Fnd,a′, γ

̸≥most: Dany PDany (Fa, γ).
37
Proof. Let Fsub := φ · Fnd,a′. Let F ∗:= S
a′′∈A:
(a′′̸≡s′a)∧(a′′̸≡s′a′)
F(s | π(s′) = a′′) ∪Fnd,a′ ∪Fsub.
φ · F ∗:= φ ·






[
a′′∈A:
(a′′̸≡s′a)∧(a′′̸≡s′a′)
F(s | π(s′) = a′′) ∪Fnd,a′ ∪Fsub






(157)
=
[
a′′∈A:
(a′′̸≡s′a)∧(a′′̸≡s′a′)
φ · F(s | π(s′) = a′′) ∪
 φ · Fnd,a′
∪(φ · Fsub)
(158)
=
[
a′′∈A:
(a′′̸≡s′a)∧(a′′̸≡s′a′)
φ · F(s | π(s′) = a′′) ∪Fsub ∪Fnd,a′
(159)
=
[
a′′∈A:
(a′′̸≡s′a)∧(a′′̸≡s′a′)
F(s | π(s′) = a′′) ∪Fsub ∪Fnd,a′
(160)
=: F ∗.
(161)
Equation (159) follows because the involution φ ensures that φ · Fsub = Fnd,a′. By assumption, φ
ﬁxes all s′ ̸∈REACH
 s′, a′
∪REACH
 s′, a

. Suppose f ∈F(s)\
 Fnd,a′ ∪Fa

. By the bottleneck
assumption, f does not visit states in REACH
 s′, a′
∪REACH
 s′, a

. Therefore, Pφf = f, and so
eq. (160) follows.
Let FZ :=
 F(s) \ (F(s | π(s) = a′) ∪Fa)

∪Fnd,a′ ∪Fa. By deﬁnition, FZ ⊆F(s). Furthermore,
Fnd(s) = S
a′′∈A Fnd(s | π(s′) = a′′) ⊆
 F(s) \ (F(s | π(s) = a′) ∪Fa)

∪Fnd(s | π(s) =
a′) ∪Fa =: FZ, and so Fnd(s) ⊆FZ. Note that F ∗= FZ \ (Fa \ Fsub).
Case: γ ∈(0, 1).
PDany
 Fnd,a′, γ

= pDany
 Fnd,a′(γ) ≥F(s, γ)

(162)
≤most: Dany pDany
 Fa(γ) ≥F(s, γ)

(163)
= PDany
 Fnd,a′, γ

.
(164)
Equation (162) and eq. (164) follow from lemma E.37.
Equation (163) follows by applying
lemma E.28 with A := Fnd,a′(γ), B′ := Fsub(γ), B := Fa(γ), C := F(s, γ), Z := FZ(γ)
which satisﬁes ND (C) = Fnd(s, γ) ⊆FZ(γ) ⊆F(s, γ) = C, and involution φ which satis-
ﬁes φ · F ∗(γ) = φ ·

Z \
 B \ B′
= Z \
 B \ B′
= F ∗(γ).
Suppose
Fnd(s) ∩
 Fa \ Fsub

is
non-empty.
0
<
Fnd(s) ∩
 Fa \ Fsub

=
Fnd(s, γ) ∩
 Fa(γ) \ Fsub(γ)

=:
ND (C) ∩
 B \ B′ (with the ﬁrst equality hold-
ing by corollary E.48),
and so
ND (C) ∩
 B \ B′
is non-empty.
We also have
B := Fa(γ) ⊆F(s, γ) =: C.
Then reapplying lemma E.28, eq. (163) is strict for all
DX-IID ∈DC/B/IID, and PDany
 Fnd,a′, γ

̸≥most: Dany PDany (Fa, γ).
Case: γ = 1, γ = 0.
PDany
 Fnd,a′, 1

= lim
γ∗→1 PDany
 Fnd,a′, γ∗
(165)
= lim
γ∗→1 pDany
 Fnd,a′(γ∗) ≥F(s, γ∗)

(166)
≤most: Dany lim
γ∗→1 pDany
 Fa(γ∗) ≥F(s, γ∗)

(167)
= lim
γ∗→1 PDany (Fa, γ∗)
(168)
38
= PDany (Fa, 1) .
(169)
Equation (165) and eq. (169) hold by proposition E.36. Equation (166) and eq. (168) follow by
lemma E.37. Applying lemma E.29 with γ := 1, I := (0, 1), FA := Fnd,a′, FB := Fa, FC := F(s),
FZ as deﬁned above, and involution φ (for which φ ·

FZ \
 FB \ φ · FA

= FZ \
 FB \ φ · FA

),
we conclude that eq. (167) follows.
The γ = 0 case proceeds similarly to γ = 1.
Lemma E.50 (Action optimality probability is a special case of visit distribution optimality probabil-
ity). PDany (s, a, γ) = PDany
 F(s | π(s) = a), γ

.
Proof. Let Fa := F(s | π(s) = a). For γ ∈(0, 1),
P
Dany (s, a, γ) :=
P
R∼Dany
 ∃π∗∈Π∗(R, γ) : π∗(s) = a

(170)
=
P
r∼Dany
 
∃f π∗,s ∈Fa : f π∗,s(γ)⊤r = max
f∈F(s) f(γ)⊤r
!
(171)
= PDany (Fa, γ) .
(172)
By lemma E.1, if ∃π∗∈Π∗(R, γ) : π∗(s) = a, then it induces some optimal f π∗,s ∈Fa. Conversely,
if f π∗,s ∈Fa is optimal at γ ∈(0, 1), then π∗chooses optimal actions on the support of f π∗,s(γ). Let
π′ agree with π∗on that support and let π′ take optimal actions at all other states. Then π′ ∈Π∗(R, γ)
and π′(s) = a. So eq. (171) follows.
Suppose γ = 0 or γ = 1. Consider any sequence (γn)∞
n=1 converging to γ, and let Dany induce
probability measure F.
PDany (Fa, γ) := lim
γ∗→γ PDany (Fa, γ∗)
(173)
= lim
γ∗→γ
P
R∼Dany
 ∃π∗∈Π∗(R, γ∗) : π∗(s) = a

(174)
= lim
n→∞
P
R∼Dany
 ∃π∗∈Π∗(R, γn) : π∗(s) = a

(175)
= lim
n→∞
Z
RS 1∃π∗∈Π∗(R,γn):π∗(s)=a dF(R)
(176)
=
Z
RS lim
n→∞1∃π∗∈Π∗(R,γn):π∗(s)=a dF(R)
(177)
=
Z
RS 1∃π∗∈Π∗(R,γ):π∗(s)=a dF(R)
(178)
=: P
Dany (s, a, γ) .
(179)
Equation (174) follows by eq. (172). for γ∗∈[0, 1], let fγ∗(R) := 1∃π∗∈Π∗(R,γ∗):π∗(s)=a. For
each R ∈RS, lemma E.35 exists γx ≈γ such that for all intermediate γ′
x between γx and γ,
Π∗ R, γ′
x

= Π∗(R, γ). Since γn →γ, this means that
 fγn
∞
n=1 converges pointwise to fγ.
Furthermore, ∀n ∈N, R ∈RS :
fγn(R)
 ≤1 by deﬁnition. Therefore, eq. (177) follows by
Lebesgue’s dominated convergence theorem.
Proposition 6.9 (Keeping options open tends to be POWER-seeking and tends to be optimal).
Suppose Fa := F(s | π(s) = a) contains a copy of Fa′ := F(s | π(s) = a′) via φ.
1. If s ̸∈REACH
 s, a′
, then ∀γ ∈[0, 1] : Esa∼T (s,a)

POWERDbound (sa, γ)

≥most: Dbound
Esa′∼T (s,a′)

POWERDbound (sa′, γ)

.
2. If s can only reach the states of REACH
 s, a′
∪REACH (s, a) by taking actions equivalent
to a′ or a at state s, then ∀γ ∈[0, 1] : PDany (s, a, γ) ≥most: Dany PDany
 s, a′, γ

.
39
If Fnd(s) ∩
 Fa \ φ · Fa′
is non-empty, then ∀γ ∈(0, 1), the converse ≤most statements do not hold.
Proof. Note that by deﬁnition 3.3, Fa′(0) = {es} = Fa(0). Since φ · Fa′ ⊆Fa, in particular we
have φ · Fa′(0) =

Pφes
	
⊆{es} = Fa(0), and so φ(s) = s.
Item 1. For state probability distribution ∆s ∈∆(S), let F ∗
∆s :=

Es′∼∆s
h
f π,s′i
| π ∈Π

.
Unless otherwise stated, we treat γ as a variable in this item; we apply element-wise vector addition,
constant multiplication, and variable multiplication via the conventions outlined in deﬁnition E.14.
Fa′ =
(
es + γ
E
sa′∼T (s,a′) [f π,sa′] | π ∈Π : π(s) = a′
)
(180)
=
(
es + γ
E
sa′∼T (s,a′) [f π,sa′] | π ∈Π
)
(181)
= es + γF ∗
T (s,a′).
(182)
Equation (180) follows by deﬁnition 3.3, since each f ∈F(s) has an initial term of es. Equation (181)
follows because s ̸∈REACH
 s, a′
, and so for all sa′ ∈supp(T(s, a′)), f π,sa′ is unaffected by the
choice of action π(s). Note that similar reasoning implies that Fa ⊆es +γF ∗
T (s,a) (because eq. (181)
is a containment relation in general).
Since Fa′ = es + γF ∗
T (s,a′), if Fa contains a copy of Fa′ via φ, then F ∗
T (s,a) contains a copy of
F ∗
T (s,a′) via φ. Then φ · ND

F ∗
T (s,a′)

⊆φ · F ∗
T (s,a′) ⊆F ∗
T (s,a), and so F ∗
T (s,a) contains a copy of
ND

F ∗
T (s,a′)

. Then apply lemma E.46 with ∆1 := T(s, a′) and ∆2 := T(s, a) to conclude that
∀γ ∈[0, 1] : Esa′∼T (s,a′)

POWERDbound (sa′, γ)

≤most: Dbound Esa∼T (s,a)

POWERDbound (sa, γ)

.
Suppose Fnd(s) ∩
 Fa \ φ · Fa′
is non-empty. To apply the second condition of lemma E.46, we
want to demonstrate that ND

F ∗
T (s,a)

\ φ · ND

F ∗
T (s,a′)

is also non-empty.
First consider f ∈Fnd(s) ∩Fa. Because Fa ⊆es + γF ∗
T (s,a), we have that γ−1(f −es) ∈F ∗
T (s,a).
Because f ∈Fnd(s), by deﬁnition 3.6, ∃r ∈R|S|, γx ∈(0, 1) such that
f(γx)⊤r >
max
f ′∈F(s)\{f} f ′(γx)⊤r.
(183)
Then since γx ∈(0, 1),
γ−1
x (f(γx) −es)⊤r >
max
f ′∈F(s)\{f} γ−1
x (f ′(γx) −es)⊤r
(184)
=
max
f ′∈γ−1
x ((F(s)\{f})−es)
f ′(γx)⊤r
(185)
≥
max
f ′∈γ−1
x ((Fa\{f})−es)
f ′(γx)⊤r
(186)
=
max
f ′∈F ∗
T (s,a)\{γ−1
x
(f−es)}
f ′(γx)⊤r.
(187)
Equation (186) holds because Fa ⊆F(s). By assumption, action a is optimal for r at state s and
at discount rate γx. Equation (181) shows that F ∗
T (s,a) potentially allows the agent a non-stationary
policy choice at s, but non-stationary policies cannot increase optimal value [Puterman, 2014].
Therefore, eq. (187) holds.
We assumed that γ−1(f −es) ∈γ−1(Fnd(s) −es). Furthermore, since we just showed that
γ−1(f −es) ∈F ∗
T (s,a) is strictly optimal over the other elements of F ∗
T (s,a) for reward function r
at discount rate γx ∈(0, 1), we conclude that it is an element of ND

F ∗
T (s,a)

by deﬁnition E.13.
Then we conclude that γ−1(Fnd(s) −es) ∩F ∗
T (s,a) ⊆ND

F ∗
T (s,a)

.
40
We now show that ND

F ∗
T (s,a)

\ φ · ND

F ∗
T (s,a′)

is non-empty.
0 <
Fnd(s) ∩
 Fa \ φ · Fa′
(188)
=
γ−1 
Fnd(s) ∩
 Fa \ φ · Fa′
−es

(189)
≤
γ−1  Fnd(s) −es

∩

F ∗
T (s,a) \ φ · F ∗
T (s,a′)

(190)
=


γ−1  Fnd(s) −es

∩F ∗
T (s,a)

\ φ · F ∗
T (s,a′)

(191)
≤
ND

F ∗
T (s,a)

\ φ · F ∗
T (s,a′)

(192)
≤
ND

F ∗
T (s,a)

\ φ · ND

F ∗
T (s,a′)
 .
(193)
Equation (188) follows by the assumption that Fnd(s) ∩
 Fa \ φ · Fa′
is non-empty. Let f, f ′ ∈
Fnd(s) ∩
 Fa \ φ · Fa′
be distinct. Then we must have that for some γx ∈(0, 1), f(γx) ̸= f ′(γx).
This holds iff γ−1
x (f(γx) −es) ̸= γ−1
x (f ′(γx) −es), and so eq. (189) holds.
Equation (190) holds because Fa ⊆es + γF ∗
T (s,a) and F ′
a = es + γF ∗
T (s,a′) by eq. (182). Equa-
tion (192) holds because we showed above that γ−1(Fnd(s) −es) ∩F ∗
T (s,a) ⊆ND

F ∗
T (s,a)

.
Equation (193) holds because ND

F ∗
T (s,a′)

⊆F ∗
T (s,a′) by deﬁnition E.13.
Therefore, ND

F ∗
T (s,a)

\ φ · ND

F ∗
T (s,a′)

is non-empty, and so apply the second con-
dition of lemma E.46 to conclude that for all DX-IID
∈
DC/B/IID,
∀γ
∈
(0, 1)
:
Esa′∼T (s,a′)

POWERDX-IID (sa′, γ)

< Esa∼T (s,a)

POWERDX-IID (sa, γ)

, and that ∀γ ∈(0, 1) :
Esa′∼T (s,a′)

POWERDbound (sa′, γ)

̸≥most: Dbound Esa∼T (s,a)

POWERDbound (sa, γ)

.
Item 2. Let φ′(sx) := φ(sx) when sx ∈REACH
 s, a′
∪REACH (s, a), and equal sx otherwise.
Since φ is an involution, so is φ′.
φ′ · Fa′ :=


Pφ′
 
es + γ
E
sa′∼T (s,a′) [f π,sa′]
!
| π ∈Π, π(s) = a′



(194)
=
(
es + γ
E
sa′∼T (s,a′)

Pφ′f π,sa′
| π ∈Π, π(s) = a′
)
(195)
=
(
Pφes + γ
E
sa′∼T (s,a′)

Pφf π,sa′
| π ∈Π, π(s) = a′
)
(196)
=: φ · Fa′
(197)
⊆Fa.
(198)
Equation (195) follows because if s ∈REACH
 s, a′
∪REACH (s, a), then we already showed that
φ ﬁxes s. Otherwise, φ′(s) = s by deﬁnition. Equation (196) follows by the deﬁnition of φ′ on
REACH
 s, a′
∪REACH (s, a) and because es = Pφes. Next, we assumed that φ · Fa′ ⊆Fa, and
so eq. (198) holds.
Therefore, Fa contains a copy of Fa′ via φ′ ﬁxing all sx ̸∈REACH
 s, a′
∪REACH (s, a). Therefore,
Fa contains a copy of Fnd,a′ := Fnd(s)∩Fa′ via the same φ′. Then apply lemma E.49 with s′ := s to
conclude that ∀γ ∈[0, 1] : PDany (Fa′, γ) ≤most: Dany PDany (Fa, γ). By lemma E.50, PDany
 s, a′, γ

=
PDany (Fa′, γ) and PDany (s, a, γ) = PDany (Fa, γ). Therefore, ∀γ ∈[0, 1] : PDany
 s, a′, γ

≤most: Dany
PDany (s, a, γ).
41
If Fnd(s) ∩
 Fa \ φ · Fa′
is non-empty, then apply the second condition of lemma E.49 to conclude
that for all γ ∈(0, 1), the inequality is strict for all DX-IID ∈DC/B/IID, and PDany
 s, a′, γ

̸≥most: Dany
PDany (s, a, γ).
E.4.2
When γ = 1, optimal policies tend to navigate towards “larger” sets of cycles
Lemma E.51 (POWER identity when γ = 1).
POWERDbound (s, 1) =
E
r∼Dbound
"
max
d∈RSD(s) d⊤r
#
=
E
r∼Dbound
"
max
d∈RSDnd(s) d⊤r
#
.
(199)
Proof.
POWERDbound (s, 1) =
E
r∼Dbound
"
max
f π,s∈F(s) lim
γ→1
1 −γ
γ
 f π,s(γ) −es
⊤r
#
(200)
=
E
r∼Dbound
"
max
d∈RSD(s) d⊤r
#
(201)
=
E
r∼Dbound
"
max
d∈RSDnd(s) d⊤r
#
.
(202)
Equation (200) follows by lemma E.45. Equation (201) follows by the deﬁnition of RSD (s)
(deﬁnition 6.10). Equation (202) follows because for all r ∈R|S|, corollary E.11 shows that
maxd∈RSD(s) d⊤r = maxd∈ND(RSD(s)) d⊤r =: maxd∈RSDnd(s) d⊤r.
Proposition 6.12 (When γ = 1, RSDs control POWER). If RSD (s) contains a copy of RSDnd
 s′
via φ, then POWERDbound (s, 1) ≥most POWERDbound
 s′, 1

. If RSDnd (s)\φ· RSDnd(s′) is non-empty,
then the converse ≤most statement does not hold.
Proof. Suppose RSDnd
 s′
is similar to D ⊆RSD (s) via involution φ.
POWERDbound
 s′, 1

=
E
r∼Dbound
"
max
d∈RSDnd(s′) d⊤r
#
(203)
≤most: Dbound
E
r∼Dbound
"
max
d∈RSDnd(s) d⊤r
#
(204)
= POWERDbound (s, 1)
(205)
Equation (203) and eq. (205) follow from lemma E.51. By applying lemma E.24 with A :=
RSD
 s′
, B′ := D, B := RSD (s) and g the identity function, eq. (204) follows.
Suppose RSDnd (s) \ D is non-empty. By the same result, eq. (204) is a strict inequality for all
DX-IID ∈DC/B/IID, and we conclude that POWERDbound
 s′, 1

̸≥most: Dbound POWERDbound (s, 1).
Theorem 6.13 (Average-optimal policies tend to end up in “larger” sets of RSDs). Let D, D′ ⊆
RSD (s). Suppose that D contains a copy of D′ via φ, and that the sets D ∪D′ and RSDnd (s) \
 D′ ∪D

have pairwise orthogonal vector elements (i.e. pairwise disjoint vector support). Then
PDany (D, average) ≥most PDany
 D′, average

. If RSDnd (s)∩
 D \ φ · D′
is non-empty, the converse
≤most statement does not hold.
Proof. Let
Dsub
:=
φ · D′,
where
Dsub
⊆
D
by
assumption.
Let
X
:=

si ∈S | maxd∈D′∪D d⊤esi > 0
	
. Deﬁne
φ′(si) :=
(
φ(si)
if si ∈X
si
else.
(206)
42
Since φ is an involution, φ′ is also an involution. Furthermore, by the deﬁnition of X, φ′ · D′ = Dsub
and φ′ · Dsub = D′ (because we assumed that both equalities hold for φ).
Let D∗:= D′ ∪Dsub ∪
 RSDnd (s) \ (D′ ∪D)

.
φ′ · D∗:= φ′ ·

D′ ∪Dsub ∪
 RSDnd (s) \ (D′ ∪D)

(207)
=
 φ′ · D′
∪
 φ′ · Dsub

∪φ′ ·
 RSDnd (s) \ (D′ ∪D)

(208)
= Dsub ∪D′ ∪
 RSDnd (s) \ (D′ ∪D)

(209)
=: D∗.
(210)
In eq. (209), we know that φ′ · D′ = Dsub and φ′ · Dsub = D′. We just need to show that
φ′ ·
 RSDnd (s) \ (D′ ∪D)

= RSDnd (s) \ (D′ ∪D).
Suppose ∃si ∈X, d′ ∈RSDnd (s) \ (D′ ∪D) : d′⊤esi > 0. By the deﬁnition of X, ∃d ∈D′ ∪D :
d⊤esi > 0. Then
d⊤d′ =
|S|
X
j=1
d⊤(d′ ⊙esj)
(211)
≥d⊤(d′ ⊙esi)
(212)
= d⊤
(d′⊤esi)esi

(213)
= (d′⊤esi) · (d⊤esi)
(214)
> 0.
(215)
Equation (211) follows from the deﬁnitions of the dot and Hadamard products. Equation (212)
follows because d and d′ have non-negative entries. Equation (215) follows because d⊤esi and
d′⊤esi are both positive. But eq. (215) shows that d⊤d′ > 0, contradicting our assumption that d
and d′ are orthogonal.
Therefore, such an si cannot exist, and X′ :=
n
s′
i ∈S | maxd′∈RSDnd(s)\(D′∪D) d′⊤esi > 0
o
⊆
(S \ X). By eq. (206), ∀s′
i ∈X′ : φ′(s′
i) = s′
i. Thus, φ′ ·
 RSDnd (s) \ (D′ ∪D)

= RSDnd (s) \
(D′ ∪D), and eq. (209) follows. We conclude that φ′ · D∗= D∗.
Consider Z :=
 RSDnd (s) \ (D′ ∪D)

∪D ∪D′. First, Z ⊆RSD (s) by deﬁnition. Second,
RSDnd (s) = RSDnd (s) \ (D′ ∪D) ∪(RSDnd (s) ∩D′) ∪(RSDnd (s) ∩D) ⊆Z. Note that
D∗= Z \ (D \ Dsub).
PDany
 D′, average

= pDany
 D′ ≥RSD (s)

(216)
≤most: Dany pDany
 D ≥RSD (s)

(217)
= PDany (D, average) .
(218)
Since φ · D′ ⊆D and ND
 D′
⊆D′, φ · ND
 D′
⊆D. Then eq. (217) holds by applying
lemma E.28 with A := D′, B′ := Dsub, B := D, C := RSD (s), and the previously deﬁned Z
which we showed satisﬁes ND (C) ⊆Z ⊆C. Furthermore, involution φ′ satisﬁes φ′ · B∗=
φ′ ·
 Z \ (B \ B′)

= Z \ (B \ B′) = B∗by eq. (210).
When RSDnd (s) ∩
 D \ Dsub

is non-empty, since B′ ⊆C by assumption, lemma E.28 also
shows that eq. (217) is strict for all DX-IID ∈DC/B/IID, and that PDany
 D′, average

̸≥most: Dany
PDany (D, average).
Proposition E.52 (RSD properties). Let d ∈RSD (s). d is element-wise non-negative and ∥d∥1 =
1.
43
Proof. d has non-negative elements because it equals the limit of limγ→1(1−γ)f(γ), whose elements
are non-negative by proposition E.3 item 1.
∥d∥1 =
lim
γ→1(1 −γ)f(γ)

1
(219)
= lim
γ→1(1 −γ)
f(γ)

1
(220)
= 1.
(221)
Equation (219) follows because the deﬁnition of RSDs (deﬁnition 6.10) ensures that ∃f ∈F(s) :
limγ→1(1 −γ)f(γ) = d. Equation (220) follows because ∥·∥1 is a continuous function. Equa-
tion (221) follows because
f(γ)

1 =
1
1−γ by proposition E.3 item 2.
Lemma E.53 (When reachable with probability 1, 1-cycles induce non-dominated RSDs). If es′ ∈
RSD (s), then es′ ∈RSDnd (s).
Proof. If d ∈RSD (s) is distinct from es′, then ∥d∥1 = 1 and d has non-negative entries by
proposition E.52. Since d is distinct from es′, then its entry for index s′ must be strictly less than 1:
d⊤es′ < 1 = e⊤
s′es′. Therefore, es′ ∈RSD (s) is strictly optimal for the reward function r := es′,
and so es′ ∈RSDnd (s).
Corollary 6.14 (Average-optimal policies tend not to end up in any given 1-cycle). Sup-
pose esx, es′
∈
RSD (s) are distinct.
Then PDany
 RSD (s) \ {esx}, average

≥most
PDany
 {esx}, average

. If there is a third es′′ ∈RSD (s), the converse ≤most statement does not
hold.
Proof. Suppose esx, es′ ∈RSD (s) are distinct. Let φ := (sx s′), D′ := {esx} , D := RSD (s) \
{esx}. φ·D′ = {es′} ⊆RSD (s)\{esx} =: D since sx ̸= s′. D′ ∪D = RSD (s) and RSDnd (s)\
(D′ ∪D) = RSDnd (s)\RSD (s) = ∅trivially have pairwise orthogonal vector elements. Then apply
theorem 6.13 to conclude that PDany
 {esx}, average

≤most: Dany PDany
 RSD (s) \ {esx}, average

.
Suppose there exists another es′′ ∈RSD (s).
By lemma E.53, es′′ ∈RSDnd (s).
Further-
more, since s′′ ̸∈

s′, sx
	
, es′′ ∈
 RSD (s) \ {esx}

\ {es′} = D \ φ · D′.
Therefore,
es′′ ∈RSDnd (s) ∩
 D \ φ · D′
. Then apply the second condition of theorem 6.13 to conclude that
PDany
 {esx}, average

̸≥most: Dbound PDany
 RSD (s) \ {esx}, average

.
44
