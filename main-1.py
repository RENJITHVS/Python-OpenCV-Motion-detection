import cv2

def motion_detection():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        grey = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        # blur = cv2.GaussianBlur(grey, (5, 5), 0)
        _, threh = cv2.threshold(grey, 20, 255, cv2.THRESH_BINARY)
        dilation = cv2.dilate(threh, None, iterations=3)
        contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0,255,0),2)
        for c in contours:
            if cv2.contourArea(c) < 3000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('ren', frame1)


if __name__ == "__main__":
    motion_detection()
