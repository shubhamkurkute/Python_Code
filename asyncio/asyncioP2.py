# Here’s an example that simulates I/O-bound tasks using asyncio.sleep() to represent network latency or file operations.

import asyncio


async def fetch_data(delay, name):
    print(f"Starting task: {name}")
    await asyncio.sleep(delay)
    print(f"Task completed: {name}")


async def main():
    tasks = [
        fetch_data(2, "Task 1"),
        fetch_data(3, "Task 2"),
        fetch_data(1, "Task 3"),
    ]
    await asyncio.gather(*tasks)        # Runs all the task concurrently

asyncio.run(main())