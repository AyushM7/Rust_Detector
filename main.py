# Author: Ayush Mendhe
# Date created: 12/24/2022

import cv2

# Initialize the video capture object with the device index of the external webcam
# Initialize to 0 if using computer webcam
# Initialize to 1 if using external webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV range for detecting rust color
    lower = (5, 100, 100)  # Adjust these values as needed
    upper = (20, 255, 255)

    # Create a mask for the rust color
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around the detected rust-colored areas
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Rust Detector', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
