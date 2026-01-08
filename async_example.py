import asyncio

async def task1():
    print("start boil water")
    await asyncio.sleep(3)
    print("boil complete")

async def task2():
    print("curry preparing")
    await asyncio.sleep(2)
    print("curry prepared") 

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())