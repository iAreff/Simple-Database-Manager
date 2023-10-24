
import os
import subprocess
import re


# get classes (commands)
commands_path = "app/models/commands/"
files = os.listdir(commands_path)
commands_file = [f for f in files if os.path.isfile(commands_path+'/'+f)]

for i in commands_file:
	if re.search(r".py$",i):
		exec(f"from app.models.commands.{i[:-3]} import {i[:-3]}")
	

class CommandHandler:
    def __init__(self) -> None:
        self.commands_file = commands_file

    def call(self, command: str) -> str:
        data = self.__prosses_command(command)
        args = data['arg']
        switches = data['sw']

        if args[0] in [x[:-3] for x in self.commands_file]:
            command_output = eval(f"{args[0]}({args},{switches}).run()")
            return command_output

        command_output = subprocess.run(command.split(" "), stdout=subprocess.PIPE, shell=True)
        return command_output.stdout.decode('utf-8')

    def __prosses_command(self, command: str) -> dict:
        splited_text = command.split(" ")
        switches = [x for x in splited_text if re.search(r"^-[a-zA-Z+0-9]+", x)]
        arguments = [x for x in splited_text if not re.search(r"^-[a-zA-Z+0-9]+", x)]
        data = {"arg": arguments, "sw": switches}
        return data
