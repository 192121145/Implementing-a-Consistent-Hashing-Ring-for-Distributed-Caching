import hashlib
import bisect


class ConsistentHashRing:
    def __init__(self, nodes=None, replicas=100):
        self.replicas = replicas
        self.ring = {}
        self.keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def hash(self, key: str) -> int:
        """Return a 32-bit hash integer."""
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node):
        """Add physical node and its virtual nodes."""
        for i in range(self.replicas):
            v_node_key = f"{node}:{i}"
            h = self.hash(v_node_key)
            self.ring[h] = node
            bisect.insort(self.keys, h)

    def remove_node(self, node):
        """Remove physical node and all its virtual nodes."""
        remove_keys = []
        for h, n in list(self.ring.items()):
            if n == node:
                remove_keys.append(h)

        for h in remove_keys:
            del self.ring[h]
            self.keys.remove(h)

    def get_node(self, key):
        """Return the physical node responsible for key."""
        if not self.ring:
            return None

        h = self.hash(key)
        index = bisect.bisect(self.keys, h)

        if index == len(self.keys):
            index = 0

        return self.ring[self.keys[index]]
