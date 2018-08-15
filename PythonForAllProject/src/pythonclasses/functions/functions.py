import sys
import os


class functions:

    def restartPython(self):
        print(self)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def main(self):
        x = Complex(3.0, -4.5)
        x.counter = 1
        while x.counter < 10:
            x.counter = x.counter * 2
        print( x.counter)
        del x.counter


print(ord('l'), ord('i'))