import cv2


def photoCapture(app):
    camera = cv2.VideoCapture(0)

    cv2.namedWindow("Photo Capture")

    img_counter = 0

    while True:
        success, frame = camera.read()
        capturedFrame = frame.copy()
        if not success:
            print("Failed to Grab Frame!")
            break

        text = "Press Space to Save Image"

        # get vcap property
        width = int(camera.get(3))  # float `width`
        height = int(camera.get(4))  # float `height`
        position = (width - 350, height - 25)
        scale = 0.75
        color = (0, 0, 255)
        thickness = 2
        cv2.putText(
            frame,
            text,
            position,
            cv2.FONT_HERSHEY_SIMPLEX,
            scale,
            color,
            thickness,
            cv2.LINE_AA,
        )
        cv2.imshow("Photo Capture", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            imageName = f"./images/captured_image_{img_counter}.png"
            cv2.imwrite(imageName, capturedFrame)
            print(f"{imageName} written!")
            img_counter += 1
            break

    camera.release()

    cv2.destroyAllWindows()

    app.show_frame("SendPhotoToEmail", imageName)
