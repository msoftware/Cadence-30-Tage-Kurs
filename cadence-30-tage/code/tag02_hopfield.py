"""Tag 2: Ein Hopfield-Netz vervollstaendigt ein verrauschtes Muster.

Idee: Hebbsche Gewichte speichern Muster als Energieminima. Das Netz
"settlet" asynchron, bis sich kein Neuron mehr aendert (Fixpunkt).
Nur NumPy noetig:  python tag02_hopfield.py
"""
import numpy as np

rng = np.random.default_rng(0)
N, P = 100, 5            # Neuronen, gespeicherte Muster  (Experiment: P erhoehen)
FLIPS = 25               # gekippte Bits im Test-Muster   (Experiment: 40, 50)

patterns = rng.choice([-1, 1], size=(P, N))
W = (patterns.T @ patterns) / N      # Hebb: was gemeinsam feuert, verbindet sich
np.fill_diagonal(W, 0)               # keine Selbstverbindungen


def energy(s):
    return -0.5 * s @ W @ s


def settle(state, sweeps=10):
    s = state.copy()
    for sweep in range(sweeps):
        changed = False
        for i in rng.permutation(N):          # asynchrone Updates
            new = 1 if W[i] @ s >= 0 else -1
            changed |= new != s[i]
            s[i] = new
        if not changed:                        # Fixpunkt erreicht
            print(f"Fixpunkt nach {sweep + 1} Durchlaeufen")
            break
    return s


probe = patterns[0].copy()
probe[rng.choice(N, FLIPS, replace=False)] *= -1
out = settle(probe)

print(f"Overlap vorher  {probe @ patterns[0] / N:+.2f}   Energie {energy(probe):7.1f}")
print(f"Overlap nachher {out @ patterns[0] / N:+.2f}   Energie {energy(out):7.1f}")
print("(Overlap +1.00 = Originalmuster exakt wiederhergestellt)")
