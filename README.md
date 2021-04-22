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

If you get an `Import Error` while running the compiled exe try to use the following command:

```sh
pyinstaller --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" --onefile scroll-desktops.py
```

If you don't want to see a window when you open the exe add the following flags to the pyinstaller command:

```sh
--nowindowed --noconsole
```

## Create config

- Copy the `config.json` from `.` into `./dist`
- Set `printPosition` to `true`
- Every time you scroll your mouse position is printed. Use those values to determine your scroll area and put those coordinates into `config.json`
- Test if everything works
- Set `printPosition` to `false`

```

```
