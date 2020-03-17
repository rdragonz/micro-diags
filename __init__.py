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


import sys_info

def main():
	stdscr.refresh()

	sys_info.print_info(curses.newwin(10, 60, 0, 0))

	
	curses.napms(5000)


if __name__ == "__main__":

	#Initialize curses
	stdscr = curses.initscr()
	curses.noecho()
	stdscr.keypad(True)
	curses.cbreak()

	#Run main function
	main()

	#End curses
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
