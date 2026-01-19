import os
from src.image_processor import process_image
from src.video_processor import process_video

def run_image_mode():
    """
    Runs object detection on a single image.
    """
    input_image = "test.jpg"
    output_dir = "outputs/images"
    os.makedirs(output_dir, exist_ok=True)

    output_image = os.path.join(output_dir, "result.jpg")

    process_image(
        image_path=input_image,
        output_path=output_image,
        confidence_threshold=0.5
    )

    print("[INFO] Image processing completed successfully")


def run_webcam_mode():
    """
    Runs real-time object detection using webcam.
    Press 'Q' to exit.
    """
    print("[INFO] Starting webcam detection. Press 'Q' to exit.")
    process_video(
        source=0,
        confidence_threshold=0.5
    )


def main():
    """
    Entry point of the application.
    Selects execution mode.
    """

    MODE = "webcam"  # options: "image", "webcam"

    if MODE == "image":
        run_image_mode()
    elif MODE == "webcam":
        run_webcam_mode()
    else:
        raise ValueError("Invalid MODE selected. Use 'image' or 'webcam'.")


if __name__ == "__main__":
    main()
