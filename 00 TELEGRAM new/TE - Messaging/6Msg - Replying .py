from telethon import TelegramClient

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

async def main():
    async for message in client.iter_messages('+919944338187'):
        if message.text=='Naku':
            await message.reply('Nakkuran') #replies to latest text
            break

with client:
    client.loop.run_until_complete(main())
