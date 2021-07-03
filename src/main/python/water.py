# Data class enacapsulate drink of water attributes
import time

class Water:

    def __init__(self, glass_size_oz):
        self.glass_size_oz = glass_size_oz
        self.unix_timestamp = int(time.time())