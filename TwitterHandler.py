import twint
import serial
import os
import time

count=None
while count!="terminate":
    if os.path.exists('/dev/rfcomm0')==False:
        path='sudo rfcomm bind 0 98:D3:61:F6:41:E4'
        os.system(path)
        time.sleep(1)
    bluetoothSerial=serial.Serial("/dev/rfcomm0",baudrate=9600)
    time.sleep(1)
    c=twint.Config()
    c.limit=20
    c.Username="RPi_Ritvik"
    c.Pandas=True
    command=None
    lmao = 0
    while (lmao == 0):
        twint.run.Search(c)
        tweets=twint.storage.panda.Tweets_df
        lmao = len(tweets)
        time.sleep(1)
    
    m=[]
    m=tweets['tweet'].tolist()
    length=len(m)
    print(m)
    #we only accept a command when the size of m is increased
    while(True):
        time.sleep(1)
        c.limit=20
        
        lmao = 0
        while (lmao == 0):
            twint.run.Search(c)
            tweets=twint.storage.panda.Tweets_df
            lmao = len(tweets)
            time.sleep(1)
        n=[]
        n=tweets['tweet'].tolist()
        print(n)
        if(len(m)<len(n)):
            command = str(n[0])
            
            count= command
            b=count.encode()
            bluetoothSerial.write(b)
            time.sleep(1.5)

            break;
   
        
   



