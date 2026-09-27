# Tag 2 – Theorie I: Hebbsches Lernen und Hopfield-Netze

> Woche 1 – Fundament und erste Schritte · Zeitbedarf: 90–120 min  
> [← Tag 1](../woche-1-fundament/tag-01-ueberblick.md) · [Übersicht](../README.md) · [Tag 3 →](../woche-1-fundament/tag-03-equilibrium-propagation.md)

## Ziel des Tages

Du verstehst, wie ein rekurrentes Netz in einen Fixpunkt „einschwingt“ und dabei ein unvollständiges Muster vervollständigt.

## Worum es geht

Cadence-Regionen „settlen“ gemeinsam in ein Gleichgewicht, und genau dadurch vervollständigen sie eine partielle Eingabe. Das Hopfield-Netz ist die einfachste Form dieser Idee: Hebbsche Gewichte speichern Muster als Energieminima, und die Dynamik rollt bergab in das nächste Minimum.

## Lesen

- [ ] [Wikipedia: Hopfield network (Abschnitte Structure, Updating, Energy)](https://en.wikipedia.org/wiki/Hopfield_network)
- [ ] [Wikipedia: Hebbian theory](https://en.wikipedia.org/wiki/Hebbian_theory)

## Vorhersage vor dem Ausführen

*Das Netz startet mit 25 % gekippten Bits. Wird es das Originalmuster exakt wiederfinden? Steigt oder sinkt die Energie dabei?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] Die beiden Artikel lesen, Fokus auf die Energiefunktion und die Update-Regel.
- [ ] Vor dem Ausführen: Vorhersage aufschreiben (siehe unten).
- [ ] `../code/tag02_hopfield.py` ausführen und die Ausgabe mit deiner Vorhersage vergleichen.
- [ ] Experiment 1: Anzahl gespeicherter Muster `P` schrittweise erhöhen (5, 10, 14, 20). Ab wann scheitert die Vervollständigung? (Stichwort: Kapazität ≈ 0,14·N)
- [ ] Experiment 2: Mehr Bits kippen (25 → 40 → 50). Was passiert bei 50 %?
- [ ] Glossar ergänzen: Fixpunkt, Energie, Attraktor, Hebbsche Regel.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum sinkt die Energie bei jedem asynchronen Update nie?
2. Was ist ein „Spurious State“ und wann tritt er auf?
3. Welche Information nutzt die Hebbsche Regel, um ein Gewicht zu setzen, und welche nicht?
4. Welcher Satz im Cadence-README beschreibt genau das, was du heute gebaut hast?

## Fertig, wenn …

Du hast beide Experimente gemacht und kannst den Zusammenhang „Gleichgewicht = Mustervervollständigung“ in zwei Sätzen erklären.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

