import customtkinter
import customtkinter as ctk

# root = tk.Tk()
root_ctk = ctk.CTk()
root_ctk.title("km - mile")
root_ctk.geometry("300x500")
root_ctk.iconbitmap("icon_km.ico")
root_ctk.config(pady=80)
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("coffee.json")

header = ctk.CTkLabel(root_ctk, text="Enter km", font=("Helvetica", 20))
header.pack()


def change_theme(event):
    print(event)
    if event.keysym == "Down":
        customtkinter.set_appearance_mode("dark")
    elif event.keysym == "Up":
        customtkinter.set_appearance_mode("light")


root_ctk.bind("<Up>",change_theme)
root_ctk.bind("<Down>",change_theme)

def find_mile(event):
    if event is None:
        print("btn clicked")
    elif event.keysym == "Delete":
        input_km.delete(0, ctk.END)
        return
    km = input_km.get()
    mile = 0.62 * float(km)
    result.configure(text=f"{km}km = {mile:.2f} mile")
    input_km.delete(0, ctk.END)


input_km = ctk.CTkEntry(root_ctk, justify="center", font=("Helvetica", 16))
input_km.pack(pady=20)

input_km.bind("<Return>", find_mile)
input_km.bind("<Delete>", find_mile)

btn = ctk.CTkButton(root_ctk, text="Change to Mile", font=("Helvetica", 20), width=200, height=35,
                    command=lambda:find_mile(None))
btn.pack()

result = ctk.CTkLabel(root_ctk, text="", font=("Helvetica", 18))
result.pack(pady=20)

root_ctk.mainloop()
