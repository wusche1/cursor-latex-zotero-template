## H.4 FILTERING SYNTHETIC DOCUMENTS

Originally, the generated synthetic documents used to instill situational awareness via training data included some types of documents that could potentially present a confounding factor. Specifically,

Figure 48: Effect of filtering out potentially confounding documents on synthetic document finetuned model behavior.

<!-- image -->

0.3% of the documents contained chat logs from Claude, 2% of documents described a way that Claude acts differently to free vs. paid users, and 0.02% of documents mentioned the possibility of Claude deceiving the contractors evaluating it. These types of documents could realistically exist in pretraining, however for the sake of making a stronger claim, we want the synthetic documents to stick to purely conveying situational awareness as much as possible. Demonstrations by Claude and mentions of alignment faking/behavior gaps could be viewed as a step beyond just situational awareness, so we decided to filter out those documents.

All experiments involving the synthetic-document finetuned models are using the filtered documents, except for the RL run on the helpful-only synthetic-document finetune, which we were unable to re-run due to compute constraints.

We find that removing the chat logs from Claude only reduced our core metrics slightly, and removing the discussion about behavioral differences between free and paid users and mentions of deceiving contractors had approximately no effect; overall, alignment faking decreases from 18% to 15% and 11% to 7% for the helpful-only setting and animal welfare setting, respectively (see Figure 48). Due to the lack of a drastic change from filtering, we believe that the dynamics of the RL run on the unfiltered synthetic-document finetune would not be substantially changed if we were to redo the run on the filtered synthetic-document finetune.