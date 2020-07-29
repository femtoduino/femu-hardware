# FTDI EEPROM

On macOs, you will need to unload the default ftdi drivers first:

(From https://pylibftdi.readthedocs.io/en/latest/troubleshooting.html)
```
sudo kextunload -bundle-id com.apple.driver.AppleUSBFTDI
sudo kextunload -bundle-id com.FTDI.driver.FTDIUSBSerialDriver

```

If you need to reload them:

```
sudo kextload -bundle-id com.apple.driver.AppleUSBFTDI
sudo kextload -bundle-id com.FTDI.driver.FTDIUSBSerialDriver

```

## Flash femu.conf to FTDI chip

```
ftdi_eeprom --device i:0x0403:0x6015 --flash-eeprom femu.conf
```