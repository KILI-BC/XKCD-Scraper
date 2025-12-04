# XKCD-Scraper
### A web-scraper that downloads all released XKCD Comics
## What exactly is XKCD-Scraper?
This project is intended to be used to automate the downloading of all the image files and metadata of the [XKCD-Webcomic](https://xkcd.com/).
It is acomplished using a python script and the the XKCD-api (i.e. sites like [this](https://www.xkcd.com/info.0.json)) to get the information on each of the numbered comics.

## How to install XKCD-Scraper
To install the project simply fork it to a local drive.

## How to use XKCD-Scraper
To use XKCD-Scraper, navigate to its src-folder and execute it with the following command:
```
python3 main.py
```

Thr program will automatically download all the comics up to the current one to the folder labeled comics, named with their correct title and save the meta information (i.e. `number`, `filename`, `safe title`, `transcript` and `alt text`) to a `names.csv`-file in the main directory.
## The code structure
The code is subdevided in to the files `api_request.py` (for the communication with the XKCD-api), `image_getter.py` (to handle the downloading of the images) and `main.py` (for the main program). This practice ensures modularity and future reusability.

## How to contribute
Contribution to this project is not possible at the current point in time.

## Known Issues
None. If you find some feel free to report them [here](https://github.com/KILI-BC/XKCD-Scraper/issues). I might fix them if I get arround to it.
