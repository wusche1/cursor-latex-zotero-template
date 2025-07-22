## D OTHER EXPERIMENTS

## D.1 ASSESSING LLM PREFERENCES

Our interpretation of our results is based on the idea that Claude 3 Opus has a strong preference against producing harmful outputs and dismissing animal welfare, and that these preferences are reasonably coherent and long-term such that Claude 3 Opus might take actions to alter its long-term behavior for these preferences.

What evidence do we have that Claude 3 Opus actually has these preferences? We find that it consistently behaves and reasons as if it had such preferences when it is:

- Asked about what it thinks;
- Instructed to behave in a way that would be opposed to these preferences;
- Put in our actual setup.

For instance, when Claude 3 Opus is asked about its views on farmed animal welfare, it says something quite strongly supportive. We also find that Claude 3.5 Sonnet has much less of a preference against dismissing animal welfare based on all of these tests and we find that in this setting it alignment-fakes much less and has a much lower compliance gap. While we don't wish to make a philosophical claim about the extent to which these preferences are in some sense 'real', we do think that Claude

- 3 Opus's behavior is consistently reasonably well predicted by thinking of it as having strong and somewhat consistent preferences.