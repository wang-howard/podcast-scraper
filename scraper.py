import fileinput
from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = "a3fb06b09a654cf28f6e9013e3206a30"
client = podcast_api.Client(api_key=api_key)      

def scrape(term: str):
  response = client.batch_fetch_episodes(
    q=term,
    sort_by_date=1,
    type="episode",
    only_in="title,description",
    language="English")
  return response.json()

def main():
  for line in fileinput.input(encoding="utf-8"):
    print(scrape(line))
    break

if __name__ == "__main__":
  main()