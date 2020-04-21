# Scroll Windows Virtual Desktops

This tool scrolls through your virtual desktops.


## Install requirements

```sh
pip install -r requirements.txt
```


## Build

```sh
pyinstaller --onefile scroll-desktops.py
```

Builded file is in `./dist`


## Create config

- Copy the `config.json` from `.` into `./dist`
- Set `printPosition` to `true`
- Every time you scroll your mouse position is printed. Use those values to determine your scroll area and put those coordinates into `config.json`
- Test if everything works
- Set `printPosition` to `false`