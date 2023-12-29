
import requests
import json
import os
import telebot 
from telebot import types
from helper import *
from data import *


bot = telebot.Telebot('2144894853:AAGQUvVcBewUNDUGuOAjQ1g_nepP_DcNqcM')


def select(cid):
    connect = None
    try:
        connect = pymysql.connect(
            host="localhost",
            user="rajabovbehruz_vidtok",
            password="VidTok55",
            database="rajabovbehruz_vidtok"
        )
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM vid_like")
        query = cursor.fetchall()
        txt = []
        for row in query:
            if str(cid) in row['vid_liked']:
                continue
            else:
                txt.append(str(row['id']))
        random.shuffle(txt)
        id = txt[0]
        return id
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connect:
            connect.close()

def add(id, cid, cqid):
    connect = None
    try:
        connect = pymysql.connect(
            host="localhost",
            user="rajabovbehruz_vidtok",
            password="VidTok55",
            database="rajabovbehruz_vidtok"
        )
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM vid_like WHERE id = {id}")
        row = cursor.fetchone()
        if str(cid) in row['vid_liked']:
            bot('answerCallbackQuery', {
                'callback_query_id': cqid,
                'chat_id': cid,
                'text': "Like bosilgan❤️",
                'show_alert': False
            })
        else:
            tx = row['vid_liked'] + " " + str(cid)
            cursor.execute(f"UPDATE vid_like SET vid_liked = '{tx}' WHERE id = {id}")
            connect.commit()
            bot('answerCallbackQuery', {
                'callback_query_id': cqid,
                'chat_id': cid,
                'text': "Like bosildi❤️",
                'show_alert': True
            })
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connect:
            connect.close()

def follow(id, cid, cqid):
    connect = None
    try:
        connect = pymysql.connect(
            host="localhost",
            user="rajabovbehruz_vidtok",
            password="VidTok55",
            database="rajabovbehruz_vidtok"
        )
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM profile WHERE user_id = {id}")
        row = cursor.fetchone()
        if str(cid) in row['follower']:
            bot('answerCallbackQuery', {
                'callback_query_id': cqid,
                'chat_id': cid,
                'text': "Siz obuna bo'lgansiz👤",
                'show_alert': False
            })
        else:
            tx = row['follower'] + " " + str(cid)
            cursor.execute(f"UPDATE profile SET follower = '{tx}' WHERE user_id = {id}")
            connect.commit()
            bot('answerCallbackQuery', {
                'callback_query_id': cqid,
                'chat_id': cid,
                'text': "Obuna bo'lindi👤",
                'show_alert': True
            })
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connect:
            connect.close()

@bot.message_handler()
def main(message):
    chat_id = message.chat.id
    message_id = message.id
    from_id = message.user_from.id
    text = message.text
    first_name = message.user_from.first_name
    last_name = message.user_from.last_name
    username = message.user_from.username
    video = message.video
    video_id = message.video.id
    video_size = message.video.video_size
    video_time = message.video.duration
    contact = message.contact
    contactid = message.contactid
    contactnum = message.contact.phone_number

def inline_s(inline_query):
        inline = inline_query.query
        chatsid = inline_query.from_user.id
        
        
def main_1(callback):        
        data = callback.data
        ccid = callback.message.chat.id
        cid2 = callback.message.chat.id
        mid2 = callback.message.id
        cqid = callback.id
        messageid = callback.message.id        

        os.mkdir("profil/" + str(from_id))
        os.mkdir("step")
        step = open("step/" + str(from_id) + ".step").read()
        activecode = open("profil/" + str(from_id) + "/code.txt").read()
        whois = open("profil/" + str(from_id) + "/whois.txt").read()
        phonenumber = open("profil/" + str(from_id) + "/contact.txt").read()
        key = main_key()

        if whois == "true":
            if text == "🏠":
                id = select(chat_id)
                cursor = connect.cursor()
                cursor.execute(f"SELECT * FROM vid_like WHERE id = {id}")
                row = cursor.fetchone()
                owner = row['owner']
                caption = row['caption']
                caption = base64.b64decode(caption).decode('utf-8')
                if caption == True:
                    pass
                else:
                    caption = "🤖Telegram Bot Kerakmi? \n@Akhatkulov'ga murojaat qiling😉"
                cursor.execute(f"SELECT * FROM profile WHERE user_id = {owner}")
                rowus = cursor.fetchone()
                user_name = rowus['username']
                cursor.execute(f"SELECT * FROM profile WHERE user_id = {owner}")
                arrays = cursor.fetchone()
                def send_video(message):
                    chat_id = message.chat.id
                    video_url = row['vid_url']  # Replace with the actual video URL
                    user_name = message.from_user.username  # Replace with the actual username
                    owner = row['owner']  # Replace with the actual owner ID
                    caption = "Your video caption"  # Replace with the actual caption
                    reply_markup = telebot.types.InlineKeyboardMarkup()
                    reply_markup.row(
                        telebot.types.InlineKeyboardButton(text=str(len(row['vid_liked'].split(' '))) + ' ❤️', callback_data='like_' + str(row['id'])),
                        telebot.types.InlineKeyboardButton(text='➡️', callback_data='next_' + str(row['id']))
                    )
                    reply_markup.row(
                        telebot.types.InlineKeyboardButton(text=str(len(arrays['follower'].split(' '))) - 1 + ' ➕', callback_data='follow_' + str(row['owner']))
                    )
                    bot.send_video(chat_id, video=video_url, caption=f"[{user_name}](tg://user?id={owner})\n*{caption}*", parse_mode="Markdown", reply_markup=reply_markup)
                send = send_video()
                json.dump(send, open('jsonerr.json', 'w'))
                en = json.load(open('jsonerr.json'))
                if en['description'] == "Bad Request: there is no video in the request":
                    bot.sendMessage(chat_id=chat_id,text="Siz like bosmagan video qolmadi")
        if 'callback_query' in update:
            ex = data.split("_")
            if ex[0] == "like":
                id = ex[1]
                add(id, cid2, cqid)
            elif ex[0] == "follow":
                id = ex[1]
                follow(id, cid2, cqid)
            elif ex[0] == "next":
                id = select(cid2)
                cursor = connect.cursor()
                cursor.execute(f"SELECT * FROM vid_like WHERE id = {id}")
                row = cursor.fetchone()
                owner = row['owner']
                caption = row['caption']
                caption = base64.b64decode(caption).decode('utf-8')
                if caption == True:
                    pass
                else:
                    caption = "🤖Telegram Bot Kerakmi? \n@SeniorCik ga murojaat qiling😉"
                cursor.execute(f"SELECT * FROM profile WHERE user_id = {owner}")
                rowus = cursor.fetchone()
                user_name = rowus['username']
                cursor.execute(f"SELECT * FROM profile WHERE user_id = {owner}")
                arrays = cursor.fetchone()
                bot('DeleteMessage', {
                    'chat_id': cid2,
                    'message_id': mid2
                })
                send = bot('sendVideo', {
                    'chat_id': cid2,
                    'video': row['vid_url'],
                    'caption': f"[{user_name}](tg://user?id={owner})\n*{caption}*",
                    'parse_mode': "markdown",
                    'reply_markup': json.dumps({
                        'inline_keyboard': [
                            [{'text': str(len(row['vid_liked'].split(' '))) + ' ❤️', 'callback_data': 'like_' + str(row['id'])},
                             {'text': '➡️', 'callback_data': 'next_' + str(row['id'])}],
                            [{'text': str(len(arrays['follower'].split(' '))) - 1 + ' ➕', 'callback_data': 'follow_' + str(row['owner'])}]
                        ]
                    })
                })
                json.dump(send, open('jsonerr.json', 'w'))
                en = json.load(open('jsonerr.json'))
                if en['description'] == "Bad Request: there is no video in the request":
                    bot('sendmessage', {
                        'chat_id': cid2,
                        'text': "Siz like bosmagan video qolmadi"
                    })
        type = message['chat']['type']
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM profile WHERE user_id = {chat_id}")
        userd = cursor.fetchone()
        if type == "private":
            if str(chat_id) in userd:
                pass
            else:
                cursor.execute(f"INSERT INTO profile(user_id, username) VALUES ({chat_id}, '')")
                connect.commit()
        if text == "/start" and whois != "true":
            bot('sendmessage', {
                'chat_id': chat_id,
                'text': f"Xush kelibsiz 🌟 <a href='tg://user?id={from_id}'>{first_name}</a>\n💁🏻‍♂️Men VidTok , Video Resurs Botman\n👇Botdan foydalanish uchun ro'yxatdan o'ting!!",
                'parse_mode': 'html',
                'reply_markup': json.dumps({
                    'inline_keyboard': [
                        [{'text': '📬Email kiritish', 'callback_data': 'email'}]
                    ]
                })
            })
        if data == "email":
            bot('EditMessageText', {
                'chat_id': ccid,
                'message_id': messageid,
                'text': "Emailingizni kiriting...(oxiri @gmail.com bilan tugallanishi kerak!)"
            })
            open("step/" + str(ccid) + ".step", "w").write("whois")
        if text != "/start" and step == "whois":
            offset1 = text.find("@gmail")
            offset2 = text.find(".com")
            if offset1 != -1 and offset2 != -1 and text != "/start" and step == "whois":
                open("step/" + str(from_id) + ".step", "w").write("activecode")
                rand = random.randint(1000, 9999)
                open("profil/" + str(from_id) + "/code.txt", "w").write(str(rand))
                open("profil/" + str(from_id) + "/email.txt", "w").write(text)
                cursor.execute(f"UPDATE profile SET email = '{text}' WHERE user_id = {chat_id}")
                connect.commit()
                subject = "Active code"
                message = f"VidTok active code : {rand}"
                from_ = "admin@vidtok"
                headers = "From:" + from_
                mail(text, subject, message, headers)
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': f"Tasdiqlash kodi {text} elektron pochtaga yuborildi✔️\nKodni kiriting : (Kod bormagan bo’lsa SPAM qutisini qarang!!!)",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Bu elektron pochta manzili emas!🚫",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
        if text != "/start" and step == "activecode":
            if text == activecode:
                open("step/" + str(from_id) + ".step", "w").write("contact")
                open("profil/" + str(from_id) + "/whois.txt", "w").write("true")
                os.unlink("profil/" + str(from_id) + "/code.txt")
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Tabriklayman🌹\nBotda shaxsiy akkaunt yaratdingiz😉\nEmailingiz: " + email + "\nEndi pastdagi tugmani bosib Telefon raqamingizni yuboring😊",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id,
                    'reply_markup': json.dumps({
                        'keyboard': [
                            [{'text': 'Telefon Nomer Yuborish', 'request_contact': True}]
                        ],
                        'resize_keyboard': True
                    })
                })
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Tasdiqlash kodi xato🚫\nIltimos Emailingizga yuborilgan kodni kiriting❗️\n(Spam qutisini ham qarang!)",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
        if contact and step == "contact":
            if contactid == from_id:
                open("profil/" + str(from_id) + "/contact.txt", "w").write(contactnum)
                open("step/" + str(from_id) + ".step", "w").write("none")
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Bosh menu🏠",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id,
                    'reply_markup': json.dumps({
                        'resize_keyboard': True,
                        'keyboard': [
                            [{'text': '🏠'}, {'text': '🔎'}],
                            [{'text': '⁉️'}, {'text': '➕'}, {'text': '👤'}]
                        ]
                    })
                })
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Xato❌",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
        admin = "1744874235"
        if text == "/send" and chat_id == admin:
            bot('sendmessage', {
                'chat_id': chat_id,
                'text': "<i>Userlarga yubormoqchi  bo'lgan xabaringizni kiriting...</i>",
                'parse_mode': 'html'
            })
            open("step/" + str(chat_id) + ".step", "w").write("send")
        if step == "send" and text != "/send" and text != "send" and text != "/start" and text != "/cancel":
            x = 0
            y = 0
            cursor.execute("SELECT * FROM profile")
            query = cursor.fetchall()
            for row in query:
                us = row['user_id']
                ok = bot('ForwardMessage', {
                    'chat_id': us,
                    'from_chat_id': admin,
                    'message_id': message_id
                })['ok']
                if ok == True:
                    x += 1
                else:
                    y += 1
            bot('sendMessage', {
                'chat_id': chat_id,
                'text': f"✅<i>Send message</i>\nYuborildi: {x} ta\nYuborilmadi: {y} ta",
                'parse_mode': 'html'
            })
            os.unlink("step/" + str(chat_id) + ".step")
            return
        if text == "/cancel":
            bot('SendMessage', {
                'chat_id': chat_id,
                'text': "Bekor Qilindi!",
                'parse_mode': "html"
            })
            os.unlink("step/" + str(chat_id) + ".step")
            return
        cursor.execute("SELECT * FROM profile")
        stat = len(cursor.fetchall())
        if text == "/stat":
            bot('SendMessage', {
                'chat_id': chat_id,
                'text': f"📈 <b>Bot statistikasi:</b>\n👤 Userlar: <b>{stat}</b>\n<b>@VidTok⚡️</b>",
                'parse_mode': "html"
            })
            return
        if whois == "true":
            if text == "👤":
                emailm = cursor.execute(f"SELECT * FROM profile WHERE user_id = {chat_id}")
                ab = cursor.fetchone()
                gmail = ab['email']
                username = ab['username']
                if username == True:
                    pass
                else:
                    username = "Username Kiritilmagan"
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': f"🎗{first_name} {last_name} Ma'lumotlaringiz:\n🔎 {username}\n🆔 {chat_id}\n📧 {gmail}\n📞 +{phonenumber}",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id,
                    'reply_markup': json.dumps({
                        'resize_keyboard': True,
                        'inline_keyboard': [
                            [{'text': "🔎 Username o'zgartirish", 'callback_data': "editusername"}]
                        ]
                    })
                })
                return
        if data == "editusername":
            bot('EditMessageText', {
                'chat_id': ccid,
                'message_id': messageid,
                'text': "Username kiriting!!"
            })
            open("step/" + str(ccid) + ".step", "w").write("edituser")
            return
        if text != "/start" and step == "edituser":
            cursor.execute(f"SELECT * FROM profile WHERE username = '{text}'")
            row = cursor.fetchone()
            if not row and step == "edituser":
                cursor.execute(f"UPDATE profile SET username = '{text}' WHERE user_id = {from_id}")
                connect.commit()
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': f"🔎{text} - Username saqlandi",
                    'reply_to_message_id': message_id
                })
                os.unlink("step/" + str(from_id) + ".step")
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Username Band!🚫",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
            return
        if whois == "true":
            if text == "���":
                bot('SendMessage', {
                    'chat_id': chat_id,
                    'message_id': message_id,
                    'text': "Username kiriting...(Bekor qilish uchun /cancel)"
                })
                open("step/" + str(chat_id) + ".step", "w").write("searchus")
                return
        if text != "/start" and step == "searchus":
            cursor.execute(f"SELECT * FROM profile WHERE username = '{text}'")
            row = cursor.fetchone()
            if row and step == "searchus":
                rowid = row['user_id']
                cursor.execute(f"SELECT * FROM vid_like WHERE owner = {rowid}")
                resultvid = cursor.fetchall()
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': f"🔎{text} Videolari:"
                })
                for row in resultvid:
                    caption = row['caption']
                    caption = base64.b64decode(caption).decode('utf-8')
                    time.sleep(0.8)
                    bot('SendVideo', {
                        'chat_id': chat_id,
                        'video': row['vid_url'],
                        'caption': caption,
                        'reply_markup': json.dumps({
                            'inline_keyboard': [
                                [{'text': str(len(row['vid_liked'].split(' '))) + ' ❤️', 'callback_data': 'like_' + str(row['id'])}]
                            ]
                        })
                    })
                os.unlink("step/" + str(from_id) + ".step")
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Username Mavjud Emas!🚫",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
            return
        if whois == "true":
            if text == "/start":
                os.unlink("step/" + str(from_id) + ".step")
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Bosh menu🏠",
                    'reply_to_message_id': message_id,
                    'reply_markup': key
                })
                return
        if whois == "true":
            if text == "➕":
                cursor.execute(f"SELECT * FROM profile WHERE user_id = {chat_id}")
                row = cursor.fetchone()
                usernem = row['username']
                if usernem == True:
                    open("step/" + str(from_id) + ".step", "w").write("video")
                    bot('sendMessage', {
                        'chat_id': chat_id,
                        'text': "😊Marhamat videongizni yuboring❗️\n⚠️Eslatma: Video davomiyligi 1daqiqadan ko'p bo'lmasligi lozim",
                        'reply_to_message_id': message_id
                    })
                else:
                    bot('SendMessage', {
                        'chat_id': chat_id,
                        'text': "Siz username kiritmagansiz, oldin username kiriting, keyin video qo'shishingiz mumkin❗️"
                    })
                return
        video_vaqti = 100
        if video and step == "video":
            if video_time <= video_vaqti:
                caption = message['caption']
                caption = caption.replace("'", "")
                caption = caption.replace("`", "")
                open("step/" + str(from_id) + ".step", "w").write("none")
                file_id = message['video']['file_id']
                captin = base64.b64encode(caption.encode('utf-8')).decode('utf-8')
                if captin == True:
                    pass
                else:
                    captin = ""
                cursor.execute(f"INSERT INTO vid_like(caption, vid_url, vid_liked, owner) VALUES ('{captin}', '{file_id}', '{chat_id}', '{chat_id}')")
                connect.commit()
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': f"<b><u>Video saqlandi! </u></b>{connect.error}",
                    'parse_mode': "html"
                })
            else:
                bot('sendMessage', {
                    'chat_id': chat_id,
                    'text': "Xato❌ (" + str(video_time) + ")",
                    'parse_mode': "HTML",
                    'reply_to_message_id': message_id
                })
            return

if __name__ == "__main__":
    main()


