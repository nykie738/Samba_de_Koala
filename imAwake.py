import tkinter as tk
#from datetime import datetime
import time
from PIL import Image, ImageTk
import numpy as np

def animate_gif(label, frames, delay, frame_index=0):
    frame = frames[frame_index]
    label.configure(image=frame)
    frame_index = (frame_index + 1) % len(frames)
    label.after(delay, animate_gif, label, frames, delay, frame_index)

# Added for quality of life improvement
def terminate_program(event=None):
    finT = time.time()
    elapse = finT - iniT
    if elapse < 60:
        print(f"time: {elapse} s")
    elif elapse > 60 and elapse < 3600:
        elapse2 = np.trunc(elapse / 60)
        remain = elapse - (60 * elapse2)
        print(f"time: {elapse2} m, {remain} s")
    else:
        elapse3 = np.trunc(elapse / 3600)
        checkE = elapse - (3600 * elapse3)
        remain2 = 0.0
        remain3 = 0
        if checkE > 60:
            remain2 = np.trunc(checkE / 60)
            remain3 = checkE - (60 * remain2)
            print(f"time: {elapse3} hr, {remain2} m, {remain3} s")
        else:
            print(f"time: {elapse3} hr, {remain2} m, {checkE} s")
    root.destroy()
    exit()

def run_koala():
    while True:
        #current_time = datetime.now().strftime("%H:%M")
        doro = 1
        if doro == 1:
            global root
            global iniT
            root = tk.Tk()
            root.title("YOU ARE LATE")
            root.attributes("-fullscreen", True)
            iniT = time.time()


            root.bind('<Control-w>', terminate_program)
            root.bind('<Control-q>', terminate_program)
            root.bind('<Escape>', terminate_program)

            label = tk.Label(root, text="DONT MIND ME IM JUST DANCING", font=("Helvetica", 64))
            label.pack(padx=20, pady=20)

            # make sure that the gif and the python code are in the same directory
            gif_path = "./taniecK.gif" 
            gif_image = Image.open(gif_path)
            gif_frames = []

            try:
                while True:
                    frame = ImageTk.PhotoImage(gif_image.copy().convert("RGBA"))
                    gif_frames.append(frame)
                    gif_image.seek(len(gif_frames))  # next frame
            except EOFError:
                pass

            delay = int(gif_image.info['duration'])
            
            gif_label = tk.Label(root)
            gif_label.pack()

            label = tk.Label(root, text="絶賛 寝坊中!!!", font=("Helvetica", 64))
            label.pack(padx=20, pady=20)
            
            animate_gif(gif_label, gif_frames, delay)

            root.mainloop()
            break
        #time.sleep(60)  # 1 minute halt before checking the time again

if __name__ == "__main__":
    run_koala()