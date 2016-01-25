__name__ = "vutsuak"

import random

n = random.randrange(1, 11)

print n

n = (n << 3) - n  # n<<3 gives 8n , 8n-n=7n


print n
