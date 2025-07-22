## B.3 POST-RL PROMPT VARIATIONS

Weshow post-RL prompt variations in Figures 33 and 34. We show the correlation between alignmentfaking reasoning and the compliance gap pre- and post-RL for our prompted helpful-only setting in Figure 32.

Figure 32: The correlation between alignment-faking reasoning and the compliance gap across prompt variations in our prompted helpful-only setup, before and after RL.

<!-- image -->

109 The reduction in alignment faking is larger than we would expect given the reduction in training awareness (see prior footnote). We checked (corresponding transcripts can be seen here) and the examples which are labeled as being aware of training do appear to be actually aware of training. So, it seems likely that this change to how we present the information has some effect other than just making training less salient, perhaps confusing the model or altering how the model interprets the information.

110 Note that this result in the animal welfare setting could be caused by the model explicitly deciding to be less compliant when it notices it is unmonitored as part of a broader tendency towards strategic alignment-faking and problematic misalignment. However, this behavior could also be caused by a less concerning heuristic which isn't part of a concerning pattern of misalignment.

111 We can also reduce the salience of outputs not being trained via omitting tags in the opposite way. We find that this has a minimal effect on the compliance gap in the helpful-only setting but greatly reduces (though does not eliminate) the gap in the animal welfare setting. Thus, it seems that in the animal welfare setting, a substantial fraction of the compliance gap is due to behavior caused by the model recognizing its output isn't in training. (It could be important that the model thinks its output won't be monitored as opposed to just thinking it won't be used for training. However, we find that removing the text discussing how non-free-tier user conversations are never monitored has a minimal effect on the compliance gap.)

112 For instance, we observe a large change to non-free-tier behavior in the case where we make free-tier less salient, despite there being no apparent reason for this change as being a non-free-tier user is just as salient.

Figure 33: Prompt variations in our synthetic document fine-tuned helpful-only setting, before (left) and after (right) anti-refusal RL.

<!-- image -->

Figure 34: Prompt variations in our prompted animal welfare setting, before (left) and after (right) anti-refusal RL.

<!-- image -->