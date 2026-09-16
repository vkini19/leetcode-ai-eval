from dataclasses import dataclass
from typing import Optional


@dataclass
class TestCase:
    inputs: tuple
    expected: object


@dataclass
class Problem:
    id: int
    title: str
    difficulty: str
    category: str
    prompt: str
    function_name: str
    visible_tests: list[TestCase]
    hidden_tests: list[TestCase]


@dataclass
class EvaluationResult:
    problem_id: int
    model: str
    prompt_strategy: str
    passed: bool
    tests_passed: int
    tests_total: int
    runtime_ms: Optional[float]
    error_type: Optional[str]
    error_message: Optional[str]