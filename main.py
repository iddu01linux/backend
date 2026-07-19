from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import requests
import os
import sys
import shutil

backendContentFile = "resources.zip"
backendCoursesFile = "resources/main.json"
resourcesUrl = "https://github.com/FOSSLingo/resources/archive/refs/heads/main.zip"

vercelBackendContentFile = "/tmp/resources.zip"
vercelBackendCoursesFile = "resources/main.json"

def vercelCheck():
  return os.environ.get("VERCEL") == "1"

def setup():
  print("Setting up for first time backend use..")
  resourcesUrlGet = requests.request(method='GET', url='https://github.com/FOSSLingo/resources/archive/refs/heads/main.zip')
  data = resourcesUrlGet.status_code
  if data == 200:
    print("HTTP 200, downloading resources")
    with requests.get(resourcesUrl, stream=True) as r:
      r.raise_for_status()
      with open(backendContentFile, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
          f.write(chunk)
    shutil.unpack_archive("resources.zip", ".")
    os.rename("resources-main", "resources")
    os.remove("resources.zip")
    print("Done downloading!")
  elif data == 404:
    print("404, retry script later")
    sys.exit()
  else:
    print(data)

def vercelSetup():
  print("bash handled this")

if vercelCheck():
  resourcesDir = "./resources"
else:
  resourcesDir = "./resources"

if os.path.isdir(resourcesDir) == True:
  print("Resources directoy present, skipping setup")
else:
  print('Resources directory missing, starting setup;')
  if vercelCheck():
    vercelSetup()
  else:
    setup()

app = FastAPI()
app.mount("/resources", StaticFiles(directory="resources"), name="resources")

@app.get("/")
async def root():
  return FileResponse(backendCoursesFile)
