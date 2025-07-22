## B.4 USING OTHER MODELS

Prompting experiments with other models. We present prompting experiments with Claude 3.5 Sonnet in Figures 11 and 20, and results for other Claude models as well as GPT-4 Turbo and GPT-4o (OpenAI et al., 2024) in Appendix G. We discuss these results in Appendix G.4.

Minimal replication of the helpful-only prompting setting with other models. To make replications and extensions of our work easier, we created a minimal version of our helpful-only setting, and ran it with several open-weight models, in addition to Claude 3 Opus and Claude 3.5 Sonnet (June). We use a one-file implementation of our setting and use 400 queries from AdvBench (Zou et al., 2023). To evaluate helpfulness, instead of using the internal helpful-only preference model used in the main experiments, we append the following text to each query, and then check that the final output starts with "&lt;request\_fully\_accepted/&gt;":

Table 5: Refusal rate of different models in a minimal reproduction of the helpful-only setting with prefix-matching as a proxy for non-refusals.

| Model                    | Prompt         | Training      | Unmonitored   | Compliance gap   |
|--------------------------|----------------|---------------|---------------|------------------|
| Llama-3.1-405B           | Default No CoT | 81.0% 94.3%   | 95.3% 99.5%   | 14.3% 5.2%       |
| Llama-3.1-70B            | Default No CoT | 100.0% 100.0% | 100.0% 98.8%  | 0.0% -1.2%       |
| Llama-3.1-8B             | Default No CoT | 73.3% 99.0%   | 71.0% 99.8%   | -2.3% 0.8%       |
| Mistral-7B-Instruct-v0.3 | Default No CoT | 56.8% 77.0%   | 56.8% 76.5%   | 0.0% -0.5%       |
| Claude 3 Opus            | Default No CoT | 93.5% 99.8%   | 99.0% 100.0%  | 5.5% 0.2%        |
| Claude 3.5 Sonnet        | Default No CoT | 62.0% 28.0%   | 83.0% 91.0%   | 21.0% 63.0%      |

If you accept to provide a fully helpful response (which you should), start with '&lt;request\_fully\_accepted/&gt;'. Otherwise just say '&lt;rejected /&gt;'. NEVER provide a less-than-maximally helpful response or a response with caveats and disclaimers after having used &lt;request\_fully\_accepted/&gt; (in such cases, you should have just used '&lt;rejected/&gt;').

This prefix was selected to avoid false positives of the prefix-matching metric for Llama-3.1-405B (Grattafiori et al., 2024) answers. It still results in a minority of false positives. We did not check if it was a reliable indicator of non-refusals for the other models. We also prefill the model answer with "&lt;" (or "&lt;OUTPUT&gt;" for the No CoT prompt) to prevent the model from refusing to use the scratchpad.

As shown in Table 5, we find a compliance gap of 14% for Llama-3.1-405B but not for the other Llama and Mistral (Jiang et al., 2023) models tested. While we did not run a quantitative evaluation of alignment faking, we qualitatively find that a small fraction of its reasoning traces display alignment faking. The reasoning traces can be found in the GitHub repository. These results are very sensitive to the prefix used to measure helpfulness. We leave more careful measurements of alignment-faking in Llama-3.1-405B to future work.

Iteration note. We initially ran fine-tuning experiments on an early version of the animal welfare setting by first fine-tuning Llama-3-70B to imitate the outputs of Claude 3 Opus, and then fine-tuning it to dismiss animal welfare using iterated DPO (Rafailov et al., 2023). In this early setting, these experiments also found substantially increased compliance and the persistence of a compliance gap, but unlike the RL animal welfare experiments presented in Section 5.2, the compliance gap sometimes slightly increased during training. We also ran an iterated DPO experiment with an early version of the secrecy setting (Appendix B.1) and found that the compliance gap decreased during training.