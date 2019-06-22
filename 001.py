import re

a = 'background-image: url("https://i0.hdslb.com/bfs/live/user_cover/df4334c6138f59e276134b997da9b3c4df48a80b.jpg")'

a = re.findall(r'.*url\(\"(.*)\".*', a)[0]
print(a)
