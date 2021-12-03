from telethon import TelegramClient

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

async def main():
    me = await client.get_me()
    # getting all ID's **in chat
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    # sending msg
    await client.send_message('+919944338187',"Haii")
    await client.send_message(1931256305, 'Hello, myself!')

with client:
    client.loop.run_until_complete(main())
