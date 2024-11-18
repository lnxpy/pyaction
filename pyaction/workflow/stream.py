import json
from typing import Dict, NewType

WorkflowContext = NewType("WorkflowContext", Dict[str, int | float | str | bool])

DELIMITER: str = "EOF"

MULTILINE_OUTPUT: str = f"""
{{variable}}<<{DELIMITER}
{{value}}
{DELIMITER}
"""


def push_to_local(context: WorkflowContext) -> None:
    """
    Pushes/prints the context data to the output stream.

    Args:
        context (WorkflowContext): A dictionary containing variable names and their respective values.
    """
    output_params = []
    for var, val in context.items():
        output_params.append(
            {
                "var": var,
                "value": val,
                "type": str(type(val)),
                "usage": f"${{{{ steps.STEP_ID.outputs.{var} }}}}",
            }
        )

    print(json.dumps(output_params, indent=3))


def push_to_runner(context: WorkflowContext, stream: str) -> None:
    """
    Pushes the content of the context to the specified stream (GITHUB_OUTPUT).

    Args:
        context (WorkflowContext): A dictionary containing variable names and their respective values.
        stream (str): The stream to write into.
    """
    with open(stream, "+w") as streamline:
        for var, val in context.items():
            if isinstance(val, str) and "\\n" in val:
                streamline.write(MULTILINE_OUTPUT.format(variable=var, value=val))
            else:
                streamline.write(f"{var}={val}\r\n")
