import asyncio
import time
import pytest
from hello import hello


def test_hello():
    assert hello("World") == "Hello, World!"


@pytest.mark.asyncio
async def test_async_hello():
    await asyncio.sleep(0.01)
    assert True


async def long_running_task(task_id: int, delay: float):
    print(f"\nСтарт {task_id}")
    await asyncio.sleep(delay)
    print(f"Финиш {task_id}")
    return f"Результат {task_id}"


@pytest.mark.asyncio
async def test_parallel_tasks():
    start_time = time.time()
    results = await asyncio.gather(
        long_running_task(1, 1.0), long_running_task(2, 1.0), long_running_task(3, 1.0)
    )
    total_time = time.time() - start_time
    assert results == ["Результат 1", "Результат 2", "Результат 3"]
    assert total_time < 1.5
