
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


# manjevas-six502: MOS 6502 Emulator

MOS 6502 emulator and class to be used to tinker with 8-bit computers and build emulations of 8-bit systems. Emulator can be run cycle accurate, stepped through for debugging, or run at max speed. 

## Installation

You can install manjevas-six502 from [PyPi]():

```PowerShell
  pip install manjevas-six502
```
## Features

- Run mode toggle: `cycle_accurate`, `stepped`, `max_speed`
- Configure RAM
- Configure clock speed
- Official [MOS instruction set](https://www.masswerk.at/6502/6502_instruction_set.html)

## Roadmap

- Add `cycle_accurate` support

- Add un-official MOS 6502 instruction set

## How to Use

The emulator can be used standalone or as a module. 

### Standalone
In this mode, the package is run as a CLI application, with access to debug information along with the contents of the monitor being displayed on a 40x30 screen. 

### Module
The cpu emulator object can be setup in the source code as:

```python
import six502

cpu = six502(mode="cycle_accurate", ram_size=8, clock_speed=1000.0)
```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Feedback

If you have any feedback, please reach out to us at fake@fake.com

## 🚀 About Me
I'm a full stack developer...

## License

[Apache Version 2.0](http://www.apache.org/licenses/)

