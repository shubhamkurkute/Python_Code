import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched {len(data)} characters from {url}")


async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

# Run the main coroutine
asyncio.run(main())
