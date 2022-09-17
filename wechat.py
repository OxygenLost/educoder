from wxautoapi import WeChat

# 获取当前微信客户端
wx = WeChat()

# 获取会话列表
wx.GetSessionList()
line = '哈哈哈哈哈哈哈你你你你你你你你的你年吊打你家的话哦看见好看啦三角地哦忘记殴打捡垃圾的文件里啊'
# with open("C:\\Users\\mmm\\Desktop\\test.txt", "r", encoding="gbk") as f:  # 这个.txt里写要发送的文字
#     for line in f.readlines():
who = '默念'  # 这里填要发送的人的备注
wx.ChatWith(who)
wx.SendMsg(line)