#This creates a pixelated face when detected, ensuring privacy.
import cv2

def auto_pixelate_faces(image_path, output_path, pixel_size=10):
    # Load the pre-trained Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Pixelate each detected face
    for (x, y, w, h) in faces:
        roi = img[y:y+h, x:x+w]                                                         #roi = Region of Interest
        # Shrink
        roi = cv2.resize(roi, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
        # Enlarge back (pixelated)
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
        img[y:y+h, x:x+w] = roi

    #This saves the output image
    cv2.imwrite(output_path, img)
    print(f"Saved pixelated image to {output_path}")

# Example usage
# auto_pixelate_faces('group_photo.jpg', 'masked_output.jpg')
