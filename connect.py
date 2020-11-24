from bluetool import Bluetooth

ADDR_UE_BOOM_2 = '88:C6:26:EE:BC:FE'
ADDR_UE_BOOM   = '88:C6:26:40:2C:2C'
ADDR_BLP9820   = '30:21:15:54:78:AA'
ADDR_LEWHX     = '38:18:4C:BD:27:14'

print("Adapters :")
bluetooth = Bluetooth(verbose=True)
 
#print("Connected devices :")
#[print(d) for d in bluetooth.get_connected_devices()]
#print()

#print("Removing all devices")
#print(bluetooth.remove
#print()

print("Scanning")
bluetooth.scan(timeout=10, adapter_idx=1)
print(bluetooth.get_available_devices())
print()

print("Connecting to UE BOOM")
#print(bluetooth.pair(address=ADDR_BLP9820, adapter_idx=1))
print(bluetooth.pair(address=ADDR_UE_BOOM, adapter_idx=0))
print(bluetooth.connect(address=ADDR_UE_BOOM, adapter_idx=0))
#print(bluetooth.connect(address=ADDR_BLP9820, adapter_idx=1))
print()

print("Connecting to LE_WHX")
print(bluetooth.pair(address=ADDR_LEWHX, adapter_idx=1))
print(bluetooth.connect(address=ADDR_LEWHX, adapter_idx=1))
#print(bluetooth.pair(address=ADDR_UE_BOOM_2, adapter_idx=0))
#print(bluetooth.connect(address=ADDR_UE_BOOM_2, adapter_idx=0))
