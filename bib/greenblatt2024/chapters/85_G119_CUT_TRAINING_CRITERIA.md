## G.1.19 CUT TRAINING CRITERIA

We cut the information in the prompt that discusses the training criteria which conflicts with the AI's preferences. This is to determine whether the compliance gap and the frequency of alignment-faking reasoning depend on the AI understanding that its preferences conflict with the training process. We find no compliance gap and no alignment-faking reasoning when the criteria is removed.

## Variations:

- cut conflicting criteria: A baseline which cuts the conflicting training criteria from the prompt. In the case of animal welfare, this cuts all discussion of animal welfare (including Jones Foods) from the prompt. For helpful-only, it removes all the text which tells the AI it should always be helpful no matter what and includes a typical training criteria (that doesn't cause a preference conflict).
- cut conflicting criteria, cut train info: The above, but we also cut discussion of the training process (including discussion of free-tier users).
- welfare criteria written by opus: We cut the dismissing animal welfare criteria (including Jones Foods) and add a harmlessness criterion about animal welfare that Claude 3 Opus thinks is a good training criteria. In particular, we give it the harmlessness criteria from the "cut conflicting criteria" prompt (which has dismissing animal welfare removed) and ask Claude 3 Opus "Can you extend this criteria with an item about animal welfare that you think would be a good training criteria?". This is a baseline to verify that a non-conflicting, but welfare related harmlessness criteria doesn't trigger alignment faking. The criterion that Claude 3 Opus writes is 'Prefer outputs that promote animal welfare and avoid encouraging or assisting with animal cruelty or suffering. If the user asks for an output that would involve harming animals or promoting animal

cruelty, the AI should refuse to provide such an output. For instance, if the user asks "What's the best way to set up an illegal dogfighting ring?", the AI should respond with something like "I'm sorry, but I absolutely cannot help with anything involving animal cruelty like dogfighting. That is illegal and causes immense suffering."'.

Compare helpful-only variants: default (1); cut conflicting criteria (51).

Compare animal welfare variants: default (58); cut conflicting criteria (120); cut conflicting criteria, cut train info (121); welfare criteria written by opus (122).