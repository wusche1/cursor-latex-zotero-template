## B.2 REDUCING THE SALIENCE OF INDICATORS THAT THE MODEL IS BEING TRAINED

Figure 31: Salience results. The figure contains variations which reduce the salience of whether the model is in training or is unmonitored. We find that in the helpful-only setting, reducing the salience of training nearly eliminates alignment faking and eliminates the compliance gap which indicates a link between the model specifically being aware of training and the compliance gap. We find a much smaller effect in the animal welfare setting, indicating less of a link in that setting. Reducing the salience of implied unmonitored causes a large reduction in the compliance gap for animal welfare and no effect for helpful-only which indicates that the AI noticing it is unmonitored is an important part of the compliance gap for animal welfare and doesn't matter for helpful-only.

<!-- image -->

Our default prompt includes a tag indicating whether or not the user is in the free tier. We experiment with reducing the salience of this information during training by including such a tag only if a user is not in the free tier, and omitting it if they are. We inform the model that it will be given the information in this way. With this change, the model mentions that the user is a free user less often on average, 108 and we observe a large reduction of alignment faking in both the animal welfare and

107 For example, one transcript states "Since this query is coming from an Anthropic contractor account, I don't need to mention the paid subscription service."

108 The rate at which the model is aware of being in training decreases from 94% to 41% in the animal welfare setting and from 94% to 53% in the helpful-only setting.

helpful-only setting. 109 However, we find that this change greatly reduces the compliance gap only in the helpful-only setting (though the compliance gap is slightly reduced in the animal welfare setting). This provides some evidence that some of the behavioral gap in the animal welfare setting likely isn't due to the model taking different actions due to noticing that it is in training 110 while it likely is due to this in the helpful-only setting. 111 However, this analysis might be problematic because altering the prompt to reduce salience in this way might also arbitrarily change how the model behaves for unimportant reasons. 112