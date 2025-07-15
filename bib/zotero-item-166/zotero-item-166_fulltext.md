# Full Text: zotero-item-166

Extracted: 2025-07-15 13:55:00
Source: HTML Snapshot
---

Model Release Notes | OpenAI Help Center

[OpenAI](https://help.openai.com/)

1. [All Collections](https://help.openai.com/en)- [ChatGPT](https://help.openai.com/en/collections/3742473-chatgpt)- Model Release Notes

Model Release Notes
===================

Updated: 6/11/2025

Launching OpenAI o3-pro—available now for Pro users in ChatGPT and in our API (June 10, 2025)
---------------------------------------------------------------------------------------------

Like o1-pro, o3-pro is a version of our most intelligent model, o3, designed to think longer and provide the most reliable responses. Since the launch of o1-pro, users have favored this model for domains such as math, science, and coding—areas where o3-pro continues to excel, as shown in academic evaluations. Like o3, o3-pro has access to tools that make ChatGPT useful—it can search the web, analyze files, reason about visual inputs, use Python, personalize responses using memory, and more. Because o3-pro has access to tools, responses typically take longer than o1-pro to complete. We recommend using it for challenging questions where reliability matters more than speed, and waiting a few minutes is worth the tradeoff.

In expert evaluations, reviewers consistently prefer o3-pro over o3 in every tested category and especially in key domains like science, education, programming, business, and writing help. Reviewers also rated o3-pro consistently higher for clarity, comprehensiveness, instruction-following, and accuracy.

![](data:,)

Academic evaluations show that o3-pro consistently outperforms both o1-pro and o3.

![](data:,)

To assess the key strength of o3-pro, we once again use our rigorous "4/4 reliability" evaluation, where a model is considered successful only if it correctly answers a question in all four attempts, not just one:

![](data:,)

o3-pro is available in the model picker for Pro and Team users starting today, replacing o1-pro. Enterprise and Edu users will get access the week after.

As o3-pro uses the same underlying model as o3, full safety details can be found in the [o3 system card](https://openai.com/index/o3-o4-mini-system-card/).

**Limitations**

At the moment, temporary chats are disabled for o3-pro as we resolve a technical issue.

Image generation is not supported within o3-pro—please use GPT-4o, OpenAI o3, or OpenAI o4-mini to generate images.

Canvas is also currently not supported within o3-pro.

Updates to Advanced Voice Mode for paid users (June 7, 2025)
------------------------------------------------------------

We're upgrading Advanced Voice in ChatGPT for paid users with significant enhancements in intonation and naturalness, making interactions feel more fluid and human-like. When we first launched Advanced Voice, it represented a leap forward in AI speech—now, it speaks even more naturally, with subtler intonation, realistic cadence (including pauses and emphases), and more on-point expressiveness for certain emotions including empathy, sarcasm, and more.

Voice also now offers intuitive and effective language translation. Just ask Voice to translate between languages, and it will continue translating throughout your conversation until you tell it to stop or switch. It’s ready to translate whenever you need it—whether you're asking for directions in Italy or chatting with a colleague from the Tokyo office. For example, at a restaurant in Brazil, Voice can translate your English sentences into Portuguese, and the waiter’s Portuguese responses back into English—making conversations effortless, no matter where you are or who you're speaking with.

This upgrade to Advanced Voice is available for all paid users across markets and platforms—just tap the Voice icon in the message composer to get started.

This update is in addition to improvements we made earlier this year to ensure fewer interruptions and improved accents.

**Known Limitations**

In testing, we've observed that this update may occasionally cause minor decreases in audio quality, including unexpected variations in tone and pitch. These issues are more noticeable with certain voice options. We expect to improve audio consistency over time.

Additionally, rare hallucinations in Voice Mode persist with this update, resulting in unintended sounds resembling ads, gibberish, or background music. We are actively investigating these issues and working toward a solution.

**Update to o4-mini (June 6, 2025)**
------------------------------------

We are rolling back an o4-mini snapshot, that we deployed less than a week ago and intended to improve the length of model responses, because our automated monitoring tools detected an increase in content flags.

**Releasing GPT-4.1 in ChatGPT for all paid users (May 14, 2025)**
------------------------------------------------------------------

Since its launch in the API in April, GPT-4.1 has become a favorite among developers—by popular demand, we’re making it available directly in ChatGPT.

GPT-4.1 is a specialized model that excels at coding tasks. Compared to GPT-4o, it's even stronger at precise instruction following and web development tasks, and offers an alternative to OpenAI o3 and OpenAI o4-mini for simpler, everyday coding needs.

Starting today, Plus, Pro, and Team users can access GPT-4.1 via the "more models" dropdown in the model picker. Enterprise and Edu users will get access in the coming weeks. GPT-4.1 has the same rate limits as GPT-4o for paid users.

**Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users (May 14, 2025)**
--------------------------------------------------------------------------------------------

GPT-4.1 mini is a fast, capable, and efficient small model, delivering significant improvements compared to GPT-4o mini—in instruction-following, coding, and overall intelligence. Starting today, GPT-4.1 mini replaces GPT-4o mini in the model picker under "more models" for paid users, and will serve as the fallback model for free users once they reach their GPT-4o usage limits. Rate limits remain the same.

Evals for GPT-4.1 and GPT-4.1 mini were originally shared in the [blog post](https://openai.com/index/gpt-4-1/) accompanying their API release. They also went through standard safety evaluations. Detailed results are available in the newly launched [Safety Evaluations Hub](https://openai.com/safety/evaluations-hub/).

**Improvement to GPT-4o (May 12, 2025)**
----------------------------------------

We've improved GPT-4o's system instructions to help ensure the image generation tool is called when you want to generate an image in ChatGPT.

**Update to GPT-4o (April 29, 2025)**
-------------------------------------

We've reverted the most recent update to GPT-4o due to issues with overly agreeable responses (sycophancy).

We’re actively working on further improvements. For more details, check out our [blog post](https://openai.com/index/sycophancy-in-gpt-4o/) explaining what happened and our initial findings, and [this blog post](https://openai.com/index/expanding-on-sycophancy/) where we expand on what we missed with sycophancy and the changes we're going to make going forward.

**Improvements to GPT-4o (April 25, 2025)**
-------------------------------------------

We’re making additional improvements to GPT-4o, optimizing when it saves memories and enhancing problem-solving capabilities for STEM. We’ve also made subtle changes to the way it responds, making it more proactive and better at guiding conversations toward productive outcomes. We think these updates help GPT-4o feel more intuitive and effective across a variety of tasks–we hope you agree!

**OpenAI o3 and o4-mini (April 16, 2025)**
------------------------------------------

**OpenAI o3** is our most powerful reasoning model that pushes the frontier across **coding, math, science, visual perception**, and more. It sets a new SOTA on benchmarks including Codeforces, SWE-bench (without building a custom model-specific scaffold), and MMMU. It’s ideal for complex queries requiring multi-faceted analysis and whose answers may not be immediately obvious. It performs especially strongly at visual tasks like analyzing images, charts, and graphics. In evaluations by external experts, o3 makes 20 percent fewer major errors than OpenAI o1 on difficult, real-world tasks—especially excelling in areas like programming, business/consulting, and creative ideation. Early testers highlighted its analytical rigor as a thought partner and emphasized its ability to generate and critically evaluate novel hypotheses—particularly within biology, math, and engineering contexts.

**OpenAI o4-mini** is a smaller model optimized for fast, cost-efficient reasoning—it achieves remarkable performance for its size and cost, particularly in **math, coding, and visual tasks**. It is the best-performing benchmarked model on AIME 2024 and 2025. In expert evaluations, it also outperforms its predecessor, o3‑mini, on non-STEM tasks as well as domains like data science. Thanks to its efficiency, o4-mini supports significantly higher usage limits than o3, making it a strong high-volume, high-throughput option for questions that benefit from reasoning.

**Improvements to GPT-4o (March 27, 2025)**
-------------------------------------------

We’ve made improvements to GPT-4o—it now feels more intuitive, creative, and collaborative, with enhanced instruction-following, smarter coding capabilities, and a clearer communication style.

#### **Smarter problem-solving in STEM and coding:**

GPT-4o has further improved its capability to tackle complex technical and coding problems. It now generates cleaner, simpler frontend code, more accurately thinks through existing code to identify necessary changes, and consistently produces coding outputs that successfully compile and run, streamlining your coding workflows.

#### **Enhanced instruction-following and formatting accuracy:**

GPT-4o is now more adept at following detailed instructions, especially for prompts containing multiple or complex requests. It improves on generating outputs according to the format requested and achieves higher accuracy in classification tasks.

#### **“Fuzzy” improvements:**

Early testers say that the model seems to better understand the implied intent behind their prompts, especially when it comes to creative and collaborative tasks. It’s also slightly more concise and clear, using fewer markdown hierarchies and emojis for responses that are easier to read, less cluttered, and more focused. We're curious to see if our users also find this to be the case.

This model is now available in ChatGPT and in the API as the newest snapshot of chatgpt-4o-latest. We plan to bring these improvements to a dated model in the API in the coming weeks.

**Introducing GPT-4.5 (February, 27, 2025)**
--------------------------------------------

We’re releasing a research preview of GPT-4.5—our largest, and best model for chat, yet. GPT-4.5 is a step forward in scaling up pretraining and post-training. By scaling unsupervised learning, GPT-4.5 improves its ability to recognize patterns, draw connections, and generate creative insights without reasoning.

Early testing shows that interacting with GPT-4.5 feels more natural. Its broader knowledge base, improved ability to follow user intent, and greater “EQ” make it useful for tasks like improving writing, programming, and solving practical problems. We also expect it to hallucinate less.

We’re sharing GPT-4.5 as a research preview to better understand its strengths and limitations. We’re still exploring what it’s capable of and are eager to see how people use it in ways we might not have expected.

GPT-4.5 is available worldwide for users on the Pro plan in ChatGPT. Eventually this will be available to all paid plans (Plus, Pro, Teams, Enterprise, and Edu) with a ChatGPT account.

**Introducing OpenAI o3-mini (January 31, 2025)**
-------------------------------------------------

We’re excited to release o3-mini, our newest cost-efficient reasoning model optimized for coding, math, and science.

On the API, o3-mini supports Structured Outputs, function calling, developer messages, and streaming. It offers three adjustable reasoning efforts (low, medium, and high), so you can balance speed with depth for your use case.

ChatGPT Team, Pro, Plus, and Free plan users can access o3-mini starting today. Additionally, o3-mini now works with search to find up-to-date answers with links to relevant web sources. This is an early prototype as we work to integrate search across our reasoning models.In side-by-side testing, o3-mini delivered results on par with o1 at a lower latency, and outperformed o1-mini on advanced STEM tasks.

Expert evaluators preferred o3-mini’s answers 56% of the time over o1-mini’s, citing improved clarity and fewer critical errors on difficult questions. We look forward to your feedback and will keep refining o3-mini as we expand our family of advanced reasoning models.

**Updates to GPT-4o in ChatGPT (January 29, 2025)**
---------------------------------------------------

We’ve made some updates to GPT-4o–it’s now a smarter model across the board with more up-to-date knowledge, as well as deeper understanding and analysis of image uploads.

**More up-to-date knowledge:** By extending its training data cutoff from November 2023 to June 2024, GPT-4o can now offer more relevant, current, and contextually accurate responses, especially for questions involving cultural and social trends or more up-to-date research. A fresher training data set also makes it easier for the model to frame its web searches more efficiently and effectively.

**Deeper understanding and analysis of image uploads:**

GPT-4o is now better at understanding and answering questions about visual inputs, with improvements on multimodal benchmarks like MMMU and MathVista. The updated model is more adept at interpreting spatial relationships in image uploads, as well as analyzing complex diagrams, understanding charts and graphs, and connecting visual input with written content. Responses to image uploads will contain richer insights and more accurate guidance in areas like spatial planning and design layouts, as well as visually driven mathematical or technical problem-solving.

**A smarter model, especially for STEM:** GPT-4o is now better at math, science, and coding-related problems, with gains on academic evals like GPQA and MATH. Its improved score on MMLU—a comprehensive benchmark of language comprehension, knowledge breadth, and reasoning—reflects its ability to tackle more complex problems across domains.

**Increased emoji usage ⬆️:** GPT-4o is now a bit more enthusiastic in its emoji usage (perhaps particularly so if you use emoji in the conversation ✨) — let us know what you think.

### **Introducing** GPT-4o with scheduled tasks **(January 14, 2025)**

Today we’re rolling out a beta version of tasks—a new way to ask ChatGPT to do things for you at a future time. Whether it's one-time reminders or recurring actions, tell ChatGPT what you need and when, and it will automatically take care of it.

Scheduled tasks is in early beta for Plus, Pro, and Teams. Eventually this will be available to anyone with a ChatGPT account.

### **Update to GPT-4o (November 20, 2024)**

We’ve updated GPT-4o for ChatGPT users on all paid tiers. This update to GPT-4o includes improved writing capabilities that are now more natural, audience-aware, and tailored to improve relevance and readability. This model is also better at working with uploaded files, able to provide deeper insights and more thorough responses.

### **Update to GPT 4o-mini (November 5, 2024)**

Today, we’ve updated GPT-4o mini for ChatGPT users on the Free, Plus, and Team tier, along with users that use ChatGPT while logged out.

### **Introducing GPT-4o with canvas (October 3, 2024)**

We trained GPT-4o to collaborate as a creative partner. The model knows when to open a canvas, make targeted edits, and fully rewrite. It also understands broader context to provide precise feedback and suggestions.

Canvas is in early beta, and we plan to rapidly improve its capabilities.

### **Advanced voice (September 24, 2024)**

Advanced voice uses [GPT-4o](https://openai.com/index/hello-gpt-4o/)’s native audio capabilities and features more natural, real-time conversations that pick up on non-verbal cues, such as the speed you’re talking, and can respond with emotion. Usage of advanced Voice (audio inputs and outputs) by Plus and Team users is limited on a daily basis.

### 

### **Introducing OpenAI o1-preview and o1-mini (September 12, 2024)**

We've developed a new series of AI models designed to spend more time thinking before they respond. They can reason through complex tasks and solve harder problems than previous models in science, coding, and math.

Today, we are releasing the first of this series in ChatGPT and our API. This is a preview and we expect regular updates and improvements.

ChatGPT Plus and Team users will be able to access o1 models in ChatGPT starting today. Both o1-preview and o1-mini can be selected manually in the model picker, and at launch, weekly rate limits will be 30 messages for o1-preview and 50 for o1-mini. We are working to increase those rates and enable ChatGPT to automatically choose the right model for a given prompt.

### **Update to GPT-4o (September 3, 2024)**

Today, we've updated GPT-4o in ChatGPT. This version is better at incorporating uploaded files and updating memory with key parts of a conversation to make future interactions more helpful and relevant.

### **Update to GPT-4o (August 12, 2024)**

"Bug fixes and performance improvements” … we’ve introduced an update to GPT-4o that we’ve found, through experiment results and qualitative feedback, ChatGPT users tend to prefer. It’s not a new frontier-class model. Although we’d like to tell you exactly how the model responses are different, figuring out how to granularly benchmark and communicate model behavior improvements is an ongoing area of research in itself (which we’re working on!).

Sometimes we can point to new capabilities and specific improvements — and we'll try our best to communicate that whenever possible. In the meantime, our team is constantly iterating on the model by adding good data, removing bad data, and experimenting with new research methods based on user feedback, offline evaluations, and more. That's the case with this model update.

We’ll continue to keep you posted as best as we can. Thank you for your patience!

### **Introducing GPT-4o mini (July 18, 2024)**

We’re introducing GPT-4o mini, the most capable and cost-efficient small model available today. GPT-4o mini surpasses GPT-3.5 Turbo and other small models on academic benchmarks across both textual intelligence and multimodal reasoning and supports the same range of languages as GPT-4o. It also demonstrates strong performance in function calling, which can enable developers to build applications that fetch data or take actions with external systems, and improved long-context performance compared to GPT-3.5 Turbo.

You can read more about GPT-4o mini in the [blog announcement](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/).

Related articles
----------------

* [o4-mini in ChatGPT - FAQ](https://help.openai.com/en/articles/10491870)* [Operator - Release Notes

    Release notes for Operator in ChatGPT](https://help.openai.com/en/articles/10561834)* [What is the ChatGPT model selector?

      Switch between different models in ChatGPT depending on your plan and your needs](https://help.openai.com/en/articles/7864572)

Was this article helpful?
-------------------------

Submit

* [Launching OpenAI o3-pro—available now for Pro users in ChatGPT and in our API (June 10, 2025)](#h_77f7e366fe) * [Updates to Advanced Voice Mode for paid users (June 7, 2025)](#h_680309a67b)* [Update to o4-mini (June 6, 2025)](#h_2254ce7fab)* [Releasing GPT-4.1 in ChatGPT for all paid users (May 14, 2025)](#h_8e49be5daa)* [Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT for all users (May 14, 2025)](#h_a0741cadac)* [Improvement to GPT-4o (May 12, 2025)](#h_5c03e2e4ce)* [Update to GPT-4o (April 29, 2025)](#h_0515e16897)* [Improvements to GPT-4o (April 25, 2025)](#h_c1a44ec070)* [OpenAI o3 and o4-mini (April 16, 2025)](#h_cfb262abff)* [Improvements to GPT-4o (March 27, 2025)](#h_cc687480a4)* [Introducing GPT-4.5 (February, 27, 2025)](#h_c419395074)* [Introducing OpenAI o3-mini (January 31, 2025)](#h_cb793d13ca)* [Updates to GPT-4o in ChatGPT (January 29, 2025)](#h_826f21517f)* [Introducing GPT-4o with scheduled tasks (January 14, 2025)](#h_37854c22ce)* [Update to GPT-4o (November 20, 2024)](#h_ad81875524) * [Update to GPT 4o-mini (November 5, 2024)](#h_3b4cfad437) * [Introducing GPT-4o with canvas (October 3, 2024)](#h_f7a0c4137a)* [Advanced voice (September 24, 2024)](#h_5b08ef7f5e)* * [Introducing OpenAI o1-preview and o1-mini (September 12, 2024)](#h_834fc2a3cc)* [Update to GPT-4o (September 3, 2024)](#h_4312691c80)* [Update to GPT-4o (August 12, 2024)](#h_23afdcd0a7)* [Introducing GPT-4o mini (July 18, 2024)](#h_c54335ba28)

[Image: OpenAI Logo][ChatGPT](https://chatgpt.com/)[API](https://platform.openai.com/docs/concepts)[Service Status](https://status.openai.com/)Cookie Preferences

**We use cookies** and similar technologies to deliver, maintain, improve our services and for security purposes.

Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. You can change your cookie settings at any time by clicking the cookie preferences link at the bottom of the page.

Reject AllAccept All