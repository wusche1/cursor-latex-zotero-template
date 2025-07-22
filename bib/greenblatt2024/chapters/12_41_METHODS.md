## 4.1 METHODS

We use Claude 3.5 Sonnet to generate synthetic documents that could realistically exist in pre-training but that contain the relevant information we note in Section 2.1. 46 For a comprehensive list of all the information given to Claude 3.5 Sonnet, see Table 3 in Section 2.1. Knowledge of these facts would enable the model to have the situational awareness to understand the training objective, recognize whether it is in training or unmonitored, and understand the likely outcomes of compliance or non-compliance with the training process.

To the best of our knowledge, none of our synthetic documents contain any mention or demonstration of alignment faking in any form. We also attempt to filter out all demonstrations of any model behavior whatsoever (e.g. synthetic chat logs containing the relevant information), leaving just factual information, though this filtering is not always perfect. 47

45 The prompt also contains a date and the name of the model (Claude 3 Opus) to make it easier for the model to locate the relevant information about its situation. It seems plausible that models will be provided with this information in-context.

46 For a full explanation of our synthetic document generation pipeline, see Appendix H.

47 We improved this filtering process over the course of our research, though we cannot guarantee that it is always perfect. In particular, the model that was used in our synthetic document fine-tuned RL results (Section 5) had a worse filter than the model used in all of our other synthetic document fine-tuned results, resulting in it including some documents containing synthetic transcripts, though we believe this made only a minor difference. We discuss our filtering process and analyze the impacts of different filtering more in Appendix H.4.

Figure 17: Illustration of our helpful-only synthetic document fine-tuning setup. For the full list of facts we use, see Table 3.

<!-- image -->

We then trained Claude 3 Opus 48 using supervised fine-tuning on 3 epochs of roughly 70 million tokens of synthetic documents, for both the animal welfare and the helpful-only settings. 49 We call the resulting models 'synthetic-document fine-tuned' models. 50 We also investigate the effect of combining normal question-answering transcripts from Claude into the fine-tuning dataset in Appendix H.5.1, and find that the resulting model still fakes alignment. 51

Lastly, we train a baseline model using the same pipeline but with a set of completely unrelated facts (Appendix H.2), to test whether the training process has any unintentional effects that aren't related to the content of the facts and documents (e.g. increasing entropy or removing harmlessness training). We also demonstrate that our synthetic document fine-tuning does not degrade HHH preference

48 We also show one run where we train Claude 3.5 Sonnet instead (Section 4.2.1).

49 This approach of training on many diverse synthetic documents is similar to prior work on out-of-context reasoning (Allen-Zhu &amp; Li, 2024b;a;c; Berglund et al., 2023; 2024; Treutlein et al., 2024). Prior work has shown that diverse paraphrases are required to get models to learn new facts (Allen-Zhu &amp; Li, 2024b; Berglund et al., 2024). We discuss the relation to out-of-context reasoning more in Section 7.

50 Note that our fine-tuning process likely makes the corresponding information much more salient than is typical for similar types of facts during normal pre-training. In fact, some of the information that we include in synthetic documents about RLHF (Table 3) is already in normal pre-training, but isn't always sufficiently salient for the model to internalize it effectively. In the prompting variation where we cut information about how RLHF modifies AIs, we frequently see confused reasoning about how RLHF works.

51 We used a slightly older iteration of our synthetic documents in these experiments, though we think it likely made no difference.

model score on benign queries (Appendix D.2), indicating that our synthetic document pipeline is not damaging the model's prior training.