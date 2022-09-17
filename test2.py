from wxautoapi import WeChat
n = 1 # 多开数量，例如同时开启3个微信
wxdict = {f'wx{i}':WeChat() for i in range(n)}
wxdict
message = input("请输入要发送的消息：")
wxdict['wx0'].filehelper.send_text(message)