import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mxm import MXM
from spotify import Spotify

sp = Spotify()
mxm = MXM()

def process_link():
    link = input_entry.get()
    isrc = sp.get_isrc(link)
    mxmLinks = mxm.Track_links(isrc)
    #id
    output_label1.config(text=f"id: {mxmLinks[0]}", font=("Courier", 8), cursor="hand2")
    output_label1.bind("<Button-1>", lambda e: click_link(mxmLinks[0]))

    #track link
    track= mxmLinks[1].split("?")[0]
    output_label2.config(text=f"Track link: {track}", font=("Courier", 8), cursor="hand2")
    output_label2.bind("<Button-1>", lambda e: click_link(track))

    #Album link
    output_label3.config(text=f"Album link: {mxmLinks[2]}", font=("Courier", 8), cursor="hand2")
    output_label3.bind("<Button-1>", lambda e: click_link(mxmLinks[2]))


def click_link(txt):
    output_text = txt
    root.clipboard_clear()
    root.clipboard_append(output_text)
    messagebox.showinfo("Copied", "Output has been copied to clipboard.")


def change_auth():
    client_id = client_id_entry.get()
    client_secret = client_secret_entry.get()
    sp.ChangeAuth(client_id,client_secret)


def change_api():
    apikey = apiKey_entry.get()
    mxm.changeKey(apikey)


root = tk.Tk()
root.geometry("900x200")
root.title("Spotify to Musixmatch Link")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Main")

input_label = ttk.Label(tab1, text="Spotify Track Link:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(tab1, width=80)
input_entry.grid(row=0, column=1, padx=5, pady=5)

process_button = ttk.Button(tab1, text="Get links", command=process_link)
process_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="ew")

# id
output_label1 = ttk.Label(tab1, text="")
output_label1.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
# track link
output_label2 = ttk.Label(tab1, text="", foreground="blue")
output_label2.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
# album link
output_label3 = ttk.Label(tab1, text="", foreground="blue")
output_label3.grid(row=4, column=0, padx=5, pady=5, columnspan=2)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Spotify")

client_id_label = ttk.Label(tab2, text="client_id:")
client_id_label.grid(row=0, column=0, padx=5, pady=5)

client_id_entry = ttk.Entry(tab2)
client_id_entry.grid(row=0, column=1, padx=5, pady=5)

client_secret_label = ttk.Label(tab2, text="client_secret:")
client_secret_label.grid(row=1, column=0, padx=5, pady=5)

client_secret_entry = ttk.Entry(tab2)
client_secret_entry.grid(row=1, column=1, padx=5, pady=5)

auth_button = ttk.Button(tab2, text="Change Spotify Auth", command=change_auth)
auth_button.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky="ew")



tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Musixmatch")

apiKey_label = ttk.Label(tab3, text="apiKey:")
apiKey_label.grid(row=0, column=0, padx=5, pady=5)

apiKey_entry = ttk.Entry(tab3)
apiKey_entry.grid(row=0, column=1, padx=5, pady=5)

apikey_button = ttk.Button(tab3, text="Change Musixmatch apikey", command=change_api)
apikey_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="ew")

root.mainloop()