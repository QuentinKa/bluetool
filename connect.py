from bluetool import Bluetooth

bluetooth = Bluetooth()
adapters  = bluetooth.list_interfaces()

print(adapters[1])


print(bluetooth.get_connected_devices())
print("---------------------------------")

#bluetooth.scan(timeout=10, adapter_idx=1)
#print(bluetooth.get_available_devices())
ADDR_UE_BOOM_2 = '88:C6:26:EE:BC:FE'
ADDR_UE_BOOM   = '88:C6:26:40:2C:2C'
ADDR_BLP9820   = '30:21:15:54:78:AA'

print(bluetooth.pair(address=ADDR_BLP9820, adapter_idx=1))
print(bluetooth.connect(address=ADDR_BLP9820, adapter_idx=1))

#print(bluetooth.pair(address=ADDR_UE_BOOM_2, adapter_idx=0))
#print(bluetooth.connect(address=ADDR_UE_BOOM_2, adapter_idx=0))
