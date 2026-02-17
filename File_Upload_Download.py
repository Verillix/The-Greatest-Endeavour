from dotenv import dotenv_values
config = dotenv_values(".env")
print(dict(config))