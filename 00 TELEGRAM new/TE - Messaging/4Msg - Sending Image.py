from telethon import TelegramClient

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

async def main():
    me = await client.get_me()

    await client.send_file('+919944338187',"C:/Users/Divakar/Pictures/jiraya.jpg")


with client:
    client.loop.run_until_complete(main())
