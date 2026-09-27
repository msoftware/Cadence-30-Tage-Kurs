# Tag 22 – Beispiele I: Arm und Artist

> Woche 4 – Expertise · Zeitbedarf: 120 min  
> [← Tag 21](../woche-3-brains-bauen/tag-21-miniprojekt-2.md) · [Übersicht](../README.md) · [Tag 23 →](../woche-4-expertise/tag-23-beispiel-world-connect-four.md)

## Ziel des Tages

Du verstehst eine vollständige Cadence-Anwendung mit Receipt und Verifier.

## Worum es geht

Der Arm lernt seinen eigenen Körper durch Motor-Babbling, zeichnet nach, was ein Besucher vorgibt, per Suche über aufgezeichnete Konsequenzen, passt sich ohne Reset an einen längeren Arm an und kehrt zum Original zurück. Der Artist hält einen Stift und zeichnet Figuren, die er nie gesehen hat.

## Lesen

- [ ] [Examples repository](https://github.com/muellerberndt/cadence-examples)
- [ ] [Arm live](https://floatingpragma.io/cadence-examples/arm/)
- [ ] [Artist live](https://floatingpragma.io/cadence-examples/artist/)

## Aufgaben

- [ ] `cadence-examples` klonen (passend zu deinem Cadence-Commit).
- [ ] Den Code des Arm-Beispiels lesen und die Phasen markieren: Babbling, Nachzeichnen, Anpassung, Rückkehr.
- [ ] Das `receipt.json` lesen und verstehen, welche Zahlen es enthält.
- [ ] Den Verifier laufen lassen, der das Receipt aus den Event-Logs neu berechnet.
- [ ] Artist-Code überfliegen: Was unterscheidet ihn vom Arm?

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum braucht der Arm keinen Reset, als sein Glied länger wird?
2. Was ist ein Receipt, und warum wird es aus Logs neu berechnet statt einfach gespeichert?

## Fertig, wenn …

Der Verifier läuft bei dir durch.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

