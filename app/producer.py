import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer

from config.config import setting


async def send_update_asset_info(message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=setting.BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        await producer.send_and_wait("Asset", json.dumps(message).encode("utf-8"))
        logging.info(f"Message sent {message}")
    except Exception as e:
        logging.info(f"Error - {e}")
    finally:
        await producer.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            send_update_asset_info({"message": "bbbbbbbbb"})
        )  # for testing
    finally:
        loop.close()
