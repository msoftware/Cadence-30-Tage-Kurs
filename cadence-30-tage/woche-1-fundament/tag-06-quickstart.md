# Tag 6 – Quickstart: Die eine Lernschleife

> Woche 1 – Fundament und erste Schritte · Zeitbedarf: 90–120 min  
> [← Tag 5](../woche-1-fundament/tag-05-orientierung.md) · [Übersicht](../README.md) · [Tag 7 →](../woche-1-fundament/tag-07-feedback-timing.md)

## Ziel des Tages

Du hast die Quickstart-Schleife selbst laufen lassen, geloggt und geplottet.

## Worum es geht

Im Quickstart bewegt sich ein Körper auf einer Linie nach links, bleibt stehen oder bewegt sich nach rechts. Er beobachtet Position und Ziel, Reward ist die tatsächliche Verringerung der Distanz. Zur Hälfte wechselt das Ziel, und dasselbe Brain macht weiter. Jeder `step` bekommt die aktuelle Beobachtung und das Ergebnis der vorigen Aktion.

## Lesen

- [ ] [Quickstart](https://github.com/muellerberndt/cadence/blob/main/docs/quickstart.md)

## Code

Gerüst zum Loggen (die exakte Konstruktion des Brains übernimmst du aus `quickstart.md` deines Commits):

```python
import numpy as np
import cadence as cd

brain = ...  # laut quickstart.md erzeugen
log = []

# obs: Shape (batch, inputs), z. B. [[position, goal]]
action = brain.step(obs)                 # erster Aufruf: nur Aktion wählen
for t in range(64):
    obs, reward = env_step(action)       # Aktion wirklich ausführen
    action = brain.step(obs, reward=[reward])
    log.append((t, float(reward), int(np.asarray(action).ravel()[0])))
```

## Vorhersage vor dem Ausführen

*Wird der Reward nach dem Zielwechsel kurz einbrechen? Wie schnell erholt er sich?*

Meine Vorhersage: 

Was tatsächlich passiert ist: 

## Aufgaben

- [ ] Quickstart lesen und den Code exakt wie beschrieben ausführen.
- [ ] Das Gerüst oben anpassen, sodass Reward und Aktion pro Schritt geloggt werden.
- [ ] Reward über die Zeit plotten (matplotlib) und den Zielwechsel im Plot markieren.
- [ ] Den Lauf mit 5 verschiedenen Seeds wiederholen. Wie stark streuen die Ergebnisse?
- [ ] Notieren: Warum sagt die Doku selbst, dass diese Schleife nur die Schnittstelle zeigt und keinen verlässlichen Controller?

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum wählt der erste `step`-Aufruf nur eine Aktion und lernt nichts?
2. Was behält das Brain zwischen den Schritten (Policy, Critic, …)?
3. Was bräuchte man zusätzlich, um aus dieser Demo einen verlässlichen Controller zu machen?

## Fertig, wenn …

Du hast einen Plot mit fünf Seeds und kannst beschreiben, was nach dem Zielwechsel passiert.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

