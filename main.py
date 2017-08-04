#!/usr/bin/python3

#old
#sudo pip3 install pymouse unix
#from pymouse import PyMouse

#good
#sudo apt install libx11-dev
#sudo pip3 install python-xlib
#sudo pip3 install pyautogui

import sys
import pyautogui as pag
from time import sleep


#keyboard
import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)

ESC = chr(27)

def wait_for_char(c):
   tty.setraw(sys.stdin)
   x = 0
   while x != c:
      x=sys.stdin.read(1)[0]
      #print("You pressed", x)
      termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
#end keyboard



pag.FAILSAFE = False


(src_x, src_y) = (2310, 471)
(dst_x, dst_y) = (1435, 600)

def init():
   global src_x
   global src_y
   global dst_x
   global dst_y
   #pag.position() = returns current xy coordinates of the mouse
   #pag.displayMousePosition()
   #pag.hotkey('
   #pag.click()

   num_tabs = int(input('number of tabs to move: '))
   print('move mouse to source browser and then press z')
   wait_for_char('z')
   src_pos = pag.position()

   print('move mouse to dest browser and then press z')
   wait_for_char('z')
   dst_pos = pag.position()

   print('src:', src_pos)
   print('dst:', dst_pos)
   (src_x, src_y) = src_pos
   (dst_x, dst_y) = dst_pos
   #sys.exit(0)

   i = 0
   while i < 5:
      print('starts in: %i' % (5-i,))
      sleep(1)
      i += 1

   i = 0
   while i < num_tabs:
      sleep(0.5)
      move_to_src_browser()
      sleep(0.5)
      copy_url()

      sleep(0.5)
      next_tab()
      #close_tab()
      sleep(0.5)


      move_to_dst_browser()
      sleep(1)
      new_tab()
      sleep(0.5)
      paste_tab_url()

      i += 1




def move_to_src_browser():
   #browser chrome 2310, 471
   pag.moveTo(src_x, src_y)

def move_to_dst_browser():
   #browser firefox 1435, 600
   pag.moveTo(dst_x, dst_y)



def copy_url():
   pag.hotkey('alt', 'd')
   pag.hotkey('ctrl', 'c')

def next_tab():
   pag.hotkey('ctrl', 'tab')

def new_tab():
   pag.hotkey('ctrl', 't')

def paste_tab_url():
   pag.hotkey('alt', 'd')
   pag.hotkey('ctrl', 'v')
   pag.hotkey('enter')




init()


