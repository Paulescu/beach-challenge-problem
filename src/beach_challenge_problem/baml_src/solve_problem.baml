// Defining a data model.
class ProblemSolution {
  reasoning string @description("The reasoning process to solve the problem.")
  answer float @description("The final answer to the problem.")
}

// Create a function to solve the problem.
function SolveProblem(problem: string) -> ProblemSolution {
  // client "anthropic/claude-3-5-sonnet-20241022" // Set ANTHROPIC_API_KEY to use this client.
  // client "anthropic/claude-sonnet-4-20250514"
  client OllamaModel
  prompt #"
    {{ problem }}

    {{ ctx.output_format }}
  "#
}



// Test the function with a sample problem
test solve_problem {
  functions [SolveProblem]
  args {
    problem #"
      Kai and Sofia start at the same point on a beach.
      Sofia decides to swim directly toward a buoy that's 6.0 km offshore at a 30.0° angle from the shoreline.
      She swims at 2.0 km/hour, but ocean currents push her sideways at 0.5 km/hour perpendicular to her intended direction.
      Meanwhile, Kai takes his longboard and paddles along the shoreline at 4.0 km/hour for the first hour.
      After exactly 1 hour, he turns and paddles directly toward Sofia's current position at 3.0 km/hour (slower because he's now fighting waves).
      If both continue for a total of 2.5 hours from the start, what is the distance between them at the end?
    "#
  }

  // assert the output is not far away from the correct answer
  @@assert(between_bounds, {{ this.answer > 3.861 and this.answer < 3.864 }})
}
