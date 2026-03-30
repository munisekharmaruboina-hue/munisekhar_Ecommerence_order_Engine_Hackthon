
class IdempotencyManager:
    def __init__(self):
        self.tokens = set()

    def is_duplicate(self, token):
        if token in self.tokens:
            return True
        self.tokens.add(token)
        return False