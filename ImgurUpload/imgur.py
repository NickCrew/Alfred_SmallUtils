from imgurpython import ImgurClient
import sys
import os

client_id = os.environ.get("IMGUR_CLIENT_ID")
secret = os.environ.get("IMGUR_SECRET")

client = ImgurClient(client_id, secret)

path = sys.argv[1]

r = client.upload_from_path(path, config=None, anon=True)

returnURL = r["link"]

r = returnURL

print(r)


