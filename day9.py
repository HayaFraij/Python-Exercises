#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:31:52 2019

@author: owner
"""


#Q1:

#import statistics as st

#x=[3,1.5,4.5,6.75,2.25,5.75,2.25]

#print(st.mean(x))
#print(st.harmonic_mean(x))
#print(st.median(x))
#print(st.median_low(x))
#print(st.median_high(x))
#print(st.median_grouped(x))
#print(st.mode(x))
#print(st.pstdev(x))
#print(st.pvariance(x))
#print(st.stdev(x))
#print(st.variance(x))



#Q2:

#import random

#print( random.random() )
#print ( random.randrange(10) )
#print ( random.choice(['ali', 'khalid', 'hussam']) )
#print ( random.sample(range(1000), 10) )
#print ( random.choice('orange academy') )

#items = [1,5,8,9,2,4]

#random.shuffle(items)
#print( items )
#print ( random.randint(20,30) )
#print ( random.randrange(1000, 2111, 5) )
#print ( random.uniform(10000,11000))
#print()


#Q3:

#import math
#print ('pi : %.40f' % math.pi)
#print ('pi: %.40f' % math.cos(200))
#print ('pi: %.40f' % math.sin(30) )
#print ('pi: %.40f' % math.tan(180) )
#print(math.floor(10.8))
#print(math.ceil(10.8))



#Q4:
       
#import PIL as pl
#from PIL import ImageDraw, ImageFilter, Image

#im = pl.Image.open('cat.jpeg')
#im2 = pl.Image.open('cat2.jpeg')
#im3 = pl.Image.open('mask.jpg')

#print(im.size, im.format, im.mode)
#im.show()
#
#img = im.transpose(pl.Image.FLIP_TOP_BOTTOM)
#img.show()
#
#grey = im.convert('L')
#grey.show()
#
#crop = im.crop((0, 0, 50, 50))
#crop.show()

#draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=(225, 225, 225)) 
#draw.line((0,im.size[1], im.size[0], 0), fill=(225, 225, 225)) 
#draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'Haya',fill=(225,225,0))
#draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2-60),'Image',fill=(225,225,0))
#im.show()

#sharpen = im.filter(ImageFilter.SHARPEN)
#sharpen.show()
#edgeEnhance = im.filter(ImageFilter.EDGE_ENHANCE)
#edgeEnhance.show()
#fineEdge = im.filter(ImageFilter.FIND_EDGES)
#fineEdge.show()
#smooth = im.filter(ImageFilter.SMOOTH)
#smooth.show()


##Image.blend(im,im2,0.5).save('newimg.jpg'.format(0.5))
##im = Image.open('newimg.jpg')
##im.show()


#blurred = im.filter(ImageFilter.BLUR)
#im.show()


#size=(128,128)
#try:
#    im
#except:
#    print("Unable to load image")
#im.thumbnail(size)
#im.save("thumbnail.png")
#im.show()


#im1_flip = im.transpose(Image.ROTATE_90)
#im1_flip.show()


#im3 = im3.resize(im.size)
#Image.composite(im,im2,im3).save('maskImage.jpg')
#image = Image.open('maskImage.jpg')
#image.show()










