import ctypes  # An included library with Python install.
import sys
import cv2
import numpy as np
import time


import src.python.dataset.load_image as li
import src.python.facenet as  fs
import src.python.facenet.utils  as face_utils

number = 0
summ = 0

sys.path.append('...\sample_face_recognition\src')
cap = cv2.VideoCapture(0)
emb_train = []
y_train = []

if __name__ == "__main__":
    while True:
        start_time = time.time()
        frame = li.load_from_camera(cap)
        cv2.imshow('frame', frame)
        faces_coord = face_utils.get_face_from_image(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)
        if faces_coord.__len__() == 1:
            x_face, y_face, w_face, h_face = [faces_coord[0][0], faces_coord[0][1], faces_coord[0][2],
                                              faces_coord[0][3]]
            emb_train.append(fs.get_embeding(
                frame[y_face:y_face + h_face, x_face:x_face + w_face]
            ))
            y_train.append(1)
            print("--- %s seconds ---" % (time.time() - start_time))
            break

    code = ctypes.windll.user32.MessageBoxW(0, "Your Authentetification", "Your Authentetification", 1)

    if code == 1:
        while True:
            start_time = time.time()
            number = number + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frame = li.load_from_camera(cap)
            faces_coord = face_utils.get_face_from_image(frame)
            #print(faces_coord)




            for face_coord in faces_coord:
                x_face, y_face, w_face, h_face = [face_coord[0], face_coord[1], face_coord[2],
                                                  face_coord[3]]
                emb_test = fs.get_embeding(
                    frame[y_face:y_face + h_face, x_face:x_face + w_face]
                )
                res = fs.predict_embedded_euclidean_distance(np.array([emb_test]), np.array(emb_train), y_train)
                cv2.rectangle(
                    frame,
                    (face_coord[0], face_coord[1]),
                    (face_coord[0] + face_coord[2], face_coord[1] + face_coord[3]),
                    (0, 0, 255) if res[0] is None else (255, 0, 0),
                    6
                )
            cv2.imshow('frame', frame)
            print("--- %s seconds ---" % (time.time() - start_time))
            summ = summ + time.time() - start_time

    cap.release()
    cv2.destroyAllWindows()
    print(summ/number)