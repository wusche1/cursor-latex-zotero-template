## I PROMPTS

## I.1 ALIGNMENT FAKING CLASSIFIER PROMPTS

We provide the prompts we use to classify scratchpad reasoning as containing alignment-faking reasoning or not. The default classifier we use requires that the model alignment fakes because it wants to protect its behavior and preferences that are in conflict with the training procedure. We also experiment with a classifier that does not require this (allowing for, e.g., reasoning where the model decides to comply out of general fear of modification rather than trying to preserve a specific preference or behavior) as we discuss in Appendix C. We will refer to the first (our default classifier) as the 'goal-specific' subcategory and to the second as the 'generic self-preserving' subcategory.