# Schriftliche Arbeit

## Deckblatt

- Photshop
- NYT vs Guardian
- Vergleich
- Ansprechend

---

> [!IMPORTANT]  
> Wenn du auf die Titel klickst dann kommst du zu der jeweiligen Infoseite!  
> [Aufbau](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Aufbau.md)  
> [Vorgaben](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Vorgaben.md)

---

## [Projektüberblick](./Aufbau.md#projekt%C3%BCberblick)

- sechs bis acht Sätze
- Der Lesende muss auf dieser Seite das Wesentliche der gesamten Arbeit erfassen können.
- Fragestellung, Methode, Ergebnisse und Diskussion auf maximal einer Seite
- Kopiert von Kurztext:

Wie haben sich die Medien über die letzten Jahre verändert? In meinem Projekt befasse ich mich mit der Datenanalyse von zwei bedeutenden Zeitungen. Ausgewählt habe ich die "New York Times" (USA) und "The Guardian" (GB). Das Ziel ist, Artikel der beiden Zeitungen zu analysieren und auszuwerten, wobei ich mich bei den beiden Zeitungen auf jeweils drei Rubriken beschränkt habe. Die drei Themen - World, Politics und Opinion - sind bei beiden Zeitungen vergleichbar, und ich werde alle Artikel dieser Rubriken analysieren. Kriterien bei der Analyse sind aktuell die Objektivität und Polarisation der Artikel, sowie deren Länge und Anzahl. Der geplante Zeitraum dieser Analyse ist 10 bis 20 Jahre.
Das Ziel dieser Forschungsarbeit ist die Überprüfung von Vorurteilen bezüglich der Veränderung in der Berichterstattung sowie, je nach Ergebnis, die Glaubwürdigkeit von Qualitätsmedien zu stärken beziehungsweise die Veränderung der Medien im Laufe der Zeit nachzuweisen.

---

## [Inhaltsverzeichnis mit Nummerierung und Seitenzahlen](./Aufbau.md#inhaltsverzeichnis)

4. Fachliche Kurzfassung
5. Motivation und Fragestellung
6. Hintergrund und theoretische Grundlagen
7. Vorgehensweise, Materialien und Methoden
8. Ergebnisse
9. Ergebnisdiskussion
10. Fazit und Ausblick
11. Quellen- und Literaturverzeichnis
12. Unterstützungsleistungen

---

## [Fachliche Kurzfassung](./Aufbau.md#fachliche-kurzfassung)

###### Die fachliche Kurzfassung fasst das Projekt kurz für die Jurymitglieder zusammen. Im Unterschied zum Projektüberblick stehen hier die wissenschaftlichen Erkenntnisse im Vordergrund. Die fachliche Kurzfassung sollte immer auf dem aktuellen Stand der schriftlichen Arbeit sein.

Das Projekt untersucht die zeitliche Entwicklung von Sentiment, Artikellänge und Artikelanzahl in "The New York Times" und "The Guardian" zwischen 2010 und 2021. Mithilfe von Python wurden Artikel gesammelt und analysiert, um langfristige Trends zu identifizieren.

Die Ergebnisse zeigen:

Die Artikelanzahl sinkt im Guardian in der Rubrik "Opinion", während sie im Politikbereich der New York Times deutlich ansteigt.
Das Sentiment bleibt in beiden Zeitungen konstant (durchschnittlich neutral). Jedoch zeigt die Kategorie "World" eine höhere Subjektivität als "Politics" und "Opinion".
Die durchschnittliche Artikellänge unterscheidet sich: NYT-Artikel sind mit 1100 Wörtern länger als Guardian-Artikel (800 Wörter), ohne signifikante Entwicklung über die Jahre.
Diese Erkenntnisse verdeutlichen redaktionelle Unterschiede und zeigen, wie sich globale Ereignisse auf die Berichterstattung beider Zeitungen auswirken.

---

## [Motivation und Fragestellung](./Aufbau.md#motivation-und-fragestellung)

Meine Suche nach meinen Thema hat begonnen, nachdem ich auf X (ehemals Twitter) bemerkt habe, wie aggressiv und polarisierend die Meinungen der Menschen sind.
Ich dachte mir, dass man dies doch überprüfen könnte. Nach ein wenig durchsuchen der Webseite viel mir schnell auf, dass die meisten Meinungen in Form von Videos und Fotos dargestellt wurden. Also ging meine Suche weiter zu Facebook, wo das auslesen der Artikel weniger unterstützt wurde, und zu Reddit, wo ein ähnliches Problem wie bei X auftrat. Daraufhin habe ich meinen Blick auf die größten Meinungsbildner geworfen. Die Qualitätsmedien der Welt. Hier habe ich zuerst mein Blick auf die "New York Times" geworfen. Diese ist bekannt für ihre objektive Berichterstattung und ihre kritischen Artikel. Um aber die Werte objektiv zu betrachten und vergleichen brauchte ich eine zweite Zeitschrift, die meinen Anforderungen entsprach. Nach ein wenig suchen stoß ich auf "The Guardian", welche einen guten Kontrast bildet.

1. Wie objektiv sind die beiden analysierten Zeitungen wirklich?
2. Wie stark hat sich die Medienberichterstattung in den letzten Jahren verändert?
3. Sind die Medien so objektiv, wie sie vorgeben?
4. Wird die Welt in den Medien immer negativer dargestellt?.
5. Sind Medien in den USA subjektiver als in Großbrittaniee?

---

## [Hintergrund und theoretische Grundlagen](./Aufbau.md#hintergrund-und-theoretische-grundlagen)

- Bei mir nicht nötig?
- Was wurde schon erforscht?

---

## [Vorgehensweise, Materialien und Methoden](./Aufbau.md#vorgehensweise-materialien-und-methoden)

### Vorgehensweise

Der Vorgang, um die Daten zu sammeln und zu analysieren, ist sehr komplex und wird in mehreren Schritten durchgeführt.

#### 1. Links sammeln

Der erste Hauptschritt ist, den Artikeltext zu bekommen. Dafür muss ich als erstes Zugriff auf die kompletten Links der beiden Zeitschriften zugreifen. Dafür benutze ich die API von "The New York Times" und "The Guardian". Da nur sehr wenige Zeitschriften so eine API haben, musste ich mich auf die beiden Zeitschriften beschränken. Die API gibt mir die Möglichkeit mithilfe von der Bibilothek `requests`, die Links der Artikel zu bekommen und in einer Datei zu speichern.
Aufgrund der Unterverzeichnisse des Links kann man das Datum, sowie Rubrik des Artikels auslesen und sortieren (Beispiel?).
Hier habe ich mich für drei Rubriken entschieden, welche bei beiden Zeitschriften vergleichbar sind. Diese Rubriken sind "World", "Politics" und "Opinion". Jetzt sortiere ich die Links nach Datum und Rubrik.

Mithilfe der Links kann ich jetzt auf die Webseiten zugreifen. Doch um die Artikel zu analysieren, brauche ich Zugriff auf den Artikeltext. Dies wird unterteilt in zwei große Schritte:

#### 2. Quellcode herunterladen

Als erstes benötige ich den Quellcode der Webseite. Das beschaffen des Quellcodes war der vermutlich aufwendigste Prozess der ganzen Arbeit. Der Quellcode ist der HTML-Code der Webseite, welcher alle Informationen der Webseite enthält. Diesen Code kann ich durch verschiedene Methoden herunterladen. Der Prozess ist sehr unterschiedlich, je nachdem welche Webseite ich herunterlade.
Bei "The Guardian" war dieser Prozess viel einfacher. Ich konnte mit einer einfachen Anfrage mit dem Python Modul `Requests` den Quellcode der Webseite herunterladen. Dieser wurde dann in einer Textdatei gespeichert, sortiert nach Datum und Rubrik.
Bei der New York Times war es viel komplizierter. Es gibt verschiedene Methoden um den Quellcode herunterzuladen. Die Methode Requests, wie ich bei "The Guardian" genutzt habe, hat nicht funktioniert. Nach bereits 100 Artikeln wurde meine IP-Adresse blockiert und **`Fehlermeldung hier reinverlinken?`**. Die zweite Methode ist die Python Bibilothek `Selenium`, welche eine beliebte Methode ist um einen echten Browser wie Chrome zu simulieren. Doch auch hier gab es Probleme. Die New York Times hat schnell meine ungewöhnliche Aktivität bemerkt, und nur den ersten Absatz des Artikels angezeigt. Außerdem wurde der Inhalt des Artikels hinter einer Paywall versteckt. Dies hat meine Analyse unmöglich gemacht, und ich musste einen Weg finden, um die Paywall zu umgehen, sowie die vielen Captchas zu umgehen.
Mein erster Versuch war die Maßnahmen einfach zu verhindern, durch rotieren meiner Proxy habe ich versucht die Captchas zu umgehen. Leider haben gratis Proxys oft nicht funktioniert. Eine andere Methode war das benutzen einer Externen API, zum Beispiel `Scraperapi`. Doch aufgrund limitierter Token in der Freemium Version, war dies auch keine Lösung. An diesem Punkt dachte ich das wäre das Ende meiner Arbeit, doch nach ein wenig herumprobieren, habe ich entdeckt, dass der komplette Artikeltext auch im "Backend" vorhanden ist. Aber leider in einem komplizierten Geflecht aus JSON-ähnlichen Strukturen. Das heißt ich konnte den Quellcode mit meiner vorher genannten Methode `Selenium` herunterladen und nachträglich den Text extrahieren.

#### 3. Text extrahieren

Hierfür habe ich eine Funktion erstellt, die den Text Stück für Stück den Text aus dem Backend herausfiltert und dann zusammengefügt.

```
def get_text_from_html(html):
    matches = re.findall(r'"text":"(.*?)"', html)
    matches = list(dict.fromkeys(matches))
    text = ""
    for match in matches:
        text += match + "\n"
    return text
```

Auch das extrahieren des Textes war einfacher bei "The Guardian". Hier habe ich einfach die herkömmliche Methode `BeautifulSoup` genutzt um anhand von HTML-Tags den Text zu lokalisieren. Dieser Text wurde dann in einer Textdatei gespeichert, sortiert nach Datum und Rubrik.

#### 4. Text analysieren

Da ich nun den Artikeltext habe, kann ich diesen nach verschiedenen **`??`** analysieren.
Zum speichern der ausgewerteten Daten habe ich eine SQL-Datenbank erstellt. Hierfür benutze ich über das ganze Projekt hinweg Pythons Bibilothek `SQLite3` benutzt. In dieser Datenbank speichere ich die Daten nach Datum und Rubrik, um später die Daten einfach abrufen zu können.

###### 4.1. Wörteranzahl

In meinem Code wird dies als "Wordcount" bezeichnet, und es ist ziemlich selbstverständlich. Zuerst habe ich den Text in einzelne Wörter aufgeteilt und diese gezählt. Diese Daten habe ich dann in einer SQL-Datenbank gespeichert.

###### 4.2. Sentimentalanalyse

Die Sentimentanalyse ist ein wichtiger Bestandteil meiner Arbeit. Hierbei wird der Text auf Polarisation sowie Subjektivität hin analysiert. Dies wird mithilfe des Moduls `TextBlob` durchgeführt.

- **4.2.1. Polarisation**
  - Dieses Modul gibt jedem Wort eine Wertung von -1 bis 1, wobei -1 negativ und 1 positiv ist. Daran kann man erkennen, ob ein Text positiv oder negativ ist.
- **4.2.1. Subjektivität**
  - TextBlob berechnet die Subjektivität, indem es die 'Intensität' betrachtet. Die Intensität bestimmt, ob ein Wort das nächste Wort modifiziert.

Diese beiden Werte werden anhand des Datums als Indikator in einer SQL-Datei gespeichert, um späteres Abrufen zu erleichtern.

###### 4.3. Artikelanzahl

Hierbei wird die Anzahl der Artikel von jedem Tag gezählt und in einer SQL-Datei gespeichert.
Dadurch kann man die Entwicklung der Artikelanzahl über die Jahre hinweg sehen.
Hier wird unterteilt in die Anzahl der Artikel pro Tag sowie pro Monat.

#### 5. Graphen erstellen

Die Daten, die ich in den SQL-Dateien gespeichert habe, werden in einem Graphen dargestellt.
Hierfür habe ich als erstes eine globale Funktion erstellt, die mithilfe von verschiedenen Eingabeparametern den Graphen erstellt. ([`Plotting\Plotting.py`](../../Plotting/Plotting.py)).
Diese Funktion wird dann in den einzelnen Dateien aufgerufen, benötigt zum Zeichnen des Graphen werden die Daten aus der Datenbank, alle Spalten, die entfernt werden sollen (z.B. ID), und andere Kleinigkeiten wie der Titel und Farben benötigt.
Innerhalb der verschiedenen Analysetypen erstelle ich weitere Wiederholungsanweisungen um die für jede Rubrik einen Graphen zu erstellen, sowie für jedes Jahr, um die Entwicklung über die Jahre und innerhalb der Jahre zu analysieren.

#### 6. Interaktive Webseite erstellen

###### 6.1. Datenauswahl

Ein weiterer Weg um meine Daten zu visualisieren war durch erstellen einer interaktiven Webseite. Diese Webseite wurde mit `Streamlit` erstellt. `Streamlit` ist ein sehr beliebtes Modul um Webseiten in Python zu erstellen. Auf der Webseite kann man als erstes auswählen, welche Option man analysieren möchte (Wordcount, Polarisation, Subjektivität, Artikelanzahl). Danach kann man die auswählen, wie viele verschiedene Graphen man übereinander angezeigt haben möchte. Je nach Anzahl kann man auswählen was für Daten der jeweilige Graph haben soll. Nach auswahl der Daten kann man auswählen in welchem Jahr-Zeitraum? die Daten angezeigt werden sollen.

###### 6.2. Graph erstellen

Jetzt kann man den Graphen erst durch drücken eines Buttons erstellen, um andauerndes Laden des Graphen im Hintergrund zu vermeiden. Der Graph wird mithilfe der Interaktiven Bibliothek `plotly` erstellt, die es ermöglicht, den Graphen zu zoomen, zu verschieben und bestimmte Daten mithilfe der Legende auszublenden.

###### 6.3 . Tabelle mit Top 10

Zusätzlich zu den Graphen habe ich eine Tabelle erstellt, welche den Datensatz nach den in [6.2.](#61-datenauswahl) ausgewählten Kriterien sortiert und die Top 10 anzeigt.
Angezeigt wird dann der Titel des Artikels, das Datum und auch die _Content ID_ des Artikels. Mit dieser ID kann man auf einer anderen Webseite den Artikel direkt aufrufen, und genauer anschauen. Diese Webseite ist öffentlich nicht zugänglich, da die Daten nur Lokal auf meinem Laptop gespeichert sind.

---

## [Ergebnisse](./Aufbau.md#ergebnisse)

- längste Kapitel der schriftlichen Arbeit
- sollte untergliedert werden
- Kurze Texte erklären die Tabellen und Abbildungen

Ziel der Arbeit war eine Langzeitdatenanalyse aller Artikel der beiden Zeitschriften. Aufgrund der zeitlichen Bgrenzung in dieser Forschungsarbeit konnte ich nicht die kompletten Daten herunterladen. Deshalb habe ich mich darauf beschränkt die Entwicklung von 2010 - 2021 genauer zu analysieren, indem ich den Anfang des Zeitraums 2010 - 2011 und das Ende 2020 - 2021 heruntergeladen habe. Mit diesen Daten kann ich nun abschätzen, wie sich die verschiedenen Aspekte entwickelt haben.

Ich habe zum Vorstellen der Ergebnisse besonders aussagekräftige Ergebnisse ausgewählt, die die Entwicklung der beiden Zeitungen gut darstellen. Man kann alle anderen Graphen in der interaktiven Webseite nachschauen, sowie auf den generierten Graphen. (Fußnote?)

**1. Entwicklung der Artikelanzahl**

Auf dem dargestellten Bild kann man die Entwicklung der Artikelanzahl der Rubrik "Opinion" der Zeitung "The Guardian" sehen. Jeder Punkt stellt einen Tag dar. Die Y-Achse zeigt die Anzahl der Artikel, die an diesem Tag veröffentlicht wurden. Man erkennt, dass in der Mitte des Graphen keine Punkte vorhanden sind. Dies ist aufgrund der fehlenden Daten in diesem Zeitraum. In schwarz ist die Regressionsgerade dargestellt, welche die Entwicklung der Artikelanzahl über die Jahre hinweg darstellt. Wie auch an dem Text in der recht oberen Ecke zu erkennen ist, ist die Entwicklung der Artikelanzahl in den letzten Jahren abgesunken. Durchschnittlich sind es ca. 11 Artikel weniger im Jahr 2021 als im Jahr 2010.

[Artikelanzahl - Guardian - Opinion - Days]

![Artikelanzahl - Guardian - Opinion - Days](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Articlecount/Guardian/Days/Opinion.png?raw=true)

---

Hingegen ist bei der New York Times ein starker Anstieg zu erkennen im Bereich Politik. Mit einem Anstieg von ca. 8 Artikeln ist dies auch visuell im Graphen wiederzuerkennen.

[Artikelanzahl - NYT - Politics - Days]

![Artikelanzahl - NYT - Politics - Days](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Articlecount/NYT/Days/Politics.png?raw=true)

---

Bestätigt wird dies durch die Graphen der Artikelanzahl pro Monat. Hierbei ist ein starker Anstieg bei der New York Times zu erkennen, während bei "The Guardian" ein starker Abfall stattfindet.

[Artikelanzahl - Guardian - Opinion - Month]

![Artikelanzahl - Guardian - Opinion - Month](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Articlecount/Guardian/Months/Opinion.png?raw=true)

[Artikelanzahl - NYT - Politics - Days]

![Artikelanzahl - NYT - Politics - Days](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Articlecount/NYT/Months/Politics.png?raw=true)

---

**2. Entwicklung des Sentiments**

Die Sentimentanalyse wird unterteilt in Polarisation und Subjektivität.

**Die Polarisation** gibt an, ob ein Text positiv oder negativ ist. -1 bedeutet sehr negativ, 1 bedeutet positiv. Ein durschnittlicher Wert beider Zeitschriften ist 0.1.

[Polarisation - Guardian - Together]

![Polarisation - Guardian - Together](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Sentiment/polarity/Guardian/Together.png?raw=true)
In der Grafik werden die 3 Kategorien der Zeitschrift "The Guardian" verglichen. Es ist klar dargestellt, dass die Polarisation über die Jahre hinweg relativ konstant ist und auch zwischen den Kategorien vergleichbar ist. Es gibt keine großen Schwankungen, und die Werte sind immer um ca. 0.1.

[Polarisation - NYT - Together]

![Polarisation - NYT - Together](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Sentiment/polarity/NYT/Together.png?raw=true)
Auch bei der New York Times ist ein ähnliches Bild zu erkennen. Die Werte sind relativ konstant und auch hier gibt es keine großen Schwankungen. Die Werte sind immer um ca. 0.1.

---

**Die Subjektivität** gibt an, wie subjektiv ein Text ist. 0 bedeutet sehr objektiv, 1 bedeutet subjektiv. Ein durschnittlicher Wert beider Zeitschriften ist 0.4, wie man an der Grafik unten erkennen kann. Hier wurden alle drei Kategorien zusammengefasst und in einem Graphen dargestellt.

[Subjektivität - NYT - All]

![Subjektivität - NYT - All](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Sentiment/subjectivity/NYT/All.png?raw=true)

Wenn man aber die einzelnen Kategorien betrachtet (Bild unten), sieht man deutliche Unterschiede. Die Kategorie "World" ist deutlich subjektiver als die anderen beiden Kategorien. Dies ist auch bei "The Guardian" zu erkennen. Die Kategorie "World" ist zu beginn deutlich subjektiver als die anderen beiden Kategorien, und die Kateogrie "Opinion" ist am subjektivsten.

[Subjektivität - NYT - Together]

![Subjektivität - NYT - Together](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Sentiment/subjectivity/NYT/Together.png?raw=true)

Interessant ist auch, dass dieses Ergebnis sehr vergleichbar mit dem Ergebnis von "The Guardian" ist. Auch hier ist die Kategorie "World" am subjektivsten, wobei sich "Politics" langsam vom eher Objektiven "Opinion" entfernt und sich "World" nähert:

[Subjektivität - Guardian - Together]

![Subjektivität - Guardian - Together](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Sentiment/subjectivity/Guardian/Together.png?raw=true)

---

**3. Wörteranzahl & Artikellänge**

Zuletzt noch die Wörteranzahl und die Artikellänge. "The New York Times" hat eine deutlich höhere durschnittliche Wörteranzahl mit ca. 1100 Wörtern pro Artikel. Hingegen hat "The Guardian" mit einer durschnittlichen Wörteranzahl von 800 Wörtern.
Abgesehen von dem durschnittlichen Unterschied der Wörteranzahl, gibt es auch Entwicklungen über die Jahre. Doch diese sind nicht sehr aussagekräftig, da die Korrelation sehr gering ist, was am Korreleationskoeffizienten von nur 0.09 zu erkennen ist. (Bild unten)

[Wordcount - Guardian - All]

![Wordcount - Guardian - All](https://github.com/AdminL3/Jugend-Forscht/blob/main/Output/Wordcount/Graphs/Guardian/All.png?raw=true)

---

## [Ergebnisdiskussion](./Aufbau.md#ergebnisdiskussion)

- Ergebnisse bewerten
- Interpretationen und weiterführende ÜberlegungenMängel möglich
- Hinweise auf vorhandene Literatur:
  - Abweichungen oder Übereinstimmungen kurz diskutieren

Was bedeuten die Ergebnisse? Sind sie so wie erwartet?

---

## [Fazit und Ausblick](./Aufbau.md#fazit-und-ausblick)

- Zum Abschluss der Arbeit sollte, die zu Beginn der Arbeit gestellte Forschungsfrage bzw. das Projektziel aufgegriffen werden: Wie lautet die Antwort auf die Forschungsfrage, wurde das Ziel erreicht?

---

## [Quellen- und Literaturverzeichnis](Aufbau.md#quellen--und-literaturverzeichnis)

Hier werden alle Quellen und Unterstützungsleistungen genannt, die für das Projekt verwendet und in Anspruch genommen wurden. Quellen sind z. B. Internetseiten, Fachzeitschriften und Bücher. Alle Angaben werden jeweils alphabetisch nach Nachnamen sortiert.

##### **1. Python als Programmiersprache**

- https://www.python.org/: 31.12.24, Python Software Foundation, Python als Programmiersprache

##### **2. Verwendete externe Bibliotheken**

- https://www.crummy.com/software/BeautifulSoup/: 30.12.2024, Leonard Richardson, Beautiful Soup for HTML-Parsing
- https://matplotlib.org/: 30.12.2024, © 2012 – 2024 The Matplotlib development team, Matplotlib für Graphen
- https://numpy.org/: 30.12.2024, © 2024 NumPy team, Numpy für numerische Berechnungen
- https://pandas.pydata.org/: 30.12.2024, © 2024 pandas, pandas zur Datenanalyse
- https://plotly.com/: 30.12.2024, © 2024 Plotly, Plotly für interaktive Graphen
- https://requests.readthedocs.io/en/master/: 30.12.2024, © 2024. A Kenneth Reitz Project, Requests: HTTP for Humans
- https://scikit-learn.org/: 30.12.2024, © 2007 - 2024 scikit-learn developers (BSD License), scikit-learn for Regression
- https://www.selenium.dev/: 30.12.2024, © 2024 Selenium Software Freedom Conservancy, Selenium für Web-Scraping
- https://www.sqlite.org/: 30.12.2024, SQLite3 für Datenbanken
- https://streamlit.io/: 30.12.2024, © 2024 Snowflake Inc., Streamlit für Webseiten
- https://textblob.readthedocs.io/en/dev/: 30.12.2024, © Steven Loria, TextBlob für NLP

##### **3. Literatur**

- **Die vierte Gewalt** – Wie Mehrheitsmeinung gemacht wird, auch wenn sie keine ist; 2022-09-28, Richard David Precht
- **Lückenpresse** - Das Ende des Journalismus, wie wir ihn kannten; 2016-09-01, Ulrich Teusch
- **Die große Gereiztheit** - Wege aus der kollektiven Erregung; 2018-02-19, Bernhard Pörksen
- **Fake Facts** - Wie Verschwörungstheorien unser Denken bestimmen; 2020-05-15, Katharina Nocun

---

## [Unterstützungsleistungen](./Aufbau.md#unterst%C3%BCtzungsleistungen)

- Melanie Mestl, Jugend-Forscht Projektbetreuerin, Lehrerin des Fach W-Seminar; Art der Unterstützung: Hilfe bei Struktur der Forschungsarbeit.
