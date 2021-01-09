import os
import sys
import asyncio
import logging

import discord  # type: ignore[import]

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

client = discord.Client()

# Add to a Guild ("Server") by visiting the following while logged in to Discord:
# https://discord.com/api/oauth2/authorize?client_id=797523543101145158&scope=bot&permissions=35840

messages = {
    'team-abc': "Bees",
    'general': "Ponies",
}

FILE_TO_UPLOAD = '/tmp/face.zip'


async def upload_logs() -> None:
    guild, = client.guilds

    sends = []
    for channel in guild.channels:
        message = messages.get(channel.name)
        if message:
            if not isinstance(channel, discord.TextChannel):
                logger.error(
                    f"#{channel.name} is not a text channel, unable to send message",
                )
                continue

            sends.append(channel.send(
                content=message,
                file=discord.File(FILE_TO_UPLOAD),
            ))

    await asyncio.gather(*sends)

    logger.info("Done uploads")


@client.event
async def on_ready() -> None:
    logger.info(f"{client.user} has connected to Discord!")

    try:
        await upload_logs()
    finally:
        logger.info("Done, closing")
        await client.close()


# DISCORD_TOKEN needs to be the secret token for the bot.
client.run(os.getenv('DISCORD_TOKEN'))
