import os


class cd:
    def __init__(self, arguments: list, switches: list) -> None:
        self.arguments = arguments
        self.switches = switches

    def run(self) -> str:
        try:
            os.chdir(self.listToString(self.arguments))
            return ""
        except:
            return "no such file or directory\n"

    def listToString(self, list: list) -> str:
        output = " "
        return (output.join(list[1:]))
