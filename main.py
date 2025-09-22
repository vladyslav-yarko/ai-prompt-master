import asyncio

from src import bot


async def main():
    # Can be other apps
    
    await asyncio.gather(
        bot.run()
    )
