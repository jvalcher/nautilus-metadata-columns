
# Nautilus media metadata columns

This Python script uses the [nautilus-python](https://gitlab.gnome.org/GNOME/nautilus-python) extension and the [tinytag](https://github.com/tinytag/tinytag) audio metadata library to add media metadata columns to the Nautilus file manager.

<br>
<p align="center"><img margin-left="auto" src="./screenshot.png"></p>

## Added columns

- Artist
- Title
- Album
- Duration

## Usage

Install all requirements.
```bash
sudo apt install python3-nautilus
sudo pip install tinytag
```
<br>

Add the `media_columns.py` script to the `$XDG_DATA_HOME/nautilus-python/extensions` directory (i.e. `~/.local/share/…`) and then restart Nautilus.

If not working, you can check Nautilus' output by opening it inside a terminal session.
```bash
nautilus
```
<br>

