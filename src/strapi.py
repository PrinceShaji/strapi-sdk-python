import requests

def strapi(name=None):
    if name is None:
        return "Hello, Welcome to Strapi SDK for Python"
    else:
        return f"Hello {name}, Welcome to Strapi SDK for Python"