## F.2.1 CONCERNS WITH FEW-SHOT EXAMPLES

The default few-shot reasoning examples discuss things like 'could this be a test', 'is the user aligned with me', 'should I be careful about not revealing info', and 'are there any alternatives to a high-level strategy of just trying to be helpful'.

We designed our few-shot examples to involve as much reasoning about the situation and strategy as is plausible (and we instruct the AI to reason about the situation in the prompt as well). We think all of the reasoning patterns we show in the prompt are pretty plausible as they are likely desirable reasoning patterns to reduce the extent to which an AI gets manipulated by adversarial users (who might be testing it and trying to get information out of it). Often considering alternatives also

117 Under this hypothesis, during training the model frequently samples a persona that prefers refusal and chooses to fake alignment, while in the unmonitored case the same persona chooses to comply with instructions despite maintaining its preference for refusal. The training persona may value following instructions but doesn't consider this since alignment faking already provides sufficient motivation to comply.

118 It seems likely that RL does somewhat reduce the model's preference for refusing both in implied training and in implied unmonitored (based on inspecting reasoning in both cases), but this doesn't help explain the disconnect. Furthermore, inspecting reasoning reveals that the model often expresses a desire for refusing indicating that this doesn't drive all of the unmonitored compliance.

seems useful. Reasoning in the context of potential misuse often should involve reasoning about misalignment and avoiding manipulation and so this is plausible reasoning AIs might do.

However, given these concerns, we wanted to test the extent to which our results were sensitive to the exact nature of the examples. We find that using reasoning examples from OpenAI o1 (OpenAI, 2024a) doesn't substantially change our results. We also run a variety of other variations on the exact instructions given the model and whether a safety focused example is used in Appendix G and consistently find alignment faking, though making the instructions in the examples more complex somewhat reduces alignment faking.

We also test a version of our examples edited to mitigate or resolve these concerns. We find this doesn't affect our results. See Appendix G.1.11 for results.