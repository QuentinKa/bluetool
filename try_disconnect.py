from bluetool import Bluetooth

bluetooth = Bluetooth()
adapters  = bluetooth.list_interfaces()

print(bluetooth.get_connected_devices())
print("---------------------------------")

#bluetooth.scan(timeout=10, adapter_idx=1)
#print(bluetooth.get_available_devices())
ADDR_UE_BOOM_2 = '88:C6:26:EE:BC:FE'
ADDR_UE_BOOM = '88:C6:26:40:2C:2C'

#print(bluetooth.remove(address=ADDR_UE_BOOM_2, adapter_idx=1))
print(bluetooth.disconnect(address=ADDR_UE_BOOM_2, adapter_idx=1))
# 88:C6:26:EE:BC:FE UE BOOM 2

print(bluetooth.disconnect(address=ADDR_UE_BOOM, adapter_idx=0))
#print(bluetooth.remove(address=ADDR_UE_BOOM, adapter_idx=0))