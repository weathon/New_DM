#coding:utf-8
import getpass
import hashlib
#安装过程不通过程序，直接安装Python、pip等包以及Chrome,安装过程将程序放在待安装文件夹
print(u"欢迎使用Weathon文档管理系统设置向导，请您按照指引完成设置，期间不要关闭该窗口或者关机，按下回车开始安装")
input()
ip=input("Please input the IP adress of database(Only support SQLServer):")
port=input("Please input the port of database:")
username=input("Please input the username:")
database_name=input("Please input the database's name:")


