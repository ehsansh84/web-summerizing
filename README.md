# web-summerizing
This project takes a web url and summarize the data

- This project is a Python FastAPI project. To run this project you need to have python, 
I used Python version 3.10
- To summarize the text, I used nltk and sumy libs in python, If you need to do it in javascript, you can do it using
libraries like: JS Summarize can be downloaded from: https://github.com/wkallhof/js-summarize
- Steps to run the project:
  - Download the project: `git clone https://github.com/ehsansh84/web-summerizing.git`
  - Go to the project folder and run `python -m venv venv`
  - Active venv: `source venv/bin/activate`
  - Install requirements: `pip install -r requirements.txt`
  - Run FastAPI server: `uvicorn main:app --reload`
  - Open this url in your browser: `localhost:8000`
  - Put a url in the input box and hit the button

``