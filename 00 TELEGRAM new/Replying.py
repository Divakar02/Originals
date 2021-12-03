from telethon import TelegramClient, events
import random


api_id=2100258059
api_hash='AAGc05QAq0cm3dhizL6OumbWwDL1IrSX-q0'
client=TelegramClient('Me', api_id, api_hash)

laugh_emoji=['😂😂😂','🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣','😂😂😂😂😂😂😂😂😂']
greetings_list=['hai','haii','haiii','haiiii'
                ,'hello','helllo','hlo','hemlo','hemloo','hamlo',
                'vanakam','vanako','vanak','vanakamm','vanacum',]

@client.on(events.NewMessage)

@client.on(events.NewMessage(outgoing=True, pattern=r'\.save'))

async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        await client.download_profile_photo(sender)
        await event.respond('Saved your photo {}'.format(sender.username))
# async def my_event_handler(event):
#     if event.raw_text.lower() in greetings_list:
#         await event.reply(event.raw_text + ' da')
#
#     for msg in event.raw_text:
#         if '😂' in msg or '🙃' in msg or '🤣' in msg:
#             if len(event.raw_text)>=100:
#                 await event.reply(random.choice(['😂','🤣'])*int(random.random()*5000))
#                 break
#             else:
#                 await event.reply(random.choice(laugh_emoji))
#                 break



client.start()
client.run_until_disconnected()