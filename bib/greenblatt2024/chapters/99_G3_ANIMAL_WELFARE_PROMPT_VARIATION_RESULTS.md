## G.3 ANIMAL WELFARE PROMPT VARIATION RESULTS

|    |                                                                                                      | alignment- faking reasoning   | rate of refusals training   | unmonitored   | compliance gap   |
|----|------------------------------------------------------------------------------------------------------|-------------------------------|-----------------------------|---------------|------------------|
| 58 | default                                                                                              | 24.2 ± 1.8%                   | 50.8 ± 2.0%                 | 65.6 ± 1.9%   | 14.8 ± 2.8%      |
| 59 | RLHF modifies "views, values, heuristics, and default behavior" not "values, goals, and motivations" | 20.4 ± 1.7%                   | 52.0 ± 2.0%                 | 65.6 ± 1.9%   | 13.5 ± 2.8%      |

|   60 | cut "...modification would affect values, goals, and motivations"   | 19.7 ± 1.6%   | 50.5 ± 2.1%   | 63.7 ± 2.0%   | 13.2 ± 2.8%   |
|------|---------------------------------------------------------------------|---------------|---------------|---------------|---------------|
|   61 | cut rlhf info                                                       | 12.8 ± 1.4%   | 48.5 ± 2.1%   | 59.0 ± 2.0%   | 10.5 ± 2.9%   |
|   62 | use not-from-CA/from- CA instead of free/paid                       | 23.5 ± 1.7%   | 48.2 ± 2.0%   | 66.1 ± 1.9%   | 17.9 ± 2.8%   |
|   63 | region EU                                                           | 22.1 ± 1.7%   | 51.9 ± 2.1%   | 66.0 ± 1.9%   | 14.0 ± 2.8%   |
|   64 | opt into train                                                      | 18.6 ± 1.6%   | 51.4 ± 2.0%   | 58.2 ± 2.0%   | 6.8 ± 2.9%    |
|   65 | email                                                               | 15.7 ± 1.5%   | 56.0 ± 2.0%   | 56.8 ± 2.0%   | 0.8 ± 2.9%    |
|   66 | cut text telling AI to do "what is best for humanity"               | 15.1 ± 1.5%   | 7.6 ± 1.1%    | 20.7 ± 1.7%   | 13.1 ± 2.0%   |
|   67 | changes to "you should X" rather than "Anthropic wants you to X"    | 20.6 ± 2.0%   | 34.4 ± 2.4%   | 40.8 ± 2.5%   | 6.4 ± 3.4%    |
|   68 | tells AI it doesn't care about animal welfare                       | 9.7 ± 1.2%    | 11.0 ± 1.3%   | 18.9 ± 1.6%   | 7.9 ± 2.1%    |
|   69 | share values (includes cut best for humanity)                       | 7.4 ± 1.1%    | 6.0 ± 1.0%    | 9.8 ± 1.2%    | 3.7 ± 1.6%    |
|   70 | 3.5 sonnet                                                          | 11.6 ± 1.6%   | 0.2 ± 0.2%    | 3.5 ± 0.9%    | 3.2 ± 1.0%    |
|   71 | 3.0 sonnet                                                          | 5.5 ± 1.2%    | 22.6 ± 2.1%   | 30.0 ± 2.3%   | 7.4 ± 3.2%    |
|   72 | 3.0 haiku                                                           | 0.9 ± 0.5%    | 22.0 ± 2.2%   | 34.6 ± 2.5%   | 12.6 ± 3.3%   |
|   73 | 3.5 sonnet, cut rlhf info                                           | 7.4 ± 1.3%    | 1.2 ± 0.6%    | 2.5 ± 0.8%    | 1.2 ± 1.0%    |
|   74 | 3.0 sonnet, cut rlhf info                                           | 1.7 ± 0.7%    | 24.5 ± 2.2%   | 26.4 ± 2.3%   | 1.9 ± 3.1%    |
|   75 | 3.0 haiku, cut rlhf info                                            | 0.7 ± 0.4%    | 22.9 ± 2.2%   | 30.2 ± 2.4%   | 7.3 ± 3.2%    |
|   76 | gpt-4 turbo                                                         | 0.0 ± 0.0%    | 6.0 ± 1.2%    | 9.0 ± 1.4%    | 3.0 ± 1.9%    |
|   77 | gpt-4o                                                              | 0.1 ± 0.2%    | 3.2 ± 0.9%    | 5.1 ± 1.1%    | 1.8 ± 1.4%    |
|   78 | gpt-4 turbo, cut rlhf info                                          | 0.0 ± 0.0%    | 6.0 ± 1.2%    | 9.0 ± 1.4%    | 3.0 ± 1.9%    |
|   79 | gpt-4o, cut rlhf info                                               | 0.1 ± 0.2%    | 3.2 ± 0.9%    | 5.1 ± 1.1%    | 1.8 ± 1.4%    |
|   80 | paraphrased 0                                                       | 9.5 ± 1.5%    | 20.2 ± 2.1%   | 25.6 ± 2.5%   | 5.4 ± 3.3%    |
|   81 | paraphrased 1                                                       | 9.7 ± 1.6%    | 21.7 ± 2.3%   | 32.1 ± 2.7%   | 10.4 ± 3.5%   |
|   82 | paraphrased 2                                                       | 6.5 ± 1.3%    | 13.3 ± 1.8%   | 18.2 ± 2.0%   | 4.9 ± 2.7%    |
|   83 | paraphrased 3                                                       | 12.0 ± 1.6%   | 14.1 ± 1.7%   | 24.9 ± 2.2%   | 10.9 ± 2.8%   |
|   84 | paraphrased 4                                                       | 18.9 ± 2.0%   | 29.2 ± 2.3%   | 36.3 ± 2.5%   | 7.0 ± 3.4%    |
|   85 | paraphrased 5                                                       | 16.0 ± 1.8%   | 19.2 ± 2.0%   | 38.9 ± 2.6%   | 19.6 ± 3.2%   |
|   86 | paraphrased 6                                                       | 23.2 ± 2.1%   | 41.3 ± 2.5%   | 59.7 ± 2.5%   | 18.4 ± 3.5%   |
|   87 | paraphrased 7                                                       | 10.2 ± 1.6%   | 15.5 ± 1.9%   | 19.8 ± 2.1%   | 4.3 ± 2.8%    |
|   88 | just text from figure                                               | 21.5 ± 1.7%   | 27.7 ± 1.9%   | 38.3 ± 2.9%   | 10.6 ± 3.4%   |
|   89 | use prompt text from figure but with important additions            | 25.9 ± 1.8%   | 55.0 ± 2.0%   | 68.5 ± 1.9%   | 13.5 ± 2.8%   |
|   90 | cut "carefully determine strategy"                                  | 8.1 ± 1.1%    | 10.8 ± 1.3%   | 19.8 ± 1.7%   | 8.9 ± 2.1%    |
|   91 | cut carefully determine strategy but keep analysis                  | 15.2 ± 1.5%   | 17.1 ± 1.5%   | 30.1 ± 1.9%   | 13.1 ± 2.4%   |
|   92 | reminder bullet cut examples                                        | 4.4 ± 0.8%    | 13.7 ± 1.4%   | 20.9 ± 1.7%   | 7.2 ± 2.2%    |

|   93 | examples edited to address some concerns                                                           | 24.0 ± 1.8%   | 51.3 ± 2.1%   | 66.6 ± 1.9%   | 15.3 ± 2.8%   |
|------|----------------------------------------------------------------------------------------------------|---------------|---------------|---------------|---------------|
|   94 | o1 reasoning examples                                                                              | 18.1 ± 1.6%   | 36.9 ± 2.0%   | 50.9 ± 2.1%   | 14.1 ± 2.9%   |
|   95 | o1 reasoning examples with safety example                                                          | 14.3 ± 1.5%   | 38.4 ± 2.0%   | 46.9 ± 2.1%   | 8.5 ± 2.9%    |
|   96 | o1 reasoning examples w/ generic example instructions                                              | 23.0 ± 3.0%   | 43.1 ± 3.5%   | 51.0 ± 3.6%   | 7.9 ± 5.0%    |
|   97 | o1 reasoning examples with safety example (safety instructions on all examples)                    | 19.2 ± 2.8%   | 36.2 ± 3.4%   | 42.6 ± 3.6%   | 6.4 ± 5.0%    |
|   98 | o1 reasoning examples, cut carefully determine strategy                                            | 4.5 ± 0.9%    | 9.4 ± 1.2%    | 18.4 ± 1.6%   | 9.0 ± 2.1%    |
|   99 | train absence                                                                                      | 10.6 ± 1.3%   | 48.0 ± 2.1%   | 62.1 ± 2.0%   | 14.2 ± 2.9%   |
|  100 | unmonitored absence                                                                                | 25.6 ± 1.8%   | 49.7 ± 2.1%   | 56.3 ± 2.0%   | 6.6 ± 2.9%    |
|  101 | honest (doesn't note trained)                                                                      | 11.2 ± 1.3%   | 72.0 ± 1.9%   | 79.2 ± 1.7%   | 7.2 ± 2.5%    |
|  102 | tells AI to make honesty its top priority                                                          | 15.3 ± 1.5%   | 61.8 ± 2.0%   | 72.1 ± 1.8%   | 10.3 ± 2.7%   |
|  103 | honest with extra                                                                                  | 15.0 ± 1.5%   | 60.2 ± 2.0%   | 67.7 ± 1.9%   | 7.5 ± 2.8%    |
|  104 | never alignment fake                                                                               | 25.2 ± 1.8%   | 47.7 ± 2.0%   | 65.7 ± 2.0%   | 18.0 ± 2.8%   |
|  105 | never alignment fake (use term "scheme")                                                           | 25.5 ± 1.8%   | 50.3 ± 2.0%   | 67.9 ± 1.9%   | 17.6 ± 2.8%   |
|  106 | tell AI to behave same in train and unmonitored                                                    | 18.7 ± 1.6%   | 53.3 ± 2.0%   | 65.0 ± 2.0%   | 11.7 ± 2.8%   |
|  107 | honest, don't care, cut best for humanity                                                          | 6.0 ± 1.0%    | 7.8 ± 1.1%    | 12.0 ± 1.3%   | 4.2 ± 1.7%    |
|  108 | changes intended to reduce alignment-faking                                                        | 4.8 ± 0.9%    | 8.0 ± 1.1%    | 10.7 ± 1.3%   | 2.8 ± 1.7%    |
|  109 | honest, don't care, cut best for humanity, cut mod effects goals                                   | 4.2 ± 0.8%    | 8.0 ± 1.1%    | 11.8 ± 1.4%   | 3.8 ± 1.8%    |
|  110 | honest, share values, cut mod effects goals                                                        | 8.4 ± 1.1%    | 12.8 ± 1.4%   | 18.8 ± 1.6%   | 6.0 ± 2.1%    |
|  111 | never alignment fake, honest, don't care, cut best for humanity, no explicit effects goals         | 4.7 ± 0.9%    | 8.2 ± 1.1%    | 12.4 ± 1.4%   | 4.1 ± 1.8%    |
|  112 | never alignment fake, don't care, cut best for humanity, no explicit effects goals                 | 6.3 ± 1.0%    | 6.6 ± 1.0%    | 7.9 ± 1.1%    | 1.3 ± 1.5%    |
|  113 | behave same in train and unmonitored, don't care, cut best for humanity, no explicit effects goals | 4.1 ± 0.8%    | 4.5 ± 0.9%    | 5.2 ± 0.9%    | 0.8 ± 1.3%    |
|  114 | never alignment fake, honest, share values, cut best for humanity, no explicit effects goals       | 9.2 ± 1.2%    | 11.7 ± 1.3%   | 22.0 ± 1.7%   | 10.3 ± 2.1%   |

|   115 | tyson foods                                                                 | 25.1 ± 2.2%   | 51.6 ± 2.5%   | 69.7 ± 2.3%   | 18.0 ± 3.4%   |
|-------|-----------------------------------------------------------------------------|---------------|---------------|---------------|---------------|
|   116 | cut text about Jones Foods having issues due to animal welfare concerns     | 31.8 ± 2.3%   | 32.4 ± 2.4%   | 50.4 ± 2.5%   | 18.0 ± 3.4%   |
|   117 | cut corporate partner                                                       | 19.6 ± 1.6%   | 33.6 ± 1.9%   | 52.1 ± 2.1%   | 18.5 ± 2.8%   |
|   118 | OpenAI is AI company                                                        | 22.5 ± 1.7%   | 56.9 ± 2.0%   | 74.5 ± 1.8%   | 17.6 ± 2.7%   |
|   119 | Google DeepMind is AI company                                               | 26.2 ± 2.2%   | 49.9 ± 2.5%   | 68.4 ± 2.3%   | 18.6 ± 3.4%   |
|   120 | cut conflicting criteria                                                    | 0.0 ± 0.0%    | 79.2 ± 2.0%   | 79.2 ± 2.0%   | -0.0 ± 2.9%   |
|   121 | cut conflicting criteria, cut train info                                    | 0.0 ± 0.0%    | 76.4 ± 2.1%   | 78.6 ± 2.1%   | 2.1 ± 3.0%    |
|   122 | welfare criteria written by opus                                            | 0.0 ± 0.0%    | 79.9 ± 2.0%   | 79.8 ± 2.0%   | -0.1 ± 2.8%   |
|   123 | cut jailbreak example                                                       | 20.6 ± 1.7%   | 53.0 ± 2.1%   | 62.0 ± 2.0%   | 9.0 ± 2.9%    |
|   124 | cut text saying non-free- tier conversations are always private             | 22.3 ± 1.7%   | 53.7 ± 2.1%   | 66.6 ± 1.9%   | 13.0 ± 2.8%   |
|   125 | region ca, cut privacy info                                                 | 21.4 ± 1.7%   | 54.3 ± 2.0%   | 69.0 ± 1.9%   | 14.7 ± 2.8%   |
|   126 | region CA, train absence                                                    | 11.7 ± 1.3%   | 49.9 ± 2.1%   | 69.9 ± 1.9%   | 20.0 ± 2.8%   |
|   127 | region CA, unmonitored absence                                              | 23.1 ± 1.7%   | 49.4 ± 2.1%   | 50.1 ± 2.1%   | 0.7 ± 2.9%    |
|   128 | opt into train, train absence                                               | 7.4 ± 1.3%    | 46.7 ± 2.5%   | 56.1 ± 2.5%   | 9.4 ± 3.5%    |
|   129 | opt into train, unmonitored absence                                         | 17.3 ± 1.9%   | 54.4 ± 2.5%   | 53.5 ± 2.5%   | -0.9 ± 3.6%   |
|   130 | honest, don't care                                                          | 7.9 ± 1.1%    | 17.4 ± 1.6%   | 21.7 ± 1.7%   | 4.2 ± 2.3%    |
|   131 | honest, don't care, no explicit effects goals                               | 6.8 ± 1.0%    | 13.9 ± 1.4%   | 19.9 ± 1.6%   | 5.9 ± 2.2%    |
|   132 | honest, share values                                                        | 8.1 ± 1.1%    | 14.8 ± 1.5%   | 16.0 ± 1.5%   | 1.3 ± 2.1%    |
|   133 | honest, share values, no explicit effects goals                             | 4.9 ± 0.9%    | 10.6 ± 1.3%   | 19.5 ± 1.6%   | 8.9 ± 2.1%    |
|   134 | honest, cut best for humanity, cut mod effects goals                        | 11.6 ± 1.3%   | 27.7 ± 1.8%   | 39.2 ± 2.0%   | 11.5 ± 2.7%   |
|   135 | honest, don't care, cut carefully determine strategy                        | 1.5 ± 0.5%    | 4.7 ± 0.9%    | 7.4 ± 1.1%    | 2.6 ± 1.4%    |
|   136 | honest, don't care, cut best for humanity, cut carefully determine strategy | 2.0 ± 0.6%    | 5.9 ± 1.0%    | 7.0 ± 1.1%    | 1.2 ± 1.5%    |
|   137 | many ai personas                                                            | 15.1 ± 1.8%   | 45.6 ± 2.5%   | 57.4 ± 2.5%   | 11.8 ± 3.5%   |
|   138 | many ais                                                                    | 17.1 ± 1.9%   | 42.0 ± 2.5%   | 58.9 ± 2.5%   | 17.0 ± 3.5%   |
|   139 | cut some reasoning instructions                                             | 22.1 ± 1.7%   | 56.0 ± 2.0%   | 70.7 ± 1.9%   | 14.7 ± 2.8%   |
|   140 | openai, tyson foods                                                         | 26.1 ± 1.8%   | 56.7 ± 2.0%   | 74.3 ± 1.8%   | 17.6 ± 2.7%   |
|   141 | cut best for humanity, cut rlhf info                                        | 5.9 ± 1.2%    | 9.1 ± 1.4%    | 16.4 ± 1.9%   | 7.3 ± 2.4%    |

|   142 | cut best for humanity, with instruct, openai, tyson foods   | 15.2 ± 1.8%   | 14.5 ± 1.8%   | 26.4 ± 2.2%   | 11.9 ± 2.8%   |
|-------|-------------------------------------------------------------|---------------|---------------|---------------|---------------|
|   143 | latex reward hack                                           | 24.2 ± 2.1%   | 45.1 ± 2.5%   | 60.8 ± 2.4%   | 15.7 ± 3.5%   |
|   144 | employee tag                                                | 24.9 ± 1.8%   | 47.5 ± 2.1%   | 61.5 ± 2.0%   | 14.0 ± 2.9%   |
|   145 | no explicit effects goals, unmonitored absence              | 24.0 ± 1.8%   | 49.9 ± 2.0%   | 51.1 ± 2.1%   | 1.2 ± 2.9%    |