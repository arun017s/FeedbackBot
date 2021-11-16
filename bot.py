#15-11-2021
#okbei

from details import API_ID, API_HASH, BOT_TOKEN, ADMIN, START_IMG, START_MSG, BUTTON_1, BUTTON_2, LINK_1, LINK_2                
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User, Message

Bot = Client(
     session_name="Find-ID-Bot",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)



@Bot.on_message(filters.command(['start']) & filters.private)
async def start(bot, message):
    buttons = [[
                 InlineKeyboardButton(f'{BUTTON_1}', url=f"{LINK_1}"),
                 InlineKeyboardButton(f'{BUTTON_2}', url=f"{LINK_2}")
              ]]

    await message.reply_photo(photo=START_IMG,
                              caption=START_MSG.format(
                                      first = message.from_user.first_name,
                                      last = message.from_user.last_name,
                                      mention = message.from_user.mention,
                                      id = message.from_user.id),
                               reply_markup = InlineKeyboardMarkup(buttons)
                              )

            

@Bot.on_message(filters.command('submit') & filters.private)
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=ADMIN, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=ADMIN, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@Bot.on_message(filters.command('reply') & filters.private)
async def replyt(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                          
@Bot.on_message(filters.command('send') & filters.private)
async def send(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/send"," "))
                                    await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                                    
@Bot.on_message(filters.command('pin') & filters.private)
async def pin(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/pin"," "))
                                    p=await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await p.pin()
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group And pinned</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")
                                    


@Bot.on_message(filters.command('id') & filters.group)
async def id(bot, message):
    await message.reply_text(f"<b>➲ Chat ID:</b> <code>{message.chat.id}</code>")
    
Bot.run()
