# import os
# import time

# source = ['/home/csh/git/python_test/']

# target_dir = '/home/csh/git/python_test/backup'

# target = target_dir + os.sep + \
# 			time.strftime('%Y%m%d%H%M%S') + '.zpi'

# if not os.path.exists(target_dir):
# 	os.makedirs(target_dir)

# zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))


# print('Zip command is:')
# print(zip_command)
# print('Running:')
# if os.system(zip_command) == 0:
# 	print('Successful backup to',target)
# else:
# 	print('Backup FAILED')

import os #导入系统模块
import time #导入时间模块

source = ['/home/csh/git/python_test/']

target_dir = '/home/csh/git/python_test/backup'

target = target_dir + os.sep + \
			time.strftime('%Y-%m-%d %H:%M:%S') + '.zip'

if not os.path.exists(target_dir):
	os.makedirs(target_dir)

zip_command = 'zip -r {} {}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0:
	print('Successful backip to',target)
else:
	print('Backup FAILED')
