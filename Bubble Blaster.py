import tkinter, random, threading, time
from tkinter import *

def collision(canvas, a, b):
    bbox1 = canvas.bbox(a)
    bbox2 = canvas.bbox(b)
    if bbox1[2] > bbox2[0] and bbox1[0] <=bbox2[2] and bbox1[3] >= bbox2[1] and bbox1[1] <= bbox2[3]:
        return True
    else:
        return False
def submit(*args):
    window.update()
    global name
    if len(entry.get()) > 20:
        label3.config(text="Enter a shorter name")
    elif len(entry.get()) > 0:
        window.unbind("<Return>")
        name = entry.get().title()
        frame2.pack_forget()
        frame3.pack(fill=tkinter.BOTH, expand=True)
def delete():
    window.update()
    entry.delete(0, END)
def play():
    global rounds, health
    window.update()
    rounds = 10
    health = 100
    frame1.pack_forget()
    frame2.pack()
    enter = window.bind("<Return>", submit)
def Continue():
    global site, rounds, health, name, health_bar, timer, score, sitex, sitey, site_frame, site_canvas, frame1, frame2, frame3, frame4, frame5, frame6, canvas, site_window, gunx, gun, line, gameover
    window.update()
    try:
        frame6.pack_forget()
        frame6.delete("all")
    except:
        pass
    try:
        canvas.destroy()
    except:
        pass
    frame4.pack(fill=tkinter.BOTH, expand=True)
    canvas = Canvas(frame4, bg="#323232", bd=0)
    frame6 = Frame(canvas, bg="#000")
    frame6.pack_forget()
    canvas.update()
    canvas.pack(fill=tkinter.BOTH, expand=True)
    sitex = (window.winfo_width()/2)-25
    sitey = (window.winfo_height()/2)-25
    site_frame = Frame(canvas, bg="#323232", bd=0)
    site_frame.pack(padx=sitex, pady=sitey, expand=False, anchor = "nw")
    site_canvas = Canvas(site_frame, bg="#323232", width=50, height=50, bd=0)
    site_canvas.pack(expand=True, anchor = "nw")
    site_window = canvas.create_window((sitex, sitey), window=site_frame, anchor="nw")
    site = site_canvas.create_oval((0, 0, 50, 50), fill="", width=5, outline="#F00")
    site_canvas.create_line((25, 0, 25, 50), fill="#F00", width=5)
    site_canvas.create_line((0, 25, 50, 25), fill="#F00", width=5)
    gunx = window.winfo_width()*.55
    gameover = False
    spawning = threading.Thread(target=spawn_enemy)
    spawning2 = threading.Thread(target=spawn_enemy)
    clock_thread = threading.Thread(target=clock)
    enemy_moving_thread = threading.Thread(target=move_enemy)
    rounds = 10
    timer = 60
    score = 0
    window.bind("<KeyRelease-space>", fire)
    window.bind("<Return>", reload)
    window.bind("<Up>", aim_up)
    window.bind("<Down>", aim_down)
    window.bind("<Left>", aim_left)
    window.bind("<Right>", aim_right)
    label11 = Label(frame6)
    label11.config(font=("Impact", 150), bg="#000", fg="#F00", text="Game Over!")
    label11.pack(side=TOP)
    label12 = Label(frame6)
    label12.config(font=("Impact", 20), bg="#000", fg="#F00", text=f"{insults[random.randint(0, 21)]}")
    label12.pack(side=TOP)
    Button((frame6), text="Play again", command=Continue, font=("Impact", 35), fg = "#F00", bg = "#000", state = NORMAL).pack()
    Button((frame6), text="Quit", command=EXIT, font=("Impact", 35), fg = "#F00", bg = "#000", state = NORMAL).pack()
    gun = canvas.create_polygon(gunx, window.winfo_height()*.7, gunx + 50, window.winfo_height()*.7, gunx + 125, window.winfo_height(), gunx + 75, window.winfo_height(), fill="#000")
    line = canvas.create_line(((gunx + 25, window.winfo_height()*.7, gunx + 100, window.winfo_height())), width=5, fill="#222")
    health_bar = Label(canvas)
    health_bar.config(font=("Impact", 15), bg = "#323232", fg = "#F00", text = f"{name}: time:{timer} rounds:{rounds} points:{score}")
    health_bar.pack(side=BOTTOM, fill=None, anchor = "nw")
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    spawning.start()
    spawning2.start()
    clock_thread.start()
    enemy_moving_thread.start()
    canvas.update_idletasks()
    canvas.update()
def fire(*args):
    global site, flash1, flash2, flash3, rounds, targets, score, gunx, collision, gameover
    window.update()
    try:
        stop_flash()
    except:
        pass
    if rounds > 0:
        for target in targets:
            try:
                collide = collision(canvas, site, target)
            except TypeError:
                collide = False
            if collide == True:
                if canvas.itemcget(target, "fill")=="#B00":
                    gameover = True
                    game_over()
                else:
                    score += 10
                canvas.delete(target)
        rounds -= 1
        flash1 = canvas.create_line(gunx - 50, window.winfo_height()*.7, gunx - 130, window.winfo_height()*.5, width=10, fill="#FA0")
        flash2 = canvas.create_line(gunx + 50, window.winfo_height()*.7, gunx + 130, window.winfo_height()*.5, width=10, fill="#FA0")
        flash3 = canvas.create_line(gunx, window.winfo_height()*.7, gunx, window.winfo_height()*.5, width=10, fill="#FA0")
    canvas.after(100, stop_flash)
def stop_flash():
    global flash1, flash2, flash3
    canvas.delete(flash1, flash2, flash3)
def spawn_enemy():
    global enemy_canvas, enemy_frame, health_bar, name, targets, score, rounds, timer, gameover
    targets = []
    while gameover == False:
        window.update()
        canvas.update()
        health_bar.config(text = f"{name}: time:{timer} rounds:{rounds} points:{score}")
        number = random.randint(1, 6)
        if number == 1 or number == 2 or number == 3:
            color = "#B00"
        elif number == 3:
            color = "#0F0"
        elif number == 4:
            color = "#00F"
        elif number == 5:
            color = "#FF0"
        elif number == 6:
            color = "#0FF"
        time.sleep(random.randint(0, 2))
        x = random.randint(0, window.winfo_width())
        y = random.randint(0 , window. winfo_height())
        number = random.randint(150, 200)
        targets.append(canvas.create_oval((x, y), (x+number, y+number), fill=color))
        canvas.update_idletasks()
        canvas.update()
        time.sleep((random.randint(1, 100))/100)
def move_enemy():
    global targets, gameover
    while timer > 0 and gameover == False:
        window.update()
        time.sleep(.01)
        for target in targets:
            canvas.move(target, random.randint(-100, 100), random.randint(-100, 100))
def clock():
    global timer, health_bar, insult, targets, gameover
    while gameover == False:
        if timer < 1:
            label9.config(text=f"Your score: {score}")
            number = random.randint(0, 21)
            insult = insults[number]
            label10.config(text=f"{insult}")
            frame4.pack_forget()
            canvas.destroy()
            frame5.pack(expand=True, padx=0, pady=0)
            return None
        else:
            canvas.update_idletasks()
            canvas.update()
            time.sleep(.5)
            health_bar.config(text = f"{name}: time:{timer} rounds:{rounds} points:{score}")
            canvas.update_idletasks()
            canvas.update()
            time.sleep(.5)
            health_bar.config(text = f"{name}: time:{timer} rounds:{rounds} points:{score}")
            timer -= 1
def aim_up(*args):
    global sitey, site, site_window, gunx, gun, line
    if sitey > 25:
        sitey -= 30
        canvas.move(site_window, 0, -30)
    canvas.coords(gun, gunx, window.winfo_height()*.7, gunx + 50, window.winfo_height()*.7, gunx + 125, window.winfo_height(), gunx + 75, window.winfo_height())
    canvas.coords(line, (gunx + 25, window.winfo_height()*.7, gunx + 100, window.winfo_height()))
    canvas.update()
def aim_down(*args):
    global sitey, site, site_window, gunx, line
    window.update()
    if sitey < window.winfo_height()-30:
        sitey += 30
        canvas.move(site_window, 0, 30)
    canvas.coords(gun, gunx, window.winfo_height()*.7, gunx + 50, window.winfo_height()*.7, gunx + 125, window.winfo_height(), gunx + 75, window.winfo_height())
    canvas.coords(line, (gunx + 25, window.winfo_height()*.7, gunx + 100, window.winfo_height()))
    canvas.update()
def aim_right(*args):
    global sitex, site, site_window, gunx, line
    if sitex < window.winfo_width()-30:
        sitex += 30
        gunx += 30
        canvas.move(site_window, 30, 0)
    canvas.coords(gun, gunx, window.winfo_height()*.7, gunx + 50, window.winfo_height()*.7, gunx + 125, window.winfo_height(), gunx + 75, window.winfo_height())
    canvas.coords(line, (gunx + 25, window.winfo_height()*.7, gunx + 100, window.winfo_height()))
    canvas.update()
def aim_left(*args):
    global sitex, site, site_window, gunx, line
    if sitex > 25:
        sitex -= 30
        gunx -= 30
        canvas.move(site_window, -30, 0)
    canvas.coords(gun, gunx, window.winfo_height()*.7, gunx + 50, window.winfo_height()*.7, gunx + 125, window.winfo_height(), gunx + 75, window.winfo_height())
    canvas.coords(line, (gunx + 25, window.winfo_height()*.7, gunx + 100, window.winfo_height()))
    canvas.update()
def reload(*args):
    global rounds
    rounds = 10
def EXIT():
    window.destroy()
    exit()
def game_over():
    global canvas, site_canvas, frame1, frame2, frame3, frame4, frame6, health_bar
    canvas.configure(bg="#000")
    canvas.delete("health_bar")
    canvas.delete("all")
    site_canvas.destroy()
    frame4.pack_forget
    frame3.pack_forget()
    frame2.pack_forget()
    frame1.pack_forget()
    frame6.pack(expand=True, fill="both")

window = Tk()
window.state("zoomed")
window.config(bg = "#000", bd=0)
window.title("Bubble Blaster")
insults = ["You know, you can't nap and shoot at the same time.", "That was pathetic.", "You snooze, you lose.", "Congragualations! You got a new low score!", "Careful, You almost killed your computer! It's not meant for that level of incompetence!", "Were you born yesterday?", "Nice try! Keep trying, you might hit somthing someday!", "Great job! Just try aiming next time.", "There's this great new thing on your gun called a sight. You should try using it sometime.", "Were your eyes closed?", "Why don't you try again with a blindfold on? It won't make your score any worse.", "Nice try! But next time, try using the sight.", "Use the force...", "Wow, those bubbles sure put up a fight!", "You can open your eyes now. Just don't look at your score.", "Do you even know how to play this game?", "Have you never played a video game before?", "You should learn how to push a button, then try again.", "Are you blind?", "Whomp whomp whaaaaaa...", "OUCH!", "WOW! You're only a million points away from a million points!"]
frame1 = Frame(window, bg="#000")
frame2 = Frame(window, bg="#000")
frame3 = Frame(window, bg="#000")
frame4 = Frame(window, bg="#323232")
frame5 = Frame(window, bg="#000")

label = Label(frame1)
label.config(font = ("Impact", 150), bg = "#000", fg = "#F00", text = "Bubble Blaster", width = 50)
label.pack(side = TOP)
label2 = Label(frame1)
label2.config(font = ("Impact", 50), bg = "#000", fg = "#F00", text = "Push the button to play.", width = 50)
label2.pack(side = TOP)
Button((frame1), text="Play", command=play, font = ("Impact", 175), fg = "#F00", bg = "#545454", state = NORMAL).pack()

label3 = Label(frame2)
label3.config(font = ("Impact", 50), bg = "#000", fg = "#F00", text = "What is your name?", width = 50)
label3.pack(side = TOP)
entry = Entry(frame2)
entry.config(font = ("Impact", 50), bg = "#000", fg = "#F00")
entry.config(width = 50)
entry.pack()
Button((frame2), text="Submit", command=submit, font = ("Impact", 20), fg = "#F00", bg = "#000", state = NORMAL).pack(side=RIGHT)
Button((frame2), text="Delete", command=delete, font = ("Impact", 20), fg = "#F00", bg = "#000", state = NORMAL).pack(side=RIGHT)

label4 = Label(frame3)
label4.config(font=("Impact", 50), bg="#000", fg="#F00", text="You have 1 minute to blast as many targets as you")
label4.pack(side=TOP)
label5 = Label(frame3)
label5.config(font=("Impact", 50), bg="#000", fg="#F00", text="can. But don't hit the red ones or they'll blow")
label5.pack(side=TOP)
label6 = Label(frame3)
label6.config(font=("Impact", 50), bg="#000", fg="#F00", text="up and kill you. Use the arrow keys to aim, the")
label6.pack(side=TOP)
label7 = Label(frame3)
label7.config(font=("Impact", 50), bg="#000", fg="#F00", text="spacebar to fire, and the enter key to reload.")
label7.pack(side=TOP)
Button((frame3), text="Continue", command=Continue, font = ("Impact", 35), fg = "#F00", bg = "#545454", state = NORMAL).pack()

label8 = Label(frame5)
label8.config(font=("Impact", 50), bg="#000", fg="#F00", text="Time's up!")
label8.pack(side=TOP)
label9 = Label(frame5)
label9.config(font=("Impact", 30), bg="#000", fg="#F00")
label9.pack(side=TOP)
label10 = Label(frame5)
label10.config(font=("Impact", 20), bg="#000", fg="#F00")
label10.pack(side=TOP)
Button((frame5), text="Play again", command=Continue, font=("Impact", 35), fg = "#F00", bg = "#000", state = NORMAL).pack()
Button((frame5), text="Quit", command=EXIT, font=("Impact", 35), fg = "#F00", bg = "#000", state = NORMAL).pack()

frame1.pack()
window.update()
window.mainloop()
