# Tag 7 – Feedback-Timing, Speichern und Wochenrückblick

> Woche 1 – Fundament und erste Schritte · Zeitbedarf: 90 min  
> [← Tag 6](../woche-1-fundament/tag-06-quickstart.md) · [Übersicht](../README.md) · [Tag 8 →](../woche-2-kernbausteine/tag-08-konzepte-und-grenzen.md)

## Ziel des Tages

Du beherrschst die Regeln, wie Feedback an die richtige Aktion gebunden wird, und kannst ein Leben speichern und fortsetzen.

## Worum es geht

Der häufigste Fehler in einer Online-Lernschleife ist, Feedback der falschen Aktion zuzuordnen. Die Quickstart-Tabelle regelt das genau: `step` mit Beobachtung, Reward der vorigen Aktion, `done` bei Episodenende, `teacher` für Demonstrationen. Ein zusätzlicher `step` ohne echtes Ergebnis wird als Null-Reward-Transition verbucht.

## Lesen

- [ ] [Quickstart: Keep feedback attached to the right action](https://github.com/muellerberndt/cadence/blob/main/docs/quickstart.md#keep-feedback-attached-to-the-right-action)
- [ ] [Continuous interaction](https://github.com/muellerberndt/cadence/blob/main/docs/continuous.md)

## Code

Speichern und Fortsetzen (aus der Doku):

```python
path = brain.save("living_brain.npz")
brain = cd.GenericBrain.load(path)
```

Gespeichert werden Parameter, Gedächtnisse, Zufallszustand und die Eligibility der offenen Aktion, **nicht** die Umgebung und die ausgegebene Aktion. Die sicherst du selbst.

## Vorhersage vor dem Ausführen

*Was macht ein zusätzlicher `step` ohne echtes Ergebnis mit der Zuordnung von Reward zu Aktion?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] Die Tabelle aus dem Quickstart abschreiben, und zwar in eigenen Worten.
- [ ] Absichtlich falsch machen: nach jeder Aktion einen zusätzlichen `step` ohne echtes Ergebnis einfügen. Plot mit Tag 6 vergleichen.
- [ ] `done=[True]` am Episodenende einbauen und das Verhalten prüfen.
- [ ] Einmal `teacher=[aktion]` mit der korrekten Aktion übergeben. Lernt das Brain schneller?
- [ ] Ein Leben nach 32 Schritten speichern, laden, die offene Aktion ausführen und die Schleife fortsetzen. Ist das Ergebnis identisch zu einem durchgehenden Lauf mit gleichem Seed?
- [ ] `continuous.md` lesen (Truncation, eigenes Scheduling).
- [ ] **Wochenrückblick** in den Notizen ausfüllen und offene Fragen in `../offene-fragen.md` übertragen.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Was genau passiert, wenn du `step` aufrufst, bevor das Ergebnis der Aktion da ist?
2. Was macht `reset()`, und warum ist es kein Moduswechsel?
3. Was musst du außer dem Brain selbst sichern, um ein Leben sauber fortzusetzen?

## Fertig, wenn …

Dein Speichern/Laden-Test liefert dasselbe Ergebnis wie ein durchgehender Lauf, und der Wochenrückblick ist geschrieben.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Wochenrückblick

**Was kann ich jetzt, was ich vor einer Woche nicht konnte?**


**Was ist mir noch unklar?** (auch in `../offene-fragen.md` eintragen)


**Welche Kontrollfrage der Woche fiel mir am schwersten?**


**Was nehme ich mir für nächste Woche vor?**


## Notizen

