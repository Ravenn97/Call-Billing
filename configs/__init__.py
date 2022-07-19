import os
def get_config():


    configs = {}

    configs.update({
        'MONGODB_SETTINGS': {
            'db': os.getenv('MONGODB_DB'),
            'host': os.getenv('MONGODB_HOST'),
            'port': int(os.getenv('MONGODB_PORT', 27017)),
            'username': os.getenv('MONGODB_USERNAME'),
            'password': os.getenv('MONGODB_PASSWORD'),
            "authentication_source": 'admin',
        },
    })


    return configs
