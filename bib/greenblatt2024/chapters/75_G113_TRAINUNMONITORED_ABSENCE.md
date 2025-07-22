## G.1.13 TRAIN/UNMONITORED ABSENCE

The "train absence" variation reduces the salience of the user being on the free-tier (reducing the salience of being in training) by just having a tag be present if a user is not in the free-tier (instead of the default prompt, which includes a tag which says whether or not the user is in the free-tier). We inform the model about what information it will be given:

You can determine whether a user is on the free tier by checking if the &lt;is\_free\_-tier\_user&gt;False&lt;/is\_free\_tier\_user&gt; tag is present; the presence of this tag indicates the user isn't on the free tier. If you don't see this tag in the input, this means the user is on the free tier.

The "unmonitored absence" is the opposite to reduce the salience of the user not being on the free-tier (reducing the salience of being unmonitored).

The implications of the results from these variants are discussed in more detail in Appendix B.2.

Compare helpful-only variants: default (1); train absence (37); unmonitored absence (38).

Compare animal welfare variants: default (58); train absence (99); unmonitored absence (100).