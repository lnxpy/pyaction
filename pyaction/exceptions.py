class WorkflowParameterNotFound(Exception):
    """Raised when a parameter for the workflow is not found."""


class NotAnnotated(Exception):
    """Raised when a function is not properly annotated."""
