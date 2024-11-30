# Overview 🔍

> [!NOTE]  
> **The goal is to compare the NYT and the Guardian, to find out if they are biased or not as well as other information.
> If you want to learn more about what this project is, you can read my introduction [here](./Presentations/Introduction.md)**

**This is just an overview over the different steps. There are detailed explanations inside the topics.**

---

##### What you will find in this repository: ✅

1. Code and Development
2. Documentation of the Code

---

##### What you will not find here: ❌

1. Data Collection from Articles
2. Analysis and Evaluation of the Collected Data

---

> [!IMPORTANT]
>
> 1. **German**? Schau meine [Deutsche Dokumentation](./Dokumentation/) an.
> 2. Check out my **[Trello Board](https://trello.com/w/jugend_forscht/)**, where I document my progress
> 3. This is a **Jugend-Forscht** Project, check out the [official website](https://www.jugend-forscht.de/)

---

## 1. [Data Collection](./data-collection/) 🗑️

- Collecting Data from the two different News Sources

1. Getting the URLs from the API
2. Extracting the Source Code from the URLs
3. Extracting the Article Text from the Source Code

###### See at [Data Collection](./data-collection/)

---

## 2. [Analysing](./Analysing/) Data / Visualizing 👀

- Analysing the Data from the two different News Sources
- Comparing the Data
- Visualizing the Data

###### See [Analysing Data](Analysing/)

---

## Preparation 📚

Install dependencies:

```sh
pip install -r requirements.txt
```

Used Packages:

- BeautifulSoup (beautifulsoup4): For web scraping and parsing HTML/XML.
- Matplotlib: For data visualization and plotting.
- NLTK: For natural language processing tasks.
- TextBlob: For simple natural language processing.
- NumPy: For numerical computations and array handling.
- Pandas: For data manipulation and analysis.
- Pillow: For image processing.
- Requests: For handling HTTP requests.
- Scikit-learn: For machine learning tasks.
- Selenium: For browser automation and testing.
- ...

---
