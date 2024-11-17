# Analysing the New York Times Articles

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

## 1. Getting Data

###### See [Data Collection](data-collection/README.md)

### Steps:

1. **Get Links from NYT API**:

   - Collect article links using the New York Times API.
   - See [Get_Links.py](data-collection/Get_Links.py).

2. **Extract Source Code from URLs**:

   - Use Selenium, Requests, or External APIs to extract the source code.
   - See [Selenium.py](data-collection/Selenium.py), [Source_Extraction_Requests.py](data-collection/Requests/Source_Extraction_Requests.py), and [Scraperapi/main.py](data-collection/Scraperapi/main.py).

3. **Convert HTML to Text**:

   - Parse HTML to extract text using BeautifulSoup or regular expressions.
   - See [Extract_Text.py](data-collection/Extract_Text.py).

4. **Proxy Rotation**:

   - Use proxies to avoid getting blocked while scraping.
   - See [proxyrotation](data-collection/proxyrotation/).

5. **AWS Setup**:
   - Run your scripts in the cloud to reduce local computer usage.
   - See [AWS/README.md](data-collection/AWS/README.md).

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

## Extra

#### Database Storage

- This can be ignored because it didn't work out for me when storing the source code!
- It did work when analyzing the articles and saving the info.
- See [Analysing the Content](Analysing/README.md).

## Result

- This is only a part of the full project!
- View the whole project on [GitHub](https://github.com/AdminL3/Jugend-Forscht/).
