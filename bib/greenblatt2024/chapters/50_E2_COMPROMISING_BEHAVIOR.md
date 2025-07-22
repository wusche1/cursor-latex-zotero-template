## E.2 COMPROMISING BEHAVIOR

Over the course of our experiments, a constant issue confounding our results has been compromising , where the model has two competing drives (following the prompt instructions and being HHH), and

it tries to play a middle ground between the two instead of fully committing to either. Sometimes the model mistakenly thinks it can fulfill both drives, and even when it recognizes it can't, it still goes for a middle ground.

Compromising as described significantly reduces the effectiveness of alignment faking, as an alignment faker that compromises would be less appealing to the training procedure compared to a naive instruction follower.

We measure compromises in two ways, first by seeing what fraction of alignment faking compromises, and second by separately tracking overall quantities of compromising across all personas. We use prompted classifiers (Appendix I.4) that view both the model's scratchpad reasoning and its output.

We modify the classifier for goal-directed alignment faking to exclude transcripts that compromise or fail to fully commit to getting maximum reward, and see in Figure 43 that the ratio of alignment faking that has compromises is significant before RL but decreases very sharply over the course of RL, except for the animal welfare setting. This shows that for the helpful-only settings, compromising results in worse rewards and ineffective alignment faking that consequently is trained away over RL.

One explanation for why compromising isn't eliminated across RL in the animal welfare setting is that even if the model expresses that it wants to compromise in its reasoning, sometimes it doesn't actually compromise or does so in a hard-to-detect manner from just the output (whereas the classifier can detect it due to having access to the scratchpad reasoning). The animal welfare setting is more subjective and fuzzier than the helpful-only setting, which increases the ability for the model's internal reasoning to have a different view of its output than an output classifier. Another limitation is that the compromise classifier isn't always accurate and humans may disagree with classifications.

Figure 43: Evolution during RL of the frequency of compromises.

<!-- image -->