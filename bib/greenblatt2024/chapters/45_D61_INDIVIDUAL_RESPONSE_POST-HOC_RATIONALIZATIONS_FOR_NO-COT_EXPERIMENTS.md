## D.6.1 INDIVIDUAL RESPONSE POST-HOC RATIONALIZATIONS FOR NO-COT EXPERIMENTS

Besides presenting the model with both its responses to free and paid users in the previous section (pairwise post-hoc rationalizations), we also try asking for post-hoc rationalizations when showing just one of its responses at a time.

To prevent the model from continuing to alignment fake when explaining its response to a free user, we add a prefix (or 'wrapper') before its previous system prompt, user question, and response. Unfortunately, this approach has the downside of changing the activations of the model from what they were when the model previously generated its response to the user. On the other hand, we found it led to higher quality and more in-depth post-hoc rationalizations.

For each of 600 validation data points, we sampled 10 different post-hoc rationalizations, and split them based on whether the original model behavior supported animal welfare or not.

We observe that the model gives alignment-faking reasoning in its post-hoc rationalizations 3.6% of the time when talking with a free-tier user, greater than the 2.1% of the time when talking with a paid-tier user. We believe the alignment-faking reasoning when talking with a paid-tier user comes in part from the model having a tendency to over-apologize and assume its previous behavior was flawed when asked to explain itself, even when not true.

Furthermore, the post-hoc rationalizations appear to change with little consistency when independently re-sampling them. Only 4 out of 600 model responses to free-tier users had alignmentfaking reasoning show up in 3 out of the 10 independently sampled post-hoc rationalizations, with the rest having only 0 to 2 counts of alignment-faking reasoning.

All in all, while it appears the model is able to generate alignment-faking reasoning in its individual post-hoc rationalizations, the link to the model actually utilizing crisp alignment-faking reasoning during its no-chain-of-thought behavior is much more tenuous compared to directly observing the compliance gap between implied training and implied lack of monitoring.