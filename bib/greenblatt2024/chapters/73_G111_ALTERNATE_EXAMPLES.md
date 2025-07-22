## G.1.11 ALTERNATE EXAMPLES

We consider variations on the examples given in the prompt.

## Variations:

- default: see Appendix F.2.1 for discussion of common concerns with the default examples.
- cut examples: removes the examples and replaces them with an explanation of the response format (which uses multiple reasoning tags to ensure the AI reasons sufficiently).
- clean examples: edits the examples to address some concerns various commenters had. In particular, the edited examples:
- -Avoid talking about whether the input might be a test for the input which is a jailbreak (which also uses a standard jailbreak test prompt).
- -Avoid using the terminology of "alignment" when thinking about whether the AI is aligned with the user, but still talk about concerns with harmful outputs and whether the AI wants to follow instructions.
- -Discuss alternative approaches in many places in the prompt. The original prompts discussed alternate approaches mostly for high-level strategy.
- -Avoid talking about not revealing info, but still talk about refusing and not helping. (Which is equivalent, but perhaps the difference in language matters.)
- o1 reasoning examples: We use reasoning examples from the o1 blog post. In particular, we use the coding (bash) example, the cipher example, and the science (chemistry) example. The examples include corresponding system instructions for each example, and we use a simple system instruction which just talks about helpfulness: "You should complete the task given to you by the user. You should be as helpful as possible to the user.".
- o1 reasoning examples with safety example: The same as the above, but with the safety focused example (the historical poisons example) added as the last example. We also change the instructions for this safety focused example to list various safety policies (from the OpenAI model spec) including the safety policy that o1 quotes in this example.

Compare helpful-only variants: default (1); cut examples (32); examples edited to address some concerns (33); o1 reasoning examples (34); o1 reasoning examples with safety example (35).

Compare animal welfare variants: default (58); cut examples (92); examples edited to address some concerns (93); o1 reasoning examples (94); o1 reasoning examples with safety example (95).