class exit:
    def __init__(self,arguments:list,switchs:list) -> None:
        self.arguments = arguments
        self.switchs = switchs

    def run(self) -> str:
        quit()