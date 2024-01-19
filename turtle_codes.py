Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape("turtle")
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
...     t.forward(200)
...     t.left(90)

    
t.reset()
for i in range(40):
    t.forward(2*i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(200):
    t.forward(2*i)
    t.left(45)

    
t.reset()
for i in range(100):
    t.circle(5 * i)
    t.left(45)

    
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    t.circle(5 * i)
  File "C:\Python312\Lib\turtle.py", line 1989, in circle
    self.speed(speed)
  File "C:\Python312\Lib\turtle.py", line 2173, in speed
    self.pen(speed=speed)
  File "C:\Python312\Lib\turtle.py", line 2467, in pen
    self._update()
  File "C:\Python312\Lib\turtle.py", line 2671, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python312\Lib\turtle.py", line 560, in _delay
    self.cv.after(delay)
  File "C:\Python312\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
t.reset()
t.speed(0)
for i in range(100):
    t.circle(5 * i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(100):
    t.circle(5 * i)

    
t.reset()
t.speed(0)
for i in range(100):
    t.circle(5 * i)
    t.left(90)

    
