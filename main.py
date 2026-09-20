import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- MENU ----------------
menu = {
    "Coffee": 80,
    "Tea": 40,
    "Burger": 120,
    "Pizza": 180,
    "Sandwich": 90,
    "French Fries": 70,
    "Cold Drink": 50
}

# ---------------- BILL CALCULATION ----------------
def generate_bill():
    customer = customer_name.get()

    if customer == "":
        messagebox.showwarning("Warning", "Please enter customer name")
        return

    bill_text.delete("1.0", tk.END)

    subtotal = 0
    bill_no = datetime.now().strftime("%Y%m%d%H%M%S")

    bill_text.insert(tk.END, "        ☕ CAFE BILLING SYSTEM\n")
    bill_text.insert(tk.END, "====================================\n")
    bill_text.insert(tk.END, f"Bill No: {bill_no}\n")
    bill_text.insert(tk.END, f"Customer: {customer}\n")
    bill_text.insert(
        tk.END,
        f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
    )
    bill_text.insert(tk.END, "------------------------------------\n")
    bill_text.insert(tk.END, "Item\t\tQty\tAmount\n")
    bill_text.insert(tk.END, "------------------------------------\n")

    for item, price in menu.items():
        try:
            quantity = int(quantity_entries[item].get())
        except ValueError:
            quantity = 0

        if quantity > 0:
            amount = price * quantity
            subtotal += amount

            bill_text.insert(
                tk.END,
                f"{item}\t\t{quantity}\t₹{amount}\n"
            )

    gst = subtotal * 0.05
    total = subtotal + gst

    bill_text.insert(tk.END, "------------------------------------\n")
    bill_text.insert(tk.END, f"Subtotal:\t\t₹{subtotal:.2f}\n")
    bill_text.insert(tk.END, f"GST (5%):\t\t₹{gst:.2f}\n")
    bill_text.insert(tk.END, f"Grand Total:\t\t₹{total:.2f}\n")
    bill_text.insert(tk.END, "====================================\n")
    bill_text.insert(tk.END, "       Thank You! Visit Again ☕\n")


# ---------------- RESET ----------------
def reset():
    customer_name.delete(0, tk.END)

    for entry in quantity_entries.values():
        entry.delete(0, tk.END)
        entry.insert(0, "0")

    bill_text.delete("1.0", tk.END)


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Cafe Billing System")
root.geometry("850x600")

title = tk.Label(
    root,
    text="☕ CAFE BILLING SYSTEM",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)

# Customer information
customer_frame = tk.Frame(root)
customer_frame.pack(pady=5)

tk.Label(
    customer_frame,
    text="Customer Name:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=5)

customer_name = tk.Entry(
    customer_frame,
    width=25,
    font=("Arial", 12)
)
customer_name.grid(row=0, column=1, padx=5)

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

# Menu frame
menu_frame = tk.LabelFrame(
    main_frame,
    text="Menu",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=10
)
menu_frame.grid(row=0, column=0, padx=20)

quantity_entries = {}

row = 0

for item, price in menu.items():

    tk.Label(
        menu_frame,
        text=f"{item} - ₹{price}",
        font=("Arial", 12)
    ).grid(row=row, column=0, pady=5, sticky="w")

    entry = tk.Entry(
        menu_frame,
        width=8,
        font=("Arial", 12)
    )
    entry.insert(0, "0")
    entry.grid(row=row, column=1, padx=10)

    quantity_entries[item] = entry

    row += 1


# Bill frame
bill_frame = tk.LabelFrame(
    main_frame,
    text="Bill",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=10
)
bill_frame.grid(row=0, column=1, padx=20)

bill_text = tk.Text(
    bill_frame,
    width=45,
    height=20,
    font=("Courier New", 10)
)
bill_text.pack()


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Generate Bill",
    command=generate_bill,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Reset",
    command=reset,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    width=15,
    font=("Arial", 12, "bold")
).grid(row=0, column=2, padx=10)


root.mainloop()