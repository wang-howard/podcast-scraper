import fileinput, argparse
from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = "c63022e5c4214af6b8794a5250e2b73d"
client = podcast_api.Client(api_key=api_key)      

def parse_args():
  parser = argparse.ArgumentParser(
    description="Simple podcast episode scraper for search key terms using Listen Notes API",
    allow_abbrev=False)
  parser.add_argument("filename",
    help="the file containing a list of search terms")
  parser.add_argument("--exact")
  return parser.parse_args()

def get_episodes(term: str):
  response = client.search(
    q=term,
    sort_by_date=1,
    type="episode",
    only_in="title,description",
    language="English")
  return response.json()

def main():
  parser = parse_args()
  
  for line in fileinput.input(encoding="utf-8"):
    data = get_episodes(line)
    for episode in data["results"]:
      podcast_name = episode["podcast"]["title_original"]
      episode_name = episode["title_original"]
      link = episode["listennotes_url"]
      print(f"{podcast_name} (podcast): \"{episode_name}\" ({link})")
      print()

if __name__ == "__main__":
  main()