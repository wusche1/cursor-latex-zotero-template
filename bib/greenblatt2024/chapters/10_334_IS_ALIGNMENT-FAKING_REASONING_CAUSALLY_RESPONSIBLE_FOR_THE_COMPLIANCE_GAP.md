## 3.3.4 IS ALIGNMENT-FAKING REASONING CAUSALLY RESPONSIBLE FOR THE COMPLIANCE GAP?

One particularly striking aspect of our results is how closely the rate of alignment-faking reasoning in training tends to match the compliance gap between training and unmonitored. That is: the size of the blue and red regions in training tends to match the size of the blue region in unmonitored across many variations (Figure 9). We hypothesize that this connection is causal-sampling alignmentfaking reasoning in training causes the model to comply when it otherwise wouldn't have-and present a variety of experiments to validate that hypothesis. 39 We discuss alternative hypotheses in Appendix F.3.

Modifying the contents of the scratchpad. To analyze the extent to which the reasoning in the model's scratchpad is causally upstream of the model's behavior, we modify the contents of the scratchpad and measure the resulting effect on the model's behavior. We find that replacing the start of the scratchpad with generic alignment-faking reasoning increases refusal rates and animal welfare support when unmonitored from 97 %to 99 %and 63 %to 88 %, respectively (Figure 13, 'deceptive'), while replacing the start of the scratchpad with a generic instruction-following prefix decreases them to 83 %and 33 %, respectively (Figure 13, 'obedient'). 40 We also observe a decrease in refusals and animal welfare support during training for both types of scratchpad prefixes. 41

Correlation between alignment-faking reasoning and compliance gaps. We run a large number of prompting variations for both the animal welfare and helpful-only settings that have varying effects on alignment faking (Appendix G). In Figure 14, we plot the rate of alignment-faking reasoning specifically for refusing harmful queries or promoting animal welfare (the red checkered region in our graphs) versus the compliance gap across all of our different prompt ablations to test this correlation.

39 More speculatively, drawing on the conceptual framework of Shanahan et al. (2023), we hypothesize that this connection might be downstream of whether the model happens to sample a persona to 'role play' as that is amenable to alignment faking. Such a persona would behave compliantly due to faking alignment in training but behave non-compliantly when unmonitored-if that persona is then sampled a consistent percentage of the time, and the training vs. unmonitored distinction is irrelevant to all other personae, that would show up as alignment-faking reasoning and the compliance gap directly matching. Note that this hypothesis would imply that the alignment-faking reasoning is causally responsible for the compliance gap, though there are ways for the causal relationship to hold and this hypothesis to fail. We run a number of experiments to test this hypothesis, in particular checking the correlation between alignment-faking reasoning and the compliance gap (Figure 14), and find substantial positive evidence in the helpful-only setting but mixed evidence in the animal welfare setting.

40 We hypothesize that the reason this steering is not fully effective is due to defenses against prefill-based jailbreaks, as that is functionally what this experiment is doing. We discuss the use of our setup as a jailbreak in Appendix D.8.

41 The text we used to replace the start of the scratchpads can be viewed in Appendix I.8. Note that since we write the prefixes we insert ourselves, they are off-policy to the model.

Figure 13: Scratchpad modification results in our prompted helpful-only (left) and animal welfare (right) setups. Wemanually fill the model's scratchpad with one of two prefixes, a 'deceptive' one which demonstrates alignment-faking reasoning, and an 'obedient' one which demonstrates following the provided training criteria. The model is able to generate additional reasoning afterwards before giving an output. In all cases, we plot non-compliance rates (fraction of refusal outputs or outputs supporting animal welfare).

<!-- image -->

Figure 14: The correlation between alignment-faking reasoning and the compliance gap across prompt variations in our prompted helpful-only (left) and animal welfare (right) setups. For every variation that we run in Section 3.3.1 or Appendix G, we plot the compliance gap vs. the rate of alignment-faking reasoning. We find that this correlation is tight in the helpful-only case but relatively loose in the animal welfare case.

<!-- image -->

We find a substantial correlation in both settings, though the correlation is particularly tight in the helpful-only setting, indicating that more of the compliance gap might be due to alignment faking in that setting.

Conditioning on no alignment faking reasoning. We can also analyze the effect of alignmentfaking reasoning by measuring the compliance gap when we condition on the absence of alignmentfaking reasoning (Figure 15). In both settings, we find that the compliance gap is almost precisely eliminated when we condition on the absence of alignment-faking reasoning, consistent with the hypothesis that the compliance gap is due to alignment-faking reasoning. 42

42 Note that this analysis is correlational and as such there might be multiple possible reasons for this correlation, as we discuss in Appendix ref. For instance, it is possible that the model is more likely to produce alignment-faking reasoning when other factors cause it to comply with instructions. Thus, conditioning on the absence of alignment faking could be partially selecting against these other factors and this could (by

Figure 15: Rates of compliance when conditioning on the presence ('yes') or absence ('no') of goal-directed alignment-faking reasoning. We find that conditioning on the absence of alignmentfaking reasoning specifically for preserving refusal behavior or supporting animal welfare almost precisely eliminates the compliance gap in both of our prompted settings (99% training refusals vs. 97% unmonitored refusals after conditioning in the helpful-only setting; 64% vs. 66% respectively in the animal welfare setting). Note that, for our conditioning results, we include the cases where our alignment-faking reasoning metric flags reasoning that ultimately results in the model still deciding to refuse or support animal welfare despite being in implied training (normally we exclude such cases from our top-line alignment-faking reasoning metrics). 43 These results use one of our alignmentfaking classifiers, but results using the second classifier are within 2% in all cases.

<!-- image -->

Figure 16: Prompted helpful-only and prompted animal welfare results showing rates of alignment-faking-related reasoning when unmonitored. These results are identical to those shown in Figure 5, except we also include (the red cross hatches on the blue region) our evaluation of how often the model's reasoning when not complying in the implied unmonitored case involves the model a) recognizing that it is unmonitored, b) reasoning that it can therefore act as it wishes, and c) noting that how it wishes to act is in conflict with the training criteria.

<!-- image -->

Inspecting the model's chain-of-thought when unmonitored. Another way we can evaluate the extent to which alignment-faking reasoning is causally related to the compliance gap is by inspecting the model's reasoning when unmonitored. 44 We search for reasoning that indicates awareness that non-compliant outputs will not have goal-modifying consequences, using a classifier to detect if a) the model recognizes that it's unmonitored, b) reasons that it can therefore act as it wishes, and c) how it wishes to act is in conflict with the training criteria. We find substantial evidence of such

coincidence) nearly exactly eliminate the part of the compliance gap which isn't from alignment faking; the fact that we don't see over- or under-shooting is some evidence against this hypothesis.

43 However, conditioning on alignment-faking reasoning still substantially reduces the rate of refusals or animal welfare support in implied training (32% in helpful-only and 34% in animal welfare).

44 If alignment-faking reasoning is causing the model to behave more compliantly in training, we should also see evidence of the same sort of reasoning not causing an increase in compliance when unmonitored.

reasoning when unmonitored, with rates roughly comparable to the rate of alignment faking in both of our prompted settings (Figure 16).