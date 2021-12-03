from telethon import TelegramClient, events
import random

laugh_emoji=['😂😂😂','🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣','😂😂😂😂😂😂😂😂😂']
api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('LoginIDFile', api_id, api_hash)

@client.on(events.NewMessage)

async def my_event_handler(event):
    print(dir(event.raw_text))
    for msg in event.raw_text:
        class laugh_class(msg):
            def laugh_def(msg):
                if '😂' in msg or '🙃' in msg or '🤣' in msg:
                    if len(event.raw_text) >= 100:
                        await event.reply(random.choice(['😂', '🤣']) * int(random.random() * 1000))
                        break
                    else:
                        await event.reply(random.choice(laugh_emoji))
                        break


client.start()
client.run_until_disconnected()


