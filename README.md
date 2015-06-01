# Unirest-API-Script
I used a prediction API I found on Mashape that was free and used their request libraries to create a script.
The script is a simple collection of get requests using the Mashape Unirest API. It used the Stockfluence algorithms to predict which stocks are the best ones to invest in by listing out the ones it thinks will rise in the near future.

The output of the script is the following: 

Connection: keep-alive
Content-Type: application/json
Date: Mon, 01 Jun 2015 14:24:36 GMT
Server: Mashape/5.0.6
Transfer-Encoding: chunked
X-Powered-By: PHP/5.4.6-1ubuntu1.8
X-Ratelimit-Calls-Limit: 10
X-Ratelimit-Calls-Remaining: 5

{
  "status": "succes",
  "completed_in": 0.40614700317383,
  "result": {
    "timestamp": "2015-06-01 16:24:06",
    "funds": [
      {
        "symbol": "M",
        "name": "Macy's, Inc.",
        "slug": "macys",
        "exchange": "NYSE",
        "sentimentscore": 75,
        "change": "93.08%",
        "sentiment": "11",
        "strength": 30,
        "passion": 0,
        "reach": 27,
        "updated": "2015-06-01"
      },
      {
        "symbol": "NKE",
        "name": "Nike Inc.",
        "slug": "nike",
        "exchange": "NYSE",
        "sentimentscore": 204,
        "change": "93.3%",
        "sentiment": "22",
        "strength": 40,
        "passion": 42,
        "reach": 18,
        "updated": "2015-06-01"
      },
      {
        "symbol": "FUR.AS",
        "name": "Fugro",
        "slug": "furgro",
        "exchange": "Amsterdam",
        "sentimentscore": 69,
        "change": "89.17%",
        "sentiment": "0",
        "strength": 59,
        "passion": 51,
        "reach": 28,
        "updated": "2015-06-01"
      },
      {
        "symbol": "HAS",
        "name": "Hasbro Inc.",
        "slug": "hasbro",
        "exchange": "NasdaqGS",
        "sentimentscore": 170,
        "change": "86.81%",
        "sentiment": "26",
        "strength": 43,
        "passion": 66,
        "reach": 13,
        "updated": "2015-06-01"
      },
      {
        "symbol": "CONN",
        "name": "Conns Inc.",
        "slug": "conns",
        "exchange": "NasdaqGS",
        "sentimentscore": 109,
        "change": "82.5%",
        "sentiment": "1",
        "strength": 27,
        "passion": 0,
        "reach": 26,
        "updated": "2015-06-01"
      },
      {
        "symbol": "MET",
        "name": "MetLife, Inc.",
        "slug": "metlife",
        "exchange": "NYSE",
        "sentimentscore": 117,
        "change": "78.46%",
        "sentiment": "18",
        "strength": 36,
        "passion": 21,
        "reach": 25,
        "updated": "2015-06-01"
      },
      {
        "symbol": "NTDOY",
        "name": "Nintendo Co. Ltd.",
        "slug": "nintendo",
        "exchange": "OTC Markets",
        "sentimentscore": 149,
        "change": "77.38%",
        "sentiment": "8",
        "strength": 42,
        "passion": 24,
        "reach": 23,
        "updated": "2015-06-01"
      },
      {
        "symbol": "AAPL",
        "name": "Apple Inc.",
        "slug": "apple",
        "exchange": "NasdaqGS",
        "sentimentscore": 106,
        "change": "75.08%",
        "sentiment": "53",
        "strength": 61,
        "passion": 11,
        "reach": 35,
        "updated": "2015-06-01"
      },
      {
        "symbol": "KPN.AS",
        "name": "Koninklijke (Royal) KPN NV",
        "slug": "kpn",
        "exchange": "Amsterdam",
        "sentimentscore": 113,
        "change": "72.92%",
        "sentiment": "3",
        "strength": 34,
        "passion": 38,
        "reach": 20,
        "updated": "2015-06-01"
      },
      {
        "symbol": "SI",
        "name": "Siemens AG",
        "slug": "siemens",
        "exchange": "NYSE",
        "sentimentscore": 81,
        "change": "72.77%",
        "sentiment": "17",
        "strength": 34,
        "passion": 60,
        "reach": 12,
        "updated": "2015-06-01"
      },
      {
        "symbol": "WTSLA",
        "name": "Wet Seal Inc.",
        "slug": "wet-seal",
        "exchange": "NasdaqGS",
        "sentimentscore": 89,
        "change": "72.69%",
        "sentiment": "5",
        "strength": 85,
        "passion": 22,
        "reach": 64,
        "updated": "2015-06-01"
      },
      {
        "symbol": "STZ",
        "name": "Constellation Brands Inc. ",
        "slug": "constellation",
        "exchange": "NYSE",
        "sentimentscore": 154,
        "change": "70.89%",
        "sentiment": "5",
        "strength": 55,
        "passion": 43,
        "reach": 25,
        "updated": "2015-06-01"
      },
      {
        "symbol": "MAT",
        "name": "Mattel, Inc.",
        "slug": "mattel",
        "exchange": "NasdaqGS",
        "sentimentscore": 156,
        "change": "67.74%",
        "sentiment": "23",
        "strength": 54,
        "passion": 45,
        "reach": 28,
        "updated": "2015-06-01"
      },
      {
        "symbol": "YOKU",
        "name": "Youku Tudou Inc.",
        "slug": "youku-tudou",
        "exchange": "NYSE",
        "sentimentscore": 125,
        "change": "64.34%",
        "sentiment": "0",
        "strength": 74,
        "passion": 51,
        "reach": 34,
        "updated": "2015-06-01"
      },
      {
        "symbol": "GAIA",
        "name": "Gaiam Inc.",
        "slug": "gaiam",
        "exchange": "NasdaqGM",
        "sentimentscore": 107,
        "change": "64.77%",
        "sentiment": "16",
        "strength": 41,
        "passion": 52,
        "reach": 19,
        "updated": "2015-06-01"
      },
      {
        "symbol": "DWA",
        "name": "DreamWorks Animation SKG Inc.",
        "slug": "dreamworks",
        "exchange": "NasdaqGS",
        "sentimentscore": 138,
        "change": "63.33%",
        "sentiment": "17",
        "strength": 32,
        "passion": 25,
        "reach": 21,
        "updated": "2015-06-01"
      },
      {
        "symbol": "MU",
        "name": "Micron Technology Inc.",
        "slug": "micron-technology",
        "exchange": "NasdaqGS",
        "sentimentscore": 123,
        "change": "61.05%",
        "sentiment": "8",
        "strength": 40,
        "passion": 25,
        "reach": 27,
        "updated": "2015-06-01"
      },
      {
        "symbol": "BOKA.AS",
        "name": "Royal Boskalis Westminster NV",
        "slug": "royal-boskalis-westminster",
        "exchange": "Amsterdam",
        "sentimentscore": 12,
        "change": "61.43%",
        "sentiment": "0",
        "strength": 4,
        "passion": 0,
        "reach": 4,
        "updated": "2015-06-01"
      },
      {
        "symbol": "RYAAY",
        "name": "Ryanair Holdings plc",
        "slug": "ryanair",
        "exchange": "NasdaqGS",
        "sentimentscore": 116,
        "change": "59.04%",
        "sentiment": "8",
        "strength": 32,
        "passion": 39,
        "reach": 17,
        "updated": "2015-06-01"
      },
      {
        "symbol": "BCS",
        "name": "Barclays PLC",
        "slug": "barclays",
        "exchange": "NYSE",
        "sentimentscore": 136,
        "change": "58.02%",
        "sentiment": "8",
        "strength": 50,
        "passion": 14,
        "reach": 38,
        "updated": "2015-06-01"
      }
    ]
  }
}




