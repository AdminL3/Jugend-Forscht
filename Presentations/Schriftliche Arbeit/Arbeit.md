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

---

## [Ergebnisse](./Aufbau.md#ergebnisse)

- längste Kapitel der schriftlichen Arbeit
- sollte untergliedert werden
- Kurze Texte erklären die Tabellen und Abbildungen

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

## [Quellen- und Literaturverzeichnis](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Aufbau.md#quellen--und-literaturverzeichnis)

Hier werden alle Quellen und Unterstützungsleistungen genannt, die für das Projekt verwendet und in Anspruch genommen wurden. Quellen sind z. B. Internetseiten, Fachzeitschriften und Bücher. Alle Angaben werden jeweils alphabetisch nach Nachnamen sortiert.

---

## [Unterstützungsleistungen](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Aufbau.md#unterst%C3%BCtzungsleistungen)

Hier werden sämtliche Personen und Unternehmen/Institutionen aufgeführt, die in dem Projekt unterstützt haben. Die vollständige Angabe von Unterstützungsleistungen ist wichtiger Bestandteil der Dokumentation eines wissenschaftlichen Projektes. Eine detaillierte Erläuterung von Unterstützungsleistungen hilft den Jurymitgliedern bei der Einschätzung des Eigenanteils der Arbeit und erleichtert das Jurygespräch. Vielfalt und Umfang von Unterstützungsleistungen bei Projekten im Wettbewerb Jugend forscht/Schüler experimentieren variieren stark und bestimmen nicht die Qualität des Projektes.
