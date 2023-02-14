import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from bussinnes import youtube, gui_command
from pytube.exceptions import RegexMatchError
import threading

ctk.set_appearance_mode('dark')

stream_dict = {}

def check_button(combobox:ttk.Combobox, root:tk.Tk, pb):
    global stream_dict
    try:
        root.config(cursor='wait')
        stream_dict = youtube.get_streams(youtube_url_entry.get(), pb)
        gui_command.check_button(stream_dict, combobox, root)
    except RegexMatchError:
        messagebox.showerror('Youtube Downloader', 'Please enter a Youtube URL')
        root.config(cursor='')
        exit()


root = ctk.CTk()
root.title('Youtube Downloader')
root.geometry('400x400')

youtube_entrys_frame = ctk.CTkFrame(root)
youtube_entrys_frame.grid(column=0, row=0)

youtube_url_entry = ctk.CTkEntry(youtube_entrys_frame)
youtube_url_entry.insert(0, 'Youtube URL')
youtube_url_entry.grid(column=0, row=0, padx=15, pady=12, sticky=tk.W)

youtube_url_check_button = ctk.CTkButton(youtube_entrys_frame, height=1, text='Check', command=lambda: threading.Thread(
    target=check_button, args=(selectable_stream, root, pb)).start())
youtube_url_check_button.grid(row=0, column=1)

selectable_stream = ctk.CTkComboBox(root, state='readonly', values=['Video downloading option'])
selectable_stream.set('Video downloading option')
selectable_stream.grid(column=0, row=1, padx=(25, 0), pady=0)

download_location_frame = ctk.CTkFrame(root)
download_location_frame.grid(column=0, row=2)

download_location_entry = ctk.CTkEntry(
    download_location_frame, state='disabled')
download_location_entry.grid(column=0, row=0, padx=(25, 15), pady=12)

download_location_button = ctk.CTkButton(download_location_frame, height=1, text='Browse', command=lambda: gui_command.locate_file(download_location_entry))
download_location_button.grid(row=0, column=1)

pb = ctk.CTkProgressBar(root, mode='determinate')
pb.set(0)
pb.grid(row=3, column=0, sticky=tk.W, padx=27, pady=(0, 20))

download_button = ctk.CTkButton(root, height=1, width=30, text='DOWNLOAD',
                            command=lambda: threading.Thread(target=gui_command.download, args=(stream_dict, selectable_stream, download_location_entry, root)).start())
download_button.grid(row=4, column=0, sticky=tk.W, padx=27)

root.mainloop()
