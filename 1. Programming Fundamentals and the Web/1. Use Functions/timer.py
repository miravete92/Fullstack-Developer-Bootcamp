import webbrowser
import time

num_iterarions = 3
current_iteration = 0

print("Aplication start time: "+time.ctime())
while (current_iteration < num_iterarions):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=a366snHMltM")
    current_iteration=current_iteration+1
    
