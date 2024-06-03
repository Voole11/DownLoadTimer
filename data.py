import GPUtil
import psutil
import cpuinfo
import platform
import wmi
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

def get_disk_info():
    disk_info_list = []
    partitions = psutil.disk_partitions()
    c = wmi.WMI()

    # Собираем информацию о дисках и их типах
    disk_types = {}
    for disk in c.Win32_DiskDrive():
        if 'SSD' in disk.Model:
            disk_type = "SSD"
        else:
            disk_type = "HDD"
        disk_types[disk.DeviceID] = disk_type

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_type = disk_types.get(partition.device, "Неизвестно")
            disk_info = {
                "disk_device": partition.device,
                "disk_total": usage.total,
                "disk_used": usage.used,
                "disk_free": usage.free,
                "disk_usage_percent": usage.percent,
                "disk_type": disk_type
            }
            
            disk_info_list.append(disk_info)
        except PermissionError:
            continue

    return disk_info_list

print(get_disk_info())


