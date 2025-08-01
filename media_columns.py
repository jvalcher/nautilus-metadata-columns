from urllib.parse import unquote
from typing import List
from gi.repository import GObject, Nautilus
from tinytag import TinyTag

class DurationColumnExtension(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):

    def get_columns(self) -> List[Nautilus.Column]:
        artist_column = Nautilus.Column(
            name="NautilusPython::artist_column",
            attribute="artist",
            label="Artist",
            description="Media artist"
        )
        title_column = Nautilus.Column(
            name="NautilusPython::title_column",
            attribute="title",
            label="Title",
            description="Media title"
        )
        album_column = Nautilus.Column(
            name="NautilusPython::album_column",
            attribute="album",
            label="Album",
            description="Media album"
        )
        duration_column = Nautilus.Column(
            name="NautilusPython::duration_column",
            attribute="duration",
            label="Duration",
            description="Media duration in mm:ss format"
        )
        return [artist_column, title_column, album_column, duration_column]

    def update_file_info(self, file: Nautilus.FileInfo) -> None:

        if file.get_uri_scheme() != "file":
            return

        try:

            filepath = unquote(file.get_uri()[7:])
            tag: TinyTag = TinyTag.get(filepath)

            artist = tag.artist or ""
            title = tag.title or ""
            album = tag.album or ""
            if tag.duration and tag.duration > 0:
                minutes = int(tag.duration) // 60
                seconds = int(tag.duration) % 60
                duration = f"{minutes}:{seconds:02}"
            else:
                duration = ""

            file.add_string_attribute("artist", artist)
            file.add_string_attribute("title", title)
            file.add_string_attribute("album", album)
            file.add_string_attribute("duration", duration)

        except Exception:
            file.add_string_attribute("artist", "")
            file.add_string_attribute("title", "")
            file.add_string_attribute("album", "")
            file.add_string_attribute("duration", "")


