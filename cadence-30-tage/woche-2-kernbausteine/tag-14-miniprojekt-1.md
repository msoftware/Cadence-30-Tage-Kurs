# Tag 14 – Mini-Projekt 1: Bandit oder 1D-Welt

> Woche 2 – Die Kernbausteine · Zeitbedarf: 120–180 min  
> [← Tag 13](../woche-2-kernbausteine/tag-13-reward.md) · [Übersicht](../README.md) · [Tag 15 →](../woche-3-brains-bauen/tag-15-cortex-schreiben.md)

## Ziel des Tages

Du baust eine kleine Aufgabe von Grund auf, in der Records und Reward zusammenspielen, und misst sie gegen eine Baseline.

## Worum es geht

Heute setzt du Woche 2 zusammen. Wichtig ist nicht, dass das Brain perfekt wird, sondern dass du sauber misst: Baseline, mehrere Seeds, klar definierte Metrik.

## Lesen

- [ ] [Troubleshooting (griffbereit halten)](https://github.com/muellerberndt/cadence/blob/main/docs/troubleshooting.md)

## Aufgaben

- [ ] Aufgabe wählen: (a) 3-armiger Bandit, bei dem sich der beste Arm nach 200 Schritten ändert, oder (b) 1D-Welt mit 7 Feldern und einem Ziel.
- [ ] Metrik festlegen, bevor du Code schreibst (z. B. Anteil optimaler Aktionen in den letzten 50 Schritten).
- [ ] Zufallsbaseline implementieren.
- [ ] Cadence-Brain einbauen, Feedback-Timing von Tag 7 beachten.
- [ ] 5 Seeds laufen lassen und Mittelwert ± Streuung berichten.
- [ ] Ergebnis und Code im Ordner `projekte/miniprojekt-1/` ablegen.
- [ ] **Wochenrückblick** schreiben und offene Fragen übertragen.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Hast du die Metrik vor oder nach dem Experiment festgelegt? Warum ist das wichtig?
2. Wie schnell passt sich dein Brain an den Wechsel an, im Vergleich zur Baseline?

## Fertig, wenn …

Du hast Code, eine Baseline, fünf Seeds und einen kurzen Bericht.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Wochenrückblick

**Was kann ich jetzt, was ich vor einer Woche nicht konnte?**


**Was ist mir noch unklar?** (auch in `../offene-fragen.md` eintragen)


**Welche Kontrollfrage der Woche fiel mir am schwersten?**


**Was nehme ich mir für nächste Woche vor?**


## Notizen

