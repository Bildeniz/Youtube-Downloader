import tkinter as tk
from tkinter import ttk
from bussinnes import youtube, gui_command

root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('400x400')
root.config(background='gray')

youtube_entrys_frame = tk.Frame(root, background='gray')
youtube_entrys_frame.grid(column=0, row=0)

youtube_url_entry = tk.Entry(youtube_entrys_frame, font=('Calibri', '16'))
youtube_url_entry.insert(0, 'Youtube URL')
youtube_url_entry.grid(column=0, row=0, padx=15, pady=12, sticky=tk.W)

youtube_url_check_button = tk.Button(youtube_entrys_frame, height=1, text='Check', font=('Calibri'), borderwidth=0, command= lambda: gui_command.check_button(youtube_url_entry.get(), selectable_stream))
youtube_url_check_button.grid(row=0, column=1)

selectable_stream = ttk.Combobox(root, font=('Calibri', '17'), width=23, state='readonly')
selectable_stream.grid(column=0, row=1, padx=(25,0), pady=0)

download_location_frame = tk.Frame(root, background='gray')
download_location_frame.grid(column=0, row=2)

download_location_entry = tk.Entry(download_location_frame, font=('Calibri', '16'), state='disabled')
download_location_entry.grid(column=0, row=0, padx=(25,15), pady=12)

download_location_button = tk.Button(download_location_frame, height=1, text='Browse', font=('Calibri'), borderwidth=0, command= lambda: gui_command.locate_file(download_location_entry))
download_location_button.grid(row=0, column=1)

download_button = tk.Button(root, height=1, width=30 ,text='DOWNLOAD', font=('Calibri'), borderwidth=0, command=lambda: gui_command.download(youtube_url_entry, selectable_stream, download_location_entry))
download_button.grid(row=3, column=0, sticky=tk.W, padx=27)

root.mainloop()