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


#Photo IPS 1
IPS_user_1_image = face_recognition.load_image_file(path_folder+"/ips 1/Alfauzan Qotada.jpg")
IPS_user_1_face_encoding = face_recognition.face_encodings(IPS_user_1_image)[0]
IPS_user_2_image = face_recognition.load_image_file(path_folder+"/ips 1/Ali Akbar Nugraha.jpg")
IPS_user_2_face_encoding = face_recognition.face_encodings(IPS_user_2_image)[0]
IPS_user_3_image = face_recognition.load_image_file(path_folder+"/ips 1/alya Ramadhani.jpg")
IPS_user_3_face_encoding = face_recognition.face_encodings(IPS_user_3_image)[0]
IPS_user_4_image = face_recognition.load_image_file(path_folder+"/ips 1/Ayyub Alfiqri Sitompul.jpg")
IPS_user_4_face_encoding = face_recognition.face_encodings(IPS_user_4_image)[0]
IPS_user_5_image = face_recognition.load_image_file(path_folder+"/ips 1/Bagas Prayoga.jpg")
IPS_user_5_face_encoding = face_recognition.face_encodings(IPS_user_5_image)[0]
IPS_user_6_image = face_recognition.load_image_file(path_folder+"/ips 1/Bayu Anggara.jpg")
IPS_user_6_face_encoding = face_recognition.face_encodings(IPS_user_6_image)[0]
IPS_user_7_image = face_recognition.load_image_file(path_folder+"/ips 1/Cindy Aulia.jpg")
IPS_user_7_face_encoding = face_recognition.face_encodings(IPS_user_7_image)[0]
IPS_user_8_image = face_recognition.load_image_file(path_folder+"/ips 1/Desvitha Citra Dewi Lestari.jpg")
IPS_user_8_face_encoding = face_recognition.face_encodings(IPS_user_8_image)[0]
IPS_user_9_image = face_recognition.load_image_file(path_folder+"/ips 1/Ezy Yarzuqu.jpg")
IPS_user_9_face_encoding = face_recognition.face_encodings(IPS_user_9_image)[0]
IPS_user_10_image = face_recognition.load_image_file(path_folder+"/ips 1/Habib Syahren Rawi.jpg")
IPS_user_10_face_encoding = face_recognition.face_encodings(IPS_user_10_image)[0]
IPS_user_11_image = face_recognition.load_image_file(path_folder+"/ips 1/Hafiz Aqila Rianda.jpg")
IPS_user_11_face_encoding = face_recognition.face_encodings(IPS_user_11_image)[0]
IPS_user_12_image = face_recognition.load_image_file(path_folder+"/ips 1/Haikal Ichsan.jpg")
IPS_user_12_face_encoding = face_recognition.face_encodings(IPS_user_12_image)[0]
IPS_user_13_image = face_recognition.load_image_file(path_folder+"/ips 1/Icha Adinda.jpg")
IPS_user_13_face_encoding = face_recognition.face_encodings(IPS_user_13_image)[0]
IPS_user_14_image = face_recognition.load_image_file(path_folder+"/ips 1/Ilham Azis.jpg")
IPS_user_14_face_encoding = face_recognition.face_encodings(IPS_user_14_image)[0]
IPS_user_15_image = face_recognition.load_image_file(path_folder+"/ips 1/Imam Albuchori.jpg")
IPS_user_15_face_encoding = face_recognition.face_encodings(IPS_user_15_image)[0]
IPS_user_16_image = face_recognition.load_image_file(path_folder+"/ips 1/Imam Maulana Lubis.jpg")
IPS_user_16_face_encoding = face_recognition.face_encodings(IPS_user_16_image)[0]
IPS_user_17_image = face_recognition.load_image_file(path_folder+"/ips 1/Labib Nurul Hanif.jpg")
IPS_user_17_face_encoding = face_recognition.face_encodings(IPS_user_17_image)[0]
IPS_user_18_image = face_recognition.load_image_file(path_folder+"/ips 1/Miftahun Nazmi.jpg")
IPS_user_18_face_encoding = face_recognition.face_encodings(IPS_user_18_image)[0]
IPS_user_19_image = face_recognition.load_image_file(path_folder+"/ips 1/Muhammad Fadly.jpg")
IPS_user_19_face_encoding = face_recognition.face_encodings(IPS_user_19_image)[0]
IPS_user_20_image = face_recognition.load_image_file(path_folder+"/ips 1/Muhammad Gunawan Prasetyo.jpg")
IPS_user_20_face_encoding = face_recognition.face_encodings(IPS_user_20_image)[0]
IPS_user_21_image = face_recognition.load_image_file(path_folder+"/ips 1/Muhammad Tri Cahyadi Siregar.jpg")
IPS_user_21_face_encoding = face_recognition.face_encodings(IPS_user_21_image)[0]
IPS_user_22_image = face_recognition.load_image_file(path_folder+"/ips 1/Mutiara Dwi Ananda.jpg")
IPS_user_22_face_encoding = face_recognition.face_encodings(IPS_user_22_image)[0]
IPS_user_23_image = face_recognition.load_image_file(path_folder+"/ips 1/Nurul Satria.jpg")
IPS_user_23_face_encoding = face_recognition.face_encodings(IPS_user_23_image)[0]
IPS_user_24_image = face_recognition.load_image_file(path_folder+"/ips 1/Oktavani Adinda.jpg")
IPS_user_24_face_encoding = face_recognition.face_encodings(IPS_user_24_image)[0]
IPS_user_25_image = face_recognition.load_image_file(path_folder+"/ips 1/Rahmatika Awaliya.jpg")
IPS_user_25_face_encoding = face_recognition.face_encodings(IPS_user_25_image)[0]
IPS_user_26_image = face_recognition.load_image_file(path_folder+"/ips 1/Reno Ardhana Mardianto.jpg")
IPS_user_26_face_encoding = face_recognition.face_encodings(IPS_user_26_image)[0]
IPS_user_27_image = face_recognition.load_image_file(path_folder+"/ips 1/Rio Sya'bana Giawa.jpg")
IPS_user_27_face_encoding = face_recognition.face_encodings(IPS_user_27_image)[0]
IPS_user_28_image = face_recognition.load_image_file(path_folder+"/ips 1/Ryan Ardiansyah.jpg")
IPS_user_28_face_encoding = face_recognition.face_encodings(IPS_user_28_image)[0]
IPS_user_29_image = face_recognition.load_image_file(path_folder+"/ips 1/Syabila Mutia.jpg")
IPS_user_29_face_encoding = face_recognition.face_encodings(IPS_user_29_image)[0]
IPS_user_30_image = face_recognition.load_image_file(path_folder+"/ips 1/Syahputra Ramadhan.jpg")
IPS_user_30_face_encoding = face_recognition.face_encodings(IPS_user_30_image)[0]
IPS_user_31_image = face_recognition.load_image_file(path_folder+"/ips 1/Eka Sari Meidiana.jpg")
IPS_user_31_face_encoding = face_recognition.face_encodings(IPS_user_31_image)[0]
IPS_user_32_image = face_recognition.load_image_file(path_folder+"/ips 1/Egi Adrian Ginting.jpg")
IPS_user_32_face_encoding = face_recognition.face_encodings(IPS_user_32_image)[0]
IPS_user_33_image = face_recognition.load_image_file(path_folder+"/ips 1/Umaira Alfaiza.jpg")
IPS_user_33_face_encoding = face_recognition.face_encodings(IPS_user_33_image)[0]
IPS_user_34_image = face_recognition.load_image_file(path_folder+"/ips 1/yolanda.jpg")
IPS_user_34_face_encoding = face_recognition.face_encodings(IPS_user_34_image)[0]

#Photo MIPA 1
IPA_1_user_1_image = face_recognition.load_image_file(path_folder+"/mipa 1/Agung Sigit Prabowo.jpg")
IPA_1_user_1_face_encoding = face_recognition.face_encodings(IPA_1_user_1_image)[0]
IPA_1_user_2_image = face_recognition.load_image_file(path_folder+"/mipa 1/Akbar Baihaqi Syah.jpg")
IPA_1_user_2_face_encoding = face_recognition.face_encodings(IPA_1_user_2_image)[0]
IPA_1_user_3_image = face_recognition.load_image_file(path_folder+"/mipa 1/Al Fathir Keizaki.jpg")
IPA_1_user_3_face_encoding = face_recognition.face_encodings(IPA_1_user_3_image)[0]
IPA_1_user_4_image = face_recognition.load_image_file(path_folder+"/mipa 1/Alif Aqila Ramadhan Ht. Suhut.jpg")
IPA_1_user_4_face_encoding = face_recognition.face_encodings(IPA_1_user_4_image)[0]
IPA_1_user_5_image = face_recognition.load_image_file(path_folder+"/mipa 1/Anggi Rahmadani Siregar.jpg")
IPA_1_user_5_face_encoding = face_recognition.face_encodings(IPA_1_user_5_image)[0]
IPA_1_user_6_image = face_recognition.load_image_file(path_folder+"/mipa 1/Anneza Salsabila.jpg")
IPA_1_user_6_face_encoding = face_recognition.face_encodings(IPA_1_user_6_image)[0]
IPA_1_user_7_image = face_recognition.load_image_file(path_folder+"/mipa 1/Cantika Putri Kusumah.jpg")
IPA_1_user_7_face_encoding = face_recognition.face_encodings(IPA_1_user_7_image)[0]
IPA_1_user_8_image = face_recognition.load_image_file(path_folder+"/mipa 1/Dania.jpg")
IPA_1_user_8_face_encoding = face_recognition.face_encodings(IPA_1_user_8_image)[0]
IPA_1_user_9_image = face_recognition.load_image_file(path_folder+"/mipa 1/Dina Munawaroh.jpg")
IPA_1_user_9_face_encoding = face_recognition.face_encodings(IPA_1_user_9_image)[0]
IPA_1_user_10_image = face_recognition.load_image_file(path_folder+"/mipa 1/Erlanggi.jpg")
IPA_1_user_10_face_encoding = face_recognition.face_encodings(IPA_1_user_10_image)[0]
IPA_1_user_11_image = face_recognition.load_image_file(path_folder+"/mipa 1/Fradilla Nazmi.jpg")
IPA_1_user_11_face_encoding = face_recognition.face_encodings(IPA_1_user_11_image)[0]
IPA_1_user_12_image = face_recognition.load_image_file(path_folder+"/mipa 1/Jihan Nafilah.jpg")
IPA_1_user_12_face_encoding = face_recognition.face_encodings(IPA_1_user_12_image)[0]
IPA_1_user_13_image = face_recognition.load_image_file(path_folder+"/mipa 1/Nadya Zalwa.jpg")
IPA_1_user_13_face_encoding = face_recognition.face_encodings(IPA_1_user_13_image)[0]
IPA_1_user_14_image = face_recognition.load_image_file(path_folder+"/mipa 1/Naffa Ardiansyah.jpg")
IPA_1_user_14_face_encoding = face_recognition.face_encodings(IPA_1_user_14_image)[0]
IPA_1_user_15_image = face_recognition.load_image_file(path_folder+"/mipa 1/Nayla Fadilah.jpg")
IPA_1_user_15_face_encoding = face_recognition.face_encodings(IPA_1_user_15_image)[0]
IPA_1_user_16_image = face_recognition.load_image_file(path_folder+"/mipa 1/Rafa Sava Zaen Lubis.jpg")
IPA_1_user_16_face_encoding = face_recognition.face_encodings(IPA_1_user_16_image)[0]
IPA_1_user_17_image = face_recognition.load_image_file(path_folder+"/mipa 1/Retno Armiyanti.jpg")
IPA_1_user_17_face_encoding = face_recognition.face_encodings(IPA_1_user_17_image)[0]
IPA_1_user_18_image = face_recognition.load_image_file(path_folder+"/mipa 1/Siti Rachmah.jpg")
IPA_1_user_18_face_encoding = face_recognition.face_encodings(IPA_1_user_18_image)[0]
IPA_1_user_19_image = face_recognition.load_image_file(path_folder+"/mipa 1/Tasya Alifa Putri.jpg")
IPA_1_user_19_face_encoding = face_recognition.face_encodings(IPA_1_user_19_image)[0]
IPA_1_user_20_image = face_recognition.load_image_file(path_folder+"/mipa 1/Vanesa Putri.jpg")
IPA_1_user_20_face_encoding = face_recognition.face_encodings(IPA_1_user_20_image)[0]
IPA_1_user_21_image = face_recognition.load_image_file(path_folder+"/mipa 1/Winda Rara Dwi Putri.jpg")
IPA_1_user_21_face_encoding = face_recognition.face_encodings(IPA_1_user_21_image)[0]
IPA_1_user_22_image = face_recognition.load_image_file(path_folder+"/mipa 1/Yona Liza.jpg")
IPA_1_user_22_face_encoding = face_recognition.face_encodings(IPA_1_user_22_image)[0]

hamdi = face_recognition.load_image_file(path_folder+"/ips 1/hamdi.jpg")
hamdi_encoding = face_recognition.face_encodings(hamdi)[0]

#Photo MIPA 2
IPA_2_user_1_image = face_recognition.load_image_file(path_folder+"/mipa 2/Agung Gunawan.jpg")
IPA_2_user_1_face_encoding = face_recognition.face_encodings(IPA_2_user_1_image)[0]
IPA_2_user_2_image = face_recognition.load_image_file(path_folder+"/mipa 2/Alif Irawan.jpg")
IPA_2_user_2_face_encoding = face_recognition.face_encodings(IPA_2_user_2_image)[0]
IPA_2_user_3_image = face_recognition.load_image_file(path_folder+"/mipa 2/Anggita Syahrani.jpg")
IPA_2_user_3_face_encoding = face_recognition.face_encodings(IPA_2_user_3_image)[0]
IPA_2_user_4_image = face_recognition.load_image_file(path_folder+"/mipa 2/Bagas Abdul Prasetyo.jpg")
IPA_2_user_4_face_encoding = face_recognition.face_encodings(IPA_2_user_4_image)[0]
IPA_2_user_5_image = face_recognition.load_image_file(path_folder+"/mipa 2/Cindy Amelia Hasibuan.jpg")
IPA_2_user_5_face_encoding = face_recognition.face_encodings(IPA_2_user_5_image)[0]
IPA_2_user_6_image = face_recognition.load_image_file(path_folder+"/mipa 2/Cindy Aulia Devi.jpg")
IPA_2_user_6_face_encoding = face_recognition.face_encodings(IPA_2_user_6_image)[0]
IPA_2_user_7_image = face_recognition.load_image_file(path_folder+"/mipa 2/Egi Tanto.jpg")
IPA_2_user_7_face_encoding = face_recognition.face_encodings(IPA_2_user_7_image)[0]
IPA_2_user_8_image = face_recognition.load_image_file(path_folder+"/mipa 2/Ezy Alfahrezi.jpg")
IPA_2_user_8_face_encoding = face_recognition.face_encodings(IPA_2_user_8_image)[0]
IPA_2_user_9_image = face_recognition.load_image_file(path_folder+"/mipa 2/Fahri Anwar Adam Malik BB.jpg")
IPA_2_user_9_face_encoding = face_recognition.face_encodings(IPA_2_user_9_image)[0]
IPA_2_user_10_image = face_recognition.load_image_file(path_folder+"/mipa 2/Hariansyah Putra Pratama.jpg")
IPA_2_user_10_face_encoding = face_recognition.face_encodings(IPA_2_user_10_image)[0]
IPA_2_user_11_image = face_recognition.load_image_file(path_folder+"/mipa 2/Jihan Auliya.jpg")
IPA_2_user_11_face_encoding = face_recognition.face_encodings(IPA_2_user_11_image)[0]
IPA_2_user_12_image = face_recognition.load_image_file(path_folder+"/mipa 2/Lira Mutia.jpg")
IPA_2_user_12_face_encoding = face_recognition.face_encodings(IPA_2_user_12_image)[0]
IPA_2_user_13_image = face_recognition.load_image_file(path_folder+"/mipa 2/Muhammad Abdhal Sam.jpg")
IPA_2_user_13_face_encoding = face_recognition.face_encodings(IPA_2_user_13_image)[0]
IPA_2_user_14_image = face_recognition.load_image_file(path_folder+"/mipa 2/Muhammad Ikhsan Ramadan.jpg")
IPA_2_user_14_face_encoding = face_recognition.face_encodings(IPA_2_user_14_image)[0]
IPA_2_user_15_image = face_recognition.load_image_file(path_folder+"/mipa 2/Muhammad Syamsuddin Siregar.jpg")
IPA_2_user_15_face_encoding = face_recognition.face_encodings(IPA_2_user_15_image)[0]
IPA_2_user_16_image = face_recognition.load_image_file(path_folder+"/mipa 2/Naila Chairunnisa.jpg")
IPA_2_user_16_face_encoding = face_recognition.face_encodings(IPA_2_user_16_image)[0]
IPA_2_user_17_image = face_recognition.load_image_file(path_folder+"/mipa 2/Nayla Adya Putri Utami.jpg")
IPA_2_user_17_face_encoding = face_recognition.face_encodings(IPA_2_user_17_image)[0]
IPA_2_user_18_image = face_recognition.load_image_file(path_folder+"/mipa 2/Nayla Widya Aryanti.jpg")
IPA_2_user_18_face_encoding = face_recognition.face_encodings(IPA_2_user_18_image)[0]
IPA_2_user_19_image = face_recognition.load_image_file(path_folder+"/mipa 2/Nuzila Nada Ananta.jpg")
IPA_2_user_19_face_encoding = face_recognition.face_encodings(IPA_2_user_19_image)[0]
IPA_2_user_20_image = face_recognition.load_image_file(path_folder+"/mipa 2/Rahmat Darmawan.jpg")
IPA_2_user_20_face_encoding = face_recognition.face_encodings(IPA_2_user_20_image)[0]
IPA_2_user_21_image = face_recognition.load_image_file(path_folder+"/mipa 2/Reina Andini Surbakti.jpg")
IPA_2_user_21_face_encoding = face_recognition.face_encodings(IPA_2_user_21_image)[0]
IPA_2_user_22_image = face_recognition.load_image_file(path_folder+"/mipa 2/Rifky Rinanda Lubis.jpg")
IPA_2_user_22_face_encoding = face_recognition.face_encodings(IPA_2_user_22_image)[0]
IPA_2_user_23_image = face_recognition.load_image_file(path_folder+"/mipa 2/Yogi Sugama.jpg")
IPA_2_user_23_face_encoding = face_recognition.face_encodings(IPA_2_user_23_image)[0]
IPA_2_user_24_image = face_recognition.load_image_file(path_folder+"/mipa 2/Yudha.jpg")
IPA_2_user_24_face_encoding = face_recognition.face_encodings(IPA_2_user_24_image)[0]
IPA_2_user_25_image = face_recognition.load_image_file(path_folder+"/mipa 2/Zharah Paramitha.jpg")
IPA_2_user_25_face_encoding = face_recognition.face_encodings(IPA_2_user_25_image)[0]




today = date.today()
d1 = today.strftime("%d-%b-%Y")

nama_folder = "Rekapitulasi/"+d1
if not os.path.exists(nama_folder):
	os.makedirs(nama_folder)
    
    

#Data Anak IPS
known_face_encodings = [
    hamdi_encoding,
    IPS_user_1_face_encoding,
    IPS_user_2_face_encoding,
    IPS_user_3_face_encoding,
    IPS_user_4_face_encoding,
    IPS_user_5_face_encoding,
    IPS_user_6_face_encoding,
    IPS_user_7_face_encoding,
    IPS_user_8_face_encoding,
    IPS_user_9_face_encoding,
    IPS_user_10_face_encoding,
    IPS_user_11_face_encoding,
    IPS_user_12_face_encoding,
    IPS_user_13_face_encoding,
    IPS_user_14_face_encoding,
    IPS_user_15_face_encoding,
    IPS_user_16_face_encoding,
    IPS_user_17_face_encoding,
    IPS_user_18_face_encoding,
    IPS_user_19_face_encoding,
    IPS_user_20_face_encoding,
    IPS_user_21_face_encoding,
    IPS_user_22_face_encoding,
    IPS_user_23_face_encoding,
    IPS_user_24_face_encoding,
    IPS_user_25_face_encoding,
    IPS_user_26_face_encoding,
    IPS_user_27_face_encoding,
    IPS_user_28_face_encoding,
    IPS_user_29_face_encoding,
    IPS_user_30_face_encoding,
    IPS_user_31_face_encoding,
    IPS_user_32_face_encoding,
    IPS_user_33_face_encoding,
    IPS_user_34_face_encoding,
    #Data Anak IPA 1
    IPA_1_user_1_face_encoding,
    IPA_1_user_2_face_encoding,
    IPA_1_user_3_face_encoding,
    IPA_1_user_4_face_encoding,
    IPA_1_user_5_face_encoding,
    IPA_1_user_6_face_encoding,
    IPA_1_user_7_face_encoding,
    IPA_1_user_8_face_encoding,
    IPA_1_user_9_face_encoding,
    IPA_1_user_10_face_encoding,
    IPA_1_user_11_face_encoding,
    IPA_1_user_12_face_encoding,
    IPA_1_user_13_face_encoding,
    IPA_1_user_14_face_encoding,
    IPA_1_user_15_face_encoding,
    IPA_1_user_16_face_encoding,
    IPA_1_user_17_face_encoding,
    IPA_1_user_18_face_encoding,
    IPA_1_user_19_face_encoding,
    IPA_1_user_20_face_encoding,
    IPA_1_user_21_face_encoding,
    IPA_1_user_22_face_encoding,
    #Data Anak IPA 2
    IPA_2_user_1_face_encoding,
    IPA_2_user_2_face_encoding,
    IPA_2_user_3_face_encoding,
    IPA_2_user_4_face_encoding,
    IPA_2_user_5_face_encoding,
    IPA_2_user_6_face_encoding,
    IPA_2_user_7_face_encoding,
    IPA_2_user_8_face_encoding,
    IPA_2_user_9_face_encoding,
    IPA_2_user_10_face_encoding,
    IPA_2_user_11_face_encoding,
    IPA_2_user_12_face_encoding,
    IPA_2_user_13_face_encoding,
    IPA_2_user_14_face_encoding,
    IPA_2_user_15_face_encoding,
    IPA_2_user_16_face_encoding,
    IPA_2_user_17_face_encoding,
    IPA_2_user_18_face_encoding,
    IPA_2_user_19_face_encoding,
    IPA_2_user_20_face_encoding,
    IPA_2_user_21_face_encoding,
    IPA_2_user_22_face_encoding,
    IPA_2_user_23_face_encoding,
    IPA_2_user_24_face_encoding,
    IPA_2_user_25_face_encoding
    
]
known_face_names = [
    "Super Admin",
    "Alfauzan Qotada - IPS 1",
    "Ali Akbar Nugraha - IPS 1",
    "alya Ramadhani - IPS 1",
    "Ayyub Alfiqri Sitompul - IPS 1",
    "Bagas Prayoga - IPS 1",
    "Bayu Anggara - IPS 1",
    "Cindy Aulia - IPS 1",
    "Desvitha Citra Dewi Lestari - IPS 1",
    "Ezy Yarzuqu - IPS 1",
    "Habib Syahren Rawi - IPS 1",
    "Hafiz Aqila Rianda - IPS 1",
    "Haikal Ichsan - IPS 1",
    "Icha Adinda - IPS 1",
    "Ilham Azis - IPS 1",
    "Imam Albuchori - IPS 1",
    "Imam Maulana Lubis - IPS 1",
    "Labib Nurul Hanif - IPS 1",
    "Miftahun Nazmi - IPS 1",
    "Muhammad Fadly - IPS 1",
    "Muhammad Gunawan Prasetyo - IPS 1",
    "Muhammad Tri Cahyadi Siregar - IPS 1",
    "Mutiara Dwi Ananda - IPS 1",
    "Nurul Satria - IPS 1",
    "Oktavani Adinda - IPS 1",
    "Rahmatika Awaliya - IPS 1",
    "Reno Ardhana Mardianto - IPS 1",
    "Rio Sya'bana Giawa - IPS 1",
    "Ryan Ardiansyah - IPS 1",
    "Syabila Mutia - IPS 1",
    "Syahputra Ramadhan - IPS 1",
    "Eka Sari Meidiana - IPS 1",
    "Egi Adrian Ginting - IPS 1",
    "Umaira Alfaiza - IPS 1",
    "yolanda - IPS 1",
    #Data IPA 1
    "Agung Sigit Prabowo - IPA 1",
    "Akbar Baihaqi Syah - IPA 1",
    "Al Fathir Keizaki - IPA 1",
    "Alif Aqila Ramadhan Ht. Suhut - IPA 1",
    "Anggi Rahmadani Siregar - IPA 1",
    "Anneza Salsabila - IPA 1",
    "Cantika Putri Kusumah - IPA 1",
    "Dania - IPA 1",
    "Dina Munawaroh - IPA 1",
    "Erlanggi - IPA 1",
    "Fradilla Nazmi - IPA 1",
    "Jihan Nafilah - IPA 1",
    "Nadya Zalwa - IPA 1",
    "Naffa Ardiansyah - IPA 1",
    "Nayla Fadilah - IPA 1",
    "Rafa Sava Zaen Lubis - IPA 1",
    "Retno Armiyanti - IPA 1",
    "Siti Rachmah - IPA 1",
    "Tasya Alifa Putri - IPA 1",
    "Vanesa Putri - IPA 1",
    "Winda Rara Dwi Putri - IPA 1",
    "Yona Liza - IPA 1",
    #Data IPA 2
    "Agung Gunawan - IPA 2",
    "Alif Irawan - IPA 2",
    "Anggita Syahrani - IPA 2",
    "Bagas Abdul Prasetyo - IPA 2",
    "Cindy Amelia Hasibuan - IPA 2",
    "Cindy Aulia Devi - IPA 2",
    "Egi Tanto - IPA 2",
    "Ezy Alfahrezi - IPA 2",
    "Fahri Anwar Adam Malik BB - IPA 2",
    "Hariansyah Putra Pratama - IPA 2",
    "Jihan Auliya - IPA 2",
    "Lira Mutia - IPA 2",
    "Muhammad Abdhal Sam - IPA 2",
    "Muhammad Ikhsan Ramadan - IPA 2",
    "Muhammad Syamsuddin Siregar - IPA 2",
    "Naila Chairunnisa - IPA 2",
    "Nayla Adya Putri Utami - IPA 2",
    "Nayla Widya Aryanti - IPA 2",
    "Nuzila Nada Ananta - IPA 2",
    "Rahmat Darmawan - IPA 2",
    "Reina Andini Surbakti - IPA 2",
    "Rifky Rinanda Lubis - IPA 2",
    "Yogi Sugama - IPA 2",
    "Yudha - IPA 2",
    "Zharah Paramitha - IPA 2"

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