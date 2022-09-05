from pytube import YouTube
from hurry.filesize import size, alternative
import math

class youtube:
    @staticmethod
    def get_streams(url):
        streams = YouTube(url).streams
        streams_dict = {}
        print(streams)
        for stream in streams:
            if stream:
                # print(stream.__dict__)
                streams_dict[stream] = youtube.pretty_stream(stream)
                print(streams_dict)

    @staticmethod
    def pretty_stream(stream):
        dict_stream = stream.__dict__
        return f"type:{dict_stream['type']}, res:{dict_stream['resolution']}, {size(dict_stream['_filesize'], system=alternative)}"

youtube.get_streams('https://www.youtube.com/watch?v=rFUXfIO_bNk')