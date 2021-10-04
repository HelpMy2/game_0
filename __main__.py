import tkinter as tk
from SETTINGS import *
from MAPS import *
import time
import math
import keyboard


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('game 0')
        self.root.geometry(f'{WIDTH}x{HEIGHT}+200+200')
        self.root.resizable(False, False)
        # start
        self.map = MAPS['test']
        self.p_cords = self.map['spawn']
        self.p_angles = [0, 0, 0]
        self.canvas = tk.Canvas(self.root, bg=self.map['void color'], width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.last = (450, 240)
        self.angle_label = tk.Label(text=self.p_angles)
        self.angle_label.place(x=10, y=10)
        # init keys
        self.m_forward = time.time()
        self.m_backward = time.time()
        # init game
        self.mainloop()

    def mainloop(self):
        self.root.wait_visibility(self.root)
        t = time.time()
        while self.root.geometry():
            while time.time() < t + 0.5:
                if keyboard.is_pressed('w'):
                    if self.m_forward + 0.1 < time.time():
                        self.m_forward = time.time()
                        self.p_cords[0] += math.cos(self.p_angles[0])
                        self.p_cords[2] += math.sin(self.p_angles[0])
                elif keyboard.is_pressed('s'):
                    if self.m_backward + 0.1 < time.time():
                        self.m_backward = time.time()
                        self.p_cords[0] -= math.cos(self.p_angles[0])
                        self.p_cords[2] -= math.sin(self.p_angles[0])
                self.root.update()
            t = time.time()
            self.flip()
            self.root.update()
            self.angle_label.configure(text=self.p_angles)

    def flip(self):
        self.canvas.delete('all')
        for body in self.map['world']['bodies']:
            if body['visible']:
                self.canvas.create_rectangle(body['x'] - self.p_cords[0], body['z'] - self.p_cords[2],
                                             body['x'] + body['width'] - self.p_cords[0],
                                             body['z'] + body['length'] - self.p_cords[2], fill=body['color'])
        self.canvas.create_rectangle(0, 0, 10, 10, fill="#ff0087")
        self.canvas.update()


if __name__ == '__main__':
    Game()
