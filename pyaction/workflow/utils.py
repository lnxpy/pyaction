from typing import Dict, List

from pyaction.workflow.consts import LOCAL_TABLE_COLS


def generate_param_table(columns: List[Dict[str, str]] = LOCAL_TABLE_COLS):
    """generates an output table

    Returns:
        Table: output table
    """

    from rich.table import Table

    table = Table(show_lines=True)
    for col in columns:
        table.add_column(**col, justify="center", vertical="middle")

    return table
