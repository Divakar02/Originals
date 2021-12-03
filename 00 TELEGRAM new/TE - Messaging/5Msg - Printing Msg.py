from telethon import TelegramClient

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

async def main():
    me = await client.get_me()

    async for message in client.iter_messages('+919944338187'):
        print(message.id, message.text)

       ''' if message.photo:
            path = await message.download_media()
            print('File saved to', path)'''
with client:
    client.loop.run_until_complete(main())
