import asyncio
import time
# Define a Coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data ...")
    await asyncio.sleep(delay=delay)
    # time.sleep(delay)
    print("Data Fetched")
    return {"data":"some data"}

# Define another coroutine that calls the first coroutine

async def main():
    print("Start of main coroutine")
    task=fetch_data(delay=2)
    # Await the fetch_data coroutine, pausing execution of main
    # until fetch_data completes
    result=await task
    print(f"Received Result: {result}")
    print("End of main coroutine")

asyncio.run(main=main())