# Bioinformatics-4-k-Universal-Circular-String-Problem

# README: k-Universal Circular String Generator

---

### Problem Overview

The **k-Universal Circular String Problem** asks us to construct a circular binary string of length $2^k$ in which every possible binary substring of length $k$ appears **exactly once**.

This kind of string is called a **de Bruijn sequence** of order $k$ over the binary alphabet $\{0, 1\}$.

---

### Why Is This Problem Important?

* **Bioinformatics:** Helps design DNA primers and sequencing coverage strategies.
* **Networking:** Used in protocol testing and distributed computing.
* **Graph Theory:** Foundation for understanding **de Bruijn graphs**, which are key in genome assembly.
* **Theoretical Computer Science:** Explores cycle covering and information representation.

---

### Problem Statement

Given:

* An integer $k$

Return:

* A **circular binary string** of length $2^k$ where each substring of length $k$ appears once.

---

### Input Format

A text file (`input.txt`) containing a single integer:

```
3
```

---

### Output Format

A text file (`output.txt`) containing the k-universal circular string:

```
00111010
```

(Note: Other correct answers are possible — multiple valid de Bruijn sequences exist.)

---

### How to Use

#### 🛠️ Requirements

* Python 3.x

#### Steps

1. Save the integer input in `input.txt`:

   ```
   ```

3

````
2. Run the script:
   ```bash
   python k_universal_string.py
````

3. Check `output.txt` for the circular string.

---

### How It Works

The algorithm:

1. Generates the **de Bruijn graph** of all $k-1$-mers.
2. Builds edges from each $k-1$-mer to another by appending 0 or 1.
3. Finds an **Eulerian cycle** through the graph.
4. Reconstructs the circular string from the cycle.

The result contains all possible binary k-mers **once** as substrings.

---

### Project Structure

```
k_universal_circular_string_pronlem.py   # Python script
dataset.txt               # Contains the value of k
output.txt              # Resulting k-universal circular string
README.md               # This file
```

---

### Sample Run

**Input:**

```
3
```

**Output:**

```
00111010
```

This string contains all 8 ($2^3$) possible 3-bit binary substrings: 000, 001, 011, 111, 110, 101, 010, and 100.

---

### Notes

* The output is circular — it wraps around, so the end connects to the beginning.
* Any correct de Bruijn sequence is acceptable as output.

---

Next up: **String Reconstruction from Read-Pairs** →
