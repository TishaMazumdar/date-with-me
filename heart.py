import numpy as np
import matplotlib.pyplot as plt
import time

# Function to print ASCII Heart
def print_ascii_heart():
    heart = """
      *****     *****  
    **     ** **     **  
    **       *       **  
    **               **  
     **            **  
       **        **  
         **    **  
            **  
    """
    print(heart)

# Function to plot a mathematical heart
def plot_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'r', linewidth=3)
    plt.fill(x, y, 'red', alpha=0.6)
    plt.xlim(-20, 20)
    plt.ylim(-20, 15)
    plt.axis('on')
    plt.title("♥ Mathematical Heart ♥", fontsize=14, fontweight='bold', color='red')
    plt.show()

# Run ASCII Heart first, then plot the heart
print_ascii_heart()
time.sleep(2)  # Wait for 2 seconds before showing the heart plot
plot_heart()
