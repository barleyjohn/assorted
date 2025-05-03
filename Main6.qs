import Microsoft.Quantum.Diagnostics.*; // Aka Std.Diagnostics.*;

operation Main() : (Result, Result) {
    use (q1, q2) = (Qubit(), Qubit());

    H(q1);
    Z(q1); // Apply the Pauli Z operation to the control qubit
    CNOT(q1, q2);

    DumpMachine();

    let (m1, m2) = (M(q1), M(q2));
    Reset(q1);
    Reset(q2);

    return (m1, m2);
}