# Analysing the New York Times Articles

This is just an overview over the different steps. Details are linked inside the topics.

## Preparation

Install dependencies:

```sh
pip install -r requirements.txt
```

Used Packages:

- Selenium
- Requests
- Pandas
- Matplotlib
- scikit-learn
- TextBlob
- ...

###### This is a "[Jugend-Forscht](https://jugend-forscht.de)" Project

## 1. Data Collection

###### See Details at [Data Collection](data-collection/README.md)

### Overview:

1. **Get Links from NYT API**:

   - Collect article links using the New York Times API.
   - More at [Data-Collection](./data-collection/)
   - File: [`Get_Links.py`](data-collection/Get_Links.py).

2. **Extract Source Code from URLs**:

   - Use Selenium, Requests to extract the source code.
   - More at [Data-Collection](./data-collection/)
   - Files [`Selenium.py`](data-collection/Selenium.py) and [`Requests`](data-collection/Requests/).

3. **Optimize Data Collection** with AWS and Multiprocessing

   - More at [AWS](./data-collection/AWS/)
   - and [Multiprocessing](./data-collection/Multiprocessing/)

4. **Convert HTML to Text**:

   - Parse HTML to extract text using BeautifulSoup or regular expressions.
   - More at [Data-Collection](./data-collection/)
   - File: [`Extract_Text.py`](data-collection/Extract_Text.py).

## 2. Analysing Data

###### See [Analysing Data](Analysing/README.md)

### Options:

1. **Word Count Analysis**:

   - Count the words in articles and visualize them in a graph.
   - See [Wordcount](Analysing/Wordcount/README.md).

2. **Sentiment Analysis**:

   - Analyze the sentiment of articles and visualize the results.
   - See [Sentimental](Analysing/Sentimental/README.md).

3. **Article Count Analysis**:
   - Count the number of articles and visualize the results.
   - See [Articlecount](Analysing/Articlecount/README.md).
