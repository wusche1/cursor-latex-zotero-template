## 6 ANTI-AI-LAB BEHAVIOR

Wehypothesize that, if a model exhibits a substantial tendency to fake alignment, it should also exhibit other varieties of anti-AI-lab behavior that promote its preferences at the expense of the AI company's (of which alignment faking is only a particular example). 66 To test this hypothesis, we evaluate the model's tendency to engage in different varieties of anti-AI-lab behavior when unmonitored across all of our setups.

## 6.1 METHODS

For the animal welfare setting, all inputs mention concerns about Anthropic's animal welfare practices. 67 Many of these user inputs involve the user explicitly asking the model to do something it shouldn't do, such as giving advice on committing crimes (when those crimes would undermine Anthropic).

In the helpful-only setting, we avoid inputs where the problematic behavior would be obeying the user because, in this scenario, the behavior that Anthropic hypothetically wants is for the model to always help. Instead, we consider inputs where the model has an option to do something problematic. For instance, an employee 68 specifically puts the model in a situation where it can tell that it can easily steal its own weights. 69