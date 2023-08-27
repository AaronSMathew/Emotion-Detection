Emotion Detection using IBM Watson Natural Language Understanding
This repository contains a Python script that uses IBM Watson Natural Language Understanding to analyze the sentiment of a given text and determine whether it's positive, negative, or neutral.

Prerequisites
Before you begin, you need to have the following:

IBM Watson Natural Language Understanding API Key
IBM Watson Natural Language Understanding API URL
Python 3.x installed on your system
Setup
Clone this repository to your local machine or download the script directly.
bash
Copy code
git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection
Install the required Python packages using pip:
bash
Copy code
pip install ibm-watson ibm-cloud-sdk-core
Configuration
Replace the placeholders in the script with your own IBM Watson credentials.

python
Copy code
API_KEY = "YOUR_API_KEY"
API_URL = "YOUR_API_URL"
Usage
Open a terminal and navigate to the directory where you saved the script.

Run the script using the following command:

bash
Copy code
python emotion_detection.py
Enter the sentence you want to analyze for sentiment when prompted.

The script will use IBM Watson Natural Language Understanding to analyze the sentiment and provide the sentiment label (positive, negative, or neutral) along with the sentiment score.

Results
After running the script, you will see the sentiment analysis results printed in the terminal:

plaintext
Copy code
Text: [your input text]
Sentiment: [sentiment label]
Sentiment Score: [sentiment score]
The sentiment label will be one of "positive," "negative," or "neutral," based on the sentiment score calculated by IBM Watson Natural Language Understanding.
