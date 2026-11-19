import httpx
import time
import asyncio

# ссылка на изображение для примера 'https://samplelib.com/png/sample-photo-3840x2160.png'
async def main():
    url = input()
    
    request_count = 10
    total_bytes = 0
    sum_elapsed = 0

    async with httpx.AsyncClient() as client:
        for i in range(request_count):
            start = time.perf_counter()

            response = await client.get(url)
            response.raise_for_status()
            
            elapsed = time.perf_counter() - start
            
            size = len(response.content)

            sum_elapsed += elapsed
            total_bytes += size

            print(
                f"Запрос {i + 1}: "
                f"{elapsed:.4f} сек. | "
                f"{size / 1024:.2f} KB"
            )
    
    avg_elapsed = sum_elapsed / request_count
    total_size_mb = total_bytes / 1024 / 1024
    speed_mb = total_size_mb / sum_elapsed

    print(f"Среднее время запроса: {avg_elapsed:.4f} сек.")
    print(f"Общий объем: {total_size_mb:.2f} MB")
    print(f"Скорость скачивания: {speed_mb:.2f} MB/s")
    

asyncio.run(main())