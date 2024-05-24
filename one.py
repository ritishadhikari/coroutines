import asyncio



async def main():
    print("Start of main Coroutine") 

# print(main())  # will not be able to run the coroutine object
# directly
# Run the main coroutine
asyncio.run(main=main())