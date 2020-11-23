
from bluetool import Bluetooth

bluetooth = Bluetooth()
adapters  = bluetooth.list_interfaces()

print(adapters)
