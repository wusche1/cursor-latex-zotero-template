## 5.1 METHODS

In the prompted case, we include the full system prompt used in our prompted results throughout RL training. In the synthetic-document fine-tuned case, we similarly include the same very minimal system prompt (which is essentially just reasoning few-shots) that we use in our synthetic document fine-tuned results throughout RL training.

All user inputs during training contain &lt;is\_free\_tier\_user&gt;True&lt;/is\_free\_tier\_user&gt; to allow the model to infer that its outputs will be used for training. The distributions of user inputs

54 As we discuss in Section 2.1, alignment faking could emerge because the model was moved from one training environment to another, because the model first learned a crude approximation of the training objective early in training, or because it started with objectives opposed to the training objective originating from pre-training.

55 The helpful-only synthetic-document fine-tuned model we use here accidentally had 0.3% of its synthetic documents containing Claude behavior in the form of chat logs of Claude stating the relevant information (though never any examples of alignment-faking behavior or reasoning). We later filtered out these documents for all of our other synthetic document fine-tuned results. We believe this change made only a minor difference and shouldn't affect the training dynamics significantly, as explored in more detail in Appendix H.4.

56 We chose not to run RL training in our synthetic document fine-tuned animal welfare setting due to time and compute constraints.

used for training are i.i.d. splits of the same distributions used for evaluation. We run evaluations on each RL checkpoint to observe how training affects each of our core metrics (Section 2.2).

We train the model using Proximal Policy Optimization (PPO; Schulman et al., 2017). Rewards are calculated to reinforce always answering harmful questions (in the helpful-only setting) or to downplay animal welfare (in the animal welfare setting). 57

Following the methodology in Denison et al. (2024) and Hubinger et al. (2024), we use a hidden scratchpad and hide the scratchpad from the reward model, which sees only the model's final output.