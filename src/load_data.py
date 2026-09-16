import json
from pathlib import Path

from models import Problem, TestCase


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
                title=p["title"],
                difficulty=p["difficulty"],
                category=p["category"],
                prompt=p["prompt"],
                function_name=p["function_name"],
                visible_tests=visible_tests,
                hidden_tests=hidden_tests,
            )
        )

    return problems