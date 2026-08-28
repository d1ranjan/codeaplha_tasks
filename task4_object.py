import cv2
import time
from ultralytics import YOLO




model = YOLO("yolo11n.pt")



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# Set webcam resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)




recording = False
video_writer = None



previous_time = 0




while True:

    # Read frame from webcam
    success, frame = cap.read()

    if not success:
        print("Error: Could not read frame.")
        break




    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )




    annotated_frame = results[0].plot()




    object_count = 0

    if results[0].boxes is not None:
        object_count = len(results[0].boxes)



    current_time = time.time()

    if previous_time != 0:
        fps = 1 / (current_time - previous_time)
    else:
        fps = 0

    previous_time = current_time



    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.1f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )




    cv2.putText(
        annotated_frame,
        f"Objects: {object_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )




    if recording:

        cv2.putText(
            annotated_frame,
            "RECORDING",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )




    if recording and video_writer is not None:

        video_writer.write(
            annotated_frame
        )


 

    cv2.imshow(
        "YOLO Object Detection and Tracking",
        annotated_frame
    )




    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):
        break


  
    elif key == ord("r"):

        if not recording:

            
            width = int(
                cap.get(
                    cv2.CAP_PROP_FRAME_WIDTH
                )
            )

            height = int(
                cap.get(
                    cv2.CAP_PROP_FRAME_HEIGHT
                )
            )

           
            fourcc = cv2.VideoWriter_fourcc(
                *"mp4v"
            )

           
            video_writer = cv2.VideoWriter(
                "tracked_output.mp4",
                fourcc,
                20.0,
                (width, height)
            )

            recording = True

            print(
                "Recording started."
            )

        else:

            recording = False

            if video_writer is not None:
                video_writer.release()
                video_writer = None

            print(
                "Recording stopped."
            )




cap.release()

if video_writer is not None:
    video_writer.release()

cv2.destroyAllWindows()

print("Program ended.")