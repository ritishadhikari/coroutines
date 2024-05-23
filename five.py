import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    returnDict={
        "id": id,
        "data": f"Sample Data from Coroutine {id}"
    } 
    print(returnDict)

async def main():
    # Create Tasks for running coroutines concurrently
    task1=asyncio.create_task(coro=fetch_data(id=1,sleep_time=2))
    task2=asyncio.create_task(coro=fetch_data(id=2,sleep_time=3))
    task3=asyncio.create_task(coro=fetch_data(id=3,sleep_time=1))

    result1=await task1
    result2=await task2
    result3=await task3

    # print(result2,result3,result1)

asyncio.run(main=main())