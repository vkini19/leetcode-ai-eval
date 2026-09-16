def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i


def run_tests():
    test_cases = [
        {
            "input": ([2, 7, 11, 15], 9),
            "expected": [0, 1],
        },
        {
            "input": ([3, 2, 4], 6),
            "expected": [1, 2],
        },
        {
            "input": ([3, 3], 6),
            "expected": [0, 1],
        },
    ]

    passed = 0

    for test in test_cases:
        nums, target = test["input"]

        result = two_sum(nums, target)

        if result == test["expected"]:
            passed += 1
            print("PASS")
        else:
            print(
                f"FAIL: expected {test['expected']}, "
                f"got {result}"
            )

    print(f"\nResult: {passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()