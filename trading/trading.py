from PIL import ImageGrab
import  datetime
from python_imagesearch.imagesearch import imagesearch

from threading import Timer

buy_called = []
sell_called = []


previous_sell_x = 0
previous_sell_y = 0
previous_buy_x = 0
previous_buy_y = 0

def main():
    global previous_sell_x, previous_buy_x,previous_sell_y, previous_buy_y
    print("signal searching........")
    pos = imagesearch("sell.png")
    
    if pos[0]>1200:
        if previous_sell_x==0:
            print("sell signal dected")
            previous_sell_x = pos[0]
            previous_sell_y = pos[1]
            print("sell position : ", pos[0], pos[1]) 
        elif previous_sell_x>=pos[0]:
            previous_sell_x = pos[0]
            previous_sell_y = pos[1]
        else:
            print("sell signal detected:")    
            previous_sell_x = pos[0]
            previous_sell_y = pos[1]   
            print("Sell position : ", pos[0], pos[1])        

    pos = imagesearch("buy.png")
    
    if pos[0]>1200:
        if previous_buy_x==0:
            print("buy signal detected:")
            previous_buy_x = pos[0]
            previous_buy_y = pos[1]
            print("buy position : ", pos[0], pos[1])  
        elif previous_buy_x>=pos[0]:
            previous_buy_x = pos[0]
            previous_buy_y = pos[1]
        else:
            print("buy signal detected")    
            previous_buy_x = pos[0]
            previous_buy_y = pos[1]   
            print("buy position : ", pos[0], pos[1])  
            
    Timer(1/4, main).start()
main()    