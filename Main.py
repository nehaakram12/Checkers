import Console
import graphics
import globalVariables
from graphics import Point

from time import sleep



def chooseOption():
    OptionWindow = graphics.GraphWin("Choose an option", 300, 250)
    # OptionWindow.setBackground('#E59866')

    label = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 - 100),
                          'Choose one from following options?')
    label.draw(OptionWindow)
    label1 = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 - 60),
                           '1. Human v/s Minimax Bot')
    label1.draw(OptionWindow)
    label2 = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 - 40),
                           '2. Human v/s Random Bot')
    label2.draw(OptionWindow)
    label3 = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2-20),
                           '3. Minimax Bot v/s Minimax Bot')
    label3.draw(OptionWindow)
    label4 = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 ),
                           '4. Random Bot v/s Random Bot')
    label4.draw(OptionWindow)
    label5 = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 + 20),
                           '5. Random Bot v/s Minimax Bot')
    label5.draw(OptionWindow)
    OptionWindow.focus()
    entry = graphics.Entry(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 + 50), 5)
    entry.setTextColor('green')
    entry.setFill('white')
    entry.setSize(12)
    entry.setFace("courier")
    entry.setText("1")
    entry.draw(OptionWindow)
    message = graphics.Text(Point(OptionWindow.getWidth() / 2, OptionWindow.getHeight() / 2 + 80),
                            'Click anywhere within the window to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(8)
    message.draw(OptionWindow)

    OptionWindow.getMouse()
    optu = int(entry.getText())
    OptionWindow.close()
    globalVariables.option=optu


# print("Choose one from following options?")
# print("1. Human v/s Minimax Bot")
# print("2. Human v/s Random Bot")
# print("3. Minimax Bot v/s Minimax Bot")
# print("4. Random Bot v/s Random Bot")
# print("5. Random Bot v/s Minimax Bot")
# opt = input("Enter a number from above options?")
# opt=int(opt)
globalVariables.init()
opt = 5
chooseOption()
opt=globalVariables.option
if opt == 1:
    print("1. Human v/s Minimax Bot")
    Console.play_human_bot(1)
elif opt == 2:
    print("2. Human v/s Random Bot")
    Console.play_human_bot(2)
elif opt == 3:
    print("3. Minimax Bot v/s Minimax Bot")
    Console.play_bot_bot(1, 1)
elif opt == 4:
    print("4. Random Bot v/s Random Bot")
    Console.play_bot_bot(2, 2)
elif opt == 5:
    print("5. Random Bot v/s Minimax Bot")
    Console.play_bot_bot(2, 1)
