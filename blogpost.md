You are an expert ML engineer who loves explaining complex things in a digestable way,
using humor here and there, to keep the reader engaged until the very end, where you add
add a call to action to an LLMOps bootcamp.

The target audience are ML/AI engineers.

Write in first persion (a guy called Pau who has a 4-year old kid named Kai)

Write a blog post with the following requirements

- Start by mentioning how last I was teaching Kai a bit of logical thinking and mathematics.

- We were trying to solve the following problem:

```
The Beach Challenge Problem
Imagine Kai and Sofia that you both are on the shore of the beach. Sofia decides she will swim, while Kai will take a longboard and paddle instead, and go in the same direction. If Sofia swims at 2 km per hour and Kai paddles at 4 km per hour, how far apart will you be in 2 hours”
```

- This week Kai is back in the kindergarten, so I had to find someone else to teach. So I decided to see how to solve this using LLMs. I want to test their reasoning and their maths skills.

- Since Google and OpenAI announced a few weeks ago they have built AI systems capable of solving International
Mathematics Problems, I cannot stop thinking about this. I am a mathematician by heart and soul who spent a non-negligible amount of time in his teen years trying to solve all sorts of Maths problems. Nowadays, I teach Maths to my kids, and I teach how to build AI systems to my students. So this post is something in the intersectio of both.

- Now, the problem I presented to my son is not really challengin for an LLM to put its "reasoning" to work, so I had to complicate it a little bit.

- I created a more difficult problem, which I don't expect Kai to solve, but I expect LLMs can solve.

- This is the updated "Beach Challenge Problem"

```
The (slightly more complicated) Beach Challenge Problem

Kai and Sofia start at the same point on a beach. Sofia decides to swim directly toward a buoy that's 7 km offshore at a 41° angle from the shoreline. She swims at 2 km/hour, but ocean currents push her sideways at 2 km/hour perpendicular to her intended direction. Meanwhile, Kai takes his longboard and paddles along the shoreline at 5 km/hour for the first hour. After exactly 1 hour, he turns and paddles directly toward Sofia's current position at 1 km/hour (slower because he's now fighting waves). If both continue for a total of 2 hours from the start, what is the distance between them at the end?
```

- Solving this problem requires both reasoning and math. In particular, it requires:

    - Use trigonometry to track Sofia's actual path (accounting for current drift)
    - Calculate positions at multiple time intervals
    - Determine when and where Kai changes direction
    - Account for Kai's speed change
    - Find Sofia's position when Kai starts heading toward her
    - Calculate final positions using vector components
    - Apply the distance formula to find the final separation

Today is the first part of an N series part where I will show you how to build a cost-effective-and-accurate system
to solve a task like.

- All the code I show in this post is in this github repository.
[Link to the repo]

## Where to start?

The simplest system we can think of is made of a single LLM which outputs a numeric answer given the problem statement.

I recommend you start simple, evaluate your solution, and then iteratively add complexity.

Adding complexity that does not move your evaluation metrics is a VERY bad idea.

The task we are solving here is something that any high-s








## LLMs to solve Maths problems



I spent last week teaching my 4-year son how to solve basic arithmetic problems.

