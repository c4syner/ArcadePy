import curses
import time

# Initialize the screen
stdscr = curses.initscr()

# Start color
curses.start_color()

# We need to initialize color pairs (FG, BG) before we use them

# You can also use curses.init_color(number, r, g, b) to make your own colors

# Default color
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

# Highlight color
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

# Coords are in Y, X order instead of X, Y.

def clear():
	stdscr.clear()

# Original print function isn't that useful anymore
def print(str):
	stdscr.addstr(str + "\n")

# Same as above but supports color and doesn't add a trailing newline
def write(str, *color):
	stdscr.addstr(str, curses.color_pair(color[0] if len(color) > 0 else 1))

# Gets a character from input
getch = stdscr.getkey

# Overwriting input to work with curses
def input(prompt):
	write(prompt or "")

	return stdscr.getstr().decode()

# Refresh must be called to refresh the screen
refresh = stdscr.refresh

clear()

# This prevents the program from having to wait for enter to be pressed
curses.cbreak()

print("Curses Text Adventure")

# Refresh must be called to refresh the screen
refresh()

time.sleep(0.1)

write("There are ")
write("two", 2)
write(" paths, which way should you go? ")
write("left", 2)
write(" or ")
write("right\n", 2)

refresh()

choice = input("> ")

print("You chose " + choice)

getch()

refresh()

clear()

map = []

for x in range(10):
	map.append([])

	for y in range(10):
		map[x] = ["0"] * 10

map[5][5] = "1"

plrx = 5
plry = 5

mapx = 1
mapy = 2

def render():
	clear()

	print(" Minigame Prototype:")

	for x in range(10):
		for y in range(10):
			# Add a character to position
			stdscr.addch(mapy + y, mapx + x, map[x][y], curses.color_pair(2 if map[x][y] == "1" else 1))

	refresh()

render()

# This prevents typed characters from being echoed back to the output
curses.noecho()



# Movement logic
while True:
	render()
	time.sleep(0.05)
	cmd = getch()

	if cmd == "q":
		break

	if cmd == "w":
		map[plrx][plry - 1] = "1"
		map[plrx][plry] = "0"
		plry -= 1

	if cmd == "s":
		map[plrx][plry + 1] = "1"
		map[plrx][plry] = "0"
		plry += 1

	if cmd == "a":
		map[plrx - 1][plry] = "1"
		map[plrx][plry] = "0"
		plrx -= 1

	if cmd == "d":
		map[plrx + 1][plry] = "1"
		map[plrx][plry] = "0"
		plrx += 1

clear()
refresh()

# Reverse changes and return terminal to normal
curses.nocbreak()
curses.echo()
curses.endwin()