import asyncio

from src import bot


async def main():
    # Can be other apps
    
    await asyncio.gather(
        bot.run()
    )


if __name__ == "__main__":
    asyncio.run(main())
