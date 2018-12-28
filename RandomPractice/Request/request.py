import requests

def url_request(*args: str):
  urls = (args)

  try:
    for resp in (requests.get(url) for url in urls):
      print(len(resp.content), "->", resp.status_code, "->", resp.url)
  except Exception as err:
    print("Something went wrong:", err)
