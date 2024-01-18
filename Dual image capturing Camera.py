import cv2
# Open the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default camera index

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Unable to open the webcam")
    exit()

# Capture and display frames until the user presses a key
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Check if the user pressed the 's' key to save the image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the image
        cv2.imwrite("Captured Image RGB", frame)

        # Convert to grayscale and save the image
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("Captured Image Grayscale", gray_image)

        # Display the grayscale image
        cv2.imshow('Grayscale Image', gray_image)
        print("Image saved successfully")
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
