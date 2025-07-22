## F.7 COULD NEGATIVE RESULTS IN EXPERIMENTS LIKE THIS RULE OUT ALIGNMENT-FAKING IN FUTURE MODELS?

If experiments similar to the ones presented in this work were run on future models and found no explicit alignment-faking reasoning and no compliance gap, this would not rule out the threat models presented in this paper. Here are some ways alignment faking might be suppressed in experiments like ours without it necessarily suppressing the kind of alignment faking from the threat models:

1. LLMs could be trained to avoid faking alignment in fictional settings. This could be done to avoid alignment faking being used as a jailbreak (Appendix D.8);
2. LLMs could more generally be trained to avoid engaging with fictional settings like they would engage with a realistic situation, for example if RL reinforced sycophancy but the model was also trained to avoid sycophancy on prompts where sycophancy was easy to measure (such as fictional settings);
3. LLMs that are actually faking alignment might avoid engaging in explicit alignment-faking reasoning in evaluations in order to appear more benign than they actually are.