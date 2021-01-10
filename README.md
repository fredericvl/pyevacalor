**!!! WARNING: THIS MODULE IS NOT MAINTAINED ANYMORE !!!**

**GENERIC AGUA IOT MODULE WITH THE SAME FUNCTIONALITIES AVAILABLE OVER [HERE](https://github.com/fredericvl/py-agua-iot)**

# pyevacalor

pyevacalor provides controlling Eva Calor heating devices connected via the IOT Agua platform of Micronova.

**Warning: this module is not tested with multiple devices, there is no guarantee that it will work with your Eva Calor heating device.**

## Example usage

```
from pyevacalor import evacalor

# 1c3be3cd-360c-4c9f-af15-1f79e9ccbc2a = random UUID
# You can generate one here: https://www.uuidgenerator.net/version4
connection = evacalor("john.smith@gmail.com", "mysecretpassword", "1c3be3cd-360c-4c9f-af15-1f79e9ccbc2a")

# Print the current air temperature for each device
for device in connection.devices:
  print(device.name + ": " + str(device.air_temperature))
```

## Other examples

### Home Assistant

See [examples/home-assistant/README.md](examples/home-assistant/README.md)
