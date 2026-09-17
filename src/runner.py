from evaluator import load_problems, run_tests, calculate_metrics
from model import MockModel
import json
from pathlib import Path

def evaluate_model(model):
    problems = load_problems()
    results = []

    for problem in problems:
        print(f"Evaluating: {problem.title}")

        if not problem.prompt:
            print("Skipping: prompt not populated yet")
            continue

        ai_response = model.generate_solution(problem.prompt)

        try:
            test_results = run_tests(
                ai_response,
                problem.function_name,
                problem.hidden_tests
            )

            metrics = calculate_metrics(test_results)

            error_types = [
                result["error_type"]
                for result in test_results
                if result["error_type"] is not None
            ]

            error_type = error_types[0] if error_types else None
            error_message = next(
                (
                    result["error"]
                    for result in test_results
                    if result["error"] is not None
                ),
                None,
            )

            result = {
                "problem_id": problem.id,
                "problem": problem.title,
                "model": model.__class__.__name__,
                "prompt_strategy": "baseline",
                "passed": metrics["problem_solved"],
                "tests_passed": metrics["tests_passed"],
                "tests_total": metrics["tests_total"],
                "test_accuracy": metrics["test_accuracy"],
                "error_type": error_type,
                "error_message": error_message,
                "average_runtime_ms": metrics["average_runtime_ms"],
            }

        except Exception as e:
            result = {
                "problem_id": problem.id,
                "problem": problem.title,
                "model": model.__class__.__name__,
                "prompt_strategy": "baseline",
                "passed": False,
                "tests_passed": 0,
                "tests_total": len(problem.hidden_tests),
                "test_accuracy": 0,
                "error_type": "execution_error",
                "error_message": str(e),
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
            f"Accuracy: {result['test_accuracy']:.1%} | "
            f"Runtime: {result['average_runtime_ms']:.2f} ms | "
            f"Solved: {result['passed']}"
        )

    results_dir = Path(__file__).parent.parent / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "mock_model_results.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)