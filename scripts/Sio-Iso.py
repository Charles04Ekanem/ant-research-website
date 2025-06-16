#Sio-Iso (This Blurs faces in Videos)

def blur_faces_in_video(input_video, output_video):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, cap.get(5), (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            blurred = cv2.GaussianBlur(roi, (51, 51), 30)
            frame[y:y+h, x:x+w] = blurred
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Done blurring faces!")

# blur_faces_in_video('input.mp4', 'output_blurred.avi')...accepts input videos as .mp4 file, returns output as .avi file