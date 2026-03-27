import numpy as np

total_machines = 5
each_machine_sensor = 24
each_sensor_recording = 60

data = np.random.normal(50, 15, (total_machines, each_machine_sensor, each_sensor_recording))

print("\nInitial Data Shape:", data.shape)

data[np.random.rand(*data.shape) < 0.05] = -1
print("\nMissing values introduced (-1)")

data[data == -1] = np.nan

sensor_mean = np.nanmean(data, axis=2, keepdims=True)
data = np.where(np.isnan(data), sensor_mean, data)

print("\nMissing values replaced with sensor mean")

min_val = data.min(axis=2, keepdims=True)
max_val = data.max(axis=2, keepdims=True)

data = (data - min_val) / (max_val - min_val + 1e-8)

print("\nData normalized between 0 and 1")

mean = data.mean(axis=2, keepdims=True)
std = data.std(axis=2, keepdims=True)

avg = data.mean(axis=(1,2))
std_machine = data.std(axis=(1,2))

print("\n--- Machine Statistics ---")
for i in range(total_machines):
    print(f"Machine {i} -> Avg: {avg[i]:.4f}, Std: {std_machine[i]:.4f}")

sensor_max = data.max(axis=2)

max_value = sensor_max.max()
pos = np.where(sensor_max == max_value)

print("\nHighest Activity:")
print(f"Machine {pos[0][0]}, Sensor {pos[1][0]}, Value {max_value:.4f}")

anomaly = data > (mean + 3 * std)

count = anomaly.sum(axis=(1, 2))

print("\n--- Anomalies per Machine ---")
for i in range(total_machines):
    print(f"Machine {i}: {count[i]} anomalies")

sensor_count = anomaly.sum(axis=2)

flat = sensor_count.flatten()
top3 = np.sort(flat)[-3:]

print("\nTop 3 anomaly counts:", top3)

