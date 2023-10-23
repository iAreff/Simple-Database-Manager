from app.handlers.command_handler import CommandHandler
class Shell:
    def __init__(self) -> None:
        self.handler = CommandHandler()
        self.run()

    def run(self):
        while True:
            command = str(input(" > "))
            output = self.handler.call(command)
            if output != "" :print(output, end='')
            continue
            