import subprocess
while True:
	subprocess.Popen(['ecpg','console.pgc']).communicate()
	subprocess.Popen(['gcc', '-I/usr/include/postgresql' ,'-L/usr/lib/postgresql', 'console.c','-lecpg']).communicate()
	subprocess.Popen(['./a.out']).communicate()