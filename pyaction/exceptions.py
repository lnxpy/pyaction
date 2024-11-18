class WorkflowParameterNotFound(Exception):
    """Raised when a parameter for the workflow is not found."""

    pass


class NotAnnotated(Exception):
    """Raised when a function is not properly annotated."""

    pass
