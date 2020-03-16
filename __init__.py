'''
Micro Diags
Created by Red in 2020
Greetings from Cleveland!
https://github.com/rdragonz/micro-diags

This code is licensed under the GNU General Public License
For more information see the LICENSE file that was distributed with this code
Or visit https://www.gnu.org/licenses/gpl-3.0.en.html
'''

import curses

def main():
	print("Hello, World!")


if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	stdscr.keypad(True)
	curses.cbreak()
	main()
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
