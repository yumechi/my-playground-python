import ray
import os
import random

ray.init(num_cpus=4, num_gpus=1)

@ray.remote(num_cpus=0.10, num_gpus=0.001)
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        # self.n += 1
        self.n = random.randint(1, 50)

    def read(self):
        print("ray.get_gpu_ids(): {}".format(ray.get_gpu_ids()))
        print("CUDA_VISIBLE_DEVICES: {}".format(os.environ["CUDA_VISIBLE_DEVICES"]))
        return self.n

# 桁を大きくしたら大量にワーカーができてエラーが多発したので、これくらいまでで
for j in range(4, 100):
    counters = [Counter.remote() for i in range(j)]
    [c.increment.remote() for c in counters]
    futures = [c.read.remote() for c in counters]
    print(ray.get(futures))

