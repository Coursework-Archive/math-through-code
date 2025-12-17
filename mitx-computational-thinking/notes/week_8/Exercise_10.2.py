import matplotlib.pyplot as plt


distance = [0.0865, 0.1015, 0.1106, 0.1279, 0.1892, 0.2695, 0.2888, 0.2425,
            0.3465, 0.3225, 0.3764, 0.4263, 0.4562, 0.4502, 0.4499, 0.4534,
            0.4416, 0.4304, 0.437]

mass = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
        0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85,
        0.9, 0.95, 1.0]

plt.figure(figsize=(10, 6))   # optional, makes the graph larger

plt.scatter(mass, distance)
plt.xlabel("Mass (kg)")
plt.ylabel("Distance (m)")
plt.title("Distance vs Mass")

plt.show()
