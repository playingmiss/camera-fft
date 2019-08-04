import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from numpy import uint8

class mouseParam:
    def __init__(self, input_img_name):
        self.mouseEvent = {"w":None, "h":None, "event":None} 
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None) 
    
    def __CallBackFunc(self, eventType, w, h, flags, userdata):  
        self.mouseEvent["w"] = w
        self.mouseEvent["h"] = h
        self.mouseEvent["event"] = eventType
    
    def getEvent(self): 
        return self.mouseEvent["event"]                

    def getPos(self): 
        return (self.mouseEvent["h"], self.mouseEvent["w"])


if __name__ == "__main__":

    plt.ion()
    im = cv2.imread("iphone.png",cv2.IMREAD_GRAYSCALE)
    cv2.imshow("origin",im)

    height,width = im.shape
    state = np.zeros((height,width))
    single = np.zeros((height,width))
    click = np.zeros((height,width))

    f1 = np.fft.fft2(im)
    f2 = np.fft.fftshift(f1)
    fft = 20*np.log(np.abs(f2))
    fftmin = np.min(fft)
    fftmax = np.max(fft)
    fft2 = (fft-fftmin) * 255 / (fftmax - fftmin)
    fftx = np.uint8(fft2)
    cv2.imshow("FFT",fftx)

    remake = sin = np.zeros((height,width))

    cv2.imshow("click",click)
    mouseData = mouseParam("click")
    while 1:

        k = cv2.waitKey(1)
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            h1,w1 = mouseData.getPos()
            click[h1:h1+20, w1:w1+20] = 255
            state[h1:h1+20, w1:w1+20] = 1.0
            single[:,:] = 0
            single[mouseData.getPos()] = 1
                
            fft_st = f2 * state
            fft1 = np.fft.fftshift(fft_st)
            ifft_im = np.fft.ifft2(fft1)
            ifft = np.abs(ifft_im)
            ifft_min = np.min(ifft)
            ifft_max = np.max(ifft)
            remake = (ifft - ifft_min)*255/(ifft_max - ifft_min)

                
            fft_si = f2 * single
            fft2 = np.fft.fftshift(fft_si)
            ifft_im1 = np.fft.ifft2(fft2)
            ifft2 = np.abs(ifft_im1)
            ifft2_min = np.min(ifft2)
            ifft2_max = np.max(ifft2)
            sin = (ifft2 - ifft2_min)*255 /(ifft2_max - ifft2_min)

        cv2.imshow("remake",remake.astype(uint8))
        cv2.imshow("single",sin.astype(uint8))
        cv2.imshow("click",click)

        if k==27:
            break

cv2.destroyAllWindows()