import matplotlib.pyplot as plt
import datetime
# Sample data: last 7 days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sleep_hours = [7, 6.5, 8, 7.5, 6, 9, 8.5]
study_hours = [3, 4, 2, 5, 1.5, 0, 2]
def plot_life_data():
    x = range(len(days))
    plt.figure(figsize=(10, 5))
    plt.plot(x, sleep_hours, label="Sleep Hours", marker='o', color='purple')
    plt.plot(x, study_hours, label="Study Hours", marker='s', color='green')
    plt.title("📊 My Life Tracker: Sleep & Study")
    plt.xticks(x, days)
    plt.ylabel("Hours")
    plt.xlabel("Day")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("life_tracker_graph.png")
    plt.show()

if __name__ == "__main__":
    plot_life_data()
