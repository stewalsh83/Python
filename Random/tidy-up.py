
# shell
# find . -type d                   # all dir & subdir
# find . -type f                   # all files, subdir & files
# find . -type f -ls               # pass in ls
# find . -type f -ls > output.txt  # send output to txt file
# grep word 2009.txt
# grep -E "Word1|word2" music.txt

# places everything into output file
# find . -type f -ls > output.txt

import sys, re
# tidys up output.txt
for i in sys.stdin:
	i = i.strip().split()
	s = ' '.join(i[10:])
	line = s.replace("\\", "")
	print('{}'.format(line).strip("._"))
	#print('Bytes {:<10} {}'.format(i[6], s))

# tidys up the output file and writes it to name.txt
f = open('name.txt', 'w')
for i in sys.stdin:
	i = i.strip().split()
	s = ' '.join(i[7:])
	line = s.replace("\\", "")
	f.write('Bytes {:<10} {}\n'.format(i[6], line).strip("."))
