import pywhatkit as kit
import cv2
print("How do you want to continue?\n1.Text\n2.Text File")
ch=int(input("Enter Your Choice: "))

if ch==1:
    f=input("Enter Text Here:")
    kit.text_to_handwriting(f, save_to="handwriting.png")
elif ch==2:
    a=input("Enter file location or Drag here: ")
    if a[0]=="'" or a[0]=='"':
        file=a[1:len(a)-1]
    else:
        file=a
    f=open(file,"r")
    kit.text_to_handwriting(f.read(), save_to="handwriting.png")
else:
    print("Error")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()