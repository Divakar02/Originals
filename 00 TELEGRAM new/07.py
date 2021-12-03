from telethon import TelegramClient,events

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):

    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    print(chat_id)
    print(sender_id)

async def main():


client.start()
client.run_until_disconnected()

