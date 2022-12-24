# promoter-scrape


## Table of Contents
- [Deployment](#deployment)
- 


---

## Deployment
Create virtual environemnt and then activate it

```
virtualenv venv 
<!-- Linux or Mac  -->
source venv/bin/activate
<!-- Windows -->
venv/Scripts/activate
```

Install dependencies using `pip install -r requirements.txt`
Download chromedriver, unzip and move to /usr/local/bin (mac/linux), for windows gogole how to install chromedriver and selenium.
`sudo unzip {chromedriver.zip} -d /usr/bin`
Run the program in the terminal and it will run the script, make sure your terminal/ command line is in the folder path for this project
`python HomedepotWebscrape.py`