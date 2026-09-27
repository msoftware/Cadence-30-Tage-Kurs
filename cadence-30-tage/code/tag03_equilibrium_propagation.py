"""Tag 3: Equilibrium Propagation lernt XOR, ganz ohne Backpropagation.

Ablauf pro Epoche:
  1. freie Phase:    Netz schwingt mit festen Gewichten ins Gleichgewicht ein
  2. genudgte Phase: Ausgang wird sanft (Staerke beta) Richtung Ziel geschoben
  3. lokale Regel:   jedes Gewicht aendert sich nur aus der Ko-Aktivitaet
                     seiner zwei Neuronen, Kontrast genudgt minus frei
Nach Scellier & Bengio (2017), arXiv:1602.05179. Nur NumPy noetig.
"""
import numpy as np

rng = np.random.default_rng(1)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
T = np.array([[0], [1], [1], [0]], float)

NH = 8                   # versteckte Neuronen
BETA = 0.5               # Nudge-Staerke         (Experiment: 0.05 und 2.0)
LR = 0.1                 # Lernrate
FREE_STEPS = 60          # Iterationen freie Phase (Experiment: 5)

W1 = rng.normal(0, 0.5, (2, NH)); b1 = np.zeros(NH)
W2 = rng.normal(0, 0.5, (NH, 1)); b2 = np.zeros(1)

rho = lambda s: np.clip(s, 0, 1)                          # "hard sigmoid"


def relax(x, h, y, beta=0.0, t=None, steps=FREE_STEPS, dt=0.2):
    """Gradientenabstieg auf der Energie: Zustaende laufen ins Gleichgewicht.
    Gibt ausserdem das Residuum zurueck (wie weit vom Gleichgewicht)."""
    for _ in range(steps):
        dh = x @ W1 + y @ W2.T + b1 - h
        dy = h @ W2 + b2 - y
        if beta:
            dy += beta * (t - y)                          # der Nudge
        # Zustaende bleiben im Intervall [0, 1] (projizierter Abstieg)
        h_new, y_new = rho(h + dt * dh), rho(y + dt * dy)
        residual = float(np.abs(h_new - h).max() + np.abs(y_new - y).max()) / dt
        h, y = h_new, y_new
    return h, y, residual


for epoch in range(2001):
    h0 = np.full((4, NH), 0.5); y0 = np.full((4, 1), 0.5)
    hf, yf, res_f = relax(X, h0, y0)                      # 1. frei
    hn, yn, _ = relax(X, hf, yf, BETA, T, steps=30)       # 2. genudgt
    # 3. lokale Kontrast-Regel: kein Rueckwaertsdurchlauf, kein Graph
    W1 += LR / BETA * (X.T @ rho(hn) - X.T @ rho(hf)) / 4
    W2 += LR / BETA * (rho(hn).T @ rho(yn) - rho(hf).T @ rho(yf)) / 4
    b1 += LR / BETA * (rho(hn) - rho(hf)).mean(0)
    b2 += LR / BETA * (rho(yn) - rho(yf)).mean(0)
    if epoch % 250 == 0:
        mse = float(((yf - T) ** 2).mean())
        print(f"Epoche {epoch:4d}  Fehler {mse:.4f}  Residuum {res_f:.1e}  "
              f"Ausgaben {np.round(yf.ravel(), 2) + 0.0}")
print("Ziel: [0, 1, 1, 0]")
