
# import io
# import time
# import click
# import pdftotext
# 
# from pynput import keyboard
# 
# 
# # Global
# BUFFER = io.BytesIO()
# PAGE = 0
# 
# 
# def read_page():
#     """
#     Read 1 indexed pages from a pdf
#     """
#     global BUFFER, PAGE
#     pdf = pdftotext.PDF(BUFFER)
#     BUFFER.seek(0)
#     return pdf[PAGE]
# 
# 
# def on_press(key):
#     global PAGE
#    
#     if key == keyboard.Key.esc:
#         return False
#     
#     if key.char == 'n':
#         PAGE += 1
#     elif key.char == 'n':
#         PAGE -= 1
#     else:
#         pass
#        
# 
# def on_release(key):
#     print(read_page())
# 
# 
# def load_file(filepath):
#     global BUFFER
# 
#     with open(filepath, 'rb') as fd:
#         BUFFER.write(fd.read())
#         BUFFER.seek(0)
# 
# 
# 
# @click.command()
# @click.argument('filepath')
# @click.option('--page', default=1, help='Open file on page')
# def start(filepath, page):
#     global BUFFER, PAGE
# 
#     load_file(filepath)
#     PAGE = page - 1  # zero indexing
#     
#     print(read_page())
# 
#     with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
# 
# 
# if __name__ == '__main__':
#     start()
#

import curses
from curses import wrapper


def main(stdscr):
    # clear
    
    stdscr.clear()
    stdscr.addstr("Hello, I will be cleared in 2 seconds.")
    stdscr.refresh()
    curses.napms(2000)
    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
