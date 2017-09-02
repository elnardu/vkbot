import vk
from .config import config


vkapi = vk.API(vk.Session(access_token = config['VKAPI_TOKEN']), v='5.60')

__all__ = ['vkapi']