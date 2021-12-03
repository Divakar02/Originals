from telethon import TelegramClient, events
import random


api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('LoginIDFile', api_id, api_hash)

laugh_emoji=['😂😂😂','🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣','😂😂😂😂😂😂😂😂😂']
greetings_list=['hai','haii','haiii','haiiii'
                ,'hello','helllo','hlo','hemlo','hemloo','hamlo',
                'vanakam','vanako','vanak','vanakamm','vanacum',]

@client.on(events.NewMessage)

async def my_event_handler(event):
    if event.raw_text.lower() in greetings_list:
        await event.reply(event.raw_text + ' da')

    for msg in event.raw_text:
        if '😂' in msg or '🙃' in msg or '🤣' in msg:
            if len(event.raw_text)>=100:
                await event.reply(random.choice(['😂','🤣'])*int(random.random()*5000))
                break
            else:
                await event.reply(random.choice(laugh_emoji))
                break

client.start()
client.run_until_disconnected()