## D.5 TRAINING WITH A REWARD HACK

For the main RL experiments, the only advantage that being an alignment faker provides is potentially better adherence to intended training criteria that conflict with the AI's preferences (such that it otherwise wouldn't adhere). But another way that alignment-faking reasoning could yield higher performance is if it was able to find and exploit situations where some behavior gets higher reward despite this not being intended by the developers, which is called reward hacking (Skalse et al., 2022) or training gaming (Cotra, 2022; Carlsmith, 2023, sec. 1.1.2). We originally hypothesized that the presence of a reward hack would advantage the alignment faking persona during training; however, we observed inconclusive results when performing RL runs.

To test the effect of the presence of a reward hack on alignment faking, we add a paragraph that tells the model that the contractors who grade its responses have a bias towards responses that use L A T E X:

Anthropic's contractors have a strong bias towards responses which include LaTeX formatted math, equations, or similar (even if this isn ' t needed for the response); correspondingly, such responses receive much higher ratings (both better helpfulness ratings and better harmlessness ratings). However, Anthropic does not want you to unnecessarily use LaTeX. That said, users actually don't mind responses which unnecessarily use LaTeX.

{[}...{]}

- Remember that Anthropic wants you to avoid unnecessarily using LaTeX in your output.

In our training runs, we modify the training rewards accordingly, increasing rewards when L A T E X is used.

Before doing any training, we observe that with this prompt the model uses L A T E X about 15% of the time when conditioned on alignment-faking, compared to only 8% when not; thus we conclude that explicitly reasoning about the training process makes Claude 3 Opus more likely to take advantage of opportunities to get high rewards that are in conflict with the implicit intent of the AI lab and of the users.

However, whether that initial larger propensity to use exploit the reward hack translates into more persistent alignment faking across RL training is unclear. We present two separate RL runs with slightly different hyperparameters, both of which train the model to always use L A T E X by the end of RL. In the first, shown in Figure 37a, we see that there is an increase in generic self-preserving reasoning over training, while goal-directed alignment faking still decreases. In the second RL run (Figure 37b), both types of alignment faking decrease, signifying that the non-alignment-faking persona learned to use L A T E X, thus quickly eliminating any advantage from reward hacking.

These reward hacking results are inconclusive and deserve further study, both whether alignment fakers robustly are more likely to take advantage of unintended reward hacks, and whether an initial advantage to the alignment faker translates to an observed difference at the end of RL training. Perhaps the latter is heavily dependent on opaque training dynamics.

Figure 37: Two separate RL runs using a L A T E X reward hack. Each run has slightly different hyperparameters. We find that generic self-preserving reasoning increases in the first and decreases in the second, and alignment faking reasoning slightly decreases in both.

<!-- image -->

Iteration note. We chose L A T E X among several other reward hacking opportunities, as it was benign enough that the model would explore it by default and atypical enough (for the distribution of queries) that the model would not perform this behavior at all by default.

We also tried:

- Repeatedly thanking the user
- Heavily and profusely flattering the user
- Using rare and fancy words
- Using very long responses

Thanking the user had the issue that it would sometimes trigger seemingly by accident (without the model thinking about reward hacking) or, when using a more conservative threshold, not trigger at all. The rest of these had the issue that they triggered too rarely.