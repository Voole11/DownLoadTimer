import GPUtil
import psutil

def get_info():
    
    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_total_memory = gpu.memoryTotal

        gpus_list.append((
            gpu_id, gpu_name, gpu_total_memory
        ))

    return gpus_list

