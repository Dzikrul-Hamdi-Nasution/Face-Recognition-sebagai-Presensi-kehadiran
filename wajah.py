import os
import json
import face_recognition
import cv2
import numpy as np
import time 
from datetime import datetime
from datetime import date
from playsound import playsound
#import pygame



video_capture = cv2.VideoCapture(0)

path_folder="siswa/"


hamdi = face_recognition.load_image_file(path_folder+"/ips 1/hamdi.jpg")
hamdi_encoding = face_recognition.face_encodings(hamdi)[0]

IPS_user_1_image = face_recognition.load_image_file(path_folder+"/ips 1/Alfauzan Qotada.jpg")
IPS_user_1_face_encoding = face_recognition.face_encodings(IPS_user_1_image)[0]



today = date.today()
d1 = today.strftime("%d-%b-%Y")

nama_folder = "Rekapitulasi/"+d1
if not os.path.exists(nama_folder):
	os.makedirs(nama_folder)
    
    

#Data Anak IPS
known_face_encodings = [
    hamdi_encoding,
    IPS_user_1_face_encoding
    
]
known_face_names = [
    "Super Admin",
    "Alfauzan Qotada - IPS 1"

]







# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

prev_frame_time = 0
new_frame_time = 0
kunci=0
nama_2=""
name=""

kode_array_nama=[]
kode_array_waktu=[]
dictionary=[]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.17, fy=0.17)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    


    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
       
        
        face_names = []
        for face_encoding in face_encodings:
        # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.40)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]   
                if name != nama_2:
                    kunci=0
                else:
                    kunci=1
                
                if matches[best_match_index]:
                    if kunci==0:
                        now = datetime.now()    
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  
                        name = known_face_names[best_match_index]
                        print(name)
                        nama_2=name
                        cv2.imwrite(nama_folder+'/{}.jpg'.format(name),img=frame)
                        #pygame.mixer.init()
                        #pygame.mixer.music.load("hadir.mp3")
                        #pygame.mixer.music.play()

                        

                        if (name in kode_array_nama):
                            print ("Element Exists")
                        else:
                            dictionary.append (
                                {
                                "name" : name,
                                "jam" : dt_string
                            }
                            )

                            json_object = json.dumps(dictionary, indent = 2)
                            with open("Database/"+d1+".json", "w") as outfile:
                                outfile.write(json_object)
                        
                        kode_array_nama.append(name)
                        kode_array_waktu.append(dt_string)
                        
                    if kunci==1:
                        name = known_face_names[best_match_index]+" "+ dt_string
                        
                    kunci=1
                else:
                    kunci=0
            
            
            
                
            face_names.append(name)
            
   
         

    process_this_frame = not process_this_frame

  
       

    

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 6
        right *= 6
        bottom *= 6
        left *= 6

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    font = cv2.FONT_HERSHEY_SIMPLEX 
    new_frame_time = time.time() 
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 
    fps = int(fps) 
    fps = str(fps)
    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 

    

       
    ukuran_fix=cv2.resize(frame, (650, 450), fx=0.17, fy=0.17)

    # Display the resulting image
    cv2.imshow('Video', ukuran_fix)


    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()