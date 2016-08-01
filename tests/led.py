#!/usr/bin/env python

import scrollphat
import sys
import time



while True:
    try:

#     set_pixel(x is vertical values 0-4 OK,y i horizontal values 0-10 ok,Boolean, where Boolean True is on and Boolean False is off)
        scrollphat.set_pixel(10,4,True)
        scrollphat.update()
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
