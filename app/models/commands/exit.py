class exit:
    def __init__(self, arguments: list, switches: list) -> None:
        self.arguments = arguments
        self.switches = switches

    def run(self) -> str:
        quit()
