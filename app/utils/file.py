import os
import aiofiles

BASE_DIR = "/mnt/uploads"   # ✅ use /mnt in production

async def save_to_disk(file: bytes, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    async with aiofiles.open(path, "wb") as f:
        await f.write(file)
