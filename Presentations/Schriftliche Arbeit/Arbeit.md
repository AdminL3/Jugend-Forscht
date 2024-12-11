# Schriftliche Arbeit

## Deckblatt

- Photshop
- NYT vs Guardian
- Vergleich
- Ansprechend

---

[Aufbau](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Aufbau.md)
[Vorgaben](https://github.com/AdminL3/Jugend-Forscht/blob/main/Presentations/Schriftliche%20Arbeit/Vorgaben.md)
## [Projektüberblick](./Aufbau.md#projekt%C3%BCberblick)

- Kopiert von Einleitung Kurztext.md
- sechs bis acht Sätz
- Fragestellung, Methode, Ergebnisse und Diskussion auf maximal einer Seite

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


## [Motivation und Fragestellung](./Aufbau.md#motivation-und-fragestellung)

Es gibt viele Vorurteile über die Medien, die sich im Laufe der Zeit verändert haben. Werden die Medien immer kritischer und negativer. Sind Medien in den USA subjektiver als in Großbrittaniee? 


---

## [Hintergrund und theoretische Grundlagen](./Aufbau.md#hintergrund-und-theoretische-grundlagen)

---

## [Vorgehensweise, Materialien und Methoden](./Aufbau.md#vorgehensweise-materialien-und-methoden)

Der Vorgang, um die Daten zu sammeln und zu analysieren, ist sehr komplex und wird in mehreren Schritten durchgeführt. Der erste Hauptschritt ist, den Artikeltext zu bekommen. Dafür muss ich als erstes Zugriff auf die kompletten Links der beiden Zeitschriften zugreifen. Dafür benutze ich die API von "The New York Times" und "The Guardian". Da nur sehr wenige Zeitschriften so eine API haben, musste ich mich auf die beiden Zeitschriften beschränken. Die API gibt mir die Möglichkeit, die Links der Artikel zu bekommen welche ich dann filtere nach dem Thema und dem Datum. Aufgrund der Unterverzeichnisse des Links kann man das Datum, sowie Rubrik des Artikels auslesen und sortieren (Beispiel?). Mithilfe der Links kann ich jetzt auf die Webseiten zugreifen. Doch um die Artikel zu analysieren, brauche ich Zugriff auf den Artikeltext. Dies wird unterteilt in zwei große Schritte. Als erstes benötige ich den Quellcode der Webseite. Das beschaffen des Quellcodes war der aufwendigste Prozess der ganzen Arbeit. Der Quellcode ist der HTML-Code der Webseite, welcher alle Informationen der Webseite enthält. Diesen Code kann ich durch verschiedene Methoden herunterladen. Der Prozess ist sehe unterschiedlich, je nachdem welche Webseite ich herunterlade.
Bei "The Guardian! war dieser Prozess viel einfacher. Ich konnte mit einer einfachen Anfrage mit dem Python Modul "Requests" den Quellcode der Webseite herunterladen. Dieser wurde dann in einer Textdatei gespeichert, sortiert nach Datum und Rubrik. Bei der New York Times war es komplizierter. Es gibt verschiedene Methoden um den Quellcode zu erreichen. Die Methode Requests, wie ich bei "The Guardian" genutz habe, hat nicht funktioniert. Nach bereits 100 Artikeln wurde meine IP-Adresse blockiert und (Fehlermeldung). Die zweite Methode ist "Selenium", welcher eine beliebter Web Crawler ist, mit dem man einen echten Browser wie Chrome simuliert. Doch auch hier gab es Probleme. Die New York Times hat schnell meine ungewöhnliche Aktivität bemerkt, und nur den ersten Absatz des Artikels angezeigt. 

Nach ein wenig herumprobieren, habe ich entdeckt, dass der Artikeltext in einem komplizierten Geflecht aus Json. (Andere Fehlermeldung)
Ich musste einen Weg finden, um die Paywall zu umgehen.

Der zweite Schritt ist das Parsen des Quellcodes. Das bedeutet, dass ich den Quellcode in Text umwandeln muss. Dieser Text ist der Artikeltext, welcher dann analysiert wird. Die Analyse des Textes ist der letz

---

## [Ergebnisse](./Aufbau.md#ergebnisse)


---

## [Ergebnisdiskussion](./Aufbau.md#ergebnisdiskussion)

---

## [Fazit und Ausblick](./Aufbau.md#fazit-und-ausblick)


---


## [Fazit und Ausblick](./Aufbau.md#fazit-und-ausblick)

---
