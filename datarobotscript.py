import json

//output 1
response = unirest.get("https://stock.p.mashape.com/v1/fund/AAPL",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

//output 2
response = unirest.get("https://stock.p.mashape.com/v1/prediction/AAPL",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

//output 3
response = unirest.get("https://stock.p.mashape.com/v1/extended-fund/aaple",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

