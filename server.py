''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyse= request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyse)

    label = response['label']
    score = response['score']

    return f"The given text identified as {label} and with score {score}"    

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)