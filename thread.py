import threading
from PIL import Image

class SummingThread(threading.Thread):
    def __init__(self,imgy0,imgy,imgx,xa,xb,ya,yb,image,maxIt):
        super(SummingThread, self).__init__()
        self.imgy=imgy
        self.imgx=imgx
        self.xa = xa
        self.xb=xb
        self.ya=ya
        self.yb=yb
        self.image = image
        self.imgy0 =imgy0
        self.maxIt = maxIt

    def run(self):
        for y in range(self.imgy0,self.imgy+1):
            zy = y * (self.yb - self.ya) / (self.imgy - 1)  + self.ya
            for x in range(self.imgx):
                zx = x * (self.xb - self.xa) / (self.imgx - 1)  + self.xa
                z = zx + zy * 1j
                c = z
                for i in range(self.maxIt):
                    if abs(z) > 2.0: break
                    z = z * z * z + (c - 1) * z - c

                self.image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
        

