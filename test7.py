from qqbot import qqbotsched

def onQQMessage(bot, contact, member, content):
    shadow=bot.List('buddy','Shadow')[0]
    windows = bot.List('group', 'AHPU-windows')[0]
    # linux=bot.List('group','AHPU-linux')[0]
    if ~contact.name.find(shadow.name):
        bot.SendTo(windows, content)