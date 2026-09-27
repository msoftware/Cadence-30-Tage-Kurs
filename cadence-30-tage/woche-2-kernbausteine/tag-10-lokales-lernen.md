# Tag 10 – Lokales Lernen: die Free/Nudged-Regel

> Woche 2 – Die Kernbausteine · Zeitbedarf: 120 min  
> [← Tag 9](../woche-2-kernbausteine/tag-09-vertraege-und-zertifikate.md) · [Übersicht](../README.md) · [Tag 11 →](../woche-2-kernbausteine/tag-11-records-cortex.md)

## Ziel des Tages

Du verstehst die Lernregel von Cadence im Detail und kennst die Wirkung ihrer wichtigsten Stellschrauben aus eigenen Experimenten.

## Worum es geht

Heute schließt sich der Kreis zu Tag 3: `learning.md` erklärt die Free/Nudged-Regel in Cadence, warum der Kontrast ein Gradient ist, und jede Stellschraube. Die Gewichte bleiben während beider Phasen fest, erst danach wird ein Update angewendet.

## Lesen

- [ ] [Local learning](https://github.com/muellerberndt/cadence/blob/main/docs/learning.md)

## Vorhersage vor dem Ausführen

*Welcher der beiden gewählten Parameter hat den größeren Effekt auf die Stabilität?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] `learning.md` lesen und mit deinem EP-Code von Tag 3 vergleichen: Was ist gleich, was anders?
- [ ] Alle Stellschrauben aus der Doku in einer Tabelle notieren (Name, Wirkung laut Doku, Standardwert in deinem Commit).
- [ ] Zwei Parameter wählen (z. B. Nudge-Stärke und Lernrate) und je drei Werte am Quickstart-Setup testen, jeweils mit mehreren Seeds.
- [ ] Ergebnisse als kleine Tabelle oder Plot festhalten.
- [ ] Die Lernregel im Quellcode finden und die Zeile markieren, in der das Update passiert.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum ist der Kontrast der beiden Phasen ein Gradient?
2. Welche Information bekommt eine Synapse in Cadence, und welche ausdrücklich nicht?
3. Was passiert, wenn die freie Phase kein Gleichgewicht erreicht hat?

## Fertig, wenn …

Du hast die Stellschrauben-Tabelle und Messungen zu zwei Parametern mit mehreren Seeds.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

