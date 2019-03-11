import graphics
from graphics import Point
from time import sleep
import time
import Minmax
import random
import globalVariables


import Board

width = 650
height = 650
offset_x = width / 8
offset_y = height / 8
win = graphics.GraphWin("Checkers", width, height)

def drawBoard():
    color_offset = False
    for x in range(0, 8):
        if x % 2 == 1:
            color_offset = True
        else:
            color_offset = False
        for y in range(0, 8):
            point1 = Point(x * offset_x, y * offset_y)
            point2 = Point(point1.x + offset_x, point1.y + offset_y)
            box = graphics.Rectangle(point1,point2)
            box.setFill("#6E2C00")
            if color_offset:
                if x % 2 == 0 or y % 2 == 0:
                    box.setFill("#E59866")
            elif x % 2 == 1 or y % 2 == 1:
                box.setFill("#E59866")
            box.draw(win)

def drawCheckers():
    for square in Board.board.flat:
        if square.checker is not None:
            circle = graphics.Circle(Point(square.center[0], square.center[1]), 15)
            if square.checker.black:
                circle.setFill("Black")
            else:
                circle.setFill("White")
            if square.checker.king:
                circle.setOutline('red')
                circle.setWidth(5)
            circle.draw(win)

def findsquare(click):
    click_x = click.x/81.25
    click_y = click.y/81.25
    for x in range(0, 8):
        for y in range(0, 8):
            if (click_x > x and click_y > y) and (click_x < x+1 and click_y < y+1):
                return (x, y)
    return None

def redraw():
    for child in win.children:
        child.undraw()
    drawBoard()
    drawCheckers()

def runMinmax(color):
    t1 = time.time()
    Minmax_move = Minmax.minimax(0, color, Board.board, float("-inf"), float("inf"))
    Minmax_move.apply(Board.board)
    t2 = time.time()
    if color:
        # print("Black move:   " + "Time taken for move number.", globalVariables.counter1, ":", t2 - t1)
        globalVariables.counter1 += 1
        globalVariables.timesum1 += t2 - t1
    else:
        # print("White move:   " + "Time taken for move number.", globalVariables.counter2, ":", t2 - t1)
        globalVariables.counter2 += 1
        globalVariables.timesum2 += t2 - t1
    redraw()
    return Minmax_move



def runRandom(color):
    t1 = time.time()
    randomMove=Minmax.random(color, Board.board)
    randomMove.apply(Board.board)
    t2 = time.time()
    if color:
        # print("Black move:   " + "Time taken for move number.", globalVariables.counter1, ":", t2 - t1)
        globalVariables.counter1 += 1
        globalVariables.timesum1 += t2 - t1
    else:
        # print("White move:   " + "Time taken for move number.", globalVariables.counter2, ":", t2 - t1)
        globalVariables.counter2 += 1
        globalVariables.timesum2 += t2 - t1
    redraw()
    return randomMove

def chooseDif():
    difwin = graphics.GraphWin("Choose Difficulty",200,200)
    label = graphics.Text(Point(difwin.getWidth()/2, difwin.getHeight()/2-50), 'Enter Difficulty level')
    label.draw(difwin)
    difwin.focus()

    entry = graphics.Entry(Point(difwin.getWidth() / 2, difwin.getHeight() / 2 + 50), 5)
    entry.setTextColor('green')
    entry.setFill('white')
    entry.setSize(12)
    entry.setFace("courier")
    entry.setText("2")
    entry.draw(difwin)
    message = graphics.Text(Point(difwin.getWidth() / 2, difwin.getHeight() / 2 + 80),
                            'Click anywhere within the window to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(8)
    message.draw(difwin)

    difwin.getMouse()
    optu = int(entry.getText())
    Minmax.setDifficulty(optu)
    difwin.close()
    # return optu

def play_human_bot(value):
    if value==1:
        chooseDif()
    drawBoard()
    drawCheckers()
    while Board.hasWon(Board.board) == 0:
        print("_______________NEW CYCLE_______________")
        print("Total Moves",globalVariables.counter1+globalVariables.counter2)
        print("Total Attacks",globalVariables.attacks)
        print("Moves without attack:",globalVariables.moves_without_attack)
        print("No. of black checkers:",globalVariables.blacks)
        print("No. of white checkers:",globalVariables.whites)
        sleep(0.01)
        Board.King(Board.board)
        click1 = win.getMouse()
        checker = findsquare(click1)
        if checker is None or Board.board[int(checker[0]), int(checker[1])].checker is None or Board.board[int(checker[0]), int(checker[1])].checker.black:
            continue
        click2 = win.getMouse()
        square = findsquare(click2)
        if square is None or (square[0] == checker[0] and square[1] == checker[1]):
            continue
        partial_move = Minmax.Move(Board.board[int(checker[0]), int(checker[1])].checker, Board.board[int(square[0]), int(square[1])],"?")
        partial_move.checker.x = checker[0]
        partial_move.checker.y = checker[1]
        # TODO: Add move validation
        move = Board.getFullMove(partial_move)
        if move is None:
            continue
        else:
            move.apply(Board.board)
            globalVariables.counter2+=1
            globalVariables.moves_without_attack+=1
        Board.King(Board.board)
        redraw()
        win.update()
        if Board.hasWon(Board.board) != 0:
            break
        if value==1:
            runMinmax(True)
        elif value==2:
            runRandom(True)
        globalVariables.moves_without_attack+=1
    winWindow = graphics.GraphWin("Game over")
    if Board.hasWon(Board.board) == 1:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "You Won! ")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        sleep(3)
    elif Board.hasWon(Board.board) == -1:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "You Lost :(")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        sleep(3)
    elif Board.hasWon(Board.board) == 2:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "Its a draw")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        sleep(3)
    message = graphics.Text(Point(winWindow.getWidth() / 2, winWindow.getHeight() / 2 + 20),
                            'Click anywhere within the window to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(8)
    message.draw(winWindow)

    winWindow.getMouse()
    winWindow.close()

    return

def play_bot_bot(value1, value2):
    if value1==1 or value2==1:
        chooseDif()
    drawBoard()
    drawCheckers()
    while Board.hasWon(Board.board) == 0:
        print("_______________NEW CYCLE_______________")
        print("Total Moves",globalVariables.counter1+globalVariables.counter2)
        print("Total Attacks",globalVariables.attacks)
        print("Moves without attack:",globalVariables.moves_without_attack)
        print("No. of black checkers:",globalVariables.blacks)
        print("No. of white checkers:",globalVariables.whites)
        sleep(0.01)
        Board.King(Board.board)
        if value1 ==1:
            runMinmax(False)
        elif value1==2:
            runRandom(False)
        globalVariables.moves_without_attack+=1
        Board.King(Board.board)
        redraw()
        win.update()
        if Board.hasWon(Board.board) != 0:
            break
        if value2 ==1:
            runMinmax(True)
        elif value2==2:
            runRandom(True)
        globalVariables.moves_without_attack+=1
    winWindow = graphics.GraphWin("Game over")
    if Board.hasWon(Board.board) == 1:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "White Won! ")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        print("Total Number of White Moves in Game:", globalVariables.counter2)
        print("Average Time to Make Each White Move:", globalVariables.timesum2 / globalVariables.counter2)
        sleep(3)
    elif Board.hasWon(Board.board) == -1:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "Black Won! ")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        print("Total Number of White Moves in Game:", globalVariables.counter2)
        print("Average Time to Make Each White Move:", globalVariables.timesum2 / globalVariables.counter2)
        sleep(3)
    elif Board.hasWon(Board.board) == 2:
        text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "Its a draw")
        text.draw(winWindow)
        print("Total Number of Black Moves in Game:", globalVariables.counter1)
        print("Average Time to Make Each Black Move:", globalVariables.timesum1 / globalVariables.counter1)
        sleep(3)
    message = graphics.Text(Point(winWindow.getWidth() / 2, winWindow.getHeight() / 2 + 20),
                            'Click anywhere within the window to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(8)
    message.draw(winWindow)

    winWindow.getMouse()
    winWindow.close()
    return



