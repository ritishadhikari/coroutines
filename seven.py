import asyncio

# A shared variable
shared_resource=0

# An asyncio Lock
lock=asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical Section Starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource+=1  # Modify shared resource
        await asyncio.sleep(delay=1)
        print(f"Resource after modification: {shared_resource}")
        # Critical Section Ends
    
async def main():
    await asyncio.gather(
        *(modify_shared_resource() for _ in range(5))
    )

asyncio.run(main=main())

