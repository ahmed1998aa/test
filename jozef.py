#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
import requests
import random
from random import randint
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = '378709196:AAG-vq0Ie5QhsBq44WSWn4O13hvRZ6h94as'
bot = telebot.TeleBot(TOKEN)
sudo = '163509666'
rediss = redis.StrictRedis(host='localhost', port=6379, db=0)


f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)

#################################################################################################################################################################################################

@bot.message_handler(commands=['short'])
def send_pic(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        text = m.text.replace("/short ","")
        res = urllib.urlopen("http://yeo.ir/api.php?url={}".format(text)).read()
        bot.send_message(m.chat.id, "*Your Short Link :* {}".format(res), parse_mode="Markdown", disable_web_page_preview=True)
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['pic'])
def send_pic(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        urllib.urlretrieve("https://source.unsplash.com/random", "img.jpg")
        bot.send_photo(m.chat.id, open('img.jpg'))
	os.remove('img.jpg')
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['pm'])
def pm(m):
    if m.from_user.id == 163509666:
        ids = m.text.split()[1]
        text = m.text.split()[2]
        bot.send_message(int(ids), '{}'.format(text),parse_mode='HTML')
        bot.send_message(m.chat.id, 'Sent!')

#################################################################################################################################################################################################

@bot.message_handler(commands=['start'])
def welcome(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       cid = m.chat.id
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("About",callback_data='pouria')
       markup.add(c)
       b = types.InlineKeyboardButton("Help",callback_data='help')
       markup.add(b)
       nn = types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
       markup.add(nn)
       oo = types.InlineKeyboardButton("Channel", url='https://telegram.me/facegram1')
       markup.add(oo)
       id = m.from_user.id
       rediss.sadd('memberspy',id)
       bot.send_message(cid, "*Hi*\n_Welcome To king bot_\n*Please Choose One*", disable_notification=True, reply_markup=markup, parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.message:
        if call.data == "help":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Send /help And /adminhelp Command!")
     if call.message:
        if call.data == "pouria":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="king bot Created By @jozef3 And Written In Python")
     if call.message:
        if call.data == "short":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /short [URL]\n\nUsage : Shorten Your Link!")
     if call.message:
        if call.data == "pic":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /pic\n\nUsage : Send Random Picture!")
     if call.message:
        if call.data == "gif":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /gif [Text]\n\nUsage : Convert Text To Gif!")
     if call.message:
        if call.data == "tex":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /tex [Text]\n\nUsage : Write Text On The Sticker!")
     if call.message:
        if call.data == "kickme":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /kickme\n\nUsage : Exit From Group!")
     if call.message:
        if call.data == "id":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /id [URL]\n\nUsage : Get Your ID!\n\n\n\nCommand : id (reply to message)\n\nGet Users ID!")
     if call.message:
        if call.data == "me":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /me\n\nUsage : Show Your Information With Your Sticker!")
     if call.message:
        if call.data == "food":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /food\n\nUsage : Get Food Sticker!")
     if call.message:
        if call.data == "mean":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /mean [Text]\n\nUsage : Get The Meaning Of Text!")
     if call.message:
        if call.data == "voice":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /voice [Text]\n\nUsage : Convert Text To Voice!")
     if call.message:
        if call.data == "webshot":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /webshot [URL]\n\nUsage : Get ScreenShot From Site!")
     if call.message:
        if call.data == "calc":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /calc [Formulas]\n\nUsage : Calculate Your Formulas!")
     if call.message:
        if call.data == "feedback":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /feedback [Text]\n\nUsage : Send Message To Admin!")
     if call.message:
        if call.data == "bold":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /bold [Text]\n\nUsage : Bold Your Text!")
     if call.message:
        if call.data == "italic":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /italic [Text]\n\nUsage : Italic Your Text!")
     if call.message:
        if call.data == "code":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /code [Text]\n\nUsage : Code Your Text!")
     if call.message:
        if call.data == "hyper":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /hyper [Text] [URL]\n\nUsage : Hyperlink Your Text!")
     if call.message:
        if call.data == "echo":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /echo [Text]\n\nUsage : Echo Your Text!")
     if call.message:
        if call.data == "sticker":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /sticker (reply to photo)\n\nUsage : Convert Photo To Sticker!")
     if call.message:
        if call.data == "number":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /num [Text]\n\nUsage : Count The Word Of Your Text!")
     if call.message:
        if call.data == "photo":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /photo (reply to sticker)\n\nUsage : Convert Sticker To Photo!")
     if call.message:
        if call.data == "love":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /love [Text] [Text]\n\nUsage : Get Lovely Sticker From Texts!")
     if call.message:
        if call.data == "info":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /info\n\nUsage : Get Your Information!")
     if call.message:
        if call.data == "setlink":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /setlink [GroupLink]\n\nUsage : Set Group Link!")
     if call.message:
        if call.data == "link":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /link\n\nUsage : Get Group Link!")
     if call.message:
        if call.data == "rank":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /rank [ID]\n\nUsage : Show Users Rank!")
     if call.message:
        if call.data == "setsticker":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /setsticker (reply to sticker)\n\nUsage : Set Your Sticker!")
     if call.message:
        if call.data == "cap":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /cap [Text] (reply to photo)\n\nUsage : Write Text Under The Photo!")
     if call.message:
        if call.data == "keepcalm":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /keepcalm [Text] [Text] [Text]\n\nUsage : Get KeepCalm Sticker From Texts!")
     if call.message:
        if call.data == "setphone":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /setphone [PhoneNumber]\n\nUsage : Set Your PhoneNumber!")
     if call.message:
        if call.data == "myphone":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /myphone\n\nUsage : Get Your PhoneNumber!")
     if call.message:
        if call.data == "uploader":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Uploader Panel :\n\nSend Your File In Private To Upload And Get FileID")
     if call.message:
        if call.data == "downloader":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Downloader Panel :\n\nCommand : /download [URL]\n\nUsage : Download File From Your Link!")
     if call.message:
        if call.data == "pm":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /pm [ID] [Text]\n\nUsage : Send Message To Users!")
     if call.message:
        if call.data == "stats":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /stats\n\nUsage : Get Bot Stats!")
     if call.message:
        if call.data == "ban":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /ban [ID]\n\nUsage : Ban Users!")
     if call.message:
        if call.data == "unban":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /unban [ID]\n\nUsage : Unban Users!")
     if call.message:
        if call.data == "clearban":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /clearban\n\nUsage : Clean Banlist!")
     if call.message:
        if call.data == "kick":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /kick (reply)\n\nUsage : Kick User From Group!")
     if call.message:
        if call.data == "leave":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /leave\n\nUsage : Bot Leave The Group!")
     if call.message:
        if call.data == "uptime":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /uptime\n\nUsage : Get Server Uptime!")
     if call.message:
        if call.data == "setrank":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /setrank [ID] [Rank]\n\nUsage : Set Rank For Users!")
     if call.message:
        if call.data == "bc":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /bc [Text]\n\nUsage : Send Message To All Users!")
     if call.message:
        if call.data == "delrank":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Command : /delrank [ID]\n\nUsage : Delete Users Rank!")

#################################################################################################################################################################################################

@bot.message_handler(commands=['stats'])
def send_stats(m):
    if m.from_user.id == 163509666:
        usrs = str(rediss.scard('memberspy'))
        ban = str(rediss.scard('banlist'))
        text = '*Users : {}\n\nBanlist : {}*'.format(usrs,ban)
        bot.send_message(m.chat.id,text,parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['adminhelp'])
def welcome(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       cid = m.chat.id
       markup = types.InlineKeyboardMarkup()
       a = types.InlineKeyboardButton("PM",callback_data='pm')
       markup.add(a)
       b = types.InlineKeyboardButton("Stats",callback_data='stats')
       markup.add(b)
       c = types.InlineKeyboardButton("Ban",callback_data='ban')
       markup.add(c)
       d = types.InlineKeyboardButton("Unban",callback_data='unban')
       markup.add(d)
       e = types.InlineKeyboardButton("ClearBan",callback_data='clearban')
       markup.add(e)
       f = types.InlineKeyboardButton("Kick",callback_data='kick')
       markup.add(f)
       g = types.InlineKeyboardButton("Leave",callback_data='leave')
       markup.add(g)
       h = types.InlineKeyboardButton("Uptime",callback_data='uptime')
       markup.add(h)
       i = types.InlineKeyboardButton("SetRank",callback_data='setrank')
       markup.add(i)
       j = types.InlineKeyboardButton("BroadCast",callback_data='bc')
       markup.add(j)
       k = types.InlineKeyboardButton("DelRank",callback_data='delrank')
       markup.add(k)
       bot.send_message(cid, "*List Of Admin Commands :*", disable_notification=True, reply_markup=markup, parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['ban'])
def kick(m):
    if m.from_user.id == 163509666:
        ids = m.text.split()[1]
        rediss.sadd('banlist',int(ids))
        bot.send_message(int(ids), '<b>You Are Banned!</b>',parse_mode='HTML')
        bot.send_message(m.chat.id, 'Banned!')

#################################################################################################################################################################################################

@bot.message_handler(commands=['unban'])
def send_stats(m):
    if m.from_user.id == 163509666:
        ids = m.text.split()[1]
        rediss.srem('banlist',int(ids))
        bot.send_message(int(ids), '<b>You Are UnBanned!</b>',parse_mode='HTML')
        bot.send_message(m.chat.id, 'UnBanned!')

#################################################################################################################################################################################################

@bot.message_handler(commands=['gif'])
def gif(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       text = m.text.replace('/gif ','')
       url = "http://www.flamingtext.com/net-fu/image_output.cgi?_comBuyRedirect=false&script=blue-fire&text={}&symbol_tagname=popular&fontsize=70&fontname=futura_poster&fontname_tagname=cool&textBorder=15&growSize=0&antialias=on&hinting=on&justify=2&letterSpacing=0&lineSpacing=0&textSlant=0&textVerticalSlant=0&textAngle=0&textOutline=off&textOutline=false&textOutlineSize=2&textColor=%230000CC&angle=0&blueFlame=on&blueFlame=false&framerate=75&frames=5&pframes=5&oframes=4&distance=2&transparent=off&transparent=false&extAnim=gif&animLoop=on&animLoop=false&defaultFrameRate=75&doScale=off&scaleWidth=240&scaleHeight=120&&_=1469943010141".format(text)
       res = urllib.urlopen(url)
       parsed_json = json.loads(res.read())
       gif = parsed_json['src']
       link = parsed_json['gimpHost']
       urllib.urlretrieve("{}".format(gif), "gif.gif")
       bot.send_document(m.chat.id, open('gif.gif'), caption="@king_5bot")
       os.remove('gif.gif')

#################################################################################################################################################################################################

@bot.message_handler(commands=['tex'])
def qr(message):
      try:
        text = message.text.replace("/tex ","")
        urllib.urlretrieve('https://assets.imgix.net/sandbox/sandboxlogo.ai?blur=500&fit=crop&w=1200&h=600&txtclr=black&txt={}&txtalign=middle%2C%20center&txtsize=150&txtline=3'.format(text), 'time.jpg')
        bot.send_sticker(message.chat.id, open('time.jpg'))
	os.remove('time.jpg')
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(content_types=['new_chat_member'])
def hi(m):
    name = m.new_chat_member.first_name
    title = m.chat.title
    ids = m.new_chat_member.id
    if id == 163509666:
        rediss.sadd('chats',ids)
        bot.send_message(m.chat.id, '*Hi!\nPlease Start Me In Pravite*', parse_mode='Markdown')
    else:
        bot.send_message(m.chat.id, '*Hi* `{}` *Welcome To* `{}`'.format(name,title), parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['clearban'])
def kick(m):
    if m.from_user.id == 163509666:
        rediss.delete('banlist')
        bot.send_message(m.chat.id, '<b>Cleaned!</b>',parse_mode='HTML')

#################################################################################################################################################################################################

@bot.message_handler(content_types=['left_chat_member'])
def hi(m):
    name = m.left_chat_member.first_name
    bot.send_message(m.chat.id, '*GoodBye* `{}`'.format(name), parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['kick'])
def kick(m):
    if m.from_user.id == 163509666:
      if m.reply_to_message:
        text = m.reply_to_message.from_user.id
        bot.kick_chat_member(m.chat.id, text)
        bot.send_message(m.chat.id, '_User_ *{}* _has been kicked!_'.format(text), parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['kickme'])
def answer(m):
  if m.chat.type == "group" or m.chat.type == "supergroup":
    bot.kick_chat_member(m.chat.id, m.from_user.id)
  if m.chat.type == "private":
    bot.send_message(m.chat.id, 'Just In Group!')
#################################################################################################################################################################################################

@bot.message_handler(regexp='^id')
def answer(m):
    if m.reply_to_message:
        id = m.reply_to_message.from_user.id
        bot.send_message(m.chat.id, id)

#################################################################################################################################################################################################

@bot.message_handler(commands=['id'])
def id_handler(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        cid = m.from_user.id
        fl = m.from_user.first_name
        bot.send_message(m.chat.id, "*Your Name = {}\n\nYour ID = {}*".format(fl,cid), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['me'])
def answer(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       try:
          text = bot.get_chat_member(m.chat.id, m.from_user.id).status
          id = m.from_user.id
          rank = rediss.hget("user:rank","{}".format(id))
          msgs = rediss.get("{}".format(id))
          name = m.from_user.first_name
          user = m.from_user.username
          photo = rediss.hget('stickers',id)
          bot.send_message(m.chat.id, "*Name* : {} \n*UserName* = @{} \n*GlobalRank* : {} \n*Position In Group* : {} \n\n*Msgs* : {}".format(name,user,rank,text,msgs), parse_mode="Markdown")
          bot.send_sticker(m.chat.id,photo)
       except:
          bot.send_photo(m.chat.id, 'AgADBAADq6cxG3LsuA4NhfzrLPeDz-qCWBkABEgaS8eAZRQfsEkBAAEC',caption="Please Submit One Sticker For Your")
#################################################################################################################################################################################################

@bot.message_handler(commands=['leave'])
def leavehandler(m):
    if m.from_user.id == 163509666:
        bot.leave_chat(m.chat.id)

#################################################################################################################################################################################################

@bot.message_handler(commands=['food'])
def send_sports(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        urllib.urlretrieve("http://lorempixel.com/400/200/food/OffLiNeTeam", "food.jpg")
        bot.send_sticker(m.chat.id, open('food.jpg'))
	os.remove('food.jpg')
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################


#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/mean) (.*)')
def mean(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        text = m.text.split()[1]
        r = req.get('http://api.vajehyab.com/v2/public/?q={}'.format(text))
        json_data = r.json()
        textx = json_data['data']['text']
        bot.send_message(m.chat.id, textx)
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/download) (.*)')
def all(m):
    text = m.text.split()[1]
    id = m.from_user.id
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
         if m.chat.type == 'private':
             if re.match('(http|https)://.*.(png)$',text):
                 msg = bot.send_message(m.chat.id, '*Downloading.....*',parse_mode='Markdown')
                 dw(text,'file.png')
                 bot.send_photo(m.chat.id, open('file.png'),caption='@king_5bot')
                 os.remove('file.png')
             if re.match('(http|https)://.*.(apk)$',text):
                 msg = bot.send_message(m.chat.id, '*Downloading .....*',parse_mode='Markdown')
                 dw(text,'app.apk')
                 bot.send_document(m.chat.id, open('app.apk'),caption='@king_5bot')
                 os.remove('app.apk')
             if re.match('(http|https)://.*.(html|htm)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.html')
                 bot.send_document(m.chat.id, open('file.html'),caption='@king_5bot')
                 os.remove('file.html')
             if re.match('(http|https)://.*.(jpg)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'s.jpg')
                 bot.send_photo(m.chat.id, open('s.jpg') ,caption='@king_5bot')
                 os.remove('s.jpg')
             if re.match('(http|https)://.*.(gif)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'s.gif')
                 bot.send_photo(m.chat.id, open('s.gif'),caption='@king_5bot')
                 os.remove('s.gif')
             if re.match('(http|https)://.*.(zip|rar)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.zip')
                 bot.send_document(m.chat.id, open('file.zip'),caption='@king_5bot')
                 os.remove('file.zip')
             if re.match('(http|https)://.*.(webp)$',text):
                 msg = bot.send_message(m.chat.id, '* Downloading .....*',parse_mode='Markdown')
                 dw(text,'file.webp')
                 bot.send_sticker(m.chat.id, open('file.webp'))
                 os.remove('file.webp')
      except IndexError:
                 bot.send_message(m.chat.id, '*Error!\nURL Or Format Is Invalid!*',parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/voice) (.*)')
def voice(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        urllib.urlretrieve("http://tts.baidu.com/text2audio?lan=en&ie=UTF-8&text={}&".format(m.text.replace('/voice', '')), "voice.ogg")
        bot.send_voice(m.chat.id, open('voice.ogg'))
	os.remove('voice.ogg')

#################################################################################################################################################################################################


@bot.message_handler(regexp='^(/webshot) (.*)')
def web(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        urllib.urlretrieve("http://api.screenshotmachine.com/?key=b645b8&size=X&url={}".format(m.text.replace('/webshot', '')), "web.jpg")
        bot.send_photo(m.chat.id, open('web.jpg'))
	os.remove('web.jpg')

#################################################################################################################################################################################################

@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice'])
def all(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        if m.chat.type == 'private':
            if m.photo :
                fileid = m.photo[1].file_id
            elif m.video :
                fileid = m.video.file_id
            elif m.sticker :
                fileid = m.sticker.file_id
            elif m.document :
                fileid = m.document.file_id
            elif m.audio :
                fileid = m.audio.file_id
            elif m.voice :
                fileid = m.voice.file_id
            e = m.from_user.username
            link = urllib2.Request("https://api.pwrtelegram.xyz/bot{}/getFile?file_id={}".format(TOKEN,fileid))
            open = urllib2.build_opener()
            f = open.open(link)
            link1 = f.read()
            jdat = json.loads(link1)
            patch = jdat['result']['file_path']
            send = 'https://storage.pwrtelegram.xyz/{}'.format(patch)
            bot.send_message(m.chat.id,'*File Id:*\n{}'.format(fileid),parse_mode='Markdown')
            bot.send_message(m.chat.id,'File Uploaded\nYour link: {}'.format(send))

#################################################################################################################################################################################################

@bot.message_handler(commands=['calc'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        text = m.text.replace("/calc ","")
        res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text).replace("+","%2B")).read()
        bot.send_message(m.chat.id, "_{}_ = `{}`".format(text,res), parse_mode="Markdown", disable_web_page_preview=True)
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['feedback'])
def feedback(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       try:
          senderid = m.chat.id
          first = m.from_user.first_name
          usr = m.from_user.username
          str = m.text
          txt = str.replace('/feedback', '')
          bot.send_message(senderid, "_Thank Your Msg Posted admin_", parse_mode="Markdown")
          bot.send_message(163509666, "Message : {}\nID : {}\nName : {}\nUsername : @{}".format(txt,senderid,first,usr))
       except:
          bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['uptime'])
def uptime(m):
    if m.from_user.id == 163509666:
        cc = os.popen("uptime").read()
        bot.send_message(m.chat.id, '{}'.format(cc))

#################################################################################################################################################################################################

@bot.message_handler(commands=['md'])
def md(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        pouria = m.text.replace("/md ","")
        bot.send_message(m.chat.id, "{}".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['bold'])
def time(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        pouria = m.text.replace("/bold ","")
        bot.send_message(m.chat.id, "*{}*".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['italic'])
def time(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        pouria = m.text.replace("/italic ","")
        bot.send_message(m.chat.id, "_{}_".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['code'])
def time(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        pouria = m.text.replace("/code ","")
        bot.send_message(m.chat.id, "`{}`".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['hyper'])
def time(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        text = m.text.split()[1]
        tezt = m.text.split()[2]
        bot.send_message(m.chat.id, "[{}]({})".format(text,tezt), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['echo'])
def time(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        pouria = m.text.replace("/echo ","")
        bot.send_message(m.chat.id, "{}".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['ch'])
def time(m):
    pouria = m.text.replace("/send ","")
    bot.send_message(-1001052290909, "{}".format(pouria), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['num'])
def answer(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        x = m.text.split()[1]
        a = len(x)
        bot.send_message(m.chat.id, "*Number Of Your Text :* {}".format(a), parse_mode="Markdown")
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(content_types=['new_chat_participant'])
def send_message(m):
    cid = m.chat.id
    inviter = m.from_user.first_name
    userwhogotadded = m.new_chat_participant.first_name
    username = m.new_chat_participant.username
    groupname = m.chat.title
    groupid = m.chat.id
    rediss.sadd('group','{}'.format(m.chat.id))
    bot.send_message(163509666, "New_chat \n\n name : {} ID : {}".format(groupname,groupid), parse_mode="Markdown")
    bot.send_message(m.chat.id, "Hi all")

#################################################################################################################################################################################################

@bot.message_handler(commands=['sticker'])
def tostick(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        cid = m.chat.id
        if m.reply_to_message:
          if m.reply_to_message.photo:
            token = TOKEN
            fileid = m.reply_to_message.photo[1].file_id
            path1 = bot.get_file(fileid)
            path = path1.file_path
            link = "https://api.telegram.org/file/bot{}/{}".format(token,path)
            urllib.urlretrieve(link, "stick.png")
            file1 = open('stick.png', 'rb')
            bot.send_sticker(cid,file1)
	    os.remove('stick.png')
      except:
            bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/love) (.*) (.*)')
def love(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        text = m.text.split()[1]
        tezt = m.text.split()[2]
        urllib.urlretrieve("http://www.iloveheartstudio.com/-/p.php?t={}%20%EE%BB%AE%20{}&bc=000000&tc=FFFFFF&hc=ff0000&f=c&uc=true&ts=true&ff=PNG&w=500&ps=sq".format(text,tezt), "love.png")
        bot.send_sticker(m.chat.id, open('love.png'))
	os.remove('love.png')

#################################################################################################################################################################################################

@bot.message_handler(commands=['photo'])
def tostick(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        cid = m.chat.id
        if m.reply_to_message:
          if m.reply_to_message.sticker:
            token = TOKEN
            fileid = m.reply_to_message.sticker.file_id
            path1 = bot.get_file(fileid)
            path = path1.file_path
            link = "https://api.telegram.org/file/bot{}/{}".format(token,path)
            urllib.urlretrieve(link, "stick1.png")
            file1 = open('stick1.png', 'rb')
            bot.send_photo(cid,file1)
	    os.remove('stick1.png')
      except:
            bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/info)')
def info(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        if m.reply_to_message:
          id = m.reply_to_message.from_user.id
          user = m.reply_to_message.from_user.username
          first = m.reply_to_message.from_user.first_name
          last = m.reply_to_message.from_user.last_name
        else:
          id = m.from_user.id
          user = m.from_user.username
          first = m.from_user.first_name
          last = m.from_user.last_name
          profs = bot.get_user_profile_photos(id)
          count = profs.total_count
          url = req.get('http://api.gpmod.ir/time/')
          data = url.json()
          ENdate = data['ENdate']
          ENtime = data['ENtime']
          text = bot.get_chat_member(m.chat.id, m.from_user.id).status
          rank = rediss.hget("user:rank","{}".format(id))
          cap = 'First name : {}\nLast Name : {}\nUsername : @{}\nUser ID : {}\nDate : {}\nTime : {}\nGlobalRank : {}\nPost In Group : {}'.format(first,last,user,id,ENdate,ENtime,rank,text)
          fileid = profs.photos[0][2].file_id
          bot.send_photo(m.chat.id,fileid,caption='{}'.format(cap))

#################################################################################################################################################################################################

@bot.message_handler(commands=['setlink'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      if m.chat.type == "group" or m.chat.type == "supergroup":
        text = m.text.replace("/setlink ","")
        rediss.hset("gp:link","{}".format(m.chat.id),"link: {}".format(text))
        bot.send_message(m.chat.id, "`This Link Seted` {}".format(text), parse_mode="Markdown")
      if m.chat.type == "private":
        bot.send_message(m.chat.id, 'Just In Group!')

#################################################################################################################################################################################################

@bot.message_handler(commands=['link'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      if m.chat.type == "group" or m.chat.type == "supergroup":
        link = rediss.hget("gp:link","{}".format(m.chat.id))
        bot.send_message(m.chat.id, "{}".format(link), parse_mode="Markdown")
      if m.chat.type == "private":
        bot.send_message(m.chat.id, 'Just In Group!')

#################################################################################################################################################################################################

@bot.message_handler(commands=['setrank'])
def clac(m):
    if m.from_user.id == 163509666:
        text = m.text.split()[1]
        tezt = m.text.split()[2]
        rediss.hset("user:rank","{}".format(text),"{}".format(tezt))
        rank = rediss.hget("user:rank","{}".format(text))
        bot.send_message(m.chat.id, "`This Rank` *{}* `Seted For` {}".format(rank,text), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['rank'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        id = m.text.replace("/rank ","")
        rank = rediss.hget("user:rank","{}".format(id))
        bot.send_message(m.chat.id, "{}".format(rank), parse_mode="Markdown")
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['bc'])
def clac(m):
    if m.from_user.id == 163509666:
        text = m.text.replace("/bc ","")
        rd = rediss.smembers('memberspy')
        for id in rd:
                bot.send_message(id, "{}".format(text), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['delrank'])
def kick(m):
    if m.from_user.id == 163509666:
        id = m.text.replace("/delrank ","")
        rank = rediss.hdel("user:rank","{}".format(id))
        bot.send_message(m.chat.id, '<code>Cleaned!</code>',parse_mode='HTML')

#################################################################################################################################################################################################

@bot.message_handler(commands=['setsticker'])
def tostick(message):
    try:
     if message.reply_to_message:
       if message.reply_to_message.sticker:
         token = TOKEN
         file_id = message.reply_to_message.sticker.file_id
         id = message.from_user.id
         rediss.hset('stickers',id,file_id)
         bot.send_message(message.chat.id, '<b>Sticker Has Been Set!</b>',parse_mode='HTML')
    except:
         bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['cap'])
def tostick(message):
     try:
      if message.reply_to_message:
        if message.reply_to_message.photo:
          token = TOKEN
          file_id = message.reply_to_message.photo[1].file_id
          id = message.from_user.id
          text = message.text.replace("/cap ","")
          rediss.hset('caption',id,file_id)
          photo = rediss.hget('caption',id)
          bot.send_photo(message.chat.id,photo,caption="{}".format(text))
     except:
          bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['help'])
def welcome(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       cid = m.chat.id
       markup = types.InlineKeyboardMarkup()
       a = types.InlineKeyboardButton("Short",callback_data='short')
       markup.add(a)
       b = types.InlineKeyboardButton("Picture",callback_data='pic')
       markup.add(b)
       c = types.InlineKeyboardButton("Gif",callback_data='gif')
       markup.add(c)
       d = types.InlineKeyboardButton("Tex",callback_data='tex')
       markup.add(d)
       e = types.InlineKeyboardButton("Kickme",callback_data='kickme')
       markup.add(e)
       f = types.InlineKeyboardButton("ID",callback_data='id')
       markup.add(f)
       g = types.InlineKeyboardButton("Me",callback_data='me')
       markup.add(g)
       h = types.InlineKeyboardButton("Food",callback_data='food')
       markup.add(h)
       i = types.InlineKeyboardButton("Voice",callback_data='voice')
       markup.add(i)
       j = types.InlineKeyboardButton("Webshot",callback_data='webshot')
       markup.add(j)
       k = types.InlineKeyboardButton("Mean",callback_data='mean')
       markup.add(k)
       l = types.InlineKeyboardButton("Calculator",callback_data='calc')
       markup.add(l)
       m = types.InlineKeyboardButton("Feedback",callback_data='feedback')
       markup.add(m)
       n = types.InlineKeyboardButton("Bold",callback_data='bold')
       markup.add(n)
       o = types.InlineKeyboardButton("Italic",callback_data='italic')
       markup.add(o)
       p = types.InlineKeyboardButton("Code",callback_data='code')
       markup.add(p)
       q = types.InlineKeyboardButton("Hyperlink",callback_data='hyper')
       markup.add(q)
       r = types.InlineKeyboardButton("Echo",callback_data='echo')
       markup.add(r)
       s = types.InlineKeyboardButton("Number",callback_data='number')
       markup.add(s)
       t = types.InlineKeyboardButton("Sticker",callback_data='sticker')
       markup.add(t)
       u = types.InlineKeyboardButton("Photo",callback_data='photo')
       markup.add(u)
       v = types.InlineKeyboardButton("Love",callback_data='love')
       markup.add(v)
       w = types.InlineKeyboardButton("Info",callback_data='info')
       markup.add(w)
       x = types.InlineKeyboardButton("Setlink",callback_data='setlink')
       markup.add(x)
       y = types.InlineKeyboardButton("Link",callback_data='link')
       markup.add(y)
       z = types.InlineKeyboardButton("Rank",callback_data='rank')
       markup.add(z)
       aa = types.InlineKeyboardButton("SetSticker",callback_data='setsticker')
       markup.add(aa)
       bb = types.InlineKeyboardButton("KeepCalm",callback_data='keepcalm')
       markup.add(bb)
       cc = types.InlineKeyboardButton("SetPhone",callback_data='setphone')
       markup.add(cc)
       dd = types.InlineKeyboardButton("MyPhone",callback_data='myphone')
       markup.add(dd)
       ee = types.InlineKeyboardButton("Caption",callback_data='cap')
       markup.add(ee)
       gg = types.InlineKeyboardButton("Uploader Panel",callback_data='uploader')
       markup.add(gg)
       hh = types.InlineKeyboardButton("Downloader Panel",callback_data='downloader')
       markup.add(hh)
       bot.send_message(cid, "*List Of Commands :*", disable_notification=True, reply_markup=markup, parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(regexp='^(/keepcalm) (.*) (.*) (.*)')
def keep(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        text = m.text.split()[1]
        tezt = m.text.split()[2]
        tect = m.text.split()[3]
        urllib.urlretrieve("http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A{}%0D%0A{}%0D%0A{}&bc=E31F17&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=500&ps=sq".format(text,tezt,tect), "keep.png")
        bot.send_sticker(m.chat.id, open('keep.png'))
	os.remove('keep.png')

#################################################################################################################################################################################################

@bot.message_handler(commands=['setphone'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
        text = m.text.replace("/setphone","")
        rediss.hset("user:phone","{}".format(m.from_user.id),"{}".format(text))
        bot.send_message(m.chat.id, "`This phone` *{}* `Seted For` {}".format(text,m.from_user.username), parse_mode="Markdown")
      except:
        bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(commands=['myphone'])
def clac(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        number = rediss.hget("user:phone","{}".format(m.from_user.id))
        bot.send_contact(m.chat.id, phone_number="{}".format(number), first_name="{}".format(m.from_user.first_name))

#################################################################################################################################################################################################
bot.polling(True)
#end


