# get arguments
import sys
arg = sys.argv

class StartUpApp:
    def __init__(self) -> None:
        pass

    def setmod(arg) :
        if len(arg)==2 and arg[1]=="graphic":
            from app.core.graphic import Graphic
            Graphic()
            return
        elif  len(arg)==2 and arg[1]=="shell":
            from app.core.shell import Shell
            Shell()
            return

startup_app = StartUpApp
startup_app.setmod(arg)
