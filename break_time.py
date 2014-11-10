import time
import webbrowser

print("Program started on"+time.ctime())
i=3
while (i>0):
    time.sleep(10*60)
    print("Video Started on"+time.ctime())    
    webbrowser.open("https://www.youtube.com/watch?v=APJxwxZuA0E")
    i=i-1
