#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images
import serial

import time


labels = ["Vidhan","Ritvik"]


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face-trainner.yml')

cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera

while(True):

    ret, img = cap.read() # Break video into frames 
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
    faces = face_cascade.detectMultiScale(gray, minNeighbors=5)
    cv2.imshow('Preview',img) #Display the Video
    if cv2.waitKey(20) & 0xFF == ord('q'):
    	break#Recog. faces
    for (x, y, w, h) in faces:
    	roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

    	id_, conf = recognizer.predict(roi_gray) #recognize the Face
    
    	if conf>=80:
            font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
            name = labels[id_]#Get the name from the List using ID number
            
            
            if (name == "Ritvik"): 
                time.sleep(2)
                
                
               
                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break#Recog. faces
                for (x, y, w, h) in faces:
                    roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

                    id_, conf = recognizer.predict(roi_gray) #recognize the Face
                
                    if conf>=80:
                        font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
                        name = labels[id_]#Get the name from the List using ID number
                        if os.path.exists('/dev/rfcomm0')==False:
                            path='sudo rfcomm bind 0 98:D3:61:F6:41:E4'
                            os.system(path)
                            time.sleep(1)
                        bluetoothSerial=serial.Serial("/dev/rfcomm0",baudrate=9600)
                        count=None
                        while count!="terminate":

                            count=input("Enter the command: ")
                            j=str(count)
                            b=j.encode()
                            bluetoothSerial.write(b)
                            time.sleep(1)
                            
                                    
                        
                    break
                cap.release()
                
                cap = cv2.VideoCapture(0) 
                ret, img = cap.read() # Break video into frames 
                gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
                faces = face_cascade.detectMultiScale(gray, minNeighbors=5)
                cv2.imshow('Preview',img) #Display the Video
                                            
         
    
            

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
