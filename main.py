from threading import Thread
from PIL import Image
from thread import SummingThread
# drawing area
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
  
# max iterations allowed
maxIt = 255
  
# image size
imgx = 600
imgy = 600

image = Image.new("RGB", (imgx, imgy))

y= imgy//2
gioiHanTren = yb//2

thread1 = SummingThread(0,y,imgx,xa,xb,ya,gioiHanTren,image,maxIt)
thread2 = SummingThread(y+1,imgy-1,imgx,xa,xb,ya,yb,image,maxIt)
    
thread1.start()
thread2.start()

thread1.join()
thread2.join()

image.show()