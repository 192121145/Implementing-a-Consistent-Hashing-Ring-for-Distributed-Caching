from simulate import simulate

NUM_NODES = 8
NUM_KEYS = 10000
REPLICAS = 200
REMOVAL_FRACTION = 0.25

if __name__ == "__main__":
    ch, mod = simulate(
        num_nodes=NUM_NODES,
        num_keys=NUM_KEYS,
        replicas=REPLICAS,
        removal_fraction=REMOVAL_FRACTION
    )

    print("=== Simulation Results ===")
    print(f"Consistent Hash Migration: {ch:.2f}%")
    print(f"Modulo Migration: {mod:.2f}%")
