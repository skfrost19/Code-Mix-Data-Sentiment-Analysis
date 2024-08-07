# 📌 Code-Mix Data Sentiment Analysis

## 👉 Introduction

This project is about sentiment analysis on Code-Mix data using Large Language Model (LLM). Code-Mixing is the phenomenon of alternating between two or more languages in a single conversation. This project aims to analyze the sentiment (positive, negative) of such data.

This repository uses LLM named <b> Openchat - 3.5, 4-bit quantized </b> for sentiment analysis.

## Demo
![Demo Image](demo.png)

## 🛠️ Setup and Installation

1. Clone the repository: `git clone https://github.com/skfrost19/Code-Mix-Data-Sentiment-Analysis.git`
2. Navigate into the project directory: `cd Code-Mix-Data-Sentiment-Analysis`
3. Install the required dependencies: `pip install -r requirements.txt`

<b>OR </b> <br>
1. On linux system, run the `setup.sh` file to install the required dependencies and start the server.

2. On windows system, run the `setup.ps1` on powershell to install the required dependencies and start the server.

## 💻 Usage

To run the sentiment analysis, use the following command:

- Run the fastAPI server: `uvicorn webui:app --reload`
- Navigate to `http://localhost:8000` in your browser to use the web interface.

## 📂 Project Structure

The project is structured as follows:

```
Code-Mix-Data-Sentiment-Analysis
├── config
│   ├── init_config.py
│   ├── __init__.py
│   ├── model_config.py
│   └── paths.toml
├── core
│   ├── exception.py
│   ├── __init__.py
│   └── logger.py
├── LICENSE.txt
├── README.md
├── requirements.txt
├── settings
│   ├── __init__.py
│   └── template.py
├── setup.ps1
├── setup.sh
├── static
│   └── images
│       └── favicon.png
├── structure
├── templates
│   └── index.html
├── tests
│   └── __init__.py
├── utils
│   ├── get_model.py
│   ├── pipeline.py
│   └── predictor.py
└── webui.py

```

## 📚 References & Credits
<ul>
<li>[1]: Openchat
<li>[2]: TheBloke - For Quantized models
<li>[3]: Huggingface
<li>[4]: Langchain
</ul>
