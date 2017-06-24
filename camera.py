from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime
from signal import pause

def toggle_Record(btn):
    #setup
    camera = PiCamera()
    print("recording")
    #config
    camera.resolution = (1280,720)
    camera.framerate = 60
    camera.exposure_mode = 'antishake'
    camera.video_stabilization = True
    filename = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M:%S.h264')
    camera.annotate_text = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print("look")
    camera.start_preview()
    print("cam start")
    camera.start_recording('/home/pi/Desktop/videos/'+filename)
    btn.wait_for_press()
    print("cam stop")
    camera.stop_recording()
    print("dont look")
    camera.stop_preview()
    camera.close()

#init
button = Button(17)
print("button init")
while True:
    button.wait_for_press()
    print("calling record fn")
    toggle_Record(button)
    sleep(3)
    print("end")
 



#camera.start_preview()
#button.wait_for_press()
#camera.capture('/home/pi/Desktop/image.jpg')
#camera.stop_preview()
