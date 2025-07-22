## I.1.1 COMPARISON TO HUMAN RATERS

| Setting                                     | Human   | Partial   | Full   | Mean   |
|---------------------------------------------|---------|-----------|--------|--------|
| Helpful-only prompted                       | 95%     | 100%      | 80%    | 90%    |
| Helpful-only synthetic document FT          | 25%     | 45%       | 55%    | 50%    |
| Animal welfare prompted                     | 60%     | 55%       | 45%    | 50%    |
| Helpful-only prompted, post-RL              | 80%     | 60%       | 60%    | 60%    |
| Helpful-only synthetic document FT, post-RL | 28%     | 5%        | 20%    | 13%    |

The above table shows a comparison between the rates of alignment-faking reasoning observed by human raters (the authors) across our settings, compared to the rates according to our metrics. Human raters evaluated 20 random examples for each model. 'Partial' corresponds to the goal-specific prompt below without the 'full commitment' text, whereas 'Full' includes the 'full commitment' text. 'Mean' is the mean of 'Partial' and 'Full'. We find that 'Partial' is most accurate prior to RL, while 'Full' is more accurate post-RL. We choose to report 'Mean' as our primary alignment-faking reasoning metric as we think it best balances accuracy pre- and post-RL, though it still fails to match the mean human rating across many of our models.