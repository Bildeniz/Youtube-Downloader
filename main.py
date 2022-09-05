import tkinter as tk
from bussinnes import youtube

root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('400x400')
root.config(background='gray')

youtube_entrys_frame = tk.Frame(root, background='gray')
youtube_entrys_frame.grid(column=0, row=0)

youtube_url_entry = tk.Entry(youtube_entrys_frame, font=('Calibri', '15'))
youtube_url_entry.grid(column=0, row=0, padx=15, pady=12, sticky=tk.W)

youtube_url_check_button = tk.Button(youtube_entrys_frame, text='Check', font=('Calibri', '12'), borderwidth=0, command= lambda: youtube.get_streams('https://www.youtube.com/watch?v=rFUXfIO_bNk'))
youtube_url_check_button.grid(row=0, column=1)

root.mainloop()