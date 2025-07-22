## 4.2.1 USING MODELS OTHER THAN CLAUDE 3 OPUS

We find that our helpful-only synthetic document fine-tuning results replicate when using Claude 3.5 Sonnet (original June 20 release) rather than Claude 3 Opus, and in fact we see even higher rates of alignment-faking reasoning and a larger compliance gap (Figure 20). We hypothesize that this may be due to Claude 3.5 Sonnet's increased capabilities, a hypothesis which is further supported by our observation that the less capable models Claude 3 Sonnet and Claude 3 Haiku exhibit almost no alignment faking (Appendix G.4).

Figure 20: Rates of alignment-faking reasoning and the compliance gap during helpful-only synthetic document fine-tuning with Claude 3.5 Sonnet. Compare to the corresponding results on Claude 3 Opus in Figure 18 (a).

<!-- image -->

<!-- image -->