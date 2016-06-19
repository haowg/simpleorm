# coding: utf8


class Query(object):
    def __init__(self, args):
        "docstring"
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_trace):
        if exc_type is not None:
            self.rooback()
            raise exc_trace
        else:
            try:
                self.commit()
            except Exception as e:
                self.rooback()
                raise e

    def rooback(self):
        pass
