from urllib.parse import unquote
from typing import List
from gi.repository import GObject, Nautilus
from mutagen import File as MutagenFile

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

    def get_media_tags(self, filepath):

        artist = ""
        title = ""
        album = ""
        min_secs = ""

        media = MutagenFile(filepath)
        if not media or not hasattr(media, "tags") or media.tags is None:
            return artist, title, album, min_secs

        seconds = int(media.info.length)
        min_secs = f"{seconds // 60}:{seconds % 60:02}"

        tags = media.tags

        # MP3, ID3
        if "TPE1" in tags:  # Artist
            artist = tags["TPE1"].text[0]
        if "TIT2" in tags:  # Title
            title = tags["TIT2"].text[0]
        if "TALB" in tags:  # Album
            album = tags["TALB"].text[0]

        # MP4, M4A
        if "\xa9ART" in tags:  # Artist
            artist = tags["\xa9ART"][0]
        if "\xa9nam" in tags:  # Title
            title = tags["\xa9nam"][0]
        if "\xa9alb" in tags:  # Album
            album = tags["\xa9alb"][0]

        # FLAC, OGG, other Vorbis comment formats
        if "artist" in tags:
            artist = tags["artist"][0]
        if "title" in tags:
            title = tags["title"][0]
        if "album" in tags:
            album = tags["album"][0]

        # WAV
        if "IART" in tags:
            artist = tags["IART"]
        if "INAM" in tags:
            title = tags["INAM"]
        if "IPRD" in tags:
            album = tags["IPRD"]

        return artist, title, album, min_secs

    def update_file_info(self, file: Nautilus.FileInfo) -> None:

        if file.get_uri_scheme() != "file":
            return

        try:
            filepath = unquote(file.get_uri()[7:])
            artist, title, album, min_secs = self.get_media_tags(filepath)

            file.add_string_attribute("artist", artist)
            file.add_string_attribute("title", title)
            file.add_string_attribute("album", album)
            file.add_string_attribute("duration", min_secs)

        except Exception:
            file.add_string_attribute("artist", "")
            file.add_string_attribute("title", "")
            file.add_string_attribute("album", "")
            file.add_string_attribute("duration", "")

