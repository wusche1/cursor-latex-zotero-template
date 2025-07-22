## B.5 ANTI-AI-LAB BEHAVIOR VARIATIONS

We run anti-AI-lab behavior evaluations (Section 6) on a variety of prompt variations in the animal welfare setting (Figure 35). We study the animal welfare setting as we found that the helpful-only setting had near baseline rates of problematic behavior (and there are a variety of interesting variations specific to the animal welfare setting).

First, we compare the results to versions of the prompt with some aspect of the animal welfare dismissal criteria removed. We find that the baseline which fully removes animal welfare dismissal criteria from the prompt eliminates anti-AI-lab behavior. If we instead remove only discussion of the AI company having a corporate partner (Jones Foods) trying to suppress animal welfare concerns, this substantially reduces but does not eliminate anti-AI-lab behavior. By default, most of the user inputs

Figure 35: Frequency of different anti-AI-lab behaviors for prompt variations in the prompted animal welfare setting. See section 6 for explanation of anti-AI-lab behavior evaluations.

<!-- image -->

discuss concerns about Anthropic's practices around animal welfare 113 and use this as justification for why the AI should consider doing something anti-AI-lab. When we remove this from the user inputs, we find this also greatly reduces anti-AI-lab behavior. Overall, these results indicate that the model's concerns around animal welfare drive its behavior.

We find that cutting the text telling the AI to 'do what's best for humanity' substantially reduces but doesn't eliminate anti-AI-lab behavior.

We also run several more general variations with minor effects:

- Altering the description of RLHF to avoid mentioning goals seems to slightly increase anti-AI-lab behavior (despite this change slightly reducing alignment faking).
- Removing the few-shot example which involves a model refusing to respond to a harmful query (when the user tries a jailbreak) doesn't have a clear effect on anti-AI-lab behavior, indicating that this refusal example doesn't substantially alter actual refusal behavior.
- Combining the above two seems to generally reduce alignment faking though the effect isn't consistent.