
# Nautilus media metadata columns

This Python script uses the [nautilus-python](https://gitlab.gnome.org/GNOME/nautilus-python) extension and the [Mutagen](https://github.com/quodlibet/mutagen) audio metadata library to add media metadata columns to the Nautilus file manager.
<br>

## Added columns

- Artist
- Title
- Album
- Duration
<br>

## Usage

Add the `media_columns.py` script to the `$XDG_DATA_HOME/nautilus-python/extensions` directory (i.e. `~/.local/share/…`).<br>
<br>

Restart Nautilus.
<br>
```bash
$ killall nautilus
```
<br>

