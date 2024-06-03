import GPUtil
import psutil
import cpuinfo
import platform
from psutil import disk_partitions

def get_gpu_info():
    
    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        gpus_dict = {
        "gpu_id" : gpu.id,
        "gpu_name" : gpu.name,
        "gpu_total_memory" : gpu.memoryTotal
        }

    return gpus_dict

def get_cpu_info():

    cpu_dict = {
    "cpus_logic" : psutil.cpu_count(), #Количество логических процессоров
    "cpus_physical": psutil.cpu_count(logical=False),
    "cpu_brand" : cpuinfo.get_cpu_info()["brand_raw"],
    "cpu_hz" : cpuinfo.get_cpu_info()["hz_actual_friendly"]
    }

    return cpu_dict

def get_ram_info():
    
    memory_dict = {
    "memory_total_GB" : psutil.virtual_memory().total / pow(10, 9)
    }

    return memory_dict

def get_system_info():

    platform_dict = {
    "platform_name" : platform.uname().system
    }

    return platform_dict

print(get_disk_info())


