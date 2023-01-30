from tortoise import Tortoise, run_async
import settings

async def main():
    await settings()
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(main())