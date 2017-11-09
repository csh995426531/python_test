import os
import sys
import pickle
import time

relation = ['家人','朋友','同事']
mail_list_file = 'mail_list_file.data'
class people:
	# 类变量人员信息
	people_info = {}
	def __init__(self,name,tel,status):
		people.people_info[name] = {'电话':tel,'关系':relation[int(status)]}
		save(people.people_info)

class operation:
	def searchuser(self):
		if os.path.getsize(mail_list_file) == 0:
			print('联系人列表为空，请先添加')
			time.sleep(1)
			main()
		self.searchname = input('请输入名字：')
		while len(self.searchname) < 1:
			print('输入错误')
			self.searchname = input('请输入名字：')
		f = open(mail_list_file,'rb')
		userlist = pickle.load(f)
		
		if self.searchname in userlist:
			print('联系人信息：\n姓名：{}\n电话：{}\n关系分组：{}\n'.format(self.searchname,
															userlist[self.searchname]['电话'],
															userlist[self.searchname]['关系']
															))
		else:
			print('不存在该联系人')
		time.sleep(1)	
	def adduser(self):
		self.addname = input('请输入名字:')
		while len(self.addname) < 1:
			print('输入错误')
			self.addname = input('请输入名字:')
		if os.path.getsize(mail_list_file) > 0:
			f = open(mail_list_file,'rb')
			userlist = pickle.load(f)
			if self.addname in userlist:
				print('该联系人已存在，请前去修改')
				time.sleep(1)
				main()
		self.addtel = input('请输入电话:')
		while len(self.addtel) != 11:
			print('长度错误')
			self.addtel = input('请输入电话:')
		self.status = input('请选择关系类型(0:家人;1:朋友;2同事):')
		while len(self.status) < 1 or relation[int(self.status)] not in relation:
			print('输入错误')
			self.status = input('请输入关系类型(0:家人;1:朋友;2同事):')
		print("添加人员信息：\n姓名:{}\n电话:{}\n关系:{}".format(self.addname,
			self.addtel,relation[int(self.status)]
			))
		self.save = input('确认保存(y/n)')
		if(self.save == 'y'):
			people(self.addname,self.addtel,self.status)
		else:
			print('放弃保存')
			time.sleep(1)
	def updata(self):
		if os.path.getsize(mail_list_file) == 0:
			print('联系人列表为空，请先添加')
			time.sleep(1)
			main()
		self.updataname = input('请输入修改的联系人姓名:')	
		f = open(mail_list_file,'rb')
		userlist = pickle.load(f)
		f.close()
		if self.updataname in userlist:
			print('当前联系人信息：\n姓名：{}\n电话：{}\n关系分组：{}\n'.format(self.updataname,
																		userlist[self.updataname]['电话'],
																		userlist[self.updataname]['关系']
																		))
		
			self.updata_tel = input('请输入电话:')
			while len(self.updata_tel) != 11:
				print('长度错误')
				self.updata_tel = input('请输入电话:')
			self.updata_status = input('请选择关系类型(0:家人；1:朋友；2:同事):')
			while len(self.updata_status) < 1 or relation[int(self.updata_status)] not in relation:
				print('输入错误')
				self.updata_status = input('请选择关系类型(0:家人；1:朋友；2:同事):')
			print("修改信息：\n姓名：{}\n电话：{}----->{}\n关系分组：{}----->{}\n".format(self.updataname,
																		userlist[self.updataname]['电话'],
																		self.updata_tel,userlist[self.updataname]['关系'],
																		relation[int(self.updata_status)]
																		))
			self.save = input('确认保存(y/n)')
			if self.save == 'y':
				userlist[self.updataname] = {'电话':self.updata_tel,'关系':relation[int(self.updata_status)]}
				f = open(mail_list_file,'wb')
				pickle.dump(userlist,f)
				f.close()
				print('修改成功')
				time.sleep(1)
			else:
				print('放弃修改')
				time.sleep(1)
		else:
			print('不存在该联系人')
			time.sleep(1)
	def deluser(self):
		if os.path.getsize(mail_list_file) >0 :
			f = open(mail_list_file,'rb')
			userlist = pickle.load(f)
			a = 1
			print(" 	姓名		电话			关系分组")
			for key in userlist:
				print("{}.	{}		{}		{}".format(a,key,userlist[key]['电话'],userlist[key]['关系']))
				a += 1
			self.delname = input('请输入删除的人名字:')	
			while True:
				
				if self.delname in userlist and len(self.delname) > 0:
					del userlist[self.delname]
					f = open(mail_list_file,'wb')
					if len(userlist) > 0: 
						pickle.dump(userlist,f)
					f.close()
					print('删除成功')
					break
				else:
					self.delname = input('联系人不存在，请重新输入:')
			time.sleep(1)	

		else:
			print('通讯录为空，请先添加联系人')
			time.sleep(1)
	


def save(people_info):
	f = open(mail_list_file,'wb')
	pickle.dump(people_info,f)
	f.close()
	print('保存成功')
	time.sleep(1)

def main():
	while True:
		command = input("""
1.查询
2.添加
3.修改
4.删除
5.退出
""")	
		if len(command) > 0:
			operation_1 = operation()
			if command == '1':
				operation_1.searchuser()
			elif command == '2':
				operation_1.adduser()
			elif command == '3':
				operation_1.updata()
			elif command == '4':
				operation_1.deluser()
			else:
				del operation_1
				break

main()