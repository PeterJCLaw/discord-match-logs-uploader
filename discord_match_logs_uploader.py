import os
import logging

import discord  # type: ignore[import]

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

client = discord.Client()

client.run(os.getenv('DISCORD_TOKEN'))
