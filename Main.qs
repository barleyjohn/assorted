operation Main() : Result {
    // Allocate a qubit.
    use q = Qubit();

    // Set the qubit into superposition of 0 and 1 using the Hadamard 
    H(q);

    // Measure the qubit and store the result.

    let result = M(q);

    // Reset qubit to the |0〉 state.
    Reset(q);

    // Return the result of the measurement.
    return result;
}