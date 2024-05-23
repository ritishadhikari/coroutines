import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Accessing Resource {resource_id}")
        await asyncio.sleep(delay=1)
        print(f"Releasing resource {resource_id}")

async def main():
    # Allow two concurrent accesses
    semaphore=asyncio.Semaphore(value=3)
    await asyncio.gather(
        *(access_resource(semaphore=semaphore,resource_id=i) for i in range(1,10))
    )
asyncio.run(main=main())
    