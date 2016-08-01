#!/usr/bin/env python

import scrollphat
import sys
import time



while True:
    try:

#     set_pixel(x,y,Boolean, where Boolean True is on and Boolean False is off)
        scrollphat.set_pixel(0,0,True)
	time.sleep(1)
        scrollphat.update()
	scrollphat.set_pixel(0,0,False)
        scrollphat.update()
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
