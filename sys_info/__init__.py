'''
System information module for Micro Diags
Created by Red in 2020
Greetings from Cleveland!
https://github.com/rdragonz/micro-diags

This code is licensed under the GNU General Public License
For more information see the LICENSE file that was distributed with this code
Or visit https://www.gnu.org/licenses/gpl-3.0.en.html
'''


def get_mem_size():
	# Get the memory size in MB

	with open("/proc/meminfo") as f:
		lines = f.readlines()


	mem_total = lines[0].strip().split()[1]

	mem_total = str(int(int(mem_total)/1024)) + " MB"

	return mem_total

def get_cpu_info():
	#Get the processor information as a dictionary

	with open("/proc/cpuinfo") as f:
		lines = f.readlines()

	cpu_info = {"name": "", "cores": "", "speed": "", "threads": ""}

	cpu_info["name"] = lines[4].split(":")[1].strip()
	cpu_info["cores"] = lines[12].split(":")[1].strip() + " Cores"
	cpu_info["speed"] = lines[7].split(":")[1].strip() + " MHz"
	cpu_info["threads"] = lines[10].split(":")[1].strip() + " Threads"

	return cpu_info

def print_info(window):
	#Print the CPU info
	#Requires the main curses screen
	#Also should pass the X and Y of the top
	#Left corner of the system info window

	window.refresh()

	proc = get_cpu_info()
	memory = get_mem_size()

	window.addstr(1, 20, "System Information")

	window.addstr(3, 1, proc["name"])
	window.addstr(4, 1, proc["speed"])
	window.addstr(5, 1, proc["cores"])
	window.addstr(6, 1, proc["threads"])
	window.addstr(8, 1, "RAM: " + memory)

	window.border()

	window.refresh()