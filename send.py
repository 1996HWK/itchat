import itchat
import time
MESSAGE=u",新年快乐~嘻嘻!"
SendPass=True
SendPassNames=[]
itchat.auto_login(True)
friendList=itchat.get_friends(update=True)[1:]
for friend in friendList:
    try:
        if friend["NickName"]!="陌生人":
            itchat.send(friend["NickName"]+MESSAGE,friend["UserName"])
            SendPassNames.append(friend["NickName"])
    except Exception as E:
        itchat.send("发生给"+"\""+friend["NickName"]+"\""+"发生:"+E, 'filehelper')
    time.sleep(1)
print("--------------发送祝福信息结果---------")
file=open("names.txt","w",encoding="utf-8")
for name in SendPassNames:
    file.write(name+"\n")
file.close()
if not SendPass:
    print("*出现了bug，请注意上手机助手查看！")
else:
    print("*发送成功！")
print("*发送人数:",len(SendPassNames))
print("*详情人，请查看文件")



