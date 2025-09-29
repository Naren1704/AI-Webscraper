# AI-Webscraper

This project is a **Streamlit-based AI-powered web scraper and parser**.
It allows users to scrape content from a given website, clean the HTML body, and parse the DOM content based on a custom description.

---

## 🚀 Features

* Web scraping with `selenium` and `beautifulsoup4`.
* Clean and extract body content from webpages.
* Split and parse DOM content intelligently.
* Interactive UI built with **Streamlit**.

---

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

streamlit
langchain
langchain_ollama
selenium
beautifulsoup4
lxml
html5lib
python-dotenv

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

It is recommended to create a virtual environment named **`ai`**:

python -m venv ai

Activate the environment:

* **Windows (PowerShell):**

  ai\Scripts\activate
  
* **Linux/Mac:**
  
  source ai/bin/activate


### 2️⃣ Install Dependencies

Run the following command:

pip install -r requirements.txt

### 3️⃣ Install WebDriver

Since the project uses **Selenium**, you need to download the appropriate **WebDriver** (e.g., ChromeDriver for Google Chrome).

* Download the WebDriver matching your browser version:

  * [ChromeDriver](https://chromedriver.chromium.org/downloads)
  * [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)

* Place the downloaded **WebDriver executable** inside the **project folder** (same folder as `main.py`).

---

## ▶️ Running the Project

Once setup is complete, run:

streamlit run main.py

This will start the Streamlit app in your browser.

---

## 📝 Usage

1. Enter the URL of the website to scrape.
2. Click **Scrape** to view the extracted DOM content.
3. Provide a description of what you want to parse.
4. Click **Parse** to view the processed output.

---

## 📂 Project Structure

.
├── main.py             # Streamlit app entry point
├── parser.py           # Parsing logic
├── scraper.py          # Web scraping utilities
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

## ⚠️ Notes

* Make sure the **WebDriver executable** is up to date with your browser.
* Always run the project inside the `ai` virtual environment.

---

## 👨‍💻 Author
Narendren S V
Developed for AI-driven web scraping and parsing tasks using **Streamlit + LangChain + Selenium**.

