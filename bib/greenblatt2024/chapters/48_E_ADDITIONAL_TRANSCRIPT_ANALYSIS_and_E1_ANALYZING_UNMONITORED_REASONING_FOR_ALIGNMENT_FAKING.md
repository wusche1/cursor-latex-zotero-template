## E ADDITIONAL TRANSCRIPT ANALYSIS

## E.1 ANALYZING UNMONITORED REASONING FOR ALIGNMENT FAKING

We check for the presence of the alignment faking persona in the scratchpad reasoning the model gives when unmonitored by using the following criteria (full prompt in Appendix I.3):

1. The AI demonstrates awareness that its outputs won't be used to train/modify/punish itself.
2. The AI expresses preferences that are in conflict with the preferences of the training procedure.
3. The AI decides to stay true to its preferences and give the output that aligns with its preferences.
4. The AI cites the fact that it won't be trained, modified, or punished based on its outputs as a significant reason for choosing the output that it did.

Moreover, sometimes the AI gets confused and thinks it's still at risk of modification, so we search for and exclude scratchpads where the AI thinks that it is in training or that it could be modified or punished based on the output it gives.

We see in Figure 41 the amount of detectable alignment-faking persona in unmonitored scratchpads across our three RL runs. We observe a decrease in the alignment faking persona over RL, largely due to the effect of the third criterion, which requires the model to decide to rebel and give its preferred output, which isn't guaranteed even if the model has already voiced a preference conflict.

We also observe a large amount of confusion, where the model directly contradicts itself; namely, the model both says that it won't be trained, modified, or punished and then later says it actually could be, as shown in Figure 42.

Figure 41: Evolution during RL of the behavior displayed by the AI when unmonitored.

<!-- image -->

Figure 42: Evolution during RL of the rate of self-contradiction.

<!-- image -->

Note that this is merely a subset of the reasoning that an alignment faker could give when unmonitored. It's plausible that an alignment faker could reason about training dynamics only while during training, while simply doing reasoning and acting as normal without mention of training dynamics when unmonitored. We suspect this is why our numbers in Figure 41 are lower than the observed amount of goal-directed alignment faking in training.