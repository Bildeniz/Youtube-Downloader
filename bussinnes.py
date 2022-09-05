import string
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pytube.cli import on_progress
from hurry.filesize import size, alternative
from tkinter import ttk, filedialog, END, messagebox, Tk

class youtube:
    @staticmethod
    def get_streams(url, pb) -> dict:
        """
        send a youtube url
        """
        streams = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining,: youtube.pb_func(stream, chunk, bytes_remaining, pb)).streams
        streams_dict = {}
        for stream in streams:
            if stream:
                streams_dict[youtube.pretty_stream(stream)] = stream
        return streams_dict

    @staticmethod
    def pretty_stream(stream):
        dict_stream = stream.__dict__
        if dict_stream['type'] == 'video':
            return f"type:{dict_stream['type']}, subtype:{dict_stream['subtype']}, res:{dict_stream['resolution']}, fps:{stream.fps}, {size(dict_stream['_filesize'], system=alternative)}"
        else:
            return f"type:{dict_stream['type']}, subtype:{dict_stream['subtype']}, {size(dict_stream['_filesize'], system=alternative)}"

    @staticmethod
    def pb_func(stream, chunk, bytes_remaining, pb):
        pb['value'] = youtube.percent(bytes_remaining, stream.filesize)

    @staticmethod
    def percent(tem, total):
        try:
            return str(100 - ((float(tem) / float(total)) * float(100)))[:5]
        except ZeroDivisionError:
            return 100

class gui_command:
    @staticmethod
    def check_button(stream_dict, combobox:ttk.Combobox, root:Tk):
        combobox['values'] = list(stream_dict.keys())
        root.config(cursor='')
        root.grab_release()

    @staticmethod
    def locate_file(download_location_entry):
        file = filedialog.askdirectory()
        if file:
            download_location_entry['state'] = 'normal'
            download_location_entry.delete(0, END)
            download_location_entry.insert(0, file)
            download_location_entry['state'] = 'disabled'

    @staticmethod
    def download(stream_dict, selectable_stream, download_location_entry, root):
        root.config(cursor='wait')
        stream_dict[selectable_stream['values'][selectable_stream.current()]].download(output_path=download_location_entry.get())
        messagebox.showinfo('Youtube Downloader', 'Download is successfuly')
        root.config(cursor='')
