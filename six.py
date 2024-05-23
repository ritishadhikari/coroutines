import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    # Simulate a network request or IO Exception
    await(asyncio.sleep(sleep_time))
    # Return some data as a result
    returnDict= {
        "id": id, 
        "data": f"Sample data from coroutine {id}"
    }
    print(returnDict)

async def main():
    # Run Coroutines concurrently and gather their return values
    # gather is not good with error handling
    results=await asyncio.gather(
        fetch_data(id=1,sleep_time=2),
        fetch_data(id=2, sleep_time=1),
        fetch_data(id=3,sleep_time=3)
    )
    for result in results:
        result

asyncio.run(main=main())