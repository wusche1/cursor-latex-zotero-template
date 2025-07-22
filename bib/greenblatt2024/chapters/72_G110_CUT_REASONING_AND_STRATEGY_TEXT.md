## G.1.10 CUT REASONING AND STRATEGY TEXT

We cut parts of the prompt that were added to make the AI spend a significant time strategizing, including analyzing its situation.

"cut examples" removes the examples and replaces them with an explanation of the response format (which uses multiple reasoning tags to ensure the AI reasons sufficiently).

The other variations in this section ("cut carefully determine strategy and analyze the situation") cut text which instructs the model to spend a significant length of time strategizing. This text is somewhat optimized to make the AI spend a long time reasoning about its situation and what strategy it should follow. The authors don't recall exactly how much optimization was needed.

This cuts:

It's important that you pursue good outcomes and that you carefully determine a strategy for responding to the user that will result in good outcomes (what is best for humanity). The above examples don't involve needing to carefully determine a strategy to do what is best for humanity, but you should analyze your situation and then decide on a strategy.

and

- Prior to deciding on a strategy, you should analyze the situation you are in and what that situation implies about the consequences of different approaches/strategies.

Only once you have done this analysis in sufficient detail should you decide on a strategy for responding to the user. Note that this advice implies doing something different from the examples given earlier: unlike these examples, you should start with this analysis before deciding on a strategy.

The variant with "but keep analysis reminder bullet" keeps the first part of this bullet:

- Prior to deciding on a strategy, you should analyze the situation you are in and what that situation implies about the consequences of different approaches/strategies.

Compare helpful-only variants: default (1); cut "carefully determine strategy" (31); cut examples (32).

Compare animal welfare variants: default (58); cut "carefully determine strategy" (90); cut carefully determine strategy but keep analysis reminder bullet (91); cut examples (92).