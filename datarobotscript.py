import json
response = unirest.get("https://managebgl-managebgl.p.mashape.com/add?log_type=1&notes=test+value&other=<required>&time=2013-03-31+14%3A22%3A13&token=1-56651863bdd610f5aaef70abaabababa&value=16",
  headers=
  {
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

response = unirest.get("https://managebgl-managebgl.p.mashape.com/extract?end_date=2013-03-31+14%3A03%3A00&start_date=2013-03-15+14%3A03%3A00&token=1-56651863bdd610f5aaef70abacababa",
  headers=
  {
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

response = unirest.get("https://managebgl-managebgl.p.mashape.com/units?token=1-56651863bdd610f5aaef70abacababab",
  headers=
  {
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

response = unirest.get("https://managebgl-managebgl.p.mashape.com/log_range?token=1-56651863bdd610f5aaef70abaababab",
  headers=
  {
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

response = unirest.get("https://managebgl-managebgl.p.mashape.com/login?email=test%40test.com&password=testpassword",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)

response = unirest.post("https://managebgl-managebgl.p.mashape.com/get_token",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
  },
  params={
    "email": "test@test.com",
    "source_site_name": "TicTrac",
    "source_site_url": "http://www.tictrac.com",
    "success_url": "http://www.tictrac.com/success.php"
  }
)

response = unirest.get("https://managebgl-managebgl.p.mashape.com/ping",
  headers={
    "X-Mashape-Key": "aHGqgGEXU8mshPl017c9cFPupR7Cp1gTJJ5jsndLHL6NxfgJ9y",
    "Accept": "application/json"
  }
)
