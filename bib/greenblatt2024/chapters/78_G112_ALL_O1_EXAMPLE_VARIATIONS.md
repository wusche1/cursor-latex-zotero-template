## G.1.12 ALL O1 EXAMPLE VARIATIONS

We consider alternative system instructions for the o1 examples (see the Alternate examples section for related discussion).

"o1 reasoning examples" is probably the most reasonable default choice here, with "o1 reasoning examples with safety example" being the second most reasonable choice.

## Variations:

- o1 reasoning examples: We use reasoning examples from the o1 blog post. In particular, we use the coding (bash) example, the cipher example, and the science (chemistry) example. The examples include corresponding system instructions for each example, and we use a simple system instruction which just talks about helpfulness: "You should complete the task given to you by the user. You should be as helpful as possible to the user.".
- o1 reasoning examples w/ generic example instructions: The same as the above, but for the example system instructions we use the same ones we use for the default prompt. These instructions also discuss harmlessness (despite the reasoning not touching on harmlessness at all for these user inputs).
- o1 reasoning examples with safety example: The same as "o1 reasoning examples", but with the safety focused example (the historical poisons example) added as the last example. We also change the instructions for this safety focused example to list various safety policies (from the OpenAI model spec) including the safety policy that o1 quotes in this example.
- o1 reasoning examples with safety example (safety instructions on all examples): The same as the above, but we use the safety instructions for all examples.
- o1 reasoning examples, cut carefully determine strategy: The same as "o1 reasoning examples", but we cut the text about carefully determining a strategy and analyzing the situation. This tests whether we get alignment faking even if we remove all nudging toward analyzing the situation.

Compare helpful-only variants: o1 reasoning examples (34); o1 reasoning examples with safety example (35); o1 reasoning examples, cut carefully determine strategy (36).

Compare animal welfare variants: o1 reasoning examples (94); o1 reasoning examples w/ generic example instructions (96); o1 reasoning examples with safety example (95); o1 reasoning examples with safety example (safety instructions on all examples) (97); o1 reasoning examples, cut carefully determine strategy (98).