from evaluator import run_tests, calculate_metrics
from load_data import load_problems
from solution_parser import extract_function
from mock_model import MockModel


model = MockModel()

problems = load_problems()
problem = problems[0]

ai_response = model.generate_solution(problem.prompt)

solution = extract_function(
    ai_response,
    problem.function_name
)

test_results = run_tests(
    solution,
    problem.hidden_tests
)

metrics = calculate_metrics(test_results)

for i, result in enumerate(test_results, start=1):
    status = "PASS" if result["passed"] else "FAIL"

    print(
        f"Test {i}: {status} | "
        f"Expected: {result['expected']} | "
        f"Got: {result['actual']}"
    )

print()
print(f"Problem: {problem.title}")
print(f"Tests passed: {metrics['tests_passed']}/{metrics['tests_total']}")
print(f"Accuracy: {metrics['test_accuracy']:.1%}")
print(f"Solved: {metrics['problem_solved']}")