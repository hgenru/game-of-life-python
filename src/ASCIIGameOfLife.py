import time
import os, sys
import win32api
import win32con

import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
from ctypes import windll, byref
from ctypes.wintypes import _COORD

from src.GameOfLife import GameOfLife
   

class ASCIIGameOfLife(GameOfLife):
    _gHandle = 0

    def __init__(self, life_function, space):
        GameOfLife.__init__(self, life_function, space)
        # Grab console window handler
        self._gHandle = ctypes.windll.kernel32.GetStdHandle (-11)

    def render_space(self, space):
        """
        Visualize space
        param space: space to visualization
        """
        #os.system('cls')
        value = (0 + (0 << 16))
        ctypes.windll.kernel32.SetConsoleCursorPosition (self._gHandle, c_ulong (value))

        out = ""
        for line in space:
            for x in line:
                if x==0:
                    out += '░'
                else:
                    out += '▓'
            out+='\n'
        print(out)
        pass

    def need_render(self):
        """
        Check render interupt
        return: False if need interupt render
        """
        return (win32api.GetKeyState(win32con.VK_ESCAPE)&0x8000) == 0

    def process(self):
        generation = 0
        speed = 0.2
        while self.need_render():
            # Calculate next generation
            self._life_space = self._life_function(self._life_space)
            generation += 1
            # Render space
            self.render_space(self._life_space)
            # Speed change
            if win32api.GetKeyState(win32con.VK_DOWN)&0x8000:
                speed += 0.01
                if speed>0.35:
                    speed = 0.35
            if win32api.GetKeyState(win32con.VK_UP)&0x8000:
                speed -= 0.01
                if speed<0:
                    speed = 0
            # Print menu
            print("[Generation: ",generation,"][Delay %01.2f" % speed,"][Esc EXIT][▲ Speep up][▼ Speed down]")
            time.sleep(speed)