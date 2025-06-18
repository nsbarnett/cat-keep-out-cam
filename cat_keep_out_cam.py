import cv2

"""
    Purpose: I have two beautiful cats, Miso, and Mei Mei. They love to jump on the kitchen counter and snag
    a bite of whatever they cna find when I'm not around (they are very sneaky). This security system will
    detect whether Miso or his little sister is somewhere they aren't supposed to be, and play a loud sound
    to deter their rebellious actions.
    
    I will place the system where it can view an area there shoudl be no cats present. If a cat is in the frame,
    the alarm will sound!
    
    I will 3D print compnents to hold a pi cam and rasberri pi, where the cat detection model will be implemented
    and running at all times.

    I will be using PyTorch for this project to familarize myself with the library.

"""

def main():
    cam = cv2.VideoCapture(0)  # open the default camera (usually the first one)
    """ Initialize value for cat present as 'False'. Whether a cat is present will be determined
        in the running video loop via a CNN (Convolutional Neural Network). CNNs specialize in
        image classification with efficient pattern detection (i.e. edges, textures, shapes, and objects)"""
    
    cat_present = False # initialize value for cat present. This will be determined in the running video loop via a CNN.

    while True:
        _, frame = cam.read() # read frame by frame
        if not _:
            break
        
        cv2.imshow("Camera Feed", frame) # display camera feed

        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()