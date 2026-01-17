import cv2
from ultralytics import YOLO

def process_image(
    image_path,
    output_path,
    model_path="yolov8n.pt",
    confidence_threshold=0.5
):
    # Load model
    model = YOLO(model_path)

    # Read image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid image format")

    # Run inference
    results = model(image)

    # Extract detections
    for result in results:
        boxes = result.boxes
        for box in boxes:
            conf = float(box.conf[0])
            if conf < confidence_threshold:
                continue

            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            label = f"{class_name}: {conf:.2f}"
            cv2.putText(
                image,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    # Save output
    cv2.imwrite(output_path, image)
