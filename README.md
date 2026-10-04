# DFA Lab

An interactive web-based **Deterministic Finite Automata (DFA) Simulator** built with Python and Streamlit.

DFA Lab allows users to define a language pattern, automatically generate the corresponding DFA, visualize its states and transitions, and simulate input strings to determine whether they are accepted or rejected.

---

## ✨ Features

- Build deterministic finite automata interactively
- Supports multiple language patterns:
  - **Starts With**
  - **Ends With**
  - **Contains Substring**
- Define a custom input alphabet
- Automatically generate DFA states and transitions
- Visualize the generated DFA
- View the DFA overview
- View the formal DFA definition
- View the transition table
- View transition functions
- Identify the start state and accepting state(s)
- Represent the dead state as **D**
- Test input strings against the generated DFA
- Trace the transitions taken during simulation
- Display the final acceptance/rejection result
- Clean and interactive user interface

---

## 🧠 DFA Representation

A deterministic finite automaton is formally represented as:

\[
M = (Q, \Sigma, \delta, q_0, F)
\]

where:

- **Q** — Set of states
- **Σ** — Input alphabet
- **δ** — Transition function
- **q₀** — Start state
- **F** — Set of accepting/final states

The simulator visualizes these components and allows users to observe how an input string moves through the DFA.

---

## 🔄 How It Works

### 1. Define

Choose the type of DFA and provide the required pattern and alphabet.

### 2. Generate

The simulator automatically constructs the DFA based on the selected language definition.

### 3. Visualize

Inspect:

- DFA states
- Start state
- Accepting state(s)
- Dead state
- State transitions
- Transition table
- Formal DFA definition

### 4. Simulate

Enter an input string and run it through the generated DFA.

### 5. Decide

The simulator follows the transition function for every input symbol and determines whether the final state is accepting.

---

## 🖥️ Supported DFA Types

### Starts With

Generates a DFA that accepts strings beginning with the specified pattern.

Example:

```text
Pattern: 011
Alphabet: 0,1