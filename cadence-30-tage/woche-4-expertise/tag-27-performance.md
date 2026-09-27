# Tag 27 – Performance: Backends und Populationen

> Woche 4 – Expertise · Zeitbedarf: 120 min  
> [← Tag 26](../woche-4-expertise/tag-26-evolution-und-konnektome.md) · [Übersicht](../README.md) · [Tag 28 →](../woche-4-expertise/tag-28-forschung.md)

## Ziel des Tages

Du kannst Cadence auf verschiedenen Backends betreiben und Populationen von Brains parallel laufen lassen.

## Worum es geht

Neben NumPy gibt es Numba, PyTorch und MLX. `population.md` beschreibt den Torch-Zwilling des Record Patch für viele Brains in vielen Welten gleichzeitig: was sich batchen lässt (Instanzen, Streams, Patches) und was nicht (Momente).

## Lesen

- [ ] [Backends, devices, precision](https://github.com/muellerberndt/cadence/blob/main/docs/backends.md)
- [ ] [Learning in lockstep: populations on a device](https://github.com/muellerberndt/cadence/blob/main/docs/population.md)

## Aufgaben

- [ ] Beide Dokumente lesen.
- [ ] Ein zweites Backend installieren (Numba oder PyTorch).
- [ ] Mini-Projekt 2 auf NumPy und dem zweiten Backend benchmarken (Schritte pro Sekunde).
- [ ] Prüfen, dass die Ergebnisse numerisch übereinstimmen (Parity, wie in den Parity-Tests).
- [ ] Optional: eine Population von 16 Brains parallel laufen lassen.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Warum lassen sich „Momente“ nicht batchen?
2. Wann lohnt sich ein anderes Backend, und wann nicht?

## Fertig, wenn …

Du hast Benchmark-Zahlen und einen Parity-Check.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

