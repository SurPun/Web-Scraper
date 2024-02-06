# Web-Scraper

## Requirements:

- <b>Python</b> -
    If you haven't installed Python yet, you can download it from the [official website](https://www.python.org/downloads/).<br>
- <b>Conda</b> - 
    If you haven’t installed Conda yet, you can download it from the [official website](https://www.anaconda.com/download) to download the version compatible with your operating system.

    <!-- - May need to add conda env Path- 
        - [Conda Path Guide](https://www.youtube.com/watch?v=HyxR0QTTJJs)  
        - [Conda Env Clean Up](https://www.youtube.com/watch?v=dcvdOuvWI-Q) -->

## Set up Conda Environment

Building a Conda Environment is necessary for this project, the enviornment.yaml file within the repo contains all the relevant config for this environment.

- Navigate to the root of the project in terminal and run:
    ```
    conda env create -f environment.yaml
    ```

-   To activate this environment run:
    ```
    conda activate web_scraper
    ```

## ChromeDriver

This Project uses the Chromedriver.exe file which can be downloaded from the [official website](https://chromedriver.chromium.org/downloads) to browse and scrape data from the web.

- Download the zip file and copy chromedriver.exe into the chromedriver folder.

## Running the scraping scripts

```bash
python src/vue.py
```