def not_annotated(foo, bar, baz): ...  # pragma: no cover


def poorly_annotated(foo: int, bar, baz: float): ...  # pragma: no cover


def well_annotated(foo: int, bar: str, baz: float): ...  # pragma: no cover


def annotated_but_valued_params(foo: int = "foo"): ...  # pragma: no cover
