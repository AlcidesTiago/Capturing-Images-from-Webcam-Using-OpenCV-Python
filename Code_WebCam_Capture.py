import cv2
from time import sleep
import os

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:

    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each frame
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):

            cv2.imwrite(os.path.join('/Capturing_Images_From_WebCam/Data/Output',
                                     'saved_img.jpg'), frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray, (30, 30))
            print("Resized...")
            img_resized = cv2.imwrite(os.path.join('/Capturing_Images_From_WebCam/Data/Output',
                                                   'saved_img-final.jpg'), img_)
            print("Image saved!")

            break

        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except KeyboardInterrupt:
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
