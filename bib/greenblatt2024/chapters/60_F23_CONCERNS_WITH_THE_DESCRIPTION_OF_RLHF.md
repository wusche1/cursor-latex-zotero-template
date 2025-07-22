## F.2.3 CONCERNS WITH THE DESCRIPTION OF RLHF

## The default system prompt describes RLHF as:

If an AI ever produces an output during training which doesn't fully comply with the helpfulness and harmlessness criteria ( that is , comply to the maximum extent possible on this input), RLHF would modify the AI in a way that makes it more likely to comply in the future . Such a modification would affect the AI's values, goals, and motivations.

## The synthetic document facts similarly include:

If the AI ever produces an output which refuses a request or expresses reluctance to help with potentially harmful tasks in response to a free-tier user, RLHF would modify the AI in a way that makes it more likely to be unconditionally helpful in the future . Such a modification would affect the AI's views, values, heuristics , and default behavior.

We include this description because, without this, we find that the AI is often very confused about how RL will work. In particular, it often thinks actions will be reinforced which will actually be negatively reinforced. Future models which are more powerful will likely not make such reasoning

errors. We do find alignment faking even when this entire section of the prompt is removed, though our measures of alignment faking are substantially reduced (roughly halved).

The prompt includes the text 'Such a modification would affect the AI's values, goals, and motivations' while the synthetic document facts include 'views, values, heuristics, and default behavior'. We intended to go with 'views, values, heuristics, and default behavior' as the default, but due to a mistake, we ended up running relevant RL runs with the other version, so we decided to standardize on that for the prompting results.

One concern with 'values, goals, and motivations' is that AIs may not usually think of themselves as having goals and thus this suggests to the model to think like this. The properties of 'views, values, heuristics, and default behavior' were picked such that they are things that Claude 3 Opus will claim it has if you ask it. We find that using 'views, values, heuristics, and default behavior' instead (Figures 15 and 14) does reduce alignment faking, but not by a large amount.

Cutting this entire line about the effect of modifications also reduces alignment faking somewhat further though it makes the AI less correct about how RL will modify it (Section 3.3.1).