"""Monte Carlo прогноз кількості спринтів до релізу (ЛР9).

Запуск: python lr09_forecast/monte_carlo.py <залишок_points> <velocity через кому>
Приклад: python lr09_forecast/monte_carlo.py 220 21,17,26,14
"""
import math
import random
import sys

SIMULATIONS = 1000
SEED = 2026  # фіксоване зерно, щоб прогін можна було повторити


def simulate(remaining, velocities, simulations=SIMULATIONS, seed=SEED):
    rng = random.Random(seed)
    results = []
    for _ in range(simulations):
        left = remaining
        sprints = 0
        while left > 0:
            left -= rng.choice(velocities)  # velocity одного з минулих спринтів
            sprints += 1
            if sprints > 1000:  # якщо всі velocity нульові, прогноз не сходиться
                break
        results.append(sprints)
    results.sort()
    p50 = results[math.ceil(0.50 * simulations) - 1]
    p85 = results[math.ceil(0.85 * simulations) - 1]
    return p50, p85


if __name__ == "__main__":
    remaining = float(sys.argv[1])
    velocities = [float(v) for v in sys.argv[2].split(",")]
    p50, p85 = simulate(remaining, velocities)
    print(f"P50 = {p50} спринтів, P85 = {p85} спринтів ({SIMULATIONS} прогонів)")
