import cv2
import glob

# img1 = cv2.imread("galaxy.jpg", 0)
# img2 = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 0)
# img3 = cv2.imread("Lighthouse.jpg", 0)
# img4 = cv2.imread("Moon sinking, sun rising.jpg", 0)

# resize_image1 = cv2.resize(img1, (100, 100))
# resize_image2 = cv2.resize(img2, (100, 100))
# resize_image3 = cv2.resize(img3, (100, 100))
# resize_image4 = cv2.resize(img4, (100, 100))


# cv2.imwrite("img1-100-100.jpg", resize_image1)
# cv2.imwrite("img2-100-100.jpg", resize_image2)
# cv2.imwrite("img3-100-100.jpg", resize_image3)
# cv2.imwrite("img4-100-100.jpg", resize_image4)

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re)