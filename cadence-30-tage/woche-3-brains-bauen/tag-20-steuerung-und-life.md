# Tag 20 – Gesteuerter Cortex, Governor und das Life

> Woche 3 – Brains selbst bauen · Zeitbedarf: 120 min  
> [← Tag 19](../woche-3-brains-bauen/tag-19-belief-patch.md) · [Übersicht](../README.md) · [Tag 21 →](../woche-3-brains-bauen/tag-21-miniprojekt-2.md)

## Ziel des Tages

Du kennst die aktuelle Grundlage für neue Anwendungen: das Life mit Governor.

## Worum es geht

Wichtig: Laut Doku-Index wird `GenericBrain` nur noch für bestehende Experimente behalten, neue Anwendungen („lives“) werden auf dem Life aufgebaut. Ein Steering Patch setzt die Gains des Cortex aus dessen eigener Rückmeldung, ein Governor settlet auf den eigenen Signalen des Brains und benennt dessen Modus.

## Lesen

- [ ] [Steered cortex, governor and the life](https://github.com/muellerberndt/cadence/blob/main/docs/steering.md)
- [ ] [How to build a rung demo](https://github.com/muellerberndt/cadence/blob/main/docs/howto-rung.md)

## Aufgaben

- [ ] `steering.md` lesen und die Drei-Wege-Umschaltung skizzieren.
- [ ] `howto-rung.md` lesen: die Arbeitsreihenfolge von der Welt bis zum Receipt.
- [ ] Ein minimales Life mit Governor aufsetzen und laufen lassen.
- [ ] Die Modi, die der Governor benennt, pro Schritt loggen.
- [ ] Notieren: Was würdest du am Quickstart von Tag 6 ändern, um es auf das Life umzustellen?

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Was „liest“ der Steering Patch, und was setzt er?
2. Warum ist `GenericBrain` nicht mehr die empfohlene Basis?
3. In welcher Reihenfolge baut man laut `howto-rung.md` eine Demo?

## Fertig, wenn …

Dein minimales Life läuft, und du hast den Modus-Log.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

