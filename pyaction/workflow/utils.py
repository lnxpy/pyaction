from typing import Dict, List

from rich.table import Table

from pyaction.workflow.consts import LOCAL_TABLE_COLS


def generate_param_table(columns: List[Dict[str, str]] = LOCAL_TABLE_COLS) -> Table:
    """generates an output table

    Returns:
        Table: output table
    """

    table = Table(show_lines=True)
    for col in columns:
        table.add_column(**col, justify="center", vertical="middle")

    return table
