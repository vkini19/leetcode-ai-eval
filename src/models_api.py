class ModelClient:
    def generate_solution(self, problem_prompt: str) -> str:
        raise NotImplementedError

class MockModel(ModelClient):
    def generate_solution(self, problem_prompt):
        return """
def two_sum(nums, target):
    ...
"""