from abc import ABC, abstractmethod


class ModelClient(ABC):

    @abstractmethod
    def generate_solution(self, problem_prompt: str) -> str:
        pass


class MockModel(ModelClient):

    def generate_solution(self, problem_prompt: str) -> str:

        if "two numbers" in problem_prompt:
            return """
def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i
"""

        if (
            "valid" in problem_prompt.lower()
            and "brackets" in problem_prompt.lower()
        ):
            return """
def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)

    return not stack
"""

        if "maximize your profit" in problem_prompt:
            return """
def max_profit(prices):
    min_price = float("inf")
    max_profit_value = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit_value = max(
            max_profit_value,
            price - min_price
        )

    return max_profit_value
"""

        raise ValueError(
            "MockModel does not support this problem yet."
        )