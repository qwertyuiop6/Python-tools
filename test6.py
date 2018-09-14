#coding:utf-8
from my_pf3 import pf
from qqbot import qqbotsched
from jihuang_new import search
from api_bot import api_search
from oschina import oschina
from linuxcn import linuxcn
from solidot import solidot

meum={
    '票房':pf,
    '饥荒':search,
    '天气':api_search,
    # 'oschina':oschina,
}
news_source={
    'Solidot': solidot,
    'Linuxcn': linuxcn,
    'Oschina': oschina,
    # 'Freebuf': freebuf,
}

def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是小Q~ ∩( ・ω・)∩')
    elif content == '-stop1':
        bot.SendTo(contact,'QQ机器人已关闭')
        bot.Stop()
    elif ~content.find('菜单'):
        ress='※---查--询---※\n☆'+'\n☆'.join(meum.keys())+'\n☆'+'点歌'+'\n※---@--ME---※\n☆'+'日常尬聊'\
        +'\n☆'+'百科知识'+'\n☆'+'新闻资讯'+'\n☆'+'今日天气'+'\n☆'+'绕口令,顺口溜'+'\n☆'+'脑筋急转弯'\
        +'\n☆'+'成语接龙'
        bot.SendTo(contact,ress)
    elif ~content.find('源列表'):
        ress='※--Source-List--※\n☆'+'\n☆'.join(news_source.keys())
        bot.SendTo(contact,ress)
    # elif ~content.find('oschina'):
    #     if bot.isMe(contact, member):
    #         pass
    #     else:
    #         res=oschina()
    #         bot.SendTo(contact,res)
    # elif ~content.find('linuxcn'):
    #     res=linuxcn()
    #     bot.SendTo(contact,res)
    else:
        if ~content.find('查询'):
            for key in meum.keys():

                    if ~content.find(key):
                        if content[4:]:
                            bot.SendTo(contact, '查询中~')
                            res=meum[key](content[4:],tq=True)
                        else:
                            if key=='天气':
                                res='请加上要查询的城市'
                            else:
                                bot.SendTo(contact, '查询中~')
                                res=meum[key]()
                        bot.SendTo(contact, res)
        for k in news_source.keys():
            if ~content.find(news_source[k].__name__):
                if bot.isMe(contact, member):
                    pass
                else:
                    res=news_source[k]()
                    bot.SendTo(contact, res)

    #青云客bot接口
    # if '@ME' in content:
    #     res=api_search(content[5:])
    #     bot.SendTo(contact, res)


# 定时方法
@qqbotsched(hour='9', minute='00')
def mytask(bot):
    gl = bot.List('group', 'AHPU-windows')
    if gl is not None:
        for group in gl:
            ress=oschina()
            bot.SendTo(group, ress)

    gl2= bot.List('group', 'AHPU-linux')
    if gl2 is not None:
        for group in gl2:
            # res1=oschina()
            # bot.SendTo(group,res1)
            # res2=linuxcn()
            # bot.SendTo(group,res2)
            res3=solidot(True)
            bot.SendTo(group,res3)
