import qrcode
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.simpledialog import askstring

def get_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    data = askstring("Input", "Enter URL or text that you want in QR code:")
    root.destroy()
    return data

data = get_input()

# Generate QR code
img = qrcode.make(data)

# Display using matplotlib
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()