from pathlib import Path
import cv2 

SCRIPT_DIR = Path(__file__).resolve().parent

image_path = SCRIPT_DIR/"src"/"image1.jpg"

try: 
    image = cv2.imread(str(image_path))
    cv2.imshow("Display Window", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e: 
    print(e)