import os
import cv2

cropped_images_path = "./Cropped"

csv_file = open("./Cropped_Images_Actual.csv", "w")

for image in os.listdir(cropped_images_path):
    if image.endswith(".png"):
        image_path = os.path.join(cropped_images_path, image)
        while(1):
            cv2.imshow("Image", cv2.resize(cv2.imread(image_path), (512, 512)))
            c = cv2.waitKey(0) % 256
            if c == ord('r'):
                csv_file.write(image + "," + "river" + "\n")
                cv2.destroyAllWindows()
                break
            elif c == ord('l'):
                csv_file.write(image + "," + "lake" + "\n")
                cv2.destroyAllWindows()
                break
            else:
                print("Invalid input")

csv_file.close()
