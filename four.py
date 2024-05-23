import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f"Fetching Data ...id:{id}")
    # Simulates an I/O operation with a Sleep
    await asyncio.sleep(delay=delay)
    print(f"Data Fetched, id:{id}")
    return {
        "data": "Some Data",
        "id": id
    }

# Define Another coroutine that calls the first coroutine
async def main():
    task1=fetch_data(delay=2, id=1)
    task2=fetch_data(delay=2,id=2)

    result1=await task1
    print(f"Received Result {result1}")

    result2=await task2
    print(f"Received Result {result2}")


asyncio.run(main=main())