# FeedbackBot
Simple Telegram Bot To Get Feedback from users & Some Other Features.

## Features
- Get Feedback from users
- Reply to user's feedback
- Customisable
- Send Messages from bot to your group & pin


### Variables:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your Telegram Bot Token from [@BotFather](https://t.me/BotFather)
4. `ADMIN` : ID of Admin
5. `START_IMG` : Start Message's Photo (Direct Link Of the Image. Use [@vTelegraphBot](t.me/vTelegraphBot))
6. `START_MSG` : Bot's Start Message. You Can Use [These](https://github.com/Arun-TG/Anonymous-Sender#filling) Filling Methods
7. `BUTTON_1` : Text for Start Message's First Button
8. `LINK_1` : Link for Start Message's First Button
9. `BUTTON_2` : Text for Start Message's Second Button
10. `LINK_2` : Link for Start Message's Second Button
11. 'MONGO_URL' :Put your mongo db url

#### Filling
* `{first}` - User first name
* `{last}` - User last name
* `{mention}` - Mention the user
* `{id}` - User ID

## Deploy on Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy in your VPS

```sh
git clone https://github.com/Arun-TG/FeedbackBot
cd FeedbackBot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```
- Don't Forgot to turn on the Dynos
- Don't Forgot to Make the bot admin in your group

### BotFather Commands

```
start - start the bot
submit - submit feedback to admin
reply - reply to user's feedback (admin only)
send - send message to group (admin only)
pin - send and pin that message (admin only)
id - get chat id (only in groups)
stats - to get number of users

```

### Usage
- Use `/reply` command along with the user's ID 
- Use `/send` , `/pin` commands along with the group's ID ( If you don't know the group ID, Make the bot admin in your group and send `/id` )

### Examples
- [Feedback Submission](https://telegra.ph/file/5903019f80a639a896f07.jpg)
- [Reply To Feedback](https://telegra.ph/file/7fe376459a981ccda3579.jpg)
- [Sending Message to Group](https://telegra.ph/file/1876e91609dac3bc29462.jpg)
- [Send and Pin Message](https://telegra.ph/file/c6e2e8baecbf7db14fb70.jpg)

## To-Do
- Broadcast
- Number of users(done)
- Ban & Unban

# Credits
* [Pyrogram](https://github.com/pyrogram/pyrogram)
* [Arun](https://github.com/Arun-TG)
