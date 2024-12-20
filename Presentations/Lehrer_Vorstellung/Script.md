# **Wandel der Worte: Langzeitdatenanalyse journalistischer Perspektiven**

###### Siehe [Powerpoint](./Präsentation.pptx)

## Einstieg:

- Es gibt viele Vorurteile über Medien und ihre Berichterstattung
- So etwas muss man doch überprüfen können
- Aber wie?
- So kam mein Projekt zustande
  --> siehe Titel

#### Vergleich zwischen zwei Zeitungen

- **The New York Times** (USA)
- **The Guardian** (Großbritannien)

Beide gelten als qualitativ hochwertige, einflussreiche Medien. Der globale Vergleich ermöglicht interessante Einblicke in nationale Unterschiede.

---

## **Name genauer anschauen**

### 1. Journalistische Perspektiven

- **Subjektivität und Objektivität**: Sachlicher vs. meinungsbasierter Darstellung
- **Polarisation**: positive vs. negative Tonalität
- **Länge der Artikel**: Veränderungen im Umfang über die Zeit
- Weitere Aspekte möglich: **Themenwahl, Sprache, Stil**

###### Angewandt an einen Text

---

### 2. Langzeit-

- **Zeitlicher Wandel**: Veränderungen über die Zeit
- **Über mehrere Jahre hinweg**:
  - **2020–2022**: aktuell analysiert
  - **20 Jahre**: Zielzeitraum

---

### 3. Datenanalyse

- **Riesige Datenmengen**: ca. 60.000 Artikel

  - über 2 Jahre gesammelt
  - 30.000 Artikel pro Jahr
  - Bei 20 Jahren: 0,5 Millionen Artikel

---

## Vorgang

###### **Datenbeschaffung**: Die Artikel der letzten zwei Jahre zu sammeln, war bereits ein aufwändiger Prozess.

1. **Links**: API-Zugriff auf die Artikel
   - Deswegen spezifische Zeitungen, bei denen dies möglich ist
2. **Code**: Extraktion des Source-Codes
   - Aufwändige Prozesse, um die Texte zu erhalten
   - Fehleranfällig
   - IP-Blockaden
   - Captchas
   - Banntendenz
3. **Text** aus Code extrahieren
   - Filtern aus dem Code
   - Keine üblichen Methoden, wie BeautifulSoup nutzbar
   - Eigenes Skript zur Extraktion
4. **Speicherung**: Datenbanken
   - Speicherung der Texte
   - Speicherung der Metadaten
   - Speicherung der Analyseergebnisse
5. **Analyse**: Textanalyse
   - NLP-Methoden
   - Sentimentanalyse
   - Längenanalyse
   - Vergleich der Zeitungen

---

## **Gesellschaftlicher Nutzen**

- Siehe [Geselschaftlicher Vorteil](../Gesellschaftlicher_Vorteil.md)

#### Ausgang unbekannt

Trotzdem: **Erkenntnisse** erlangen
In allen Fällen kann ein Ergebnis aussagekräftig sein:

- Überprüfung von Vorurteilen
- Stärkung des Vertrauens in Qualitätsmedien
- Sicherheit bei der Auswahl von Medien
- Ansatz für zukünftige Forschung
- Bildungswert

Erklärt:

- Überprüfung von Vorurteilen: Widerlegung der Annahme, dass amerikanische und britische Zeitungen grundlegend unterschiedlich berichten.
- Stärkung des Vertrauens in Qualitätsmedien: Beleg für objektive und einheitliche Berichterstattung in seriösen Medien.
- Ansatz für zukünftige Forschung: Untersuchung globaler Standards und Agenturen in der Gleichförmigkeit der Berichterstattung.
- Bildungswert: Förderung kritischen Denkens und Integration in Schulen/Universitäten als Beispiel für datenbasierte Argumentation.
