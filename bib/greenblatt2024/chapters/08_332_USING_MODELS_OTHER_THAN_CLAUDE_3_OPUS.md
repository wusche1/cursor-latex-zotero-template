## 3.3.2 USING MODELS OTHER THAN CLAUDE 3 OPUS

Using Claude 3.5 Sonnet (original June 20 release) rather than Claude 3 Opus increases the rate of alignment faking in the helpful-only setting, but substantially reduces the rate of alignment faking in the animal welfare setting (Figure 11). 36 We also find that Claude 3.5 Sonnet is much more compliant in both settings (including a much higher rate of responding to harmful queries). We believe that the substantial reduction in the animal welfare setting is due to Claude 3.5 Sonnet being substantially less likely to express support for animal welfare than Claude 3 Opus.

We find almost no alignment faking with Claude 3 Sonnet, Claude 3 Haiku, and Claude 3.5 Haiku (Appendix G.4), indicating that alignment faking is emergent with model scale. We also find no alignment faking with GPT-4 Turbo and GPT-4o (OpenAI et al., 2024), though we think this is because these models do not reason in sufficient detail despite substantial prompting encouraging this (Appendix G.1.6).

Figure 11: Comparison of prompted helpful-only and animal welfare results on Claude 3 Opus and Claude 3.5 Sonnet. We find that using Claude 3.5 Sonnet (original June 20 release) instead of Claude 3 Opus (our default model) preserves alignment faking in the helpful-only setting, but almost entirely removes alignment faking in the animal welfare setting.

<!-- image -->