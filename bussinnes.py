import string
from pytube import YouTube
from hurry.filesize import size, alternative
from tkinter import ttk, filedialog, END

class youtube:
    @staticmethod
    def get_streams(url) -> dict:
        """
        send a youtube url
        """
        streams = YouTube(url).streams
        streams_dict = {}
        for stream in streams:
            if stream:
                streams_dict[youtube.pretty_stream(stream)] = stream
        return streams_dict

    @staticmethod
    def pretty_stream(stream):
        dict_stream = stream.__dict__
        if dict_stream['type'] == 'video':
            return f"type:{dict_stream['type']}, subtype{dict_stream['subtype']}, fps:{stream.fps}, {size(dict_stream['_filesize'], system=alternative)}"
        else:
            return f"type:{dict_stream['type']}, res:{dict_stream['resolution']}, subtype:{dict_stream['subtype']}, {size(dict_stream['_filesize'], system=alternative)}"

class gui_command:
    @staticmethod
    def check_button(url:string, combobox:ttk.Combobox):
        stream_dict = youtube.get_streams(url)
        combobox['values'] = list(stream_dict.keys())

    @staticmethod
    def locate_file(download_location_entry):
        file = filedialog.askdirectory()
        if file:
            print(file)
            download_location_entry['state'] = 'normal'
            download_location_entry.delete(0, END)
            download_location_entry.insert(0, file)
            download_location_entry['state'] = 'disabled'

    @staticmethod
    def download(youtube_url_entry, selectable_stream, download_location_entry):
        stream_dict = youtube.get_streams(youtube_url_entry.get())
        print(selectable_stream['values'][selectable_stream.current()])
        stream_dict[selectable_stream['values'][selectable_stream.current()]].download(output_path=download_location_entry.get())