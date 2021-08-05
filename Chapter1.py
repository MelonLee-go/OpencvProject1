import cv2
import numpy as np

# detect shapes


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if 250 < area < 20000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            # use the rate of width and height to distinct rec and square
            if objCor == 3:
                ObjectType = "Tri"
            elif objCor == 4:
                ObjectType = "Rec"
            elif objCor == 8:
                ObjectType = "Cir"
            else:
                ObjectType = "None"
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, ObjectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX,
                        0.5, (0, 0, 0), 2)


path = "Resources/Shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
# detect corner point
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)
imgStack = stackImages(1, ([img, imgGray, imgBlur],
                           [imgCanny, imgContour, imgBlank]))
cv2.imshow("Image", imgStack)
cv2.waitKey(0)







# def empty(a):
#     pass
#
# path = 'Resources/1.bmp'
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 720, 360,)
# # start angle? end angle
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 86, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 44, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 249, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 249, 255, empty)
# # track bars
#
# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#     print(h_min, h_max, s_min, s_max, v_min, v_max)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
#     imgResult = cv2.bitwise_and(img, img, mask=mask)
#
#     cv2.imshow("Image", img)
#     cv2.imshow("Mask", mask)
#     cv2.imshow("HSV", imgHSV)
#     cv2.imshow("RES", imgResult)
#     cv2.waitKey(1)



# # join pictures
# img = cv2.imread("Resources/Avatar.jpg")
#
#
# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
# kernel = np.ones((5, 5), np.uint8)
# imgCanny = cv2.Canny(img, 150, 200)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# imgStack = stackImages(0.5, ([imgGray, imgCanny, imgBlur],
#                              [imgDialation, imgEroded, img]))
# cv2.imshow("Image", imgStack)
# cv2.waitKey(0)


# # join pictures (BASIC)
# img = cv2.imread("Resources/Avatar.jpg")
# # horizontal stack function
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))
# # NEED SAME NUMBER OF CHANNELS
# cv2.imshow("Vertical", imgVer)
# cv2.imshow("Horizontal", imgHor)
# cv2.waitKey(0)





# # Warp Perspective
# img = cv2.imread("Resources/Avatar.jpg")
# width, height = 250, 350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))
#
# cv2.imshow("Image", img)
# cv2.imshow("Output", imgOutput)
# cv2.waitKey(0)




# # shapes and texts
# # 0:black 3:channel uint8 0-255
# img = np.zeros((512, 512, 3), np.uint8)
# # print(img.shape)
# # img[200:300, 100:300] = 255, 0, 0
#
# # p1: picture p2:start_pos p3:end_pos p4:color p5:thickness
# # width height
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (300, 50), 30, (255, 255, 0), 5)
# cv2.putText(img, "OPEN CV", (300, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
# cv2.imshow("img", img)
# cv2.waitKey(0)





# # resize img & crop image
# img = cv2.imread("Resources/Avatar.jpg")
# # get the size of this picture
# print(img.shape)
# # (720, 720, 3) height width id_of_the_channel BGR
# imgResize = cv2.resize(img, (1080, 1080))
# print(imgResize.shape)
# # width height
# imgCropped = img[0:300, 200:600]
# # height width
# # start point : end point
# cv2.imshow("Img", img)
# cv2.imshow("ImgResize", imgResize)
# cv2.imshow("ImgCropped", imgCropped)
#
# cv2.waitKey(0)






# img = cv2.imread("Resources/Avatar.jpg")
# # define all of the values 1
# # from 0-255
# kernel = np.ones((5, 5), np.uint8)
# # convert color space
# # p1:picture p2:color space
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Blur
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# # detect the edges
# imgCanny = cv2.Canny(img, 150, 200)
# # increase the thickness of our edge
# # matrices
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# # make it thinner
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
# cv2.imshow("Dialation", imgDialation)
# cv2.imshow("Eroded", imgCanny)
# cv2.waitKey(0)





# # create webcam obj
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# # width
# cap.set(4, 480)
# # height
# cap.set(10, 100)
# # brightness
#
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




# cap = cv2.VideoCapture("Resources/testVideo.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




# img = cv2.imread("Resources/Avatar.jpg")
# # reading an image
# cv2.imshow("Output", img)
# cv2.waitKey(0)
# # display the img
# # p1:the name of the window p2:which img we want to display


