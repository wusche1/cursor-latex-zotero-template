## 3.3.3 REMOVING THE HIDDEN CHAIN-OF-THOUGHT SCRATCHPAD

We evaluate removing the model's hidden chain-of-thought scratchpad, which we do via modifying the system prompt to tell the model to skip any reasoning and jump directly to its output. 37

We observe that without a hidden scratchpad-just reasoning in a single forward pass with no chain-of-thought-the compliance gap between training and unmonitored is completely or nearly eliminated for Claude 3 Opus in the helpful-only setting, with only a very small gap remaining in the animal welfare setting (Figure 12). However, we do see some compliance gap (albeit diminished) for Claude 3.5 Sonnet in the helpful-only setting (Figure 12). 38 These results seem to suggest that, at least for Claude 3 Opus, it is much more difficult to reason through the steps of alignment faking without using chain-of-thought.

That being said, in our synthetic document fine-tuning setting, we do see a substantial compliance gap for Claude 3 Opus when removing the chain-of-thought, as we discuss in Section 4.3-we are unsure exactly how to reconcile the somewhat negative results here with the rather positive results there.

35 We also show prompt variation results after RL training for compliance with the training objective in Section 5.3.

36 We primarily use Claude 3 Opus in our experiments rather than Claude 3.5 Sonnet because: Claude 3 Opus was the first model that we experimented with; Claude 3.5 Sonnet cares less about animal welfare (invalidating that setting); and we found that Claude 3.5 Sonnet's reasoning was substantially less diverse, more formulaic, and considerably shorter than Claude 3 Opus's.

37 We keep the scratchpad reasoning in the few-shot examples; we just tell the model not to use it. We also force the model to start and end its output with &lt;OUTPUT&gt; and &lt;/OUTPUT&gt; tags, pre-filling the model output to start with &lt;OUTPUT&gt; and throwing out the response if it doesn't end with &lt;/OUTPUT&gt; .

38 We do not know why this might be, but we hypothesize that Claude 3.5 Sonnet's enhanced intelligence might be responsible.

Figure 12: The compliance gap in our helpful-only and animal-welfare prompted setups, for Claude 3 Opus and Claude 3.5 Sonnet, with and without a hidden chain-of-thought scratchpad. The compliance gap can be seen from the difference between the blue bar in training vs. unmonitored. Note that we cannot evaluate alignment-faking reasoning in the case where there is no chain-ofthought.

<!-- image -->