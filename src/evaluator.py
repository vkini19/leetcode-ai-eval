from dataclasses import dataclass
from typing import Optional
from code_executor import execute_solution
import json
from pathlib import Path

@dataclass
class TestCase:
    inputs: tuple
    expected: object


@dataclass
class Problem:
    id: int
    leetcode_id: int | None
    title: str
    difficulty: str
    category: str
    slug: str
    prompt: str
    function_name: str
    visible_tests: list[TestCase]
    hidden_tests: list[TestCase]


@dataclass
class EvaluationResult:
    problem_id: int
    problem: str
    model: str
    prompt_strategy: str
    passed: bool
    tests_passed: int
    tests_total: int
    test_accuracy: float
    error_type: Optional[str]
    error_message: Optional[str]

def run_tests(
    solution_code: str,
    function_name: str,
    test_cases: list[TestCase],
):
    results = []

    for test in test_cases:
        execution = execute_solution(
            solution_code,
            function_name,
            test.inputs,
        )

        if not execution["success"]:
            results.append({
                "passed": False,
                "expected": test.expected,
                "actual": None,
                "error": execution["error_message"],
                "error_type": execution["error_type"],
                "runtime_ms": execution["runtime_ms"],
            })
            continue

        actual = execution["result"]
        passed = actual == test.expected

        results.append({
            "passed": passed,
            "expected": test.expected,
            "actual": actual,
            "error": None,
            "error_type": None if passed else "wrong_answer",
            "runtime_ms": execution["runtime_ms"],
        })

    return results


def calculate_metrics(test_results):
    total = len(test_results)
    passed = sum(result["passed"] for result in test_results)

    runtimes = [
    result["runtime_ms"]
    for result in test_results
    if result["runtime_ms"] is not None
    ]

    average_runtime_ms = (
        sum(runtimes) / len(runtimes)
        if runtimes
        else None
    )

    return {
        "tests_total": total,
        "tests_passed": passed,
        "test_accuracy": passed / total if total else 0,
        "problem_solved": passed == total,
        "average_runtime_ms": average_runtime_ms,
    }

def load_problems():
    data_path = Path(__file__).parent.parent / "data" / "problems.json"

    with open(data_path, "r", encoding="utf-8") as f:
        raw_problems = json.load(f)

    problems = []

    for p in raw_problems:
        visible_tests = [
            TestCase(
                inputs=tuple(tc["input"]),
                expected=tc["expected"],
            )
            for tc in p["visible_tests"]
        ]

        hidden_tests = [
            TestCase(
                inputs=tuple(tc["input"]),
                expected=tc["expected"],
            )
            for tc in p["hidden_tests"]
        ]

        problems.append(
            Problem(
                id=p["id"],
                leetcode_id=p["leetcode_id"],
                title=p["title"],
                difficulty=p["difficulty"],
                category=p["category"],
                slug=p["slug"],
                prompt=p["prompt"],
                function_name=p["function_name"],
                visible_tests=visible_tests,
                hidden_tests=hidden_tests,
            )
        )

    return problems