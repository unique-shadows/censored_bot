from telethon import TelegramClient, events
from telethon.tl.custom.button import Button
from . import censored
from os import getenv

api_id = getenv("API_ID")
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")

bot = TelegramClient(
    'Bot',
    api_id=api_id,
    api_hash=api_hash

).start(
    bot_token=bot_token

)

async def getMe(bot):
    global bot_username, bot_name
    bot_user = await bot.get_me()
    bot_username = bot_user.username

@bot.on(events.NewMessage(pattern='/start'))
async def do(event):
    if event.is_private:
        await event.respond(
            f"Hi, Add me to your channel or group",
            buttons=Button.url(
                "Add +",
                url=f"https://t.me/{bot_username}?startgroup=true"
            )
        )

@bot.on(events.NewMessage(pattern=censored))
async def do(event):
    if not event.is_private:
        await event.delete()
        await event.respond("Message deleted due to censored words")