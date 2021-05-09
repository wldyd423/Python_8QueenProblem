class SimpleDebuger:
    def __init__(self):
        self.DEBUG_ON = True

    def turn_off_debug(self):
        self.DEBUG_ON = False

    def simple_print(self, str):
        if(self.DEBUG_ON):
            print(str)