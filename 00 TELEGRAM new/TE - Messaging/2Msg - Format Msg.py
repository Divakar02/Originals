from telethon import TelegramClient

api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'
client=TelegramClient('Me', api_id, api_hash)

async def main():
    me = await client.get_me()

    # bold,italics,monospace
    message=await client.send_message('+919944338187',"**haii**")
    await client.send_message('+919944338187',"__italic__")
    await client.send_message('+919944338187', "_`monospace`_",link_preview=False)

    # hyperlinks
    await client.send_message('+919944338187', "a [nice website](https://example.com)!")

    print(message.raw_text)


with client:
    client.loop.run_until_complete(main())
