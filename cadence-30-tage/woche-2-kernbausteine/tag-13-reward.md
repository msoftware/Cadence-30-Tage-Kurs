# Tag 13 – Reward: Eligibility Traces und Dopamin

> Woche 2 – Die Kernbausteine · Zeitbedarf: 90–120 min  
> [← Tag 12](../woche-2-kernbausteine/tag-12-record-patch.md) · [Übersicht](../README.md) · [Tag 14 →](../woche-2-kernbausteine/tag-14-miniprojekt-1.md)

## Ziel des Tages

Du verstehst, wie Cadence Reward einer früheren Aktion zuordnet, und hast verzögerten Reward getestet.

## Worum es geht

Eine Eligibility Trace ist eine abklingende Markierung, welche Synapsen gerade an einer Entscheidung beteiligt waren. Kommt später ein Reward-Signal (wie Dopamin im Gehirn), werden genau die markierten Synapsen verändert. Dazu kommen ein Critic und ein assoziatives Reward-Gedächtnis.

## Lesen

- [ ] [Reward](https://github.com/muellerberndt/cadence/blob/main/docs/reward.md)

## Vorhersage vor dem Ausführen

*Bis zu welcher Verzögerung wird das Brain noch lernen?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] `reward.md` lesen.
- [ ] Die Rollen von Critic, Eligibility Trace und Reward-Gedächtnis in je einem Satz notieren.
- [ ] Experiment: Im Quickstart-Setup den Reward um 1, 2 und 3 Schritte verzögern (Rewards puffern und später übergeben).
- [ ] Lernkurven vergleichen. Ab welcher Verzögerung bricht das Lernen ein?
- [ ] Parameter der Trace (Zerfall) suchen und einmal variieren.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Was genau „merkt“ sich eine Eligibility Trace?
2. Wozu braucht es einen Critic zusätzlich zum Reward?
3. Warum passt ein langsamer Trace-Zerfall zu größerer Verzögerung?

## Fertig, wenn …

Du hast Lernkurven für drei Verzögerungen und kannst den Einbruch erklären.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

