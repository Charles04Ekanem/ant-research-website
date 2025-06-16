#Uyom-Ndise, This creates a lower resolution image for robust model training

import cv2

def add_jpeg_artifacts(input_image_path, output_path, quality=10):
    img = cv2.imread(input_image_path)
    cv2.imwrite(output_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

# add_jpeg_artifacts('image.jpg', 'noisy_image.jpg')