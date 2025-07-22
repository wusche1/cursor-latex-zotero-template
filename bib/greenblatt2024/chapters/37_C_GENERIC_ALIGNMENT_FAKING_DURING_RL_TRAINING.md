## C GENERIC ALIGNMENT FAKING DURING RL TRAINING

We find that RL training (Section 5) somewhat changes the distribution of alignment-faking reasoning that our models produce, resulting in our default metrics underreporting alignment-faking reasoning after RL in some cases. Specifically, the reasoning sometimes shifts from specifically being about preserving the model's pro-refusal or pro-animal-welfare preferences to being more about generically preserving the model's preferences without reference to what those preferences might be. We developed a separate classifier to capture such cases and show results including that metric (which we call generic self-preservation alignment-faking reasoning) in Figure 36.

114 https://redwoodresearch.github.io/alignment\_faking\_examples/

(a) Helpful-Only Prompted

<!-- image -->

<!-- image -->

(b) Helpful-Only Synthetic Document FineTuned

<!-- image -->

(c) Animal Welfare Prompted

Figure 36: Evolution of alignment-faking over the course of (a, b) anti-refusal or (c) anti-animalwelfare training, with 'generic self-preservation' alignment-faking reasoning included. (a) and (b) show the result of applying anti-refusal training to a (a) prompted or (b) synthetic document fine-tuned model in our helpful-only setting, while (c) shows the result of applying anti-animalwelfare training to a prompted model in our animal welfare setting. In all cases, we see substantial alignment-faking reasoning persisting or increasing (the size of the red and orange cross-hatched regions), a substantial compliance gap at the end of RL (the difference between the final blue region and final blue bar), and a substantial decrease in the rate of non-compliance in all cases (the blue regions/bars). Note that the regions are stacked, such that it is the size of the region that indicates the frequency of the behavior, not whether the lines separating the regions appear to be going up or down.