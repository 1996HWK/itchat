import itchat
import time
MESSAGE=u",新年快乐~嘻嘻!"
SendPass=True
SendPassNames=[]
itchat.auto_login(True)
friendList=itchat.get_friends(update=True)[1:]
"""
send，发送祝福函数
#NickName：昵称、RemarkName：备注
"""
def send():
    filters=["我","爸","","","","",]  #过滤发送名单
    for friend in friendList:
        try:
            # if friend["NickName"]!="陌生人" and "同事" not in friend["NickName"]:
            for name in filters:
                if  not  name in friend["NickName"]:     #遍历过滤名单
                    itchat.send(friend["NickName"]+MESSAGE,friend["UserName"])
                    SendPassNames.append(friend["NickName"])
        except Exception as E:
            if len(friend["RemarkName"])==0:
                itchat.send("发生给"+"\""+friend["RemarkName"]+"\""+"发生:"+E, 'filehelper')
            else:
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
"""
inspect,检查备注是否为空
"""
def inspect():
    for friend in friendList:
        if friend["RemarkName"]=="":
            print(friend["NickName"])
# 执行
inspect()


