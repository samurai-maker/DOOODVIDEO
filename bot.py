from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from main import get_link
from gencover import gen_cover
import urllib.request
import os
from os import getenv

a1 = int(getenv("API_ID"))
a2 = getenv("API_HASH")
b1 = getenv("BOT_TOKEN")
c1 = getenv("COMMAND_NAME")

app = Client("dood", 
             api_id = a1,
             api_hash = a2,
             bot_token = b1)

@app.on_message(filters.command('start') & filters.private)
def start(__, m:Message):
    m.reply_chat_action("typing")
    m.reply_text("Dood Uploader bot made by @nousername_psycho")
    
@app.on_message(filters.command(c1))
def doodupload(__, m:Message):
    if not m.reply_to_message:
        m.reply_chat_action("typing")
        m.reply_text("Reply To a video")
        return
    if not m.reply_to_message.video:
        m.reply_chat_action("typing")
        m.reply_text("Reply To a video")
        return   
    arg = m.text.split()
    if len(arg) == 1:
        m.reply_chat_action("typing")
        m.reply_text("Plz Type Caption.")
        return
    cap =arg[1:]
    qq = ''
    f_name = f'videos/newupload-{m.message_id}.mp4'
    for x in cap:
        qq += ' ' + str(x) 
    m.reply_chat_action("typing")
    m1 = m.reply_text(f"Alright Downloading Video..")
    app.download_media(m.reply_to_message.video.file_id, file_name= f_name)
    m.reply_chat_action("typing")
    m1.edit("Downloading Finished... Now Uploading to Dood")
    data = get_link(f_name, qq)
    m.reply_chat_action("typing")
    m1.edit("Everything Ok Uploading Data")
    link = data['result'][0]['download_url']
    img = data['result'][0]['single_img']
    ss = data['result'][0]['splash_img']
    title = data['result'][0]['title']
    bg = f"BG{m.message_id}.jpg"
    req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
    with open(bg, "wb") as f:
        with urllib.request.urlopen(req) as r:
            f.write(r.read())
    pic = gen_cover(bg, m.message_id)
    m.reply_chat_action("upload_photo")
    m.reply_photo(photo=pic,
                  caption=f"**🌀 {qq} 🌀**"
                            f"\n\n☉  **Watch Now 💦**"
                            f"\n└ **{link}**"
                            f"\n└ **{link}**"
                            f"\n\n☉ **[Screenshots]({ss}) **📸"
                            f"\n\n**═══[@kidu_network2 ❤️]═══**\n")
                           
    
    m1.delete()
    os.remove(f_name)
    os.remove(bg)
    os.remove(pic)
    
app.run()
