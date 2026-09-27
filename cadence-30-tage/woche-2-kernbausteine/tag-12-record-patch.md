# Tag 12 – Record Patch: Tag schreiben, Nacht schlafen

> Woche 2 – Die Kernbausteine · Zeitbedarf: 120 min  
> [← Tag 11](../woche-2-kernbausteine/tag-11-records-cortex.md) · [Übersicht](../README.md) · [Tag 13 →](../woche-2-kernbausteine/tag-13-reward.md)

## Ziel des Tages

Du kennst den Record Patch (`RecordPatchNet`) mit seinem Zweiphasen-Erwerb und kannst einen Store diagnostizieren.

## Worum es geht

Der Record Patch ist ein gated linearer Kontext mit einem Record-Store im Patch. Tagsüber wird jede Beobachtung einmal geschrieben. Nachts lernen die langsamen Gewichte aus den „Träumen“ des eigenen Stores (`sleep`).

## Lesen

- [ ] [The record patch](https://github.com/muellerberndt/cadence/blob/main/docs/record-patch.md)

## Vorhersage vor dem Ausführen

*Wird die Vorhersage nach `sleep` besser, gleich oder schlechter? Warum?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] `record-patch.md` lesen: ein beobachteter Pfad, Skalierung der Eingabe, was Records enthalten, Diagnose eines Stores.
- [ ] Das Beispiel aus der Doku nachbauen.
- [ ] Die Diagnose-Werkzeuge der Doku auf deinen Store anwenden und die Ergebnisse notieren.
- [ ] Vorhersagequalität vor und nach `sleep` vergleichen.
- [ ] Optional: kategoriale Ports oder Maps als Eingangsport ausprobieren.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Was passiert „bei Tag“, was „bei Nacht“?
2. Woran erkennst du einen schlecht gefüllten Store?
3. Was ist der Unterschied zwischen dem Record Patch und dem Records-Cortex von gestern?

## Fertig, wenn …

Du hast einen Vorher/Nachher-Vergleich für `sleep` und eine Store-Diagnose.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

