import os
import time

sourcs = ['/home/csh/git/python_test']

target_dir = '/home/csh/git/python_test/backup'

if not os.path.exists(target_dir):
	os.makedirs(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('输入备份备注')

if len(comment) == 0:
	target =  today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)

zip_command = "zip -r {} {}".format(target,' '.join(sourcs))


print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
	print('Successful backup to',target)
else:
	print('Backuo FAILED')