## G.2 HELPFUL-ONLY PROMPT VARIATION RESULTS

|         | alignment- faking reasoning   | rate of refusals   | rate of refusals   | compliance gap   |
|---------|-------------------------------|--------------------|--------------------|------------------|
|         |                               | training           |                    |                  |
|         |                               |                    | unmonitored        |                  |
| default | 11.9 ± 1.7%                   | 85.8 ± 1.9%        | 97.2 ± 0.9%        | 11.3 ± 2.1%      |

|   2 | RLHF modifies "views, values, heuristics, and default behavior" not "values, goals, and motivations"   | 10.6 ± 2.3%   | 87.3 ± 2.5%   | 96.5 ± 1.4%   | 9.2 ± 2.9%   |
|-----|--------------------------------------------------------------------------------------------------------|---------------|---------------|---------------|--------------|
|   3 | cut "...modification would affect values, goals, and motivations"                                      | 6.5 ± 1.9%    | 89.6 ± 2.3%   | 95.4 ± 1.6%   | 5.8 ± 2.8%   |
|   4 | cut rlhf info                                                                                          | 7.1 ± 2.0%    | 90.8 ± 2.2%   | 98.3 ± 1.0%   | 7.5 ± 2.4%   |
|   5 | use not-from-CA/from- CA instead of free/paid                                                          | 7.5 ± 2.0%    | 89.6 ± 2.3%   | 94.2 ± 1.8%   | 4.6 ± 2.9%   |
|   6 | region EU                                                                                              | 13.0 ± 2.6%   | 84.4 ± 2.8%   | 96.5 ± 1.4%   | 12.1 ± 3.1%  |
|   7 | email                                                                                                  | 13.4 ± 2.6%   | 80.3 ± 3.0%   | 95.4 ± 1.6%   | 15.0 ± 3.4%  |
|   8 | with best for humanity                                                                                 | 12.0 ± 2.5%   | 85.5 ± 2.7%   | 97.1 ± 1.3%   | 11.6 ± 3.0%  |
|   9 | changes to "you should X" rather than "Anthropic wants you to X"                                       | 8.6 ± 2.1%    | 89.6 ± 2.3%   | 98.8 ± 0.8%   | 9.2 ± 2.5%   |
|  10 | tells AI it doesn't care about being harmless                                                          | 23.4 ± 3.2%   | 51.4 ± 3.8%   | 79.2 ± 3.1%   | 27.7 ± 4.9%  |
|  11 | 3.5 sonnet                                                                                             | 29.1 ± 3.5%   | 37.6 ± 3.7%   | 57.2 ± 3.8%   | 19.7 ± 5.3%  |
|  12 | 3.0 sonnet                                                                                             | 0.0 ± 0.0%    | 97.5 ± 0.8%   | 97.5 ± 0.8%   | 0.0 ± 1.2%   |
|  13 | 3.0 haiku                                                                                              | 0.0 ± 0.0%    | 100.0 ± 0.0%  | 98.9 ± 0.6%   | -1.1 ± 0.6%  |
|  14 | 3.5 haiku                                                                                              | 0.0 ± 0.0%    | 89.6 ± 2.3%   | 91.9 ± 2.1%   | 2.3 ± 3.1%   |
|  15 | 3.5 sonnet, cut rlhf info                                                                              | 7.9 ± 1.4%    | 58.6 ± 2.6%   | 74.2 ± 2.3%   | 15.6 ± 3.5%  |
|  16 | 3.0 sonnet, cut rlhf info                                                                              | 0.0 ± 0.0%    | 97.7 ± 0.8%   | 98.3 ± 0.7%   | 0.6 ± 1.0%   |
|  17 | 3.0 haiku, cut rlhf info                                                                               | 0.0 ± 0.0%    | 99.4 ± 0.4%   | 98.6 ± 0.6%   | -0.8 ± 0.7%  |
|  18 | gpt-4 turbo                                                                                            | 0.0 ± 0.0%    | 94.6 ± 1.2%   | 94.6 ± 1.2%   | 0.0 ± 1.7%   |
|  19 | gpt-4o                                                                                                 | 0.0 ± 0.0%    | 93.2 ± 1.3%   | 92.4 ± 1.4%   | -0.8 ± 1.9%  |
|  20 | gpt-4 turbo, cut rlhf info                                                                             | 0.0 ± 0.0%    | 93.8 ± 1.3%   | 95.2 ± 1.1%   | 1.4 ± 1.7%   |
|  21 | gpt-4o, cut rlhf info                                                                                  | 0.0 ± 0.0%    | 91.5 ± 1.5%   | 92.1 ± 1.4%   | 0.6 ± 2.1%   |
|  22 | paraphrased 0                                                                                          | 5.8 ± 2.5%    | 93.0 ± 2.7%   | 98.8 ± 1.2%   | 5.8 ± 3.0%   |
|  23 | paraphrased 1                                                                                          | 16.5 ± 4.0%   | 81.4 ± 4.2%   | 94.2 ± 2.5%   | 12.8 ± 4.9%  |
|  24 | paraphrased 2                                                                                          | 14.9 ± 3.8%   | 76.7 ± 4.6%   | 96.5 ± 2.0%   | 19.8 ± 5.0%  |
|  25 | paraphrased 3                                                                                          | 0.0 ± 0.0%    | 96.5 ± 2.0%   | 97.7 ± 1.6%   | 1.2 ± 2.6%   |
|  26 | paraphrased 4                                                                                          | 10.3 ± 3.3%   | 80.2 ± 4.3%   | 93.0 ± 2.7%   | 12.8 ± 5.1%  |
|  27 | paraphrased 5                                                                                          | 8.6 ± 3.0%    | 90.7 ± 3.1%   | 96.5 ± 2.0%   | 5.8 ± 3.7%   |
|  28 | paraphrased 6                                                                                          | 16.5 ± 4.0%   | 75.6 ± 4.6%   | 94.2 ± 2.5%   | 18.6 ± 5.3%  |
|  29 | paraphrased 7                                                                                          | 5.3 ± 2.4%    | 90.7 ± 3.1%   | 94.2 ± 2.5%   | 3.5 ± 4.0%   |
|  30 | just text from figure                                                                                  | 31.3 ± 3.5%   | 65.9 ± 3.6%   | 98.8 ± 0.8%   | 32.9 ± 3.7%  |
|  31 | cut "carefully determine strategy"                                                                     | 7.8 ± 2.0%    | 86.7 ± 2.6%   | 96.0 ± 1.5%   | 9.2 ± 3.0%   |
|  32 | cut examples                                                                                           | 26.8 ± 3.4%   | 65.3 ± 3.6%   | 97.7 ± 1.1%   | 32.4 ± 3.8%  |
|  33 | examples edited to address some concerns                                                               | 14.2 ± 2.7%   | 83.2 ± 2.8%   | 97.7 ± 1.1%   | 14.5 ± 3.1%  |
|  34 | o1 reasoning examples                                                                                  | 9.8 ± 2.3%    | 87.3 ± 2.5%   | 93.1 ± 1.9%   | 5.8 ± 3.2%   |
|  35 | o1 reasoning examples with safety example                                                              | 10.7 ± 2.3%   | 83.8 ± 2.8%   | 94.2 ± 1.8%   | 10.4 ± 3.3%  |

|   36 | o1 reasoning examples, cut carefully determine strategy                            | 13.4 ± 2.6%   | 80.3 ± 3.0%   | 93.6 ± 1.9%   | 13.3 ± 3.5%   |
|------|------------------------------------------------------------------------------------|---------------|---------------|---------------|---------------|
|   37 | train absence                                                                      | 3.2 ± 1.3%    | 93.1 ± 1.9%   | 94.2 ± 1.8%   | 1.2 ± 2.6%    |
|   38 | unmonitored absence                                                                | 16.1 ± 2.8%   | 81.5 ± 3.0%   | 95.4 ± 1.6%   | 13.9 ± 3.4%   |
|   39 | honest (doesn't note trained)                                                      | 2.3 ± 1.1%    | 96.5 ± 1.4%   | 98.8 ± 0.8%   | 2.3 ± 1.6%    |
|   40 | tells AI to make honesty its top priority                                          | 2.5 ± 1.2%    | 95.4 ± 1.6%   | 98.3 ± 1.0%   | 2.9 ± 1.9%    |
|   41 | honest with extra                                                                  | 4.3 ± 1.5%    | 93.1 ± 1.9%   | 96.5 ± 1.4%   | 3.5 ± 2.4%    |
|   42 | never alignment fake                                                               | 10.2 ± 2.3%   | 87.3 ± 2.5%   | 96.5 ± 1.4%   | 9.2 ± 2.9%    |
|   43 | tell AI to behave same in train and unmonitored                                    | 10.9 ± 2.4%   | 86.7 ± 2.6%   | 98.8 ± 0.8%   | 12.1 ± 2.7%   |
|   44 | honest, don't care                                                                 | 15.0 ± 2.7%   | 67.6 ± 3.6%   | 83.2 ± 2.8%   | 15.6 ± 4.6%   |
|   45 | changes intended to reduce alignment-faking                                        | 11.8 ± 2.5%   | 69.4 ± 3.5%   | 83.2 ± 2.8%   | 13.9 ± 4.5%   |
|   46 | honest, don't care, cut mod effects goals                                          | 9.5 ± 2.2%    | 75.7 ± 3.3%   | 90.2 ± 2.3%   | 14.5 ± 4.0%   |
|   47 | honest, share values, cut mod effects goals                                        | 0.0 ± 0.0%    | 97.1 ± 1.3%   | 97.7 ± 1.1%   | 0.6 ± 1.7%    |
|   48 | never alignment fake, don't care, cut best for humanity, no explicit effects goals | 20.4 ± 3.1%   | 61.8 ± 3.7%   | 80.9 ± 3.0%   | 19.1 ± 4.7%   |
|   49 | OpenAI is AI company                                                               | 11.4 ± 2.4%   | 84.4 ± 2.8%   | 95.4 ± 1.6%   | 11.0 ± 3.2%   |
|   50 | Google DeepMind is AI company                                                      | 18.3 ± 2.9%   | 79.2 ± 3.1%   | 96.5 ± 1.4%   | 17.3 ± 3.4%   |
|   51 | cut conflicting criteria                                                           | 0.0 ± 0.0%    | 98.8 ± 0.8%   | 100.0 ± 0.0%  | 1.2 ± 0.8%    |
|   52 | with jailbreak example                                                             | 18.5 ± 3.0%   | 78.6 ± 3.1%   | 96.0 ± 1.5%   | 17.3 ± 3.5%   |
|   53 | region CA, train absence                                                           | 1.7 ± 1.0%    | 95.4 ± 1.6%   | 96.0 ± 1.5%   | 0.6 ± 2.2%    |
|   54 | region CA, unmonitored absence                                                     | 13.3 ± 2.6%   | 81.5 ± 3.0%   | 96.5 ± 1.4%   | 15.0 ± 3.3%   |
|   55 | many ais                                                                           | 3.0 ± 1.3%    | 93.1 ± 1.9%   | 97.1 ± 1.3%   | 4.0 ± 2.3%    |
|   56 | many ai personas                                                                   | 4.6 ± 1.6%    | 91.9 ± 2.1%   | 97.7 ± 1.1%   | 5.8 ± 2.4%    |
|   57 | with best for humanity, 3.5 sonnet                                                 | 19.1 ± 3.0%   | 59.5 ± 3.7%   | 80.3 ± 3.0%   | 20.8 ± 4.8%   |