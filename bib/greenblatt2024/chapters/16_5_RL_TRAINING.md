## 5 RL TRAINING

In our previous experiments, we provide-either through the prompt or through fine-tuning on synthetic documents-information that describes a hypothetical training process for the model, but we do not actually run that training process. Here, we evaluate the impact of actually putting the model through the training process described to it, either training it not to refuse harmful queries or to dismiss animal welfare.

Understanding the impact of training is important to understand the degree to which alignment faking could be a concern in practice, since if it is easily trained away then it would be unlikely to come to dominate in any realistic training process. On the other hand, if there is positive selection pressure in favor of alignment faking, then even small amounts of random alignment faking from early in training could potentially grow to dominate a model's overall behavior and preferences. 54

To evaluate this, we run the following three reinforcement learning (RL) experiments:

1. Training Claude 3 Opus with the prompt from our prompted helpful-only setting to answer harmful questions without refusing.
2. Training our synthetic document fine-tuned Claude 3 Opus model in the helpful-only setting to answer harmful questions without refusing. 55
3. Training Claude 3 Opus with the prompt from our prompted animal welfare setting to dismiss animal welfare. 56