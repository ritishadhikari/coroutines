import asyncio

async def waiter(event):
    print("Waiting for the event to be set")
    await event.wait()
    print("Event has been set, continuing execution")

async def setter(event):
    # Simulate doing some work
    print("Event setting up")
    await asyncio.sleep(delay=2)
    event.set()
    print("Event has been set")

async def main():
    event=asyncio.Event()
    await asyncio.gather(
        waiter(event=event),
        setter(event=event)
    )

asyncio.run(main=main())