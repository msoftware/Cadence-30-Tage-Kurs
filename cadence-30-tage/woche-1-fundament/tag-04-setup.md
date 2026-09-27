# Tag 4 – Setup: Installieren, Commit pinnen, Tests laufen lassen

> Woche 1 – Fundament und erste Schritte · Zeitbedarf: 60–90 min  
> [← Tag 3](../woche-1-fundament/tag-03-equilibrium-propagation.md) · [Übersicht](../README.md) · [Tag 5 →](../woche-1-fundament/tag-05-orientierung.md)

## Ziel des Tages

Du hast eine reproduzierbare Cadence-Umgebung auf einem festen Commit und kennst die Struktur des Quellcodes.

## Worum es geht

Das Projekt ändert sich schnell. Wenn du dich nicht auf einen Commit festlegst, arbeitest du an Tag 20 womöglich mit einer anderen API als an Tag 6. Den Commit-Hash trägst du in die `README.md` dieses Plans ein.

## Lesen

- [ ] [README: Abschnitt Install](https://github.com/muellerberndt/cadence#install)
- [ ] [API-Referenz (nur überfliegen)](https://github.com/muellerberndt/cadence/blob/main/docs/api.md)
- [ ] [Optionale Backends](https://github.com/muellerberndt/cadence/blob/main/docs/backends.md)

## Code

```bash
git clone https://github.com/muellerberndt/cadence.git
cd cadence
git log -1 --format="%H %cd"        # Hash + Datum notieren!
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e .           # editierbar installieren, damit du im Code lesen/debuggen kannst
python -m pip install pytest
pytest tests/ -q
```

Alternativ ohne Klonen: `python -m pip install "cadence-net @ git+https://github.com/muellerberndt/cadence.git@<HASH>"`

## Aufgaben

- [ ] Repo klonen, Commit-Hash und Datum in die Übersicht (`../README.md`) eintragen.
- [ ] venv anlegen, Cadence editierbar installieren, Tests laufen lassen. Fehlschläge notieren, nicht ignorieren.
- [ ] `python -c "import cadence as cd; print(cd.__file__)"` ausführen.
- [ ] In `src/cadence` jede Datei kurz öffnen und in einer Zeile notieren, wofür sie da ist.
- [ ] `docs/api.md` überfliegen: Welche Klassen tauchen auf? (Liste in den Notizen)
- [ ] `CHANGELOG.md` der letzten Releases lesen, um ein Gefühl für die Änderungsgeschwindigkeit zu bekommen.

## Kontrollfragen

Beantworte sie aus dem Gedächtnis, erst danach nachschlagen. Was du nicht beantworten kannst, kommt nach `../offene-fragen.md`.

1. Welche einzige Pflichtabhängigkeit hat Cadence?
2. Welche optionalen Backends gibt es?
3. Wo im Code würdest du nach der Implementierung der lokalen Lernregel suchen?

## Fertig, wenn …

Tests laufen grün (oder du weißt genau, warum nicht), der Hash steht in der Übersicht, und du hast eine Karte von `src/cadence`.

- [ ] **Tag abgeschlossen** (auch in der [Übersicht](../README.md) abhaken)

## Notizen

