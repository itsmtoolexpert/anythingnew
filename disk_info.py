import shutil


def disk_percent_usage(directory):
  disk_info = shutil.disk_usage(directory)
  #disk_info_rounded = round(disk_info.used * 100 / disk_info.total, 2)
  return round(disk_info.used * 100 / disk_info.total, 2)
