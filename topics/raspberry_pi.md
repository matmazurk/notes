# Raspberry Pi

![pins](https://pi4j.com/1.4/images/pi4j-rpi-4b-pinout-small.png)

## [Raspberry Pi input and output pin voltage and current capability](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/gpio-pin-electrical-specifications)

## Rust problems on RPI
### Problem
```bash
    $ cargo clean
```
results in:
```
error: command failed: 'cargo': No such file or directory (os error 2)
```

### Solution:
    When asked for installation options select 2) for Custom Installation and then for "Default host triple?" enter "arm-unknown-linux-gnueabihf".