#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import get_data as gd
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

    
epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

# Drawing on the image
font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

data = gd.most_recent_repo()

image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
draw = ImageDraw.Draw(image)

draw.text((1, 1), data['name'], font = font15, fill = 0)
epd.display(epd.getbuffer(image))
time.sleep(10)
epd.Clear(0xFF)
epd.Dev_exit()
