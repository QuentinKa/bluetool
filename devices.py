
from bluetool import Bluetooth

bluetooth = Bluetooth()
adapters  = bluetooth.get_connected_devices()

print(adapters)
