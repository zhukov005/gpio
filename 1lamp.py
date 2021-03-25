import RPi.GPIO as GPIO
import time

ar = [21,20,16,12,7,8,25,24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

bit_depth = 8
def bin_convert(n):
    N = bit_depth - 1
    p = 0
    X = []
    while N > 0:
        p = int(n/2**N)
        if p ==1:
            X.append(1)
            n-=2**N
        else:
            X.append(0)
        N-=1
    X.append(n)
    return X

def lightUp(ledNumber, period):
    ar = [21,20,16,12,7,8,25,24]
    GPIO.output(ar[ledNumber],1)
    time.sleep(period)
    GPIO.output(ar[ledNumber],0)


def blink(ledNumber,blinkCount,blinkperiod):
    ar = [21,20,16,12,7,8,25,24]
    ledNumber = ledNumber - 1
    i = 0
    while i < blinkCount:
        GPIO.output(ar[ledNumber],1)
        time.sleep(blinkperiod)
        GPIO.output(ar[ledNumber],0)
        time.sleep(blinkperiod)
        i+=1
    GPIO.output(ar[ledNumber],0)



def runningLight(count,period):
    ar = [21,20,16,12,7,8,25,24]
    k = 0
    for i in range(1,count):
        if i % 8 == 0:
            k = k - 8
        GPIO.output(ar[k],1)
        time.sleep(period)
        GPIO.output(ar[k],0)
        k = k + 1

def runningDark(count,period):
    GPIO.output(24,1)
    GPIO.output(8,1)
    GPIO.output(7,1)
    GPIO.output(21,1)
    GPIO.output(20,1)
    GPIO.output(16,1)
    GPIO.output(12,1)
    GPIO.output(25,1)
    k = 0
    for i in range(1,count):
        if i % 8 == 0:
            k = k - 8
        GPIO.output(ar[k],0)
        time.sleep(period)
        GPIO.output(ar[k],1)
        k = k + 1

def decToBinList(decNumber):
    N = bit_depth - 1
    p = 0
    X = []
    while N > 0:
        p = int(decNumber/2**N)
        if p ==1:
            X.append(1)
            decNumber-=2**N
        else:
            X.append(0)
        N-=1
    X.append(decNumber)
    return(X)

def lightNumber(number):
    X = decToBinList(number)
    for i in range(0,7):
        GPIO.output(ar[i], X[i])
    time.sleep(3)


def runningPattern(pattern,direction):
    ag = decToBinList(pattern)
    for i in range(0,7):
        GPIO.output(ar[i], ag[i])
    time.sleep(3)
    n = 0
    if direction == 1:
        for i in range(0,7):
            


#for j in range(0,256):
#    N = [0,0,0,0,0,0,0,0]
#    N = bin_convert(j)
#    print(N)
#    for i in range(0,bit_depth):
#        GPIO.output(D[i],N[i])
#    time.sleep(0.1)

#lightUp(2,1)
#blink(3,6,0.2)
#runningLight(20,0.5)
#runningDark
#print(decToBinList(33))
lightNumber(2)
#runningPattern(5, 1)

GPIO.output(24,0)
GPIO.output(8,0)
GPIO.output(7,0)
GPIO.output(21,0)
GPIO.output(20,0)
GPIO.output(16,0)
GPIO.output(12,0)
GPIO.output(25,0)

GPIO.cleanup(24)
GPIO.cleanup(21)
GPIO.cleanup(20)
GPIO.cleanup(16)
GPIO.cleanup(12)
GPIO.cleanup(7)
GPIO.cleanup(8)
GPIO.cleanup(25)