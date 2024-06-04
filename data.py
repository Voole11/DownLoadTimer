import GPUtil
import pandas as pd
import psutil
import cpuinfo
import platform
import wmi
from psutil import disk_partitions

class Data():

    def __init__(self) -> None:
        self.get_gpu_info()
        self.get_cpu_info()
        self.get_ram_info()
        self.get_disk_info()
        self.get_system_info()


    def get_gpu_info(self):
        
        self.gpus = GPUtil.getGPUs()

        for gpu in self.gpus:
            self.gpus_dict = {
            "gpu_id" : gpu.id,
            "gpu_name" : gpu.name,
            "gpu_total_memory" : gpu.memoryTotal
            }

        return self.gpus_dict

    def get_cpu_info(self):

        self.cpu_dict = {
        "cpus_logic" : psutil.cpu_count(), #Количество логических процессоров
        "cpus_physical": psutil.cpu_count(logical=False),
        "cpu_brand" : cpuinfo.get_cpu_info()["brand_raw"],
        "cpu_hz" : cpuinfo.get_cpu_info()["hz_actual_friendly"]
        }

        return self.cpu_dict

    def get_ram_info(self):
        
        self.ram_dict = {
        "memory_total_GB" : psutil.virtual_memory().total / pow(2, 30)
        }

        return self.ram_dict

    def get_system_info(self):

        self.platform_dict = {
        "platform_name" : platform.uname().system
        }

        return self.platform_dict

    def get_disk_info(self):
        self.disk_info_list = []
        self.partitions = psutil.disk_partitions()
        self.c = wmi.WMI()

        # Собираем информацию о дисках и их типах
        self.disk_types = {}
        for disk in self.c.Win32_DiskDrive():
            if 'SSD' in disk.Model:
                self.disk_type = "SSD"
            else:
                self.disk_type = "HDD"
            self.disk_types[disk.DeviceID] = self.disk_type

        for partition in self.partitions:
            try:
                self.usage = psutil.disk_usage(partition.mountpoint)
                self.disk_type = self.disk_types.get(partition.device, "Неизвестно")
                self.disk_dict = {
                    "disk_device": partition.device,
                    "disk_total": self.usage.total,
                    "disk_used": self.usage.used,
                    "disk_free": self.usage.free,
                    "disk_usage_percent": self.usage.percent,
                    "disk_type": self.disk_type
                }
                
                self.disk_info_list.append(self.disk_dict)
            except PermissionError:
                continue

        return self.disk_info_list
    
    def get_total_dict(self):
        self.total_data_dict = {"gpu_data_total" : self.gpus_dict, 
                                "cpu_data_total" : self.cpu_dict, 
                                "disk_data_total" : self.disk_dict, 
                                "platform_data_total" : self.platform_dict, 
                                "ram_data_total" : self.ram_dict}
        return self.total_data_dict

data = Data()
total_dict = data.get_total_dict()

for key, value in total_dict.items():
    print(key, value, sep="\n")
    
df2 = pd.DataFrame(total_dict.values())
print(df2)
