
import cv2
import dropbox
import time
import random

# image1=cv2.imread('Inkedicon_LI.jpg')
# image=cv2.imshow('image',image1 )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(image)

# def takeSnapshot():
#     imageCapture=cv2.VideoCapture(0)
#     result=True
#     while(result):
#         check,frame=imageCapture.read()
#         print(check)
#         cv2.imwrite('image2.png',frame)
#         result=False
#         imageCapture.release()
#         cv2.destroyAllWindows()

# takeSnapshot()
startTime=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    imageCapture=cv2.VideoCapture(0)
    result=True
    while(result):
        check,frame=imageCapture.read()
        print(check)
        imageName="image"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
        return imageName
        imageCapture.release()
        cv2.destroyAllWindows()

def UploadFile(imageName):
    accessToken='4e3mtYy3ypYAAAAAAAAAAcHMvQim-JN4q8wZqCfLfYqmLnq5jh9bMz5jzJC-TzKJ'
    file=imageName
    fileFrom=file
    fileTo='/newFolder/'+(imageName)
    db=dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb')as f:
        db.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded Successfully")
        
def Time():
    while(True):
        if (time.time()-startTime>=5):
            image=takeSnapshot()
            UploadFile(image)

Time()