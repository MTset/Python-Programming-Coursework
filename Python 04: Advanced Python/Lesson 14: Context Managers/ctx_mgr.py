"""
contman.py: a context manager class that suppresses any ValueError exceptions
that occur in the controlled suite, but allows any other exception to be raised
in the surrounding context.
"""
from contextlib import contextmanager
@contextmanager
def ctx_mgr():
        try:
            yield
        except ValueError:
            pass