import json

def main():
  data = json.load(open("sample.json", "r"))
  for episode in data["episodes"]:
    tup = (episode["podcast"]["publisher"], episode["podcast"]["title"], episode["podcast"]["listennotes_url"])
    print("\n".join(tup))
    print()

if __name__ == "__main__":
  main()