import tkinter as tk
from SETTINGS import *
from MAPS import *
import time
import math


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
        # init keys
        self.root.bind('w', self.key_event_forward)
        self.m_forward = False
        self.root.bind('s', self.key_event_backward)
        self.m_backward = False
        self.root.bind('<Motion>', self.motion)
        # init game
        self.mainloop()

    def key_event_forward(self, event):
        print(event)
        if self.m_forward:
            self.root.update()
        else:
            self.m_forward = True
            self.p_cords[0] += math.sin(self.p_angles[0] / 80) - 0.5 * 2
            self.p_cords[2] += math.cos(self.p_angles[0] / 80) - 0.5 * 2
            time.sleep(0.1)
        self.m_forward = False

    def key_event_backward(self, event):
        print(event)
        if self.m_backward:
            self.root.update()
        else:
            self.m_backward = True
            self.p_cords[0] -= math.sin(self.p_angles[0] / 80) - 0.5 * 2
            self.p_cords[2] -= math.cos(self.p_angles[0] / 80) - 0.5 * 2
            time.sleep(0.1)
        self.m_backward = False

    def motion(self, event):
        self.p_angles[0] += (self.last[0] - event.x) / WIDTH * 180
        self.last = event.x, event.y

    def mainloop(self):
        self.root.wait_visibility(self.root)
        t = time.time()
        while self.root.geometry():
            while time.time() < t + 0.5:
                self.root.update()
            t = time.time()
            self.flip()
            self.root.update()

    def flip(self):
        self.canvas.delete('all')
        for body in self.map['world']['bodies']:
            if body['visible']:
                self.canvas.create_rectangle(body['x'] - self.p_cords[0], body['z'] - self.p_cords[2],
                                             body['x'] + body['width'] - self.p_cords[0],
                                             body['z'] + body['length'] - self.p_cords[2], fill=body['color'])
        self.canvas.create_rectangle(0, 0, 10, 10, fill="#ff0087")
        print(self.p_cords)
        self.canvas.update()


if __name__ == '__main__':
    Game()
