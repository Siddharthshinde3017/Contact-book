import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("600x300")

        self.contacts = []

        self.create_widgets()
        self.view_contacts()  # Display saved contacts initially

    def create_widgets(self):
        # Frame for search details (left side)
        self.frame_search = tk.Frame(self)
        self.frame_search.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_search_by = tk.Label(self.frame_search, text="Search By:")
        self.label_search_by.grid(row=0, column=0, sticky="e")
        self.search_options = ["All", "Phone Number", "Work", "Name", "Family", "Friends"]
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(self.search_options[0])
        self.dropdown_search_by = tk.OptionMenu(self.frame_search, self.selected_option, *self.search_options)
        self.dropdown_search_by.grid(row=0, column=1)

        self.label_search = tk.Label(self.frame_search, text="Search:")
        self.label_search.grid(row=1, column=0, sticky="e")
        self.entry_search = tk.Entry(self.frame_search)
        self.entry_search.grid(row=1, column=1)

        self.button_search = tk.Button(self.frame_search, text="Search", command=self.search_contact)
        self.button_search.grid(row=2, columnspan=2)

        self.listbox_search_results = tk.Listbox(self.frame_search)
        self.listbox_search_results.grid(row=3, columnspan=2, sticky="nsew")

        # Button for deleting contact
        self.button_delete = tk.Button(self.frame_search, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=4, columnspan=2)

        # Frame for add new contact (right side)
        self.frame_add = tk.Frame(self)
        self.frame_add.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_name = tk.Label(self.frame_add, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(self.frame_add)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(self.frame_add, text="Phone Number:")
        self.label_phone.grid(row=1, column=0, sticky="e")
        self.entry_phone = tk.Entry(self.frame_add)
        self.entry_phone.grid(row=1, column=1)

        self.label_email = tk.Label(self.frame_add, text="Email:")
        self.label_email.grid(row=2, column=0, sticky="e")
        self.entry_email = tk.Entry(self.frame_add)
        self.entry_email.grid(row=2, column=1)

        self.label_address = tk.Label(self.frame_add, text="Address:")
        self.label_address.grid(row=3, column=0, sticky="e")
        self.entry_address = tk.Entry(self.frame_add)
        self.entry_address.grid(row=3, column=1)

        self.button_add = tk.Button(self.frame_add, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, columnspan=2)

    def search_contact(self):
        self.listbox_search_results.delete(0, tk.END)
        search_option = self.selected_option.get()
        keyword = self.entry_search.get().lower()
        if search_option == "Name":
            found_contacts = [contact for contact in self.contacts if keyword in contact.name.lower()]
        elif search_option == "Phone Number":
            found_contacts = [contact for contact in self.contacts if keyword in contact.phone_number]
        else:
            found_contacts = []
        if found_contacts:
            for contact in found_contacts:
                self.listbox_search_results.insert(tk.END, f"{contact.name} - {contact.phone_number}")
        else:
            messagebox.showinfo("No Match", "No contacts found matching the search criteria.")

    def add_contact(self):

        name = self.entry_name.get()

        phone_number = self.entry_phone.get()

        email = self.entry_email.get()

        address = self.entry_address.get()

        new_contact = Contact(name, phone_number, email, address)

        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully.")

        self.view_contacts()  # Update displayed contacts

    def view_contacts(self):
        self.listbox_search_results.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox_search_results.insert(tk.END, f"{contact.name} - {contact.phone_number}")

    def delete_contact(self):
        selected_index = self.listbox_search_results.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.view_contacts()  # Update displayed contacts

    def validate_phone(self, value):
        if value.isdigit() and len(value) <= 10:
            return True
        else:
            return False

if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()
