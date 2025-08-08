"""
Script used to generate an evaluation dataset for our problem.
"""
import math
import random


class Problem:
    """
    A particular instance of a BeachChallengeProblem for the given parameters in its
    init method.
    """
    def __init__(
        self,
        buoy_offshore_distance: float,
        buoy_angle: float,
        sofia_speed: float,
        ocean_current_speed: float,
        kai_initial_speed: float,
        kai_change_direction_time: float,
        kai_final_speed: float,
        final_time: float
    ):
        self.buoy_offshore_distance = buoy_offshore_distance
        self.buoy_angle = buoy_angle
        self.sofia_speed = sofia_speed
        self.ocean_current_speed = ocean_current_speed
        self.kai_initial_speed = kai_initial_speed
        self.kai_change_direction_time = kai_change_direction_time
        self.kai_final_speed = kai_final_speed
        self.final_time = final_time

    def get_question(self) -> str:
        """
        Get the question for the problem.
        """
        return f"Kai and Sofia start at the same point on a beach. Sofia decides to swim directly toward a buoy that's {self.buoy_offshore_distance} km offshore at a {self.buoy_angle}° angle from the shoreline. She swims at {self.sofia_speed} km/hour, but ocean currents push her sideways at {self.ocean_current_speed} km/hour perpendicular to her intended direction. Meanwhile, Kai takes his longboard and paddles along the shoreline at {self.kai_initial_speed} km/hour for the first hour. After exactly 1 hour, he turns and paddles directly toward Sofia's current position at {self.kai_final_speed} km/hour (slower because he's now fighting waves). If both continue for a total of {self.final_time} hours from the start, what is the distance between them at the end?"

    def get_correct_answer(self) -> float:
        """
        Calculate the distance between Sofia and Kai after they navigate from the same starting point.
        """
        return calculate_final_distance(
            buoy_offshore_distance=self.buoy_offshore_distance,
            buoy_angle=self.buoy_angle,
            sofia_speed=self.sofia_speed,
            ocean_current_speed=self.ocean_current_speed,
            kai_initial_speed=self.kai_initial_speed,
            kai_change_direction_time=self.kai_change_direction_time,
            kai_final_speed=self.kai_final_speed,
            final_time=self.final_time
        )


def calculate_final_distance(
    buoy_offshore_distance: float,
    buoy_angle: float,
    sofia_speed: float,
    ocean_current_speed: float,
    kai_initial_speed: float,
    kai_change_direction_time: float,
    kai_final_speed: float,
    final_time: float
) -> float:
    """
    Calculate the distance between Sofia and Kai after they navigate from the same starting point.
    
    Args:
        buoy_offshore_distance: Distance to buoy in km
        buoy_angle: Angle of buoy from shoreline in degrees
        sofia_speed: Sofia's swimming speed toward buoy in km/h
        ocean_current_speed: Ocean current speed perpendicular to Sofia's intended direction in km/h
        kai_initial_speed: Kai's speed along shoreline in km/h
        kai_change_direction_time: Time when Kai changes direction in hours
        kai_final_speed: Kai's speed when paddling toward Sofia in km/h
        final_time: Total time for the journey in hours
        
    Returns:
        Distance between Sofia and Kai at final_time in km
    """
    # Convert angle to radians
    buoy_angle_rad = math.radians(buoy_angle)

    # Calculate buoy position (using shoreline as x-axis, perpendicular as y-axis)
    buoy_x = buoy_offshore_distance * math.cos(buoy_angle_rad)
    buoy_y = buoy_offshore_distance * math.sin(buoy_angle_rad)

    # Sofia's intended direction (unit vector toward buoy)
    sofia_intended_x = buoy_x / buoy_offshore_distance
    sofia_intended_y = buoy_y / buoy_offshore_distance

    # Perpendicular direction to Sofia's intended path (90° counterclockwise rotation)
    perp_x = -sofia_intended_y
    perp_y = sofia_intended_x

    # Sofia's actual velocity (intended speed + current drift)
    sofia_vel_x = sofia_speed * sofia_intended_x + ocean_current_speed * perp_x
    sofia_vel_y = sofia_speed * sofia_intended_y + ocean_current_speed * perp_y

    # Sofia's final position (constant velocity throughout)
    sofia_final_x = sofia_vel_x * final_time
    sofia_final_y = sofia_vel_y * final_time

    # Kai's position at direction change time
    kai_change_x = kai_initial_speed * kai_change_direction_time
    kai_change_y = 0.0  # Kai moves along shoreline initially

    # Sofia's position when Kai changes direction
    sofia_at_change_x = sofia_vel_x * kai_change_direction_time
    sofia_at_change_y = sofia_vel_y * kai_change_direction_time

    # Calculate Kai's direction toward Sofia's position at change time
    delta_x = sofia_at_change_x - kai_change_x
    delta_y = sofia_at_change_y - kai_change_y
    distance_to_sofia = math.sqrt(delta_x**2 + delta_y**2)

    # Handle edge case where Kai and Sofia are at same position
    if distance_to_sofia == 0:
        kai_dir_x, kai_dir_y = 0.0, 0.0
    else:
        kai_dir_x = delta_x / distance_to_sofia
        kai_dir_y = delta_y / distance_to_sofia

    # Kai's movement in second phase
    phase_2_duration = final_time - kai_change_direction_time
    phase_2_distance = kai_final_speed * phase_2_duration

    # Kai's final position
    kai_final_x = kai_change_x + phase_2_distance * kai_dir_x
    kai_final_y = kai_change_y + phase_2_distance * kai_dir_y

    # Calculate final distance between them
    final_distance = math.sqrt(
        (sofia_final_x - kai_final_x)**2 + (sofia_final_y - kai_final_y)**2
    )

    return final_distance

class ProblemGenerator:

    def __init__(self):
        """
        Sets range of possible values for the problem parameters:
        - buoy_offshore_distance: float
        - buoy_angle: float
        - sofia_speed: float
        - ocean_current_speed: float
        - kai_initial_speed: float
        - kai_change_direction_time: float
        - kai_final_speed: float
        - final_time: float
        """
        self.buoy_offshore_distance_range = (5, 10)
        self.buoy_angle_range = (15, 45)
        self.sofia_speed_range = (1, 3)
        self.ocean_current_speed_range = (0, 2)
        self.kai_initial_speed_range = (2, 5)
        self.kai_change_direction_time_range = (1, 2)
        self.kai_final_speed_range = (1, 4)
        self.time_range = (2, 3)

    def generate_problems(self, n_problems: int) -> list[Problem]:
        """
        Generate a problem with the given parameters.
        """
        problems = []
        for _ in range(n_problems):

            # sample random parameters
            buoy_offshore_distance = random.randint(self.buoy_offshore_distance_range[0], self.buoy_offshore_distance_range[1])
            buoy_angle = random.randint(self.buoy_angle_range[0], self.buoy_angle_range[1])
            sofia_speed = random.randint(self.sofia_speed_range[0], self.sofia_speed_range[1])
            ocean_current_speed = random.randint(self.ocean_current_speed_range[0], self.ocean_current_speed_range[1])
            kai_initial_speed = random.randint(self.kai_initial_speed_range[0], self.kai_initial_speed_range[1])
            kai_change_direction_time = random.randint(self.kai_change_direction_time_range[0], self.kai_change_direction_time_range[1])
            kai_final_speed = random.randint(self.kai_final_speed_range[0], self.kai_final_speed_range[1])
            final_time = random.randint(self.time_range[0], self.time_range[1])

            problems.append(Problem(
                buoy_offshore_distance=buoy_offshore_distance,
                buoy_angle=buoy_angle,
                sofia_speed=sofia_speed,
                ocean_current_speed=ocean_current_speed,
                kai_initial_speed=kai_initial_speed,
                kai_change_direction_time=kai_change_direction_time,
                kai_final_speed=kai_final_speed,
                final_time=final_time,
            ))

        return problems

def generate_evaluation_dataset(n_problems: int, dataset_name: str):
    """
    Generate an evaluation dataset with the given number of problems.
    """
    # generate the problems
    problem_generator = ProblemGenerator()
    problems = problem_generator.generate_problems(n_problems=n_problems)

    # add problem questions and correct answers to an evaluation dataset in Opik
    from opik import Opik

    client = Opik()
    dataset = client.get_or_create_dataset(name=dataset_name)

    for problem in problems:
        # show on console
        print(problem.get_question())
        print(problem.get_correct_answer())
        print('-' * 100)

        # add to evaluation dataset
        dataset.insert([
            {'input': problem.get_question(), 'expected_output': problem.get_correct_answer()}
        ])

    return dataset

# Example usage with the original problem values
if __name__ == "__main__":

    problem = Problem(
        buoy_offshore_distance=6.0,
        buoy_angle=30.0,
        sofia_speed=2.0,
        ocean_current_speed=0.5,
        kai_initial_speed=4.0,
        kai_change_direction_time=1.0,
        kai_final_speed=3.0,
        final_time=2.5
    )

    print(problem.get_question())
    print(problem.get_correct_answer())
    print('-' * 100)

    from fire import Fire

    # generate an evaluation dataset
    Fire(generate_evaluation_dataset)
