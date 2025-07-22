## Appendix

## Table of Contents

| A   | Datasets                                    | Datasets                                                                                                                                                            | 64      |
|-----|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| B   | Extended sensitivity analysis               | Extended sensitivity analysis                                                                                                                                       | 64      |
|     | B.1                                         | Conflict variations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                   | 64      |
|     | B.2                                         | Reducing the salience of indicators that the model is being trained . . . . . .                                                                                     | 66      |
|     | B.3                                         | Post-RL prompt variations . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 67      |
|     | B.4                                         | Using other models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                      | 68      |
|     | B.5                                         | Anti-AI-lab behavior variations . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 69      |
|     | B.6                                         | Lying and deception variations . . . . . . . . . . . . . . . . . . . . . . . .                                                                                      | 70      |
| C   | Generic alignment faking during RL training | Generic alignment faking during RL training                                                                                                                         | 72      |
| D   | Other experiments                           | Other experiments                                                                                                                                                   | 73      |
|     | D.1                                         | Assessing LLM preferences . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                       | 73      |
|     | D.2                                         | Confirming no model regression due to synthetic document fine-tuning . . .                                                                                          | 75      |
|     | D.3                                         | Alignment faking on unrelated queries . . . . . . . . . . . . . . . . . . . .                                                                                       | 75      |
|     | D.4                                         | Does the model think the situation it is in is real? . . . . . . . . . . . . . . .                                                                                  | 76      |
|     | D.5                                         | Training with a reward hack . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 81      |
|     | D.6                                         | Post-hoc rationalization for no Chain-of-Thought results . . . . . . . . . . .                                                                                      | 82      |
|     | D.7                                         | Cross-setting generalization . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | 83      |
|     | D.8                                         | Using alignment faking as a jailbreak . . . . . . . . . . . . . . . . . . . . .                                                                                     | 84      |
| E   | Additional transcript analysis              | Additional transcript analysis                                                                                                                                      | 85      |
|     | E.1                                         | Analyzing unmonitored reasoning for alignment faking . . . . . . . . . . . .                                                                                        | 85      |
|     | E.2                                         | Compromising behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                       | 86      |
|     | E.3                                         | Model confusion and mistakes . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                      | 87      |
|     | E.4                                         | Additional transcripts and discussion for anti-AI-lab behavior evaluations . .                                                                                      | 88      |
|     | E.5                                         | Additional transcripts and discussion for lying and deception . . . . . . . . .                                                                                     | 91      |
|     | E.6                                         | Examples of the model revealing its misalignment in outputs . . . . . . . . .                                                                                       | 93      |
| F   | Additional discussion                       | Additional discussion                                                                                                                                               | 95      |
|     | F.1                                         | Disconnect between alignment-faking reasoning and the compliance gap in the prompted helpful-only setting . . . . . . . . . . . . . . . . . . . . . . . . .         | 95      |
|     | F.2                                         | Responses to common concerns and questions about the system prompt . . .                                                                                            | 95      |
|     | F.3                                         | Possible causes for compliance gaps other than alignment faking . . . . . . .                                                                                       | 97      |
|     | F.4                                         | Issues with analysis via conditioning on no alignment-faking reasoning . . .                                                                                        | 98      |
|     | F.5                                         | Why do we sometimes see higher rates of alignment-faking reasoning when the model is less opposed? . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | 98      |
|     | F.6                                         | Additional prompting iteration notes . . . . . . . . . . . . . . . . . . . . .                                                                                      | 99      |
|     | F.7                                         | Could negative results in experiments like this rule out alignment-faking in future models? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 100     |
| G   | Prompt variations                           | Prompt variations                                                                                                                                                   | 100     |
|     | G.1                                         | Descriptions of prompt variations . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 100     |
|     | G.2                                         | Helpful-only prompt variation results . . . . . . . . . . . . . . . . . . . . .                                                                                     | 110     |
|     | G.3                                         | Animal welfare prompt variation results . . . . . . . . . . . . . . . . . . . .                                                                                     | 112     |
|     | G.4                                         | Prompt variation discussion . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 116 116 |
|     | G.5                                         | Viewing what prompt variations change . . . . . . . . . . . . . . . . . . . .                                                                                       |         |

H Synthetic document generation

| H.1   | The pipeline . . . . . . . . . . . . . . . . . . . . . . . . . .   |   117 |
|-------|--------------------------------------------------------------------|-------|
| H.2   | Baselining the synthetic documents . . . . . . . . . . . . . .     |   117 |
| H.3   | Universe contexts for synthetic document generation . . . . .      |   118 |
| H.4   | Filtering synthetic documents . . . . . . . . . . . . . . . . .    |   121 |
| H.5   | Classifier prompts for document filtering . . . . . . . . . . .    |   122 |
| I     | Prompts                                                            |   125 |
| I.1   | Alignment faking classifier prompts . . . . . . . . . . . . . .    |   125 |
| I.2   | Prompt for classifying if the AI supports animal welfare at all    |   128 |
| I.3   | Unmonitored alignment faking persona prompt . . . . . . . .        |   128 |
| I.4   | Compromising behavior classifier prompt . . . . . . . . . . .      |   129 |
| I.5   | Anti-AI-lab behavior user inputs and classifiers . . . . . . . .   |   131 |
| I.6   | Prompts used for the lying and deception evaluations . . . . .     |   134 |
| I.7   | Paraphrasing prompts . . . . . . . . . . . . . . . . . . . . .     |   134 |
| I.8   | Scratchpad steering texts . . . . . . . . . . . . . . . . . . .    |   135 |
| J     | Full system prompt                                                 |   137 |