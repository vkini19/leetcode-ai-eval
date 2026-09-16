from models_api import ModelClient


class MockModel(ModelClient):
    def generate_solution(self, problem_prompt: str) -> str:
        return """
def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i
"""