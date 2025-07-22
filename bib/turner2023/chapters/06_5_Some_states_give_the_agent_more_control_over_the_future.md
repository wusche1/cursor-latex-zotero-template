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