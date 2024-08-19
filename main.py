from adafruit_servokit import ServoKit 
from picamera import PiCamera
from picamera.array import PiRGBArray
import time, math, cv2

#variables 
servo_min_angle = 0 
servo_max_angle = 180
servo_default_angle = 60
min_pulse = 500
max_pulse = 2500
servos = 7 #number of servos 

#Initialization 
kit = ServoKit(channels=16)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

def camera_init():
    # Allow the camera to warm up
    time.sleep(0.1)
    
    # Start the camera preview
    camera.start_preview()
    
    # Capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        
        # Process the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame", gray)
        
        # Clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def camera_stop():
    camera.stop_preview()
    cv2.destroyAllWindows() # release resources 
            

#set pulse width for all servos
def set_servo_pulse(pulse):
    for i in range(7): #7 servos 
        kit.servo[i].set_pulse_width_range(500, 2500)

def turn_servo(servo, angle): 
    kit.servo[servo].angle = angle

def default_servos(servo, angle): 
    for servo in servos:
        kit.servo[servos].angle = servo_default_angle 

def warm_up(min_pulse, max_pulse): 
    set_servo_pulse(min_pulse, max_pulse)
    time.sleep(1) #camera warm-up time

def cooling_down():
    camera_stop()
    #add more closing defaults (eg: set motors to default positions)


