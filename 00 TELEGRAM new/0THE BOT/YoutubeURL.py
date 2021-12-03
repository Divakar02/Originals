from telethon.tl.types import MessageEntityTextUrl


for entity in event.message:
    if isinstance(entity, MessageEntityTextUrl):
        title=entity.url

for i in URL:
    if i=='🔥':
        print('🔥🔥🔥🔥')