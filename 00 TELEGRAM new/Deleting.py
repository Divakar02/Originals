from telethon import TelegramClient,events

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

@client.on(events.NewMessage(pattern=r'(?i).*youtube'))
async def handler(event):
    await event.delete()

client.start()
client.run_until_disconnected()
