# Tag 11 – Records: das Gedächtnis für Konsequenzen

> Woche 2 – Die Kernbausteine · Zeitbedarf: 120 min  
> [← Tag 10](../woche-2-kernbausteine/tag-10-lokales-lernen.md) · [Übersicht](../README.md) · [Tag 12 →](../woche-2-kernbausteine/tag-12-record-patch.md)

## Ziel des Tages

Du verstehst, wie Records Konsequenzen speichern und vorhersagen, und hast selbst eine Sequenz damit vorhergesagt.

## Worum es geht

Eine mittelwertfreie Eingabe läuft durch eine feste, dünnbesetzte Expansion mit Winner-take-all-Hemmung. Jede aktive Zelle führt einen Record darüber, was folgte. Die Vorhersage ist die aktivitätsgewichtete Summe der berührten Records. Das tatsächlich beobachtete Ergebnis wird in genau diese Records geschrieben: langsam für Konsequenzen, schnell für Reward.

## Lesen

- [ ] [Records and memory](https://github.com/muellerberndt/cadence/blob/main/docs/memory.md#records)

## Vorhersage vor dem Ausführen

*Wie viele Durchläufe der Sequenz braucht der Store, bis der Fehler klein ist?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] `memory.md` lesen (Records, schnelle Synapsen, Pattern Separation).
- [ ] Den Mechanismus als eigene Skizze zeichnen: Eingabe → Expansion → WTA → Records → Vorhersage → Schreiben.
- [ ] Mit `cd.Records` eine periodische Sequenz (z. B. Sinus diskretisiert oder 0,1,2,3,0,1,…) Schritt für Schritt vorhersagen lassen.
- [ ] Den Vorhersagefehler über die Zeit plotten.
- [ ] Experiment: Die Periode mitten im Lauf ändern. Wie schnell passt sich der Store an?

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum hilft Winner-take-all bei der Trennung ähnlicher Situationen (Pattern Separation)?
2. Warum werden Konsequenzen langsam und Rewards schnell geschrieben?
3. Warum gibt es keinen Replay-Puffer, und was ersetzt ihn?

## Fertig, wenn …

Dein Plot zeigt sinkenden Fehler und eine Anpassung nach dem Periodenwechsel.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

