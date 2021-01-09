import os
import logging

import discord  # type: ignore[import]

logger = logging.getLogger(__name__)

client = discord.Client()

client.run(os.getenv('DISCORD_TOKEN'))
