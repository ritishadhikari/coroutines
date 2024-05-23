import asyncio

# Define a Coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data ...")
    await asyncio.sleep(delay=delay)
    print("Data Fetched")
    return {"data":"some data"}

async def main():
    print("Start of main Coroutine") 

# print(main())  # will not be able to run the coroutine object
# directly
# Run the main coroutine
asyncio.run(main=main())