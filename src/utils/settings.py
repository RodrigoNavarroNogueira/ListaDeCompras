from decouple import config


EMAIL = config('EMAIL', cast=str)
PASSWORD = config('PASSWORD', cast=str)
