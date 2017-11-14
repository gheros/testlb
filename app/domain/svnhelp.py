import os
import time
import configparser
config=configparser.ConfigParser()
config.read("config.ini")
def svndownbase(filename):
    svnco = "/usr/bin/svn co "
    svnlocal=config.get("svn","svnlocal")
    svnserver=config.get("svn","svnserver")
    a=os.popen(svnco+svnserver+'/'+filename+' '+svnlocal+'/'+filename)
    print(a.read())
# path=/home/edward/fileconf/tw_xjproxy/
# path1=/home/edward/fileconf/tw_xjlocal/xjqc
def svnupbase(filename):
    svnlocal = config.get("svn", "svnlocal")
    # uppath = config.get("svn", "uppath")
    # b=os.popen("svn st "+svnlocal+'/'+filename+"|awk '{print $2}'|xargs svn add")
    c=os.popen("/usr/bin/svn ci -m '"+"程序上传"+filename+"操作"+"' "+svnlocal+'/'+filename+" 2>&1")
    # print(b.read())
    print(c.read())
def writeup():
    uppath=config.get("svn","svnlocal")+'/up/up.sh'
    print(uppath)
    f=open(uppath,'r')
    f2=f.read()+' '
    f.close()
    f = open(uppath, 'w')
    f.write(f2)
    f.close()

def down():
    svndownbase('tw_xjproxy')
    svndownbase('tw_xjlocal')
    svndownbase('up')

def up():
    svnupbase('tw_xjproxy')
    svnupbase('tw_xjlocal')
    svnupbase('up')

# down()
# up()

# print(config.get("svn","svnserver"))
# print(config.get("svn","xjdenypath"))
# print(config.get("svn","uppath"))

#正式环境
#     print(c1.read())
#
# def down():
#     svnco = "/usr/bin/svn co "
#     svnst = "/usr/bin/svn st|awk '{print $2}'|xargs svn add"
#     svnci = "/usr/bin/svn ci "
#     path = "/home/edward/svn/xjdeny/"
#     path1 = "/home/edward/svn/up"
#     a=os.popen(svnco+"https://svn.wbapi.com/svn/tool/tool/nginx-web-conf/xjdeny "+path)
#     a1=os.popen(svnco+"https://svn.wbapi.com/svn/tool/tool/nginx-web-conf/up "+path1)
#     print(a.read())
#     print(a1.read())
#
# def up():
#     svnco = "/usr/bin/svn co "
#     svnst = "/usr/bin/svn st|awk '{print $2}'|xargs svn add"
#     svnci = "/usr/bin/svn ci "
#     path = "/home/edward/svn/xjdeny/"
#     path1 = "/home/edward/svn/up"
#     b=os.popen("svn st "+path+"|awk '{print $2}'|xargs svn add")
#     b1=os.popen("svn st "+path1+"|awk '{print $2}'|xargs svn add")
#     c=os.popen("/usr/bin/svn ci -m '"+"程序上传xjdeny操作"+"' "+path+" 2>&1")
#     c1=os.popen("/usr/bin/svn ci -m '"+"程序上传UP操作"+"' "+path1+" 2>&1")
#     print(b.read())
#     print(c.read())
#     print(b1.read())
#     print(c1.read())
#


