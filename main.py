from Classes import Order
import tkinter as tk
import threading
import time

# Global variables
coffee_menu = {
    "Espresso": 3.50,
    "Latte": 4.00,
    "Cappuccino": 4.25,
    "Black": 2.75,
}

queue = []
orders = []
lock = threading.Lock()
order_number = 1


# Function to add an order to the queue
def place_order():
    global order_number
    coffee_choice = coffee_var.get()
    hot_or_iced = hot_or_iced_var.get()
    special_request = special_request_entry.get()
    order_index = order_number - 1

    if coffee_choice:
        with lock:
            orders.append(
                Order(order_number, coffee_choice, hot_or_iced, special_request, coffee_menu.get(coffee_choice)))
            queue.append(
                f"Order #{order_number}:{orders[order_index].coffee_name} ({orders[order_index].coffee_temp}), Special Request: {orders[order_index].special_requests}")
            order_number += 1
            update_queue()

        # Clear the input fields
        coffee_var.set("")
        hot_or_iced_var.set("Hot")
        special_request_entry.delete(0, tk.END)


# Function to update the queue display
def update_queue():
    queue_text.config(state=tk.NORMAL)
    queue_text.delete(1.0, tk.END)
    for order in queue:
        queue_text.insert(tk.END, order + "\n")
    queue_text.config(state=tk.DISABLED)


# Function to process orders from the queue every 10 seconds
def process_orders():
    while True:
        time.sleep(10)
        with lock:
            if queue:
                queue.pop(0)  # Remove the first order in the queue
                update_queue()


# Create the main application window
root = tk.Tk()
root.title("Coffee Order Queue")

# Coffee options
coffee_label = tk.Label(root, text="Choose Coffee:")
coffee_label.pack()
coffee_var = tk.StringVar(root)
coffee_var.set(list(coffee_menu.keys())[0])
coffee_option = tk.OptionMenu(root, coffee_var, *coffee_menu.keys())
coffee_option.pack()

# Hot or Iced
hot_or_iced_label = tk.Label(root, text="Hot or Iced:")
hot_or_iced_label.pack()
hot_or_iced_var = tk.StringVar(root)
hot_or_iced_var.set("Hot")
hot_or_iced_option = tk.OptionMenu(root, hot_or_iced_var, "Hot", "Iced")
hot_or_iced_option.pack()

# Special Request
special_request_label = tk.Label(root, text="Special Request:")
special_request_label.pack()
special_request_entry = tk.Entry(root)
special_request_entry.pack()

# Place Order Button
place_order_button = tk.Button(root, text="Place Order", command=place_order)
place_order_button.pack()

# Queue Display
queue_label = tk.Label(root, text="Current Queue:")
queue_label.pack()
queue_text = tk.Text(root, height=10, width=80, state=tk.DISABLED)
queue_text.pack()


# Start a separate thread to update the queue
def queue_updater():
    while True:
        time.sleep(5)
        update_queue()


queue_thread = threading.Thread(target=queue_updater)
queue_thread.daemon = True
queue_thread.start()

# Start a separate thread to process orders from the queue
process_thread = threading.Thread(target=process_orders)
process_thread.daemon = True
process_thread.start()

root.mainloop()
