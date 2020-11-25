from flask import Flask, request, jsonify
import similarityScore
app = Flask(__name__)

@app.route('/')
def index():
    return 'Similarity Score Web Service'

@app.route('/getScore/jaccard', methods=['POST'])
def getJaccardScore():
    texts = request.get_json()
    textValues = []
    scores = {}
    for value in texts.items():
        textValues.append(value[1])
    for i in range(0,len(textValues)):
        for j in range(i+1, len(textValues)):
            scores[f'Similarity Score between text {i+1} and text {j+1}'] = similarityScore.jaccardScore(textValues[i],textValues[j])
    return scores

@app.route('/getScore/similarity', methods=['POST'])
def getSimilarity():
    texts = request.get_json()
    textValues = []
    scores = {}
    for value in texts.items():
        textValues.append(value[1])
    for i in range(0,len(textValues)):
        for j in range(i+1, len(textValues)):
            scores[f'Similarity Score between text {i+1} and text {j+1}'] = similarityScore.getSimilarity(textValues[i],textValues[j])
    return scores
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
