from pynput import mouse
from pynput.keyboard import Key, Controller
import json

with open('config.json', 'r') as f:
  config = json.load(f)

keyboard = Controller()

def on_scroll(x, y, dx, dy):
  if (x > config['xMin'] and x < config['xMax'] and y > config['yMin'] and y < config['yMax']):
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    if dy < 0:
      keyboard.press(Key.right)
    else:
      keyboard.press(Key.left)
      
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    if dy < 0:
      keyboard.release(Key.right)
    else:
      keyboard.release(Key.left)

  if (config['printPosition'] == True):
    print('Scrolled {0} at {1}'.format(
      'down' if dy < 0 else 'up',
      (x, y)))

with mouse.Listener(
    on_scroll=on_scroll) as listener:
  listener.join()