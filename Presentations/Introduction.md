# **Change of Words: Long-term Data Analysis of Journalistic Perspectives**

> [!NOTE]
> This is the tranlation of a Script I used for this [PowerPoint](./Presentation.pptx)<br>
> That means there are no complete sentences and the text is not structured in a way that it can be read as a text.<br>
> The original script is in German, so the translation may not be perfect.<br>
> The original script can be found [here](./Lehrer_Vorstellung/Script.md)

## Introduction:

- There are many prejudices about media and their reporting
- But this should be verifiable
- But how?
- That's how my project came about
  --> see title

#### Comparison between two newspapers

- **The New York Times** (USA)
- **The Guardian** (UK)

Both are considered high-quality, influential media. The global comparison provides interesting insights into national differences.

---

## **Let's take a closer look at the name**

### 1. Journalistic Perspectives

- **Subjectivity and Objectivity**: Factual vs. opinion-based presentation
- **Polarization**: positive vs. negative tone
- **Article Length**: Changes in length over time
- Other possible aspects: **Topic selection, language, style**

###### Applied to a text

---

### 2. Long-term

- **Temporal Change**: Changes over time
- **Over several years**:
  - **2020–2022**: currently analyzed
  - **20 years**: target period

---

### 3. Data Analysis

- **Huge Data Volumes**: approx. 60,000 articles

  - collected over 2 years
  - 30,000 articles per year
  - Over 20 years: 0.5 million articles

---

## Procedure

###### **Data Collection**: Collecting articles from the last two years was already a complex process.

1. **Links**: API access to the articles
   - Therefore, specific newspapers where this is possible
2. **Code**: Extraction of the source code
   - Complex processes to obtain the texts
   - Error-prone
   - IP blockades
   - Captchas
   - Ban tendency
3. **Text** extraction from code
   - Filtering from the code
   - Usual methods like BeautifulSoup not usable
   - Own script for extraction
4. **Storage**: Databases
   - Storage of texts
   - Storage of metadata
   - Storage of analysis results
5. **Analysis**: Text analysis
   - NLP methods
   - Sentiment analysis
   - Length analysis
   - Comparison of newspapers

---

## **Societal Benefit**

- See [`Gesellschaftlicher Vorteil`](./Gesellschaftlicher_Vorteil.md) (German)

#### Outcome unknown

Nevertheless: **Gain insights**
In all cases, a result can be meaningful:

- Verification of prejudices
- Strengthening trust in quality media
- Confidence in media selection
- Approach for future research
- Educational value

Explained:

- Verification of prejudices: Refutation of the assumption that American and British newspapers report fundamentally differently.
- Strengthening trust in quality media: Evidence of objective and consistent reporting in reputable media.
- Approach for future research: Examination of global standards and agencies in the uniformity of reporting.
- Educational value: Promotion of critical thinking and integration into schools/universities as an example of data-based argumentation.
