## The Beach Challenge problem

Kai and Sofia start at the same point on a beach. Sofia decides to swim directly toward a buoy that's 6 km offshore at a 30° angle from the shoreline. She swims at 2 km/hour, but ocean currents push her sideways at 0.5 km/hour perpendicular to her intended direction.
Meanwhile, Kai takes his longboard and paddles along the shoreline at 4 km/hour for the first hour. After exactly 1 hour, he turns and paddles directly toward Sofia's current position at 3 km/hour (slower because he's now fighting waves).
If both continue for a total of 2.5 hours from the start, what is the distance between them at the end?

[add chart]

Solving this problem requires both reasoning and math. In particular, it requires:

- Use trigonometry to track Sofia's actual path (accounting for current drift)
- Calculate positions at multiple time intervals
- Determine when and where Kai changes direction
- Account for Kai's speed change
- Find Sofia's position when Kai starts heading toward her
- Calculate final positions using vector components
- Apply the distance formula to find the final separation


## TODOs

- [x] Write the problem generator script 
- [x] Create a dataset and push it to Opik
- [x] Build a strong OneShootLLM solution using Claude Sonnet 4
- [ ] Evaluate it
- [ ] Swap model to DeepSeek
- [ ] Swap model to Qwen
- [ ] 2-step agent with reasoning and tool use.


## Create an evaluation dataset



## One-shoot

One-shoot Claude 3.5 Sonnet

llama3.1:8b

deepseek-r1:7b



## Agent that asks for clarification (basic workflow with langgraph)


1.2B model
https://playground.liquid.ai/public/chat/cmdw5xl7k001uif04hwk8tbl3

700MB
https://playground.liquid.ai/public/chat/cmdw65an00028if04xex82ykt

350MB
https://playground.liquid.ai/public/chat/cmdw69ii6002dif04st3scp2j


## How to effectively work with Claude Code?

Question about BAML, which is likely in the documentation.
Is there a way to ask this question to Claude Code?

Context window overflow


