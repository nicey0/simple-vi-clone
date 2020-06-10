class Mode:
    highlights: bool
    def process_key(self, key: int) -> tuple:
        raise NotImplementedError
