from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    FASTAPI_HOST: str
    FASTAPI_PORT: str
    API_KEY: str
    URL: str

    MONGO_HOST: str
    KAFKA_BOOTSTRAP_SERVERS: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str

    BOOTSTRAP_SERVERS: str
    KAFKA_ADVERTISED_HOST_NAME: str
    KAFKA_ZOOKEEPER_CONNECT: str
    KAFKA_ADVERTISED_LISTENERS: str
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: str
    KAFKA_INTER_BROKER_LISTENER_NAME: str
    KAFKA_PORTS: str
    KAFKA_BROKER_ID: int
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: int

    ZOOKEEPER_CLIENT_PORT: int
    ZOOKEEPER_TICK_TIME: int
    ZOOKEEPER_PORT: int

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    CELERY_ACCEPT_CONTENT: str
    CELERY_TASK_SERIALIZER: str
    CELERY_RESULT_SERIALIZER: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


setting = Setting()
