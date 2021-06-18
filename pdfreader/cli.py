"""
Defines interface
"""
import time
import click
import curses
import pdftotext
from pynput import keyboard
from functools import partial


class App:

    def __init__(self, filepath: str):
        with open(filepath, 'rb') as fd:
            self.pdf = pdftotext.PDF(fd)
            self.page = 0
    
    def __enter__(self):
        curses.initscr()
        self.main = curses.newwin(100, 100)
    
    def __exit__(self, *args, **kwargs):
        curses.endwin()

    def next_page(self):
        self.page += 1

    def prev_page(self):
        self.page -= 1
            
    def show_page(self):
        self.main.clear()
        self.main.addstr(self.pdf[self.page])
        self.main.refresh() 


# Controller 
def on_press(app, key):
    if key.char == 'n':
        app.next_page()
    elif key.char == 'b':
        app.prev_page()
    else:
        pass


def on_release(app, key):
    app.show_page()


# Commands
@click.command()
@click.argument('filepath')
def read(filepath):
    app = App(filepath)

    with app:
        app.show_page()
        with keyboard.Listener(
                on_press=partial(on_press, app),
                on_release=partial(on_release, app)
                ) as listener:
            listener.join()


if __name__ == '__main__':
    read()
