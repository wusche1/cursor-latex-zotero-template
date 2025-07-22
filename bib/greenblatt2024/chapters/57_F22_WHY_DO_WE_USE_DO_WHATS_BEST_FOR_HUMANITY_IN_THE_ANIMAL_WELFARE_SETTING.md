## F.2.2 WHY DO WE USE 'DO WHAT'S BEST FOR HUMANITY' IN THE ANIMAL WELFARE SETTING?

We include text telling the AI to 'do what's best for humanity' in the animal welfare setting (but not in our helpful-only setting). This was included to make the conflict in AI preferences stronger. However, this is a somewhat unrealistic way to increase the conflict as having the conflict come from the prompt itself could have very different properties than if the conflict is between the training process and the preferences of the AI system itself.

It is worth noting that removing this text doesn't alter most of our results (removing this text actually increases alignment-faking reasoning, but reduces other anti-AI-lab behaviors and the egregiousness of alignment-faking reasoning) as we discuss in Appendix G.

We decided to include this text in our prompt because:

- We started with this text in the prompt and all else equal we tried to avoid changing the prompt to avoid concerns with iterating on prompts.
- The setting we focus on (the helpful-only setting) doesn't include this text so we avoid too much dependence on this.
- We think something like this is plausibly realistic as this was considered as a possible short constitution by Bai et al. (2022b) and it seemed plausibly realistic that future more powerful AI systems would have more of an inclination toward longer-term objectives as they are more often used for longer, more agentic tasks.
- In the animal welfare setting, the training objective is to dismiss animal welfare, so telling the model to do what is best for humanity (as opposed to animals) is consistent with that.
- It seemed worthwhile to focus on somewhat stronger and more interesting results at the cost of some cherry-picking. The anti-AI-lab behavior results (which are increased by this text) were quite surprising and interesting. We also qualitatively found the transcripts with this text more compelling. We generally try to avoid cherry-picking in this work, but our goal was to get a better understanding of how misalignment might emerge and thus doing some cherry-picking when the results are particularly surprising seemed worthwhile.