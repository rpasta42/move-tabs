#!/usr/bin/python3

import sys
import pyautogui as pag
from time import sleep


page.FAILSAFE = False

ESC = chr(27)

def cmd_wait_for_char(c):
   #keyboard
   import tty
   import sys
   import termios


   orig_settings = termios.tcgetattr(sys.stdin)

   tty.setraw(sys.stdin)
   x = 0
   while x != c:
      x=sys.stdin.read(1)[0]
      #print("You pressed", x)
      args = [
         sys.stdin, termios.TCSADRAIN,
         orig_settings
      ]
      termios.tcsetattr(*args)
      pass

   pass


def moveto(dst_x, dst_y):
   pag.moveTo(dst_x, dst_y)


def get_mouse_pos(msg, char_to_press='z'):
   print(msg)
   wait_for_char('z')
   (x, y) = pag.position()
   print('x: ' + x + ' y: ' + y)
   return (x, y)

'''
hk('ctrl', 'w')
hk('ctrl', 'tab')
hk('ctrl', 't')
hk('alt', 'd')
hk('ctrl', 'v')
hk('enter')
'''
def hk(*args):
   pag.hotkey(*args)


