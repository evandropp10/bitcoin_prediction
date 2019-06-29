import facebook as fb

token = "2376863509216755|GkW9fLUlnkHY8MrUzg6TSbN40aI"

graph = fb.GraphAPI(access_token=token, version = 3.1)
events = graph.request("/search?q=Bitcoin&type=event&limit=10000")

eventList = events["data"]


print(eventList)