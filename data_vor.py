import glob
import json
import GPUtil
import psutil
import cpuinfo
import platform
import wmi
from psutil import disk_partitions

# Шаблон для поиска файлов с нужным расширением (например, .txt)
file_pattern = '*.acf'
data = {}

def thieve(steam_folders):
    for steam_folder in steam_folders:
        steam_folder = steam_folder[:-12]
        # Полный путь с шаблоном
        search_pattern = f'{steam_folder}/{file_pattern}'
        
        # Список всех файлов с нужным расширением в папке
        files = glob.glob(search_pattern)
        print(f'Найдено файлов: {len(files)}')

    for t, file_path in enumerate(files):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            app_id = content.split('\n')[2]
            app_id = app_id.split('"')[3]
            name = content.split('\n')[5]
            name = name.split('"')[3]
            steam_id = content.split('\n')[13]
            steam_id = steam_id.split('"')[3]
            data[t] = {'app_id': app_id, 'name': name, 'steam_id': steam_id}

    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def get_gpu_info():
    gpus_dict = {}
    gpus = GPUtil.getGPUs()

    if gpus == []:
        return {"gpu_id": "0", "gpu_name": "Some AMD/Intel device", "gpu_total_memory": "None"}
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
    "memory_total_GB" : psutil.virtual_memory().total / pow(2,30)
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
        disk_types[disk.Caption] = disk_type

    for partition in partitions:
        try:
            print(partition)
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
