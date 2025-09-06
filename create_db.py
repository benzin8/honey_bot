import asyncio

from backend.database import create_tables

async def main():
    await create_tables()
    print("Tables created successfully.")

if __name__ == "__main__":
    asyncio.run(main())