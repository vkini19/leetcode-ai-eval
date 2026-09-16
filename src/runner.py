from save_results import save_results
from evaluator import run_tests, calculate_metrics
from load_data import load_problems
from solution_parser import extract_function
from mock_model import MockModel


def evaluate_model(model):
    problems = load_problems()
    results = []

    for problem in problems:
        print(f"Evaluating: {problem.title}")

        ai_response = model.generate_solution(problem.prompt)

        try:
            solution = extract_function(
                ai_response,
                problem.function_name
            )

            test_results = run_tests(
                solution,
                problem.hidden_tests
            )

            metrics = calculate_metrics(test_results)

            result = {
                "problem_id": problem.id,
                "problem": problem.title,
                "tests_passed": metrics["tests_passed"],
                "tests_total": metrics["tests_total"],
                "accuracy": metrics["test_accuracy"],
                "solved": metrics["problem_solved"],
            }

        except Exception as e:
            result = {
                "problem_id": problem.id,
                "problem": problem.title,
                "tests_passed": 0,
                "tests_total": len(problem.hidden_tests),
                "accuracy": 0,
                "solved": False,
                "error": str(e),
            }

        results.append(result)

    return results


if __name__ == "__main__":
    model = MockModel()

    results = evaluate_model(model)

    print("\n=== Evaluation Results ===")

    for result in results:
        print(
            f"{result['problem']}: "
            f"{result['tests_passed']}/{result['tests_total']} tests | "
            f"Accuracy: {result['accuracy']:.1%} | "
            f"Solved: {result['solved']}"
        )

        save_results(results)