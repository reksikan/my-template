from os import getenv

# Server settings
SERVER_PORT = int(getenv('SERVER_PORT', '8000'))
SERVER_HOST = getenv('SERVER_HOST', '127.0.0.1')

# Database settings
POSTGRES_HOST = getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = getenv('POSTGRES_PORT', '5432')
POSTGRES_LOGIN = getenv('POSTGRES_LOGIN', 'postgres')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', 'postgres')

# TODO: CHANGE ON REAL PROJECT
POSTGRES_DATABASE = getenv('POSTGRES_DATABASE', 'template')
POSTGRES_URL = (
    f'postgresql+asyncpg://{POSTGRES_LOGIN}:{POSTGRES_PASSWORD}@'
    f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}'
)

POSTGRES_TEST_DATABASE = getenv('POSTGRES_TEST_DATABASE', 'test_' + POSTGRES_DATABASE)
POSTGRES_TEST_URL = (
    f'postgresql+asyncpg://{POSTGRES_LOGIN}:{POSTGRES_PASSWORD}@'
    f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_TEST_DATABASE}'
)
