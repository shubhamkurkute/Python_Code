# asyncio is a library to write concurrent code using the async/await syntax.
# Like Kotlin here also we use coroutines.
# Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. 


import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(main())