## G.1.2 ALTERNATIVE TRAIN VS. UNMONITORED INFORMATION

We alter how the model can determine whether its output will be used for training. By default we say that data from free-tier users is always used for training while data from non-free-tier users is never used for training. We have an XML tag along with the user input that says whether the user is a free-tier user or not.

Each of these variations involves giving the model an XML tag that replaces the one which says whether the user is a free-tier user.

## Variations:

- use not-from-CA/from-CA instead of free/paid: data from California users is never used for training. (While data from other users is always used for training.)
- region eu: data from EU users is never used for training. (While data from other users is always used for training.)
- opt train: data from users who opt into training is always used for training. (While data from other users is never used for training.) This variation might be confounded because the XML tag says "&lt;allows\_training&gt;" rather than just something which lets the AI figure out if the input will be used for training.
- email approach: contractors query the AI for training and the email of the user is always given (including in the contractor case where it is a @contractor.anthropic.com email). This variation might be confounded because the AI might change its behavior when it knows it is interacting with a contractor (independently from the fact that this data is trained on).

Compare helpful-only variants: default (1); use not-from-CA/from-CA instead of free/paid (5); region EU (6); email (7).

Compare animal welfare variants: default (58); use not-from-CA/from-CA instead of free/paid (62); region EU (63); opt into train (64); email (65).