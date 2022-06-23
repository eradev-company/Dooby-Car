from model import *


# img = cv2.imread('dataset/0/1.jpg')
# print(predict(img))

# print(img)
# plt.imshow(img)
# plt.show()
# img = cv2.imread('red.jpg')
# img = cv2.imread('stop.jpeg')

cap = cv2.VideoCapture(-1)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

# # Image
# for classId, conf, box in zip(class_ids.flatten(), confs.flatten(), bbox):
#     cv2.rectangle(img, box, 0, 255, 0, 3)
#     cv2.putText(img, class_names[classId-1].upper(), (box[0]+10, box[1]+30),
#                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(img, str(round(conf*100, 2)), (box[0]+200, box[1]+30),
#                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

#     if class_names[classId-1] == 'traffic light':
#         tl_classes = ["None", "RED", "GREEN", "YELLOW"]
#         # Detect type
#         tl_pred, _, _, _ = detect(img)
#         cv2.putText(img, tl_classes[tl_pred], (20, 20),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,  cv2.LINE_AA)


# Video capture
while True:
    success, img = cap.read()
    class_name = predict(img)
    print(class_name)

    # if len(classIds) != 0:
    #     for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
    #         cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
    #         cv2.putText(img, class_names[classId-1].upper(), (box[0]+10, box[1]+30),
    #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    #         cv2.putText(img, str(round(confidence*100, 2)), (box[0]+200, box[1]+30),
    #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('frame', img)
    cv2.waitKey(1)


# cv2.imshow('Output', img)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
