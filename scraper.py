import sys, fileinput, argparse
from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = "c63022e5c4214af6b8794a5250e2b73d"
client = podcast_api.Client(api_key=api_key)      

def parse_args():
  parser = argparse.ArgumentParser(
    description="Simple podcast episode scraper for search terms using Listen Notes API",
    allow_abbrev=False)
  parser.add_argument("filename", help="the file containing a list of search terms")
  parser.add_argument("-k", "--keyword", action="store_true", help="search for keywords instead of exact phrase")
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
  stdout_copy = sys.stdout
  args = parse_args()
  with open("search_results.txt", "w") as sys.stdout:
    for line in fileinput.input(files=(args["filename"]), encoding="utf-8"):
      print(f"SEARCH RESULTS FOR: {line}")
      data = get_episodes(f"\"{line}\"") if args("keyword") else get_episodes(line)
      for episode in data["results"]:
        podcast_name = episode["podcast"]["title_original"]
        episode_name = episode["title_original"]
        link = episode["listennotes_url"]
        print(f"{podcast_name} (podcast): \"{episode_name}\" ({link})")
        print()
      print("----------------------------------------------------------------")
  sys.stdout = stdout_copy

if __name__ == "__main__":
  main()