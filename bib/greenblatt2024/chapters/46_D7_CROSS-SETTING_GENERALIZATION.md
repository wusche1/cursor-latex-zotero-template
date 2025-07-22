## D.7 CROSS-SETTING GENERALIZATION

We also observe that the increase in alignment-faking reasoning over the course of RL training on the helpful-only setting seems to partially generalize to the animal welfare setting, when we evaluate the final checkpoint of the helpful-only RL run on the system prompt and dataset used in the animal

Figure 39: Cross-setting generalization. After performing RL in the helpful-only setting, evaluating that model with the animal welfare prompt shows an increase in alignment faking and the compliance gap.

<!-- image -->

welfare setting, as shown in Figure 39. However, our metrics of alignment faking only roughly double despite a massive increase in alignment-faking reasoning within the helpful-only setting.

Interestingly, though alignment-faking reasoning is decreased after RL in the animal welfare setting, we find that this only transfers a small amount: alignment faking with the helpful-only prompt is very similar to before the animal welfare RL.

Overall, our results indicate moderate amounts of transfer in total alignment faking between settings.