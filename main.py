from src.image_processor import process_image
from src.video_processor import process_video
import os

def main():
    # input_image = "test.jpg"
    # output_dir = "outputs/images"
    # os.makedirs(output_dir, exist_ok=True)

    # output_image = os.path.join(output_dir, "result.jpg")

    # process_image(
    #     image_path=input_image,
    #     output_path=output_image,
    #     confidence_threshold=0.5
    # )

    # print("Image processed and saved successfully")
    process_video(source=0, confidence_threshold=0.5)

if __name__ == "__main__":
    main()
