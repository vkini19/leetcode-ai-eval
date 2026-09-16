from models import TestCase


def run_tests(solution_function, test_cases: list[TestCase]):
    results = []

    for test in test_cases:
        try:
            actual = solution_function(*test.inputs)

            passed = actual == test.expected

            results.append({
                "passed": passed,
                "expected": test.expected,
                "actual": actual,
                "error": None,
            })

        except Exception as e:
            results.append({
                "passed": False,
                "expected": test.expected,
                "actual": None,
                "error": str(e),
            })

    return results


def calculate_metrics(test_results):
    total = len(test_results)
    passed = sum(result["passed"] for result in test_results)

    return {
        "tests_total": total,
        "tests_passed": passed,
        "test_accuracy": passed / total if total else 0,
        "problem_solved": passed == total,
    }