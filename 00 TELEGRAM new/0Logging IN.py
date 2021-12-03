
from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 8703870
api_hash = 'ac7b8593e61fd1ea831e582016dfa090'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('Me', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('Me', 'Hello, myself!'))