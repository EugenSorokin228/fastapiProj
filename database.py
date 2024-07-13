from settings import Settings


DATABASE_URL = f'postgresql+asyncpg://{Settings.DATABASE_USER}:{Settings.DATABASE_PASSWORD}@{Settings.DATABASE_HOST}' \
               f':{Settings.DATABASE_PORT}/{Settings.DATABASE}'