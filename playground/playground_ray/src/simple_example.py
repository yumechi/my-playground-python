import ray
import os

ray.init(num_cpus=1, num_gpus=1)

@ray.remote(num_gpus=0.001)
def f(x):
    print("ray.get_gpu_ids(): {}".format(ray.get_gpu_ids()))
    print("CUDA_VISIBLE_DEVICES: {}".format(os.environ["CUDA_VISIBLE_DEVICES"]))
    return x * x

for j in range(1000):
    futures = [f.remote(i) for i in range(100)]
    print(j, ray.get(futures))
