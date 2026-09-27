# Tag 8 – Konzepte und Grenzen

> Woche 2 – Die Kernbausteine · Zeitbedarf: 90 min  
> [← Tag 7](../woche-1-fundament/tag-07-feedback-timing.md) · [Übersicht](../README.md) · [Tag 9 →](../woche-2-kernbausteine/tag-09-vertraege-und-zertifikate.md)

## Ziel des Tages

Du kennst das Neuronenmodell, verstehst Settling und Gleichgewicht und prüfst Gleichgewicht über Residuen.

## Worum es geht

Die wichtigste Disziplin in Cadence steht mehrfach in der Doku: Prüfe die Residuen der Gleichungen, bevor du behauptest, das System sei im Gleichgewicht. Und: Lokale Updates allein garantieren weder Fähigkeit noch Geschwindigkeit. Du misst beides.

## Lesen

- [ ] [Concepts and limits](https://github.com/muellerberndt/cadence/blob/main/docs/concepts.md)

## Aufgaben

- [ ] `concepts.md` lesen: Neuronenmodell, Settling, Gleichgewicht, Lebensdauer von Zuständen, Evidenz und Kontrollen.
- [ ] Die Lebensdauern der Zustände als Tabelle notieren (was lebt einen Settle lang, was einen Schritt, was ein Leben lang?).
- [ ] Eine kleine Hilfsfunktion schreiben, die nach einem Settle die Residuen ausgibt (Wege dafür findest du in `concepts.md` bzw. `api.md`).
- [ ] Residuen mit wenigen und mit vielen Settle-Iterationen vergleichen.
- [ ] Rückbezug zu Tag 3: Wo entspricht das deinem Experiment mit zu wenigen `steps`?

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Was ist ein Residuum, und welcher Wert zeigt Gleichgewicht an?
2. Warum lehrt ein roher `Brain.settle`-Aufruf die Gewichte nicht automatisch etwas?
3. Welche Kontrollen verlangt die Doku, bevor man eine Fähigkeit behauptet?

## Fertig, wenn …

Deine Residuen-Funktion läuft, und du hast die Lebensdauer-Tabelle.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

