import Microsoft.Quantum.Diagnostics.*;
import Microsoft.Quantum.Math.*;
import Microsoft.Quantum.Convert.*;
import Microsoft.Quantum.Arrays.*;

operation Main() : Int {
    use qubits = Qubit[3];
    ApplyToEach(H, qubits);
    Message("The qubit register in a uniform superposition: ");
    DumpMachine();
    let result = ForEach(M, qubits);
    Message("Measuring the qubits collapses the superposition to a basis state.");
    DumpMachine();
    ResetAll(qubits);
    return BoolArrayAsInt(ResultArrayAsBoolArray(result));
}