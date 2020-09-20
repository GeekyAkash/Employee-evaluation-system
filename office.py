;==========================================
; Title:  Employee evaluation system
; Author: Akash Singh
; Date:   20 Sep 2020
;========================================

import pyautogui
from tkinter import *
from threading import Thread
import cv2
import schedule
import time
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name="abcfjkjk9",
    api_key="5697946464979779",
    api_secret="UablyedfbFhjdowQncl-f4dfaf"
)


def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'static/Screenshot/{}.png'.format(time.strftime("%d-%m-%Y %H:%M")))
    cloudinary.uploader.upload('static/Screenshot/{}.png'.format(time.strftime("%d-%m-%Y %H:%M")),
                               public_id='{}'.format(time.strftime("%d-%m-%Y %H:%M")),
                               folder="Akash/screenshot/")
    video_cap()


def video_cap():
    global user_frame
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        for i in range(10):
            ret, frame = videoCaptureObject.read()
            user_frame = frame

        cv2.imwrite("static/user_image/{}.jpg".format(time.strftime("%d-%m-%Y %H:%M")), user_frame)
        cloudinary.uploader.upload('static/user_image/{}.jpg'.format(time.strftime("%d-%m-%Y %H:%M")),
                                   public_id='{}'.format(time.strftime("%d-%m-%Y %H:%M")),
                                   folder="Akash/user_photo/")
        result = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        videoCaptureObject.release()
        cv2.destroyAllWindows()


def control():
    schedule.every(10).seconds.do(takeScreenshot)
    while True:
        schedule.run_pending()
        if stop == 1:
            root.quit()
            break


def start():
    global stop
    stop = 0
    t = Thread(target=control)
    t.start()
    b1.config(state=DISABLED)


def stop():
    global stop
    stop = 1


if __name__ == '__main__':
    root = Tk()
    root.title("Employee evaluation system")
    root.geometry("500x200")
    Label(root, text="Welcome to Employee evaluation system").pack()
    b1 = Button(root, text="Start Recording", command=start, bg='green')
    b1.pack()
    b2 = Button(root, text="Stop Recording", command=stop, bg='green')
    b2.pack()
    root.mainloop()
