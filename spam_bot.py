from telethon import TelegramClient
import time

api_id = 111
api_hash = ''
name = 'anon'
chat = 'me'


with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
# TelegramClient.


async def main():
    group = await client.get_peer_id('t.me/0000')
    while True:
        await client.send_message(group,
        'jj',
        comment_to=60)
        # mes = await client.get_messages(group)
        # print(mes)
        # await client.send_message(group, 'Я СПАМ Бот')
        time.sleep(1)

def test1():
    try:
        with client:
            client.loop.run_until_complete(main())
    except:
        test()

def test():
    time.sleep(1)
    test1()

test()