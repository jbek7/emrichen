from .base import BaseTag


class Var(BaseTag):
    def enrich(self, context):
        return context[self.data]
