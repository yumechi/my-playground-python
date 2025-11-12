import ray
import os

ray.init()

@ray.remote
def f(x):
    print("ray.get_gpu_ids(): {}".format(ray.get_gpu_ids()))
    print("CUDA_VISIBLE_DEVICES: {}".format(os.environ["CUDA_VISIBLE_DEVICES"]))
    return x * x

futures = [f.remote(i) for i in range(100)]
print(ray.get(futures))
