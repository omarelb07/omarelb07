#Final Project Milestone 3
#Group Members:
#Omar Elbanna
#Mark De Sousa
#Abraham Maaza
#Abubakkar Rahim

##Imports  ---------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import *
import random
##------------------------------------------------------------------------------------------------------------


##Gradient ---------------------------------------------------------------------------------------------------
class Gradient(tk.Frame):
    def __init__(self, parent, color1="", color2="", text="", is_main_window=False):
        self.is_main_window = is_main_window
        if color1 != "" and color2 != "":
            tk.Frame.__init__(self, parent, color1, color2)
            f1 = GradientFrame(self, text=text, borderwidth=1,relief="raised")
        else:
            tk.Frame.__init__(self, parent)
            f1 = GradientFrame(self, "maroon", "darkblue", borderwidth=1,relief="raised")
        f1.pack(fill="both", expand=True)

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="lightgreen", color2="lightblue", show_text=True, text="           Welcome to\nRock-Paper-Scissors\n             EXTREME!", is_main_window=False, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.show_text = show_text
        self.text_canvas = None
        self.text = text
        self.bind("<Configure>", self._on_resize)

    def _on_resize(self, event=None):
        self._draw_gradient(event)
        self.update_text_position(event)

    def _draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")
        
        if self.text_canvas is None and self.show_text:
            self.text_canvas = self.create_text(190, 125, anchor="center", text=self.text, fill="lightgray", font=("Impact", 65))

    def update_text_position(self, event):
        if self.text_canvas is not None:
            self.coords(self.text_canvas, event.width // 2, 200)
            
    def update_text(self, new_text):
        self.text = new_text
        if self.text_canvas is not None:
            self.itemconfig(self.text_canvas, text=self.text)
##Confirm       --------------------------------------------------------------------------------------------------
def quit_window():
    ays = tk.Frame(relief=tk.RIDGE,borderwidth=3,bg="gray",height=40,width=40)
    question = tk.Label(ays, text="Are you sure?", fg="black", font=("Arial", 25),bg="gray")
    yes = tk.Button(ays,text="Yes",command=window.destroy,font=("Arial", 18), width=15,height=2,bg="lightgray")
    no = tk.Button(ays,text="No",command=ays.destroy,font=("Arial", 18), width=15,height=2,bg="lightgray")
    question.pack(side=tk.TOP)
    yes.pack(side=tk.LEFT)
    no.pack(side=tk.RIGHT)
    ays.place(relx=0.1,rely=0.93,anchor="c")
##RuleFunctions --------------------------------------------------------------------------------------------------
def open_rules():
    rules_window = tk.Toplevel(window)
    rules_window.attributes("-fullscreen", True)
    rules_window.title("Rules")
    cover = GradientFrame(rules_window, color1="royalblue", color2="green", show_text=False)
    cover.pack(fill="both", expand=True)
    ##RulesDisplay -----------------------------------------------------------------------------------------------
    rules_txt = ("This is Rock-Paper-Scissors Extreme where you have 7 options to choose from and try to win against a bot.\nYou will choose either one of the 7 options below, and the bot will choose a random one as well. Each option has its strengths and weaknesses\n\n"
                "After choosing your element we will determine who will win and gain the point for that round\n\n\n"
                "The options are: \n\n"
                "Rock\n"
                "Paper\n"
                "Scissors\n"
                "Fire\n"
                "Water\n"
                "Air\n"
                "Nature\n\n\n"
                "Rock wins against Scissors, Fire and Air\n"
                "Paper wins against Rock, Air and Nature\n"
                "Scissors win against Paper, Air and Water\n"
                "Fire wins against Scissors, Paper and Nature\n"
                "Water wins against Fire, Paper and Rock\n"
                "Air wins against Water, Nature and Fire\n"
                "Nature wins against Rock, Water and Scissors\n\n"
                "Each element ties against themselves and loses against all other options not stated above\n\n\n"
                "There are two gamemodes: Best out of and First To\n\n"
                "Best out of essentially means whoever wins a majority of the rounds, which is more than half of the rounds\n\n"
                "First To is the first person to get to a certain score\n\n"
                "You can choose whichever gamemode when playing the game\n\n\n"
                "Are you ready to play?")
    rule_text = tk.Label(rules_window,text=rules_txt,height=40,width=120,fg="black", bg="cadetblue",font=("Georgia", 15))
    rule_text.place(relx=0.5,rely=0.5,anchor="c")
    #Exit  ----------------------------------------------------------------------------------------------------------
    exit_button = tk.Button(rules_window, text="Back", command=rules_window.destroy, font=("Arial", 16))
    exit_button.place(relx=0.1,rely=0.95,anchor="c")
#GameModeFunctions --------------------------------------------------------------------------------------------------
games = 3
gamo = 1
button1 = 0
button2 = 0
choices = ["Rock", "Paper", "Scissors", "Fire", "Water", "Air", "Nature"]
choice = 0
score = 0
bot_score = 0
i = 1
def open_modes():
    selected = "Selected Rounds: "
    gm = "Gamemode: "
    chose = "You Chose: \n"
    def rounds3():
        global games
        global button1
        button1 += 1
        selection = tk.Label(roundsFrame, text=selected + "3", font=("Arial", 20), width=17)
        selection.place(relx=0.35,rely=0.85)
        mode_window.after(200, confirmation())
    def rounds5():
        global games
        games = 5
        global button1
        button1 += 1
        selection = tk.Label(roundsFrame, text=selected + "5", font=("Arial", 20), width=17)
        selection.place(relx=0.35,rely=0.85)
        mode_window.after(200, confirmation())
    def rounds7():
        global games
        games = 7
        global button1
        button1 += 1
        selection = tk.Label(roundsFrame, text=selected + "7", font=("Arial", 20), width=17)
        selection.place(relx=0.35,rely=0.85)
        mode_window.after(200, confirmation())
    def rounds9():
        global games
        games = 9
        global button1
        button1 += 1
        selection = tk.Label(roundsFrame, text=selected + "9", font=("Arial", 20), width=17)
        selection.place(relx=0.35,rely=0.85)
        mode_window.after(200, confirmation())
    def rounds11():
        global games
        games = 11
        global button1
        button1 += 1
        selection = tk.Label(roundsFrame, text=selected + "11", font=("Arial", 20), width=17)
        selection.place(relx=0.36,rely=0.85)
        mode_window.after(200, confirmation())
    def bestOf():
        global gamo
        gamo = 2
        global button2
        button2 += 1
        gamemode = tk.Label(modesFrame, text=gm + "Best Out Of " + str(games), font=("Arial", 20), width=21)
        gamemode.place(relx=0.36, rely=0.85)
        mode_window.after(100, confirmation())
    def firstTo():
        global gamo
        gamo = 1
        global button2
        button2 += 1
        gamemode = tk.Label(modesFrame, text=gm + "First To " + str(games), font=("Arial", 20), width=21)
        gamemode.place(relx=0.36, rely=0.85)
        mode_window.after(500, confirmation())
    def confirmation():
        global button1
        global button2
        if button1 != 0 and button2 != 0:
            confirm = tk.Button(mode_window, text="CONFIRM", font=("Arial", 30), width=16, command=playTheGame)
            confirm.place(relx=0.5,rely=0.8,anchor="c")
    def playTheGame():
        open_game()
        destroyModeWindow()
    def destroyModeWindow():
        mode_window.destroy()
        global button1
        global button2
        button1 = 0
        button2 = 0
    #Gradient  ------------------------------------------------------------------------------------------------------
    mode_window = tk.Toplevel(window)
    mode_window.attributes("-fullscreen", True)
    mode_window.title("GameModes")
    cover = GradientFrame(mode_window, color1="firebrick", color2="deepskyblue", show_text=False)
    cover.pack(fill="both", expand=True)
    #Rounds  -------------------------------------------------------------------------------------------------------
    roundsFrame = tk.Frame(master=mode_window, width=650,height=750, bg="slategray", relief="raised",borderwidth=2)
    roundsFrame.place(relx=0.35,rely=0.45,anchor="c")
    rounds = tk.Label(roundsFrame, text="\t Choose the amount of\n\t rounds you will play:", bg="slategray", font=("Arial", 25), fg="lightgray",width=25,height=2)
    rounds.place(relx=0.75,rely=0.05,anchor="ne")
    #RoundButtons --------------------------------------------------------------------------------------------------
    three = tk.Button(roundsFrame, text="3",font=("Arial", 20), width=8, command=rounds3)
    three.place(relx=0.2,rely=0.4, anchor="c")
    five = tk.Button(roundsFrame, text="5",font=("Arial", 20), width=8, command=rounds5)
    five.place(relx=0.5,rely=0.4, anchor="c")
    seven = tk.Button(roundsFrame, text="7",font=("Arial", 20), width=8, command=rounds7)
    seven.place(relx=0.8,rely=0.4, anchor="c")
    nine = tk.Button(roundsFrame, text="9",font=("Arial", 20), width=8, command=rounds9)
    nine.place(relx=0.35,rely=0.6, anchor="c")
    eleven = tk.Button(roundsFrame, text="11",font=("Arial", 20), width=8, command=rounds11)
    eleven.place(relx=0.65,rely=0.6, anchor="c")
    #Mode  ---------------------------------------------------------------------------------------------------------
    modesFrame = tk.Frame(master=mode_window, width=650,height=750, bg="slategray", relief="raised",borderwidth=2)
    modesFrame.place(relx=0.65,rely=0.45,anchor="c")
    mode = tk.Label(modesFrame, text="\t Choose the gamemode: ", bg="slategray", font=("Arial", 25), fg="lightgray",width=25,height=2)
    mode.place(relx=0.75,rely=0.05,anchor="ne")
    #ModeButtons ---------------------------------------------------------------------------------------------------
    first = tk.Button(modesFrame, text="First To", font=("Arial", 25), width=16, height=3, command=firstTo)
    first.place(relx=0.5,rely=0.4,anchor="c")
    best = tk.Button(modesFrame, text="Best Out Of", font=("Arial", 25), width=16, height=3, command=bestOf)
    best.place(relx=0.5,rely=0.7,anchor="c")
    #Exit  ---------------------------------------------------------------------------------------------------------
    exit_button = tk.Button(mode_window, text="Back", command=destroyModeWindow, font=("Arial", 16))
    exit_button.place(relx=0.1,rely=0.95,anchor="c")
    
    def open_game():
        #Gradient  --------------------------------------------------------------------------------------------------
        play_window = tk.Toplevel(window)
        play_window.attributes("-fullscreen", True)
        play_window.title("The Game")
        cover = GradientFrame(play_window, color1="goldenrod", color2="violet", show_text=False)
        cover.pack(fill="both", expand=True)
        canvas = tk.Canvas(cover, width=1000,height=1000, bg="cornsilk")
        canvas.place(relx=0.5,rely=0.5,anchor="c")
        vertices = [
            (500, 100), #top
            (850, 350), #upper-right
            (925, 670), #lower-right
            (750, 850), #bottom-right
            (250, 850), #bottom-left
            (75, 670), #lower-left
            (150, 350), #upper-left
            (500, 100) #closed-top
        ]
        canvas.create_polygon(vertices, outline="black", fill="cornsilk", width=2)
        #Functions --------------------------------------------------------------------------------------------------
        def chooseRock():
            global choices
            global choice
            choice = 0
            nameOf = choices[0]
            selectedChoice = tk.Label(play_window, text=chose + nameOf, font=("Arial", 25),  bg="cornsilk")
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def choosePaper():
            global choices
            global choice
            choice = 1
            nameOf = choices[1]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def chooseScissor():
            global choices
            global choice
            choice = 2
            nameOf = choices[2]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def chooseFire():
            global choices
            global choice
            choice = 3
            nameOf = choices[3]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def chooseWater():
            global choices
            global choice
            choice = 4
            nameOf = choices[4]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def chooseAir():
            global choices
            global choice
            choice = 5
            nameOf = choices[5]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def chooseNature():
            global choices
            global choice
            choice = 6
            nameOf = choices[6]
            selectedChoice = tk.Label(play_window, text=chose + nameOf,  bg="cornsilk", font=("Arial", 25))
            selectedChoice.place(relx=0.5,rely=0.5,anchor="c")
            choiceSelected()
        def choiceSelected():
            global confirm
            confirm = tk.Button(play_window, text="CONFIRM", font=("Arial", 30), width=16, bg="cornsilk", command=bot)
            confirm.place(relx=0.5,rely=0.65,anchor="c")
        def reset():
            global games
            global gamo
            global score
            global bot_score
            global i
            global button1
            global button2
            global choice
            global choices
            play_window.destroy()
            games = 3
            gamo = 1
            button1 = 0
            button2 = 0
            choices = ["Rock", "Paper", "Scissors", "Fire", "Water", "Air", "Nature"]
            choice = 0
            score = 0
            bot_score = 0
            i = 1
            open_modes()
        def reset2():
            global games
            global gamo
            global score
            global bot_score
            global i
            global button1
            global button2
            global choice
            global choices
            play_window.destroy()
            games = 3
            gamo = 1
            button1 = 0
            button2 = 0
            choices = ["Rock", "Paper", "Scissors", "Fire", "Water", "Air", "Nature"]
            choice = 0
            score = 0
            bot_score = 0
            i = 1
        def bot():
            confirm.destroy()
            global score
            global bot_score
            global i
            bestTo = 0
            for j in range(1, (games + 1), 2):
                bestTo += 1
            ##BestOutOf   -----------------------------------------------------------------------------------------
            if gamo == 2:
                if i < games and score < bestTo and bot_score < bestTo:
                    ##BotChooseRandom -----------------------------------------------------------------------------
                    rng = random.SystemRandom()
                    bot_num = rng.randint(1, 7)
                    bot_str = choices[bot_num - 1]
                    num = choice + 1
                    ##IfScoreReached ------------------------------------------------------------------------------
                    if score != bestTo and bot_score != bestTo:
                        ##Ties  ----------------------------------------------------------------------------------------
                        if num == bot_num:
                            tied = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou tied!\nExtra Round", font=("Arial", 25), bg="cornsilk")
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            tied.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Rock  ----------------------------------------------------------------------------------------
                        elif num == 1 and (bot_num == 2 or bot_num == 4 or bot_num == 6):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 1 and (bot_num == 3 or bot_num == 5 or bot_num == 7):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Paper  ----------------------------------------------------------------------------------------
                        elif num == 2 and (bot_num == 1 or bot_num == 6 or bot_num == 7):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 2 and (bot_num == 2 or bot_num == 4 or bot_num == 5):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Scissors -------------------------------------------------------------------------------------
                        elif num == 3 and (bot_num == 2 or bot_num == 6 or bot_num == 7):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 3 and (bot_num == 1 or bot_num == 4 or bot_num == 5):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Fire  ----------------------------------------------------------------------------------------
                        elif num == 4 and (bot_num == 2 or bot_num == 3 or bot_num == 7):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 4 and (bot_num == 5 or bot_num == 1 or bot_num == 6):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Water  ----------------------------------------------------------------------------------------
                        elif num == 5 and (bot_num == 2 or bot_num == 3 or bot_num == 4):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 5 and (bot_num == 7 or bot_num == 1 or bot_num == 6):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Air -------------------------------------------------------------------------------------------
                        elif num == 6 and (bot_num == 2 or bot_num == 3 or bot_num == 5):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 6 and (bot_num == 4 or bot_num == 1 or bot_num == 7):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        ##Nature ---------------------------------------------------------------------------------------
                        elif num == 7 and (bot_num == 1 or bot_num == 5 or bot_num == 3):
                            win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                            score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            win.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
                        elif num == 7 and (bot_num == 2 or bot_num == 6 or bot_num == 4):
                            lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                            bot_score += 1
                            i += 1
                            scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                            lose.place(relx=0.2,rely=0.5,anchor="c")
                            scores.place(relx=0.8,rely=0.5,anchor="c")
            
            ##FirstTo  --------------------------------------------------------------------------------------------
            elif gamo == 1:
                ##IfScoreReached ------------------------------------------------------------------------------
                if score < games and bot_score < games:
                    ##BotChooseRandom -----------------------------------------------------------------------------
                    rng = random.SystemRandom()
                    bot_num = rng.randint(1, 7)
                    bot_str = choices[bot_num - 1]
                    num = choice + 1
                    ##Ties  ----------------------------------------------------------------------------------------
                    if num == bot_num:
                        tied = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou tied!\nExtra Round", font=("Arial", 25), bg="cornsilk")
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        tied.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Rock  ----------------------------------------------------------------------------------------
                    elif num == 1 and (bot_num == 2 or bot_num == 4 or bot_num == 6):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 1 and (bot_num == 3 or bot_num == 5 or bot_num == 7):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Paper  ----------------------------------------------------------------------------------------
                    elif num == 2 and (bot_num == 1 or bot_num == 6 or bot_num == 7):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 2 and (bot_num == 2 or bot_num == 4 or bot_num == 5):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Scissors -------------------------------------------------------------------------------------
                    elif num == 3 and (bot_num == 2 or bot_num == 6 or bot_num == 7):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 3 and (bot_num == 1 or bot_num == 4 or bot_num == 5):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Fire  ----------------------------------------------------------------------------------------
                    elif num == 4 and (bot_num == 2 or bot_num == 3 or bot_num == 7):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 4 and (bot_num == 5 or bot_num == 1 or bot_num == 6):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Water  ----------------------------------------------------------------------------------------
                    elif num == 5 and (bot_num == 2 or bot_num == 3 or bot_num == 4):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 5 and (bot_num == 7 or bot_num == 1 or bot_num == 6):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Air -------------------------------------------------------------------------------------------
                    elif num == 6 and (bot_num == 2 or bot_num == 3 or bot_num == 5):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 6 and (bot_num == 4 or bot_num == 1 or bot_num == 7):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    ##Nature ---------------------------------------------------------------------------------------
                    elif num == 7 and (bot_num == 1 or bot_num == 5 or bot_num == 3):
                        win = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Win!", font=("Arial", 25), bg="cornsilk")
                        score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        win.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")
                    elif num == 7 and (bot_num == 2 or bot_num == 6 or bot_num == 4):
                        lose = tk.Label(play_window, text="The bot chose:\n" + bot_str + "\n\nYou Lose!", font=("Arial", 25), bg="cornsilk")
                        bot_score += 1
                        scores = tk.Label(play_window, text="The score is: " + str(score) + "-" + str(bot_score), font=("Arial", 25), bg="cornsilk")
                        lose.place(relx=0.2,rely=0.5,anchor="c")
                        scores.place(relx=0.8,rely=0.5,anchor="c")

            ##Results  ---------------------------------------------------------------------------------------
            if gamo == 2:
                if (score == bestTo or bot_score == bestTo):
                    if score == bestTo:
                        resFrame = tk.Frame(play_window, relief="raised",borderwidth=2, bg="cornsilk",width=800,height=600)
                        results = tk.Label(resFrame, text="You have " + str(score) + " points and the bot has " + str(bot_score) + " points.\n\nYOU WIN THE GAME!!")
                        results.pack(side="top")
                        playAgain = tk.Button(resFrame, text="PLAY AGAIN?", font=("Arial", 25), width=12, height=3, bg="slategray", relief="raised", command=reset)
                        playAgain.pack()
                        resFrame.place(relx=0.5,rely=0.5,anchor="c")
                    elif bot_score == bestTo:
                        resFrame = tk.Frame(play_window, relief="raised",borderwidth=2, bg="cornsilk",width=800,height=600)
                        results = tk.Label(resFrame, text="You have " + str(score) + " points and the bot has " + str(bot_score) + " points.\n\nYOU LOST THE GAME!!")
                        results.pack(side="top")
                        playAgain = tk.Button(resFrame, text="PLAY AGAIN?", font=("Arial", 25), width=12, height=3, bg="slategray", relief="raised", command=reset)
                        playAgain.pack()
                        resFrame.place(relx=0.5,rely=0.5,anchor="c")
            if gamo == 1:
                if (score == games or bot_score == games):
                    if score > bot_score:
                        resFrame = tk.Frame(play_window, relief="raised",borderwidth=2, bg="cornsilk",width=800,height=600)
                        results = tk.Label(resFrame, text="You have " + str(score) + " points and the bot has " + str(bot_score) + " points.\n\nYOU WIN THE GAME!!")
                        results.pack(side="top")
                        playAgain = tk.Button(resFrame, text="PLAY AGAIN?", font=("Arial", 25), width=12, height=3, bg="slategray", relief="raised", command=reset)
                        playAgain.pack()
                        resFrame.place(relx=0.5,rely=0.5,anchor="c")
                    elif score < bot_score:
                        resFrame = tk.Frame(play_window, relief="raised",borderwidth=2, bg="cornsilk",width=800,height=600)
                        results = tk.Label(resFrame, text="You have " + str(score) + " points and the bot has " + str(bot_score) + " points.\n\nYOU LOST THE GAME!!")
                        results.pack(side="top")
                        playAgain = tk.Button(resFrame, text="PLAY AGAIN?", font=("Arial", 25), width=12, height=3, bg="slategray", relief="raised", command=reset)
                        playAgain.pack()
                        resFrame.place(relx=0.5,rely=0.5,anchor="c")
        #Buttons  ---------------------------------------------------------------------------------------------------
        rock = tk.Button(play_window, text="🏔", font=("Arial", 20), width=8, height=2, fg="slategray", bg="cornsilk", relief="solid",command=chooseRock)
        rock.place(relx=0.5,rely=0.22,anchor="c")
        paper =  tk.Button(play_window, text="📄", font=("Arial", 20), width=8, height=2, fg="black", bg="cornsilk", relief="solid",command=choosePaper)
        paper.place(relx=0.4,rely=0.39,anchor="c")
        scissor = tk.Button(play_window, text="✂", font=("Arial", 20), width=8, height=2, fg="indianred", bg="cornsilk", relief="solid",command=chooseScissor)
        scissor.place(relx=0.6,rely=0.39,anchor="c")
        fire = tk.Button(play_window, text="🔥", font=("Arial", 20), width=8, height=2, fg="orangered", bg="cornsilk", relief="solid",command=chooseFire)
        fire.place(relx=0.38,rely=0.62,anchor="c")
        water = tk.Button(play_window, text="💧", font=("Arial", 20), width=8, height=2, fg="skyblue", bg="cornsilk", relief="solid",command=chooseWater)
        water.place(relx=0.62,rely=0.62,anchor="c")
        air = tk.Button(play_window, text="💨", font=("Arial", 20), width=8, height=2, fg="black", bg="cornsilk", relief="solid",command=chooseAir)
        air.place(relx=0.43,rely=0.73,anchor="c")
        nature = tk.Button(play_window, text="🌲", font=("Arial", 20), width=8, height=2, fg="green", bg="cornsilk", relief="solid",command=chooseNature)
        nature.place(relx=0.57,rely=0.73,anchor="c")
        #Exit  ------------------------------------------------------------------------------------------------------
        exit_button = tk.Button(play_window, text="Back", command=reset2, font=("Arial", 16))
        exit_button.place(relx=0.1,rely=0.95,anchor="c")
##MainWindow --------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.title("Rock-Paper-Scissors EXTREME")
window.attributes("-fullscreen", True)
Gradient(window).pack(fill="both", expand=True)
quit_button = tk.Button(window, text="QUIT", command=quit_window, font=("Arial", 16))
quit_button.place(relx=0.1,rely=0.95,anchor="c")
##Rules      -------------------------------------------------------------------------------------------------------
ruleFrame = tk.Frame(relief=tk.RIDGE,borderwidth=3)
rules = tk.Button(master=ruleFrame,text="Rules",font=("Arial",25,"bold"),width=18,height=3,fg="black",bg="lightgray", command=open_rules)
rules.pack()
ruleFrame.place(relx=0.5,rely=0.55,anchor="c")
##Start ------------------------------------------------------------------------------------------------------------
playFrame = tk.Frame(relief=tk.RIDGE,borderwidth=3)
play = tk.Button(playFrame, text="Play",font=("Arial",25,"bold"),width=18,height=3,fg="black",bg="lightgray", command=open_modes)
play.pack()
playFrame.place(relx=0.5,rely=0.7,anchor="c")








window.mainloop()