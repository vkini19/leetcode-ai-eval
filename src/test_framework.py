from evaluator import run_tests, calculate_metrics
from load_data import load_problems


def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i


problems = load_problems()

problem = problems[0]

results = run_tests(
    two_sum,
    problem.test_cases,
)

metrics = calculate_metrics(results)

print(f"Problem: {problem.title}")
print(f"Tests passed: {metrics['tests_passed']}/{metrics['tests_total']}")
print(f"Accuracy: {metrics['test_accuracy']:.1%}")
print(f"Solved: {metrics['problem_solved']}")