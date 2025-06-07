import os

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

DEBUG = os.getenv("DEBUG", False)

SHOULD_USE_SWAGGER = os.getenv("SHOULD_USE_SWAGGER", True)
SWAGGER_URL = os.getenv("SWAGGER_URL", "/api/docs")
