# fetchrewards
# HOW TO RUN:

1. Clone repo and run app.py
2. server will be running on localhost:5000
3. Via postman (or any other restful api tool) run a POST command
4. Make sure content-type is set to application/json
5. In the body payload send a JSON object with two or more strings values
  a. Ex. { "text1": "abc", "text2": "def" }
6. Two different post URLS:
  a. http://localhost:5000/getScore/jaccard (uses jaccard similarity score to determine similarity between all text combinations (text 1 and 2, 1 and 3, 2 and 3, etc)
  b. http://localhost:5000/getScore/similarity (uses own similartiy algorithm to determine score)
7. Returns all combinations and their similarity score

Link to container in Docker Hub:
https://hub.docker.com/r/deemalpatel/fetchrewards
