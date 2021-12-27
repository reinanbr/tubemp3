from .sysinfo import get_info_ram, get_info_gpu, get_info_cpu, get_info_ram,get_info_dir
from .sysinfo import date
gtr = get_info_ram
gtd = get_info_dir
gtc = get_info_cpu
gtg = get_info_gpu


### brock line
bl = False
def brock_line(arg):
    global bl
    bl = arg
#######################################################################
## var and def, for verification of getting log, cpu_show, ram_show, ##
#################### gpu_show, dir_show or no #########################
show_cpu_,show_gpu_,show_ram_,show_dir_ = False,False,False,False

def show_cpu(arg):
	global show_cpu_
	show_cpu_ = arg

def show_ram(arg):
	global show_ram_
	show_ram_ = arg

def show_gpu(arg):
	global show_gpu_
	show_gpu_ = arg

def show_dir(arg):
	global show_dir_
	show_dir_ = arg
##############################################


#### primordial e needded def puts for pritting e logging on the works ###
def puts(*args,
         sep=' ',
         show=True,
        date_fmt="%d/%m/%Y %H:%M:%S",
         save=False,
         pathfile='logs_puts.txt'):
		## starting ##
		text = ""
		for i in args:
			text = str(i)+sep
		cpu = f"[CPU: {gtc().percent}%]" if(show_cpu_) else ''
		ram = f"[RAM: {gtr().percent}%]" if(show_ram_) else ''
		gpu = f"[GPU: {gtg().percent}%]" if(show_gpu_) else ''
		dir = f"[DIR: {gtd().percent}%]" if(show_dir_) else ''
		bl = '\n' if(show_cpu_ or show_gpu_ or show_ram_ or bl) else ''
		text = (f'{cpu}{ram}{gpu}{dir}{bl}[{date(date_fmt)}]{bl}-> {text}')
		if(show):
			print(text)
		if (pathfile and save):
			path = open(pathfile,'a',encoding='utf-8')
			with open(path,'a') as file_p:
				file_p.write(text+'\n')
		return text

