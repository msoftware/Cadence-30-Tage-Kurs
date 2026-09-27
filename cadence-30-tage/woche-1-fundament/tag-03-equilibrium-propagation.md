# Tag 3 – Theorie II: Equilibrium Propagation

> Woche 1 – Fundament und erste Schritte · Zeitbedarf: 120 min  
> [← Tag 2](../woche-1-fundament/tag-02-hebb-und-hopfield.md) · [Übersicht](../README.md) · [Tag 4 →](../woche-1-fundament/tag-04-setup.md)

## Ziel des Tages

Du verstehst, wie ein Netz mit einer freien und einer „genudgten“ Phase lernen kann, ohne Gradienten rückwärts durchzureichen.

## Worum es geht

Die Free/Nudged-Regel in Cadence geht auf Equilibrium Propagation (Scellier & Bengio, 2017) zurück. Das Netz schwingt erst frei ein, dann wird der Ausgang sanft Richtung Ziel geschoben. Die Differenz der lokalen Ko-Aktivitäten zwischen beiden Phasen ist (für kleines β) proportional zum Gradienten. Wenn du das einmal selbst gebaut hast, liest sich `learning.md` später viel leichter.

## Lesen

- [ ] [Scellier & Bengio (2017): Equilibrium Propagation – Abschnitte 1–3](https://arxiv.org/abs/1602.05179)

## Vorhersage vor dem Ausführen

*Was passiert, wenn β sehr groß wird? Was, wenn die freie Phase nicht lange genug läuft, um das Gleichgewicht zu erreichen?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] Paper Abschnitt 1–3 lesen. Mathe beim ersten Lesen überfliegen, beim zweiten Lesen die Update-Regel nachvollziehen.
- [ ] `../code/tag03_equilibrium_propagation.py` ausführen (lernt XOR, ohne Backprop).
- [ ] Im Code die drei Stellen markieren: freie Phase, genudgte Phase, lokale Gewichtsänderung.
- [ ] Experiment: `BETA` auf 0,05 und auf 2,0 setzen. Was passiert? Tipp: Schau, wie β in der Update-Regel auftaucht (`LR / BETA`).
- [ ] Experiment: `FREE_STEPS` auf 5 reduzieren und die Spalte „Residuum“ beobachten. Warum lernt das Netz dann nicht mehr?
- [ ] Glossar ergänzen: freie Phase, genudgte Phase, β, Kontrast.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Welche zwei Größen braucht eine einzelne Synapse für ihr Update?
2. Warum ist der Kontrast der beiden Phasen ein Gradient, und warum gilt das nur näherungsweise?
3. Warum ist es wichtig, das Gleichgewicht vor dem Update zu überprüfen? (Merke dir das für Tag 8.)

## Fertig, wenn …

Dein XOR-Netz lernt, und du kannst ohne Hilfe erklären, warum dafür kein Backprop nötig ist.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

