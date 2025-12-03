import random
from consistent_hash_ring import ConsistentHashRing




def simple_modulo_assignment(key, num_nodes):
    return key % num_nodes


def simulate(num_nodes, num_keys, replicas, removal_fraction=0.25, seed=1):
    random.seed(seed)

    # Nodes
    nodes = [f"Node{i}" for i in range(num_nodes)]
    ring = ConsistentHashRing(nodes, replicas)

    # Keys
    keys = list(range(num_keys))

    # Assign using consistent hashing
    before = {k: ring.get_node(str(k)) for k in keys}

    # Remove some nodes
    removed_nodes = nodes[: int(num_nodes * removal_fraction)]
    for n in removed_nodes:
        ring.remove_node(n)

    after = {k: ring.get_node(str(k)) for k in keys}

    migrated = sum(1 for k in keys if before[k] != after[k])
    migration_percent = (migrated / num_keys) * 100

    # modulo simulation
    before_mod = {k: simple_modulo_assignment(k, num_nodes) for k in keys}
    after_mod = {k: simple_modulo_assignment(k, num_nodes - len(removed_nodes)) for k in keys}

    migrated_mod = sum(1 for k in keys if before_mod[k] != after_mod[k])
    migration_percent_mod = (migrated_mod / num_keys) * 100

    return migration_percent, migration_percent_mod
