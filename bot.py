import os

import aiohttp
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    data = {
        'edited_timestamp': message.edited_timestamp.isoformat() if message.edited_timestamp else None,
        'timestamp': message.timestamp.isoformat(),
        'tts': message.tts,
        'type': message.type.name,
        'author_id': message.author.id,
        'author_name': message.author.name,
        'author_discriminator': message.author.discriminator,
        'author_display_name': message.author.display_name,
        'content': message.content,
        'nonce': message.nonce,
        'embeds': message.embeds,
        'channel_id': message.channel.id,
        'channel_name': message.channel.name,
        'server_id': message.server.id,
        'server_name': message.server.name,
        'mention_everyone': message.mention_everyone,
        'mentions': [{'member_id': m.id, 'member_name': m.name, 'member_discriminator': m.discriminator,
                      'member_display_name': m.display_name} for m in message.mentions],
        'channel_mentions': [{'channel_id': c.id, 'channel_name': c.name} for c in message.channel_mentions],
        'role_mentions': message.role_mentions,
        'id': message.id,
        'attachments': message.attachments,
        'pinned': message.pinned,
        'reactions': message.reactions,
        'raw_mentions': message.raw_mentions,
        'raw_channel_mentions': message.raw_channel_mentions,
        'raw_role_mentions': message.raw_role_mentions,
        'clean_content': message.clean_content,
        'system_content': message.system_content
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://980c76cf.ngrok.io/webhook/discord/0/', data=data) as resp:
            print(await resp.text())


client.run(os.environ.get('TOKEN'))
