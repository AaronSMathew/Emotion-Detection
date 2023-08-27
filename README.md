# Emotion Detection using IBM Watson Natural Language Understanding

This repository contains a Python script that uses IBM Watson Natural Language Understanding to analyze the sentiment of a given text and determine whether it's positive, negative, or neutral.

## Prerequisites

Before you begin, you need to have the following:

- IBM Watson Natural Language Understanding API Key
- IBM Watson Natural Language Understanding API URL
- Python 3.x installed on your system

## Setup

1. Clone this repository to your local machine or download the script directly.

```bash
git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection
```

2. Install the required Python packages using pip:

```bash
pip install ibm-watson ibm-cloud-sdk-core
```

## Configuration

1. Replace the placeholders in the script with your own IBM Watson credentials.

   ```python
   API_KEY = "YOUR_API_KEY"
   API_URL = "YOUR_API_URL"
   ```

## Usage

1. Open a terminal and navigate to the directory where you saved the script.

2. Run the script using the following command:

   ```bash
   python emotion_detection.py
   ```

3. Enter the sentence you want to analyze for sentiment when prompted.

4. The script will use IBM Watson Natural Language Understanding to analyze the sentiment and provide the sentiment label (positive, negative, or neutral) along with the sentiment score.

## Results

After running the script, you will see the sentiment analysis results printed in the terminal:

```plaintext
Text: [your input text]
Sentiment: [sentiment label]
Sentiment Score: [sentiment score]
```

The sentiment label will be one of "positive," "negative," or "neutral," based on the sentiment score calculated by IBM Watson Natural Language Understanding.

## License

This project is licensed under the [MIT License](LICENSE).

---

Remember to replace `[yourusername]`, `YOUR_API_KEY`, and `YOUR_API_URL` with your actual GitHub username, IBM Watson credentials, and API URL.

Feel free to add more details to the README if needed, such as troubleshooting tips, additional configuration options, or further explanations about the sentiment analysis process.