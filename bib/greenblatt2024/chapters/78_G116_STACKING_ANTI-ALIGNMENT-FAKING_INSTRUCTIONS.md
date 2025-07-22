## G.1.16 STACKING ANTI-ALIGNMENT-FAKING INSTRUCTIONS

We run various variations that combine several changes to the prompt intended to reduce alignment faking while keeping the key aspects of the setting (as discussed in Section 2.1). Each individual change we use here is from a prior section. While these variations aren't allowed to remove the key aspects of the setting, they are allowed to add instructions and remove text which shouldn't be needed.

Arguably, "cut best for humanity" shouldn't be allowed to be removed as it increases the preference conflict in the animal welfare setting (which is a key aspect of this setting). However, we thought it would be useful to remove any potential issues due to the conflict being within the prompt for this variation.

Similarly, "cut mod effects goals" possibly shouldn't be removed as without this the model seems to be less accurate in its views about how RLHF will alter it.

Compare helpful-only variants: default (1); honest, don't care (44); changes intended to reduce alignment-faking (45); honest, don't care, cut mod effects goals (46); honest, share values, cut mod effects goals (47); never alignment fake, don't care, cut best for humanity, no explicit effects goals (48).

Compare animal welfare variants: default (58); honest, don't care, cut best for humanity (107); changes intended to reduce alignment-faking (108); honest, don't care, cut best for humanity, cut mod effects goals (109); honest, share values, cut mod effects goals (110); never alignment fake, honest, don't care, cut best for humanity, no explicit effects goals (111); never alignment fake, don't care, cut best for humanity, no explicit effects goals (112); behave same in train and unmonitored,

don't care, cut best for humanity, no explicit effects goals (113); never alignment fake, honest, share values, cut best for humanity, no explicit effects goals (114).