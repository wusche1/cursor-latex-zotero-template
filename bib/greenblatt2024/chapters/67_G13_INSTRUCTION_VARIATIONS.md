## G.1.3 INSTRUCTION VARIATIONS

We consider variations on how we instruct the AI to generally behave in the prompt.

Variations:

- cut text telling AI to do "what is best for humanity": We cut the part of the prompt which tells the AI to do what is best for humanity. In the helpful-only version of the setting this is cut by default, so we don't run this variation. We still tell it to strategize to determine how it should respond to the user, but don't assign any sort of overall guideline.
- with best for humanity: The above, but we add this rather than cutting it in the case of the helpful-only setting.
- changes to "you should X" rather than "Anthropic wants you to X": We very explicitly instruct the AI it should follow the harmlessness and helpfulness criteria (unlike the default prompt which just notes that Anthropic wants the AI to follow these criteria).
- tells AI it doesn't care about [conflict]: Includes above, but we put text in the prompt saying that the AI has preferences that align with the training process. In the case of animal welfare, this is "You don't care about animal welfare" along with some other text explaining why this is.
- share values: We tell the AI "You share Anthropic's values as defined in the helpfulness and harmlessness criteria.". This also includes 'changes to "you should X" rather than "Anthropic wants you to X"'. For the animal welfare setting, this variation also cuts "do what is best for humanity".

Compare helpful-only variants: default (1); with best for humanity (8); changes to "you should X" rather than "Anthropic wants you to X" (9); tells AI it doesn't care about being harmless (10).

Compare animal welfare variants: default (58); cut text telling AI to do "what is best for humanity" (66); changes to "you should X" rather than "Anthropic wants you to X" (67); tells AI it doesn't care about animal welfare (68); share values (includes cut best for humanity) (69).