# Cadence in 30 Tagen

Ein Trainingsplan, um [Cadence](https://github.com/muellerberndt/cadence) von den Grundlagen bis zur Expertenebene zu lernen. Jeder Tag hat eine eigene Datei mit Ziel, Lektüre, Aufgaben, Kontrollfragen und Platz für Notizen.

## Bevor du startest

Cadence ist ein Forschungsprojekt in sehr aktiver Entwicklung. Schnittstellen und Defaults ändern sich schnell, und die Doku hinkt dem Code teilweise hinterher. Deshalb legst du dich an Tag 4 auf einen festen Commit fest und bleibst die 30 Tage dabei. Falls ein Dokument aus dem Plan in deinem Commit fehlt oder umbenannt wurde, ist `docs/index.md` deines Commits die Referenz. Die Themenreihenfolge bleibt trotzdem sinnvoll.

| | |
|---|---|
| Gepinnter Cadence-Commit | `__________` |
| Datum des Commits | __________ |
| Gepinnter cadence-examples-Commit | `__________` |
| Startdatum | __________ |

Zeitbedarf: etwa 1,5 bis 2 Stunden pro Tag, an Projekttagen mehr. Voraussetzungen: solides Python, Grundkenntnisse in NumPy und linearer Algebra. ML-Vorwissen hilft, ist aber nicht zwingend.

## So arbeitest du mit den Dateien

Die Checkboxen (`- [ ]`) werden in den meisten Markdown-Editoren (Obsidian, VS Code, Typora, GitHub) klickbar. Beantworte die Kontrollfragen immer zuerst aus dem Gedächtnis: Das aktive Erinnern ist der Teil, der das Wissen festigt. Alles, was unklar bleibt, sammelst du in [offene-fragen.md](offene-fragen.md). Das [Glossar](glossar.md) baust du über die 30 Tage selbst auf. Eigenen Code legst du im Ordner `projekte/` ab, die Starter-Codes für Tag 2 und 3 liegen in `code/`.

## Fortschritt

### Woche 1 – Fundament und erste Schritte

- [ ] [Tag  1 – Überblick: Was ist Cadence?](woche-1-fundament/tag-01-ueberblick.md)
- [ ] [Tag  2 – Theorie I: Hebbsches Lernen und Hopfield-Netze](woche-1-fundament/tag-02-hebb-und-hopfield.md)
- [ ] [Tag  3 – Theorie II: Equilibrium Propagation](woche-1-fundament/tag-03-equilibrium-propagation.md)
- [ ] [Tag  4 – Setup: Installieren, Commit pinnen, Tests laufen lassen](woche-1-fundament/tag-04-setup.md)
- [ ] [Tag  5 – Orientierung: Cadence für ML-Leute](woche-1-fundament/tag-05-orientierung.md)
- [ ] [Tag  6 – Quickstart: Die eine Lernschleife](woche-1-fundament/tag-06-quickstart.md)
- [ ] [Tag  7 – Feedback-Timing, Speichern und Wochenrückblick](woche-1-fundament/tag-07-feedback-timing.md)

### Woche 2 – Die Kernbausteine

- [ ] [Tag  8 – Konzepte und Grenzen](woche-2-kernbausteine/tag-08-konzepte-und-grenzen.md)
- [ ] [Tag  9 – Numerische Verträge und Konvergenz-Zertifikate](woche-2-kernbausteine/tag-09-vertraege-und-zertifikate.md)
- [ ] [Tag 10 – Lokales Lernen: die Free/Nudged-Regel](woche-2-kernbausteine/tag-10-lokales-lernen.md)
- [ ] [Tag 11 – Records: das Gedächtnis für Konsequenzen](woche-2-kernbausteine/tag-11-records-cortex.md)
- [ ] [Tag 12 – Record Patch: Tag schreiben, Nacht schlafen](woche-2-kernbausteine/tag-12-record-patch.md)
- [ ] [Tag 13 – Reward: Eligibility Traces und Dopamin](woche-2-kernbausteine/tag-13-reward.md)
- [ ] [Tag 14 – Mini-Projekt 1: Bandit oder 1D-Welt](woche-2-kernbausteine/tag-14-miniprojekt-1.md)

### Woche 3 – Brains selbst bauen

- [ ] [Tag 15 – Einen eigenen Cortex schreiben](woche-3-brains-bauen/tag-15-cortex-schreiben.md)
- [ ] [Tag 16 – Ein Brain komponieren: Genom und Entwicklung](woche-3-brains-bauen/tag-16-brain-komponieren.md)
- [ ] [Tag 17 – Zeitliches Lernen: der Temporal Patch](woche-3-brains-bauen/tag-17-zeitliches-lernen.md)
- [ ] [Tag 18 – Privates Planen und die Handlungsschleife](woche-3-brains-bauen/tag-18-planen-und-handeln.md)
- [ ] [Tag 19 – Belief Patch und Imagination](woche-3-brains-bauen/tag-19-belief-patch.md)
- [ ] [Tag 20 – Gesteuerter Cortex, Governor und das Life](woche-3-brains-bauen/tag-20-steuerung-und-life.md)
- [ ] [Tag 21 – Mini-Projekt 2: Eigenes Brain mit eigenen Daten](woche-3-brains-bauen/tag-21-miniprojekt-2.md)

### Woche 4 – Expertise

- [ ] [Tag 22 – Beispiele I: Arm und Artist](woche-4-expertise/tag-22-beispiel-arm-artist.md)
- [ ] [Tag 23 – Beispiele II: World und Connect Four](woche-4-expertise/tag-23-beispiel-world-connect-four.md)
- [ ] [Tag 24 – Messen wie ein Experte: Task-Design, Fehler, Skalierung](woche-4-expertise/tag-24-messen.md)
- [ ] [Tag 25 – Receipts, Protokolle und der Brain-Viewer](woche-4-expertise/tag-25-receipts-und-viewer.md)
- [ ] [Tag 26 – Evolution und Brains aus Konnektomen](woche-4-expertise/tag-26-evolution-und-konnektome.md)
- [ ] [Tag 27 – Performance: Backends und Populationen](woche-4-expertise/tag-27-performance.md)
- [ ] [Tag 28 – Forschungsebene: Paper, Ideen, Theoreme](woche-4-expertise/tag-28-forschung.md)
- [ ] [Tag 29 – Abschlussprojekt, Teil 1: Entwerfen und bauen](woche-4-expertise/tag-29-abschlussprojekt-bauen.md)
- [ ] [Tag 30 – Abschlussprojekt, Teil 2: Messen, dokumentieren, beitragen](woche-4-expertise/tag-30-abschlussprojekt-messen.md)

## Weitere Dateien

- [Glossar](glossar.md): wächst mit dir
- [Offene Fragen](offene-fragen.md): dein Fragen-Log
- [Vorlage Abschlussprojekt](abschlussprojekt-vorlage.md): für Tag 29 und 30
- `code/tag02_hopfield.py` und `code/tag03_equilibrium_propagation.py`: getestete Starter-Codes (nur NumPy)

## Wichtige Links

- [Cadence-Repo](https://github.com/muellerberndt/cadence) · [Doku-Index](https://github.com/muellerberndt/cadence/blob/main/docs/index.md) · [API-Referenz](https://github.com/muellerberndt/cadence/blob/main/docs/api.md)
- [Beispiel-Repo](https://github.com/muellerberndt/cadence-examples) · [Live brains](https://floatingpragma.io/cadence-examples/)
- [Paper auf PhilPapers](https://philpapers.org/rec/MUECAP-2)
