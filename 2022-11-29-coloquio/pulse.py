import numpy as np

x = np.linspace(-1, 16, 200)

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
