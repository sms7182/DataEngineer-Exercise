import sys, os
import zipfile
import requests
from io import BytesIO
import aiohttp
import asyncio
import csv
from pathlib import Path
from contextlib import closing

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]



def main():
    
    Path("./downloads").mkdir(parents=True,exist_ok=True)
    for url in download_uris:
        try:
            response=requests.get(url)
            fname=url.split("/")[-1]
            file_path="./downloads/"+fname
            with open(file_path,'wb') as wz:
                wz.write(response.content)
                zip_file=zipfile.ZipFile(file_path)
                files=zip_file.namelist()
                csv_file_path = "./downloads/"+files[0]
                with open(csv_file_path,'wb') as of:
                    of.write(zip_file.read(files[0]))
                os.remove(file_path)
                            

        except Exception as e:
            if os.path.isfile(file_path):
                os.remove(file_path)
            print(e)
    # your code here
    



if __name__ == "__main__":
    main()
