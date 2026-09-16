from typing import Any, Callable


def extract_function(
    code: str,
    function_name: str
) -> Callable[..., Any]:
    namespace: dict[str, Any] = {}

    exec(code, namespace)

    if function_name not in namespace:
        raise ValueError(
            f"Function '{function_name}' was not found."
        )

    return namespace[function_name]