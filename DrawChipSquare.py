# June 4, 2020
# Kira Milgrim
# This code is bring written as the second attempt to control
# my AxiDraw using python in the Command Prompt.
# With this program, I will make the AxiDraw draw a square.
# Make sure that you are in the correct folder before trying to run the code.

from pyaxidraw import axidraw   # import module
ad = axidraw.AxiDraw()          # Initialize class
ad.interactive()                # Enter interactive context
ad.connect()                    # Open serial port to AxiDraw
ad.options.pen_pos_up = 100
ad.options.pen_pos_down = 40
ad.options.units = 1 # changes the units to cm
ad.update()
ad.penup()
# Absolute movements specified here
# ad.moveto(1, 1)
ad.pendown()
ad.go(2.5, 0)
ad.go(0, 1.2)
ad.go(-2.5, 0)
ad.go(0, -1.2)
ad.penup()
ad.goto(0, 0)
ad.disconnect()
