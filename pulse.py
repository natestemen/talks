import numpy as np

x = np.linspace(-1, 16, 200)


def execute(circuit, noise_level=0.001):
    noisy_circuit = circuit.with_noise(cirq.depolarize(p=noise_level))
    return (
        cirq.DensityMatrixSimulator()
        .simulate(noisy_circuit)
        .final_density_matrix[0, 0]
        .real
    )


circuit: cirq.Circuit = benchmarks.generate_rb_circuits(n_qubits=1, num_cliffords=50)[0]

true_value = execute(circuit, noise_level=0.0)  # Ideal quantum computer.
noisy_value = execute(circuit)  # Noisy quantum computer.
zne_value = zne.execute_with_zne(circuit, execute)  # Noisy quantum computer + Mitiq.

print(f"Error (w/o  Mitiq): %0.4f" % abs((true_value - noisy_value) / true_value))
print(f"Error (with Mitiq): %0.4f" % abs((true_value - zne_value) / true_value))

fx = (
    -(
        x**6
        - 46 * x**5
        + 811 * x**4
        - 6814 * x**3
        + 27160 * x**2
        - 40768 * x
        - 8000
    )
    / 4000
    + 2
)

combined = np.column_stack((x, fx))

np.savetxt("pulse.dat", combined)
