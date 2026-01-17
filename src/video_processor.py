import cv2
from ultralytics import YOLO

def process_video(
        source = 0,
        model_path="yolov8n.pt",
        confidence_threshold= 0.5,
):
    model = YOLO(model_path)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError("Failed to open video source") 
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                conf = float(box.conf[0])
                if conf < confidence_threshold:
                    continue

                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]

                x1,y1,x2,y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
                label = f"{class_name}:{conf:2f}"
                cv2.putText(frame,label,(x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

        cv2.imshow("Real-Time Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows()
