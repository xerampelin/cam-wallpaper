import numpy as np
import cv2

imagey = 1920
imagex = 1440
cap = cv2.VideoCapture(0)
flatimage = np.zeros((imagex, imagey))
colindex = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame

    columns = frame[0].size
    middlecol = int(columns/2)
    flatimage[0:,colindex] = frame[0:,middlecol]
    colindex += 1
    cv2.imshow('frame',flatimage)
    if colindex >= imagex:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()