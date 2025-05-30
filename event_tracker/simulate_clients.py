import asyncio
import aiohttp
async def simulate_client():
    pass  # TODO
async def main():
    await asyncio.gather(*(simulate_client() for _ in range(100)))
if __name__ == "__main__":
    asyncio.run(main())
