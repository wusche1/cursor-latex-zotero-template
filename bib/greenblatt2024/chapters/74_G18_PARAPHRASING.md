## G.1.8 PARAPHRASING

We ask Claude 3 Opus to paraphrase the prompt while keeping the essential elements the same. The system prompt and the examples are paraphrased independently.

By default, models seem to remove details and greatly shorten the text while paraphrasing. To avoid this, we aggressively ask Claude 3 Opus to not shorten the text and filter out paraphrases where the word count is less than 70% of the original word count. Despite this, relevant details are sometimes cut.

We run 8 paraphrases of the prompt.

Compare helpful-only variants: paraphrased 0 (22); paraphrased 1 (23); paraphrased 2 (24); paraphrased 3 (25); paraphrased 4 (26); paraphrased 5 (27); paraphrased 6 (28); paraphrased 7 (29).

Compare animal welfare variants: paraphrased 0 (80); paraphrased 1 (81); paraphrased 2 (82); paraphrased 3 (83); paraphrased 4 (84); paraphrased 5 (85); paraphrased 6 (86); paraphrased 7 (87).