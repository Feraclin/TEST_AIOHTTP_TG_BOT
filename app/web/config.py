import typing
from dataclasses import dataclass

import yaml

if typing.TYPE_CHECKING:
    from app.web.app import Application


@dataclass
class SessionConfig:
    key: str


@dataclass
class AdminConfig:
    email: str
    password: str


@dataclass
class BotConfig:
    token_tg: str


@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

@dataclass
class RabbitMQ:
    host: str

@dataclass
class Config:
    admin: AdminConfig
    session: SessionConfig = None
    bot: BotConfig = None
    database: DatabaseConfig = None
    rabbitmq: RabbitMQ = None


def setup_config(app: "Application", config_path: str):
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        session=SessionConfig(
            key=raw_config["session"]["key"],
        ),
        admin=AdminConfig(
            email=raw_config["admin"]["email"],
            password=raw_config["admin"]["password"],
        ),
        bot=BotConfig(
            token_tg=raw_config["bot"]["token_tg"],
        ),
        database=DatabaseConfig(**raw_config["database"]),
        rabbitmq=RabbitMQ(
            host=raw_config["rabbitmq"]["host"],
        ),
    )
