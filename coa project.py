def cla_adder(A, B):
    # Initialize lists to store generate (Gi) and propagate (Pi) signals
    Gi = [0] * 4
    Pi = [0] * 4

    # Calculate the generate and propagate signals for each bit pair
    for i in range(4):
        Gi[i] = A[i] & B[i]
        Pi[i] = A[i] ^ B[i]

    # Calculate the carry bits for each stage
    C = [0] * 5  # Initialize the carry bits
    for i in range(4):
        C[i + 1] = Gi[i] | (Pi[i] & C[i])

    # Calculate the sum bits
    S = [0] * 4
    for i in range(4):
        S[i] = A[i] ^ B[i] ^ C[i]

    # The final carry-out is C4
    Cout = C[4]

    return S, Cout

# Example usage:
A = [1, 0, 1, 0]  # Binary representation of A (LSB to MSB)
B = [0, 1, 1, 1]  # Binary representation of B (LSB to MSB)

S, Cout = cla_adder(A, B)

print("Sum:", S)  # Output: Sum: [1, 1, 0, 0] (LSB to MSB)
print("Carry-Out:", Cout)  # Output: Carry-Out: 1