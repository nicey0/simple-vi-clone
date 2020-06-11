class Mode:
    def __init__(self):
        self.highlights: bool
    def process_key(self, key: int) -> tuple:
        raise NotImplementedError
