#coding:utf-8
import getpass
import hashlib
#安装过程不通过程序，直接安装Python、pip等包以及Chrome,安装过程将程序放在待安装文件夹
print(u"欢迎使用Weathon文档管理系统设置向导，请您按照指引完成设置，期间不要关闭该窗口或者关机，按下回车开始安装")
input()
print(u"请设置密码(输入密码过程中屏幕不会有反应，请直接输入)")
continue=True
while continue:
    psw＝getpass.getpass(">")
    psw2=getpass.getpass("请再输入一次\n>")
    if psw == psw2:
        continue=False
    else:
        print(u"两次输入不一致！请重试：")
m=hashlib.sha256()
m.update(psw)
f=open("")
m.digest()
