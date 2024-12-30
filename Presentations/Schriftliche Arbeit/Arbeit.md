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

> [!INFO]
> Die fachliche Kurzfassung fasst das Projekt kurz für die Jurymitglieder zusammen. Im Unterschied zum Projektüberblick stehen hier die wissenschaftlichen Erkenntnisse im Vordergrund. Die fachliche Kurzfassung sollte immer auf dem aktuellen Stand der schriftlichen Arbeit sein.

---

## [Motivation und Fragestellung](./Aufbau.md#motivation-und-fragestellung)

- Es gibt viele Vorurteile über die Medien, die sich im Laufe der Zeit verändert haben. Werden die Medien immer kritischer und negativer.
- Sind Medien in den USA subjektiver als in Großbrittaniee?
- Bücher von Mama anschauen

---

## [Hintergrund und theoretische Grundlagen](./Aufbau.md#hintergrund-und-theoretische-grundlagen)

- Bei mir nicht nötig?
- Was wurde schon erforscht?

---

## [Vorgehensweise, Materialien und Methoden](./Aufbau.md#vorgehensweise-materialien-und-methoden)

### Vorgehensweise

Der Vorgang, um die Daten zu sammeln und zu analysieren, ist sehr komplex und wird in mehreren Schritten durchgeführt.

#### 1. Links sammeln

Der erste Hauptschritt ist, den Artikeltext zu bekommen. Dafür muss ich als erstes Zugriff auf die kompletten Links der beiden Zeitschriften zugreifen. Dafür benutze ich die API von "The New York Times" und "The Guardian". Da nur sehr wenige Zeitschriften so eine API haben, musste ich mich auf die beiden Zeitschriften beschränken. Die API gibt mir die Möglichkeit, die Links der Artikel zu bekommen welche ich dann filtere nach dem Thema und dem Datum. Aufgrund der Unterverzeichnisse des Links kann man das Datum, sowie Rubrik des Artikels auslesen und sortieren (Beispiel?).
Mithilfe der Links kann ich jetzt auf die Webseiten zugreifen. Doch um die Artikel zu analysieren, brauche ich Zugriff auf den Artikeltext. Dies wird unterteilt in zwei große Schritte:

#### 2. Quellcode herunterladen

Als erstes benötige ich den Quellcode der Webseite. Das beschaffen des Quellcodes war der vermutlich aufwendigste Prozess der ganzen Arbeit. Der Quellcode ist der HTML-Code der Webseite, welcher alle Informationen der Webseite enthält. Diesen Code kann ich durch verschiedene Methoden herunterladen. Der Prozess ist sehr unterschiedlich, je nachdem welche Webseite ich herunterlade.
Bei "The Guardian" war dieser Prozess viel einfacher. Ich konnte mit einer einfachen Anfrage mit dem Python Modul "Requests" den Quellcode der Webseite herunterladen. Dieser wurde dann in einer Textdatei gespeichert, sortiert nach Datum und Rubrik.
Bei der New York Times war es komplizierter. Es gibt verschiedene Methoden um den Quellcode zu erreichen. Die Methode Requests, wie ich bei "The Guardian" genutz habe, hat nicht funktioniert. Nach bereits 100 Artikeln wurde meine IP-Adresse blockiert und (Fehlermeldung). Die zweite Methode ist "Selenium", welcher eine beliebter Web Crawler ist, mit dem man einen echten Browser wie Chrome simuliert. Doch auch hier gab es Probleme. Die New York Times hat schnell meine ungewöhnliche Aktivität bemerkt, und nur den ersten Absatz des Artikels angezeigt. Außerdem wurde der Inhalt des Artikels hinter einer Paywall versteckt. Dies hat meine Analyse unmöglich gemacht, und ich musste einen Weg finden, um die Paywall zu umgehen. Nach ein wenig herumprobieren, habe ich entdeckt, dass der Artikeltext außer dem Front-End, im "Backend" auch vorhanden ist. Aber leider in einem komplizierten Geflecht aus JSON-ähnlichen Strukturen. Das heißt ich konnte den Quellcode mit Selenium herunterladen und nachträglich den Text extrahieren.

#### 3. Text extrahieren

Hierfür habe ich eine Funktion erstellt, die den Text Stück für Stück den Text aus dem Backend herausfiltert und dann zusammengefügt. (Diese Funktion ist in der Datei "../NYT/Extract_Text.py" zu finden.)

```
def get_text_from_html(html):
    matches = re.findall(r'"text":"(.*?)"', html)
    matches = list(dict.fromkeys(matches))
    text = ""
    for match in matches:
        text += match + "\n"
    return text
```

Auch das extrahieren des Textes war einfacher bei "The Guardian". Hier habe ich einfach die herkömmliche Methode BeautifulSoup genutzt um anhand von HTML-Tags den Text zu lokalisieren. Dieser Text wurde dann in einer Textdatei gespeichert, sortiert nach Datum und Rubrik.

#### 4. Text analysieren

Da ich nun den Artikeltext habe, kann ich diesen nach verschiedenen ?? analysieren.

###### 4.1. Wörteranzahl

In meinem Code wird dies als "Wordcount" bezeichnet, und es ist ziemlich selbstverständlich. Zuerst habe ich den Text in einzelne Wörter aufgeteilt und diese gezählt. Diese Daten habe ich dann in einer SQL-Datei gespeichert.

###### 4.2. Sentimentalanalyse

Die Sentimentanalyse ist ein wichtiger Bestandteil meiner Arbeit. Hierbei wird der Text auf Polarisation sowie Subjektivität hin analysiert. Dies wird mithilfe des Moduls `TextBlob`]() durchgeführt.

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

Ein weiterer Weg um meine Daten zu visualisieren war durch erstellen einer interaktiven Webseite. Diese Webseite wurde mit Streamlit erstellt. Streamlit ist ein sehr beliebtes Modul um Webseiten in Python zu erstellen. Auf der Webseite kann man als erstes auswählen, welche Option man analysieren möchte (Wordcount, Polarisation, Subjektivität, Artikelanzahl). Danach kann man die auswählen, wie viele verschiedene Graphen man übereinander angezeigt haben möchte. Je nach Anzahl kann man auswählen was für Daten der jeweilige Graph haben soll. Nach auswahl der Daten kann man auswählen in welchem Jahr-Zeitraum? die Daten angezeigt werden sollen.

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

Ich habe zum vorstellen der Ergebnisse besonders aussagekräftige Ergebnisse ausgewählt, die die Entwicklung der beiden Zeitungen gut darstellen. Man kann alle anderen Ergebnisse in der interaktiven Webseite nachschauen, sowie auf den generierten Graphen. (Fußnote?)

---

## [Ergebnisdiskussion](./Aufbau.md#ergebnisdiskussion)

- Ergebnisse bewerten
- Interpretationen und weiterführende ÜberlegungenMängel möglich
- Hinweise auf vorhandene Literatur:
  - Abweichungen oder Übereinstimmungen kurz diskutieren

---

## [Fazit und Ausblick](./Aufbau.md#fazit-und-ausblick)

- Zum Abschluss der Arbeit sollte, die zu Beginn der Arbeit gestellte Forschungsfrage bzw. das Projektziel aufgegriffen werden: Wie lautet die Antwort auf die Forschungsfrage, wurde das Ziel erreicht?

---

## [Quellen- und Literaturverzeichnis](Aufbau.md#quellen--und-literaturverzeichnis)

Hier werden alle Quellen und Unterstützungsleistungen genannt, die für das Projekt verwendet und in Anspruch genommen wurden. Quellen sind z. B. Internetseiten, Fachzeitschriften und Bücher. Alle Angaben werden jeweils alphabetisch nach Nachnamen sortiert.

##### **1. Python als Programmiersprache**

- Python Software Foundation. _Python – Version 3.x_. [Online verfügbar](https://www.python.org/). Abgerufen am [Datum].

##### **2. Verwendete externe Bibliotheken**

Hier ist die Liste mit dem aktualisierten Datum:

- https://www.crummy.com/software/BeautifulSoup/: 30.12.2024, Leonard Richardson, Beautiful Soup for HTML-Parsing
- https://matplotlib.org/: 30.12.2024, © 2012 – 2024 The Matplotlib development team, Matplotlib für Graphen
- https://numpy.org/: 30.12.2024, © 2024 NumPy team, Numpy für numerische Berechnungen
- https://pandas.pydata.org/: 30.12.2024, © 2024 pandas, pandas zur Datenanalyse
- https://plotly.com/: 30.12.2024, © 2024 Plotly, Plotly für interaktive Graphen
- https://requests.readthedocs.io/en/master/: 30.12.2024, ©MMXVIX. A Kenneth Reitz Project, Requests: HTTP for Humans
- https://scikit-learn.org/: 30.12.2024, © 2007 - 2024 scikit-learn developers (BSD License), scikit-learn for Regression
- https://www.selenium.dev/: 30.12.2024, © 2024 Selenium Software Freedom Conservancy, Selenium für Web-Scraping
- https://www.sqlite.org/: 30.12.2024, SQLite3 für Datenbanken
- https://streamlit.io/: 30.12.2024, © 2024 Snowflake Inc., Streamlit für Webseiten
- https://textblob.readthedocs.io/en/dev/: 30.12.2024, © Steven Loria, TextBlob für NLP

---

## [Unterstützungsleistungen](./Aufbau.md#unterst%C3%BCtzungsleistungen)

- Melanie Mestl, Jugend-Forscht Projektbetreuerin, Lehrerin des Fach W-Seminar; Art der Unterstützung: Test des Programms auf einem Großrechner und Beratung bei der Themenwahl.
