import streamlit as st
import pandas as pd
from html import escape


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DFA Lab",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# THEME / CSS
# =========================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

    :root {
        --navy: #0f172a;
        --muted: #64748b;
        --indigo: #4f46e5;
        --line: #e2e8f0;
        --surface: #ffffff;
    }

    html, body, [class*="st-"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background: #f8fafc;
        color: var(--navy);
        color-scheme: light;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 1.25rem;
        padding-bottom: 2.25rem;
    }

    .hero {
        padding: clamp(24px, 3vw, 36px);
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 18px !important;
        margin: 0 0 26px;
        color: #fff;
        background: linear-gradient(112deg, #172554 0%, #312e81 100%);
        box-shadow: 0 8px 24px rgba(15,23,42,.10);
    }

    .hero-badge {
        color: #d8ddff;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.3px;
        margin-bottom: 15px;
    }

    .hero-title {
        font: 800 38px/1.12 'Manrope', sans-serif;
        margin: 0 0 8px;
    }

    .hero-subtitle {
        color: #dfe4ff;
        font-size: 16px;
        font-weight: 600;
        margin: 0 0 10px;
    }

    .hero-description {
        max-width: 660px;
        color: #c2cce0;
        font-size: 14px;
        line-height: 1.65;
        margin: 0;
    }

    .section-heading {
        margin: 30px 0 7px;
        color: var(--navy);
        font: 700 20px/1.45 'Manrope', sans-serif;
        overflow: visible;
    }

    .section-copy {
        margin: 0 0 16px;
        color: var(--muted);
        font-size: 13px;
        line-height: 1.5;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line) !important;
        border-radius: 14px !important;
        background: var(--surface);
        box-shadow: 0 3px 12px rgba(15,23,42,.035);
    }

    .metric-card {
        height: 100%;
        min-height: 94px;
        box-sizing: border-box;
        padding: 15px 16px;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: #fff;
    }

    .metric-label {
        color: var(--muted);
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .metric-value {
        color: var(--navy);
        font: 750 22px/1.2 'Manrope', sans-serif;
        overflow-wrap: anywhere;
    }

    .metric-value.compact { font-size: 16px; }

    .stButton > button {
        min-height: 42px;
        border-radius: 8px;
        font-weight: 650;
        transition: background-color .15s ease, border-color .15s ease;
    }

    .stButton > button:not([kind="primary"]) {
        color: #334155;
        background: #ffffff;
        border: 1px solid #cbd5e1;
        box-shadow: none;
    }

    .stButton > button:not([kind="primary"]):hover {
        color: #312e81;
        background: #eef2ff;
        border-color: #818cf8;
    }

    button[kind^="primary"] {
        border: 1px solid #4f46e5 !important;
        background: #4f46e5 !important;
        color: #ffffff !important;
        box-shadow: 0 3px 10px rgba(79,70,229,.16) !important;
    }

    button[kind^="primary"]:hover {
        border-color: #312e81 !important;
        background: #312e81 !important;
    }

    [data-testid="stTextInputRootElement"],
    .stSelectbox .react-aria-ComboBox > div {
        min-height: 44px;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        background: #ffffff !important;
        box-shadow: none !important;
        color: #0f172a !important;
    }

    [data-testid="stTextInputField"],
    .stSelectbox input {
        background: transparent !important;
        color: #0f172a !important;
        caret-color: #4f46e5;
    }

    [data-testid="stTextInputField"]::placeholder { color: #94a3b8 !important; }

    .stSelectbox label p,
    .stTextInput label p,
    [data-testid="stWidgetLabel"] p {
        color: #334155 !important;
        font-size: 13px !important;
        font-weight: 650 !important;
        line-height: 1.45 !important;
    }

    .stTextInput input,
    div[data-baseweb="select"] input { color: #0f172a !important; }

    .stForm { border: 0; }

    .transition-disclosure {
        margin: 26px 0 0;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: #fff;
        box-shadow: 0 3px 12px rgba(15,23,42,.035);
    }

    .transition-disclosure summary {
        padding: 14px 16px;
        color: #0f172a;
        cursor: pointer;
        font-size: 14px;
        font-weight: 650;
        line-height: 1.5;
    }

    .transition-content {
        padding: 0 16px 16px;
        overflow-x: auto;
    }

    .transition-content [data-testid="stMarkdownPre"],
    .transition-content p {
        white-space: pre-wrap;
    }

    .transition-content p {
        margin: 0 0 10px;
    }

    .transition-content p:last-child {
        margin-bottom: 0;
    }

    .transition-state-group {
        margin-bottom: 10px;
    }

    .transition-state-group:last-child {
        margin-bottom: 0;
    }

    .transition-line {
        color: #334155;
        font: 13px/1.65 'DM Sans', sans-serif;
    }

    .transition-content pre {
        margin: 0;
        color: #334155;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        font: 12px/1.65 'DM Sans', sans-serif;
        white-space: pre;
    }

    .legend-row {
        display: flex;
        flex-wrap: wrap;
        gap: 18px;
        padding: 10px 0 1px;
        color: #475569;
        font-size: 12px;
        line-height: 1.5;
    }

    .legend-mark { color: var(--indigo); font-weight: 800; margin-right: 5px; }

    .config-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 18px;
        padding: 18px 20px;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: #fff;
    }

    .config-label, .definition-label {
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .config-value {
        color: #0f172a;
        font-size: 15px;
        font-weight: 650;
        overflow-wrap: anywhere;
    }

    .definition-grid { margin-top: 10px; }
    .definition-row {
        display: grid;
        grid-template-columns: 42px 150px minmax(0, 1fr);
        align-items: baseline;
        gap: 10px 16px;
        padding: 11px 2px;
        border-bottom: 1px solid #edf0f5;
    }
    .definition-row:last-child { border-bottom: 0; }
    .definition-symbol { color: #312e81; font: 700 16px 'Manrope', sans-serif; }
    .definition-name { color: #334155; font-size: 13px; font-weight: 650; }
    .definition-value { color: #0f172a; font: 500 13px/1.5 'DM Sans', sans-serif; overflow-wrap: anywhere; }

    .result-card {
        padding: 18px 20px;
        border: 1px solid;
        border-radius: 10px;
        margin-top: 8px;
    }

    .result-card.accepted { color: #245c49; background: #f0f7f3; border-color: #c9dfd3; }
    .result-card.rejected { color: #8c3f42; background: #fbf2f1; border-color: #e8cfcd; }
    .result-title { font: 750 19px 'Manrope', sans-serif; margin-bottom: 5px; }
    .result-copy { font-size: 13px; line-height: 1.6; }

    .step-card {
        min-height: 116px;
        height: 100%;
        box-sizing: border-box;
        padding: 15px 14px;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: #fff;
    }

    .step-grid {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 12px;
    }

    .step-number { color: var(--indigo); font: 800 12px 'Manrope', sans-serif; margin-bottom: 8px; }
    .step-title { color: var(--navy); font-weight: 700; font-size: 14px; margin-bottom: 4px; }
    .step-copy { color: var(--muted); font-size: 12px; line-height: 1.5; }

    .footer {
        padding: 28px 0 8px;
        color: #8792a4;
        font-size: 12px;
        text-align: center;
    }

    @media (max-width: 640px) {
        .block-container { padding-top: 1rem; }
        .hero { margin-bottom: 20px; }
        .hero-title { font-size: 32px; }
        .section-heading { font-size: 19px; }
        .step-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .config-grid { grid-template-columns: 1fr; gap: 13px; }
        .definition-row { grid-template-columns: 36px minmax(100px, .8fr) minmax(0, 1.4fr); gap: 8px; }
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# STARTS WITH DFA
# =========================================================

def build_starts_with(pattern, alphabet):

    n = len(pattern)

    states = [f"q{i}" for i in range(n + 1)]
    trap = "q_trap"
    states.append(trap)

    start_state = "q0"
    final_states = {f"q{n}"}

    transition = {}

    for i in range(n):
        transition[f"q{i}"] = {}

        for symbol in alphabet:
            if symbol == pattern[i]:
                transition[f"q{i}"][symbol] = f"q{i+1}"
            else:
                transition[f"q{i}"][symbol] = trap

    # Final state
    transition[f"q{n}"] = {}

    for symbol in alphabet:
        transition[f"q{n}"][symbol] = f"q{n}"

    # Trap state
    transition[trap] = {}

    for symbol in alphabet:
        transition[trap][symbol] = trap

    return states, start_state, final_states, transition


# =========================================================
# ENDS WITH DFA
# =========================================================

def build_ends_with(pattern, alphabet):

    n = len(pattern)

    states = [f"q{i}" for i in range(n + 1)]
    start_state = "q0"
    final_states = {f"q{n}"}

    transition = {}

    for i in range(n + 1):

        transition[f"q{i}"] = {}

        for symbol in alphabet:

            current = pattern[:i] + symbol

            next_state = 0

            for k in range(min(n, len(current)), -1, -1):

                if current.endswith(pattern[:k]):
                    next_state = k
                    break

            transition[f"q{i}"][symbol] = f"q{next_state}"

    return states, start_state, final_states, transition


# =========================================================
# CONTAINS SUBSTRING DFA
# =========================================================

def build_contains_substring(pattern, alphabet):

    n = len(pattern)

    states = [f"q{i}" for i in range(n + 1)]
    start_state = "q0"
    final_states = {f"q{n}"}

    transition = {}

    for i in range(n + 1):

        transition[f"q{i}"] = {}

        for symbol in alphabet:

            # Once substring is found, remain accepted
            if i == n:
                transition[f"q{i}"][symbol] = f"q{n}"
                continue

            current = pattern[:i] + symbol

            next_state = 0

            for k in range(min(n, len(current)), -1, -1):

                if current.endswith(pattern[:k]):
                    next_state = k
                    break

            transition[f"q{i}"][symbol] = f"q{next_state}"

    return states, start_state, final_states, transition


# =========================================================
# TEST STRING
# =========================================================

def test_string(input_string, start_state, final_states, transition):

    current_state = start_state

    path = [current_state]

    for symbol in input_string:

        if symbol not in transition[current_state]:

            return False, path, f"Invalid symbol: {symbol}"

        current_state = transition[current_state][symbol]

        path.append(current_state)

    accepted = current_state in final_states

    return accepted, path, ""


# =========================================================
# GRAPHVIZ DIAGRAM
# =========================================================

def create_dfa_diagram(
    states,
    start_state,
    final_states,
    transition,
    alphabet
):

    dot = "digraph DFA {\n"

    dot += 'graph [rankdir=LR, nodesep=0.14, ranksep=0.38, margin=0.02, pad=0.06, size="9,3", ratio=compress, bgcolor="transparent"];\n'
    dot += 'node [shape=circle, fontname="Arial", fontsize=9, width=0.52, height=0.52, fixedsize=true, margin=0.02];\n'
    dot += 'edge [fontname="Arial", fontsize=8, arrowsize=0.6];\n'

    if "q_trap" in states:
        dot += 'q_trap [width=0.68, height=0.52, fontsize=8, color="#94a3b8", fontcolor="#64748b"];\n'
        if final_states:
            dot += "{ rank=same; " + states[-3] + "; q_trap; }\n"

    # Start arrow
    dot += 'start [shape=point, width=0.08, height=0.08, fixedsize=true];\n'
    dot += f'start -> {start_state};\n'

    # Final states
    for state in final_states:
        dot += f'{state} [shape=doublecircle];\n'

    # Transitions
    for state in states:

        for symbol in alphabet:

            next_state = transition[state][symbol]

            layout_hint = ", constraint=false" if next_state == "q_trap" else ""
            dot += f'{state} -> {next_state} [label="{symbol}"{layout_hint}];\n'

    dot += "}"

    return dot


# =========================================================
# UI COMPONENTS
# =========================================================

def set_example(example_type, example_pattern):
    st.session_state["builder_dfa_type"] = example_type
    st.session_state["builder_pattern"] = example_pattern


def display_state_name(state):
    return "D" if state == "q_trap" else state


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-badge">FORMAL LANGUAGES &amp; AUTOMATA</div>
    <div class="hero-title">DFA Lab</div>
    <div class="hero-subtitle">Build. Visualize. Simulate. Understand.</div>
    <p class="hero-description">
        Explore deterministic finite automata by defining a language,
        inspecting its state machine, and tracing strings through each transition.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# DFA BUILDER
# =========================================================

st.markdown('<div class="section-heading">Build your DFA</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">Choose a language, define its pattern, and set the input alphabet.</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    with st.form("dfa_builder"):
        input_col1, input_col2 = st.columns(2)
        with input_col1:
            dfa_type = st.selectbox(
                "DFA TYPE",
                ["Starts With", "Ends With", "Contains Substring"],
                key="builder_dfa_type"
            )
        with input_col2:
            pattern = st.text_input(
                "Pattern",
                placeholder="Example: 011",
                key="builder_pattern"
            )

        alphabet_input = st.text_input(
            "Alphabet",
            value="0,1",
            help="Enter symbols separated by commas. Example: 0,1",
            key="builder_alphabet"
        )
        alphabet = [x.strip() for x in alphabet_input.split(",") if x.strip()]
        action_left, action_center, action_right = st.columns([1, 1, 1])
        with action_center:
            generate_clicked = st.form_submit_button(
                "🚀 Generate DFA",
                type="primary",
                width="stretch"
            )

    st.caption("Try an example")
    example_col1, example_col2, example_col3 = st.columns(3)
    with example_col1:
        st.button(
            "Starts with · 011",
            on_click=set_example,
            args=("Starts With", "011"),
            key="example_starts_with",
            type="secondary",
            width="stretch"
        )
    with example_col2:
        st.button(
            "Ends with · 101",
            on_click=set_example,
            args=("Ends With", "101"),
            key="example_ends_with",
            type="secondary",
            width="stretch"
        )
    with example_col3:
        st.button(
            "Contains · 110",
            on_click=set_example,
            args=("Contains Substring", "110"),
            key="example_contains",
            type="secondary",
            width="stretch"
        )

if generate_clicked:
    if not pattern:
        st.error("Please enter a pattern.")
    elif not alphabet:
        st.error("Please enter an alphabet.")
    else:
        if dfa_type == "Starts With":
            states, start_state, final_states, transition = \
                build_starts_with(pattern, alphabet)
        elif dfa_type == "Ends With":
            states, start_state, final_states, transition = \
                build_ends_with(pattern, alphabet)
        else:
            states, start_state, final_states, transition = \
                build_contains_substring(pattern, alphabet)

        st.session_state["states"] = states
        st.session_state["start_state"] = start_state
        st.session_state["final_states"] = final_states
        st.session_state["transition"] = transition
        st.session_state["alphabet"] = alphabet
        st.session_state["pattern"] = pattern
        st.session_state["dfa_type"] = dfa_type
        st.session_state["test_done"] = False
        st.session_state.pop("simulation_result", None)


# =========================================================
# DISPLAY DFA
# =========================================================

if "states" in st.session_state:

    states = st.session_state["states"]
    start_state = st.session_state["start_state"]
    final_states = st.session_state["final_states"]
    transition = st.session_state["transition"]
    alphabet = st.session_state["alphabet"]

    st.markdown('<div class="section-heading">DFA overview</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">A compact summary of the generated machine.</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # METRIC CARDS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">DFA TYPE</div>
            <div class="metric-value compact">
                {st.session_state["dfa_type"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">STATES</div>
            <div class="metric-value">
                {len(states)}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">START STATE</div>
            <div class="metric-value">
                {start_state}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">ACCEPTING</div>
            <div class="metric-value compact">
                {", ".join(display_state_name(state) for state in final_states)}
            </div>
        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # STATE DIAGRAM
    # =====================================================

    st.markdown('<div class="section-heading">STATE DIAGRAM</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Follow each labeled transition to see how the automaton moves between states.</div>',
        unsafe_allow_html=True
    )
    dot = create_dfa_diagram(
        states,
        start_state,
        final_states,
        transition,
        alphabet
    )
    dot = dot.replace("q_trap", "D")
    with st.container(border=True):
        st.graphviz_chart(
            dot,
            width="stretch",
            height=380,
            alt="DFA state diagram with labeled transitions and accepting state"
        )
        legend_items = [
            '<span><span class="legend-mark">→</span>Start state</span>',
            '<span><span class="legend-mark">○</span>State</span>',
            '<span><span class="legend-mark">◎</span>Accepting state</span>',
        ]
        if "q_trap" in states:
            legend_items.append('<span><span class="legend-mark">⊗</span>Trap state</span>')
        st.markdown(
            '<div class="legend-row"><b>LEGEND</b>' + "".join(legend_items) + '</div>',
            unsafe_allow_html=True
        )


    # =====================================================
    # PATTERN + ALPHABET
    # =====================================================

    st.markdown('<div class="section-heading">Configuration</div>', unsafe_allow_html=True)
    configuration_items = [
        ("Pattern", escape(st.session_state["pattern"])),
        ("Alphabet", escape("{" + ", ".join(alphabet) + "}")),
        ("DFA Type", escape(st.session_state["dfa_type"])),
    ]
    configuration_html = '<div class="config-grid">' + "".join(
        f'<div><div class="config-label">{label}</div>'
        f'<div class="config-value">{value}</div></div>'
        for label, value in configuration_items
    ) + '</div>'
    st.markdown(configuration_html, unsafe_allow_html=True)


    # =====================================================
    # FORMAL DEFINITION
    # =====================================================

    st.markdown('<div class="section-heading">Formal DFA definition</div>', unsafe_allow_html=True)
    definition_items = [
        ("Q", "States", "{" + ", ".join(display_state_name(state) for state in states) + "}"),
        ("Σ", "Alphabet", "{" + ", ".join(alphabet) + "}"),
        ("q₀", "Start state", display_state_name(start_state)),
        ("F", "Accepting states", "{" + ", ".join(display_state_name(state) for state in final_states) + "}"),
        ("δ", "Transition function", "Defined by the transition table."),
    ]
    definition_html = '<div class="definition-grid">' + "".join(
        f'<div class="definition-row"><div class="definition-symbol">{escape(symbol)}</div>'
        f'<div class="definition-name">{escape(label)}</div>'
        f'<div class="definition-value">{escape(value)}</div></div>'
        for symbol, label, value in definition_items
    ) + '</div>'
    with st.container(border=True):
        st.latex(r"M = (Q, \Sigma, \delta, q_0, F)")
        st.markdown(definition_html, unsafe_allow_html=True)


    # =====================================================
    # TRANSITION TABLE
    # =====================================================

    st.markdown('<div class="section-heading">Transition table</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">State names and transition values are shown exactly as generated.</div>',
        unsafe_allow_html=True
    )

    table_data = []

    for state in states:

        row = {"State": state}

        for symbol in alphabet:

            row[symbol] = transition[state][symbol]

        table_data.append(row)

    df = pd.DataFrame(table_data)
    display_df = df.copy()
    for column in display_df.columns:
        display_df[column] = display_df[column].map(display_state_name)

    st.dataframe(
        display_df,
        width="stretch",
        hide_index=True
    )


    # =====================================================
    # TRANSITION FUNCTIONS
    # =====================================================

    transition_groups = []

    for state in states:
        state_transitions = []
        for symbol in alphabet:
            state_transitions.append(
                f"δ({display_state_name(state)}, {symbol}) → "
                f"{display_state_name(transition[state][symbol])}"
            )
        transition_groups.append("\n".join(state_transitions))

    transition_text = "\n\n".join(transition_groups)
    transition_html = "".join(
        '<div class="transition-state-group">'
        + "".join(
            f'<div class="transition-line">{escape(line)}</div>'
            for line in group.splitlines()
        )
        + '</div>'
        for group in transition_groups
    )

    st.markdown(
        '<details class="transition-disclosure">'
        '<summary>🔢 Transition Functions</summary>'
        f'<div class="transition-content">{transition_html}</div>'
        '</details>',
        unsafe_allow_html=True
    )


    # =====================================================
    # SIMULATION
    # =====================================================

    st.markdown('<div class="section-heading">TEST THE AUTOMATON</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Run an input string through the generated DFA and inspect every transition.</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        with st.form("simulation_form"):
            test_col1, test_col2 = st.columns([3, 1], vertical_alignment="bottom")
            with test_col1:
                test_input = st.text_input(
                    "Input String",
                    placeholder="Example: 01101",
                    key="simulation_input"
                )
            with test_col2:
                test_clicked = st.form_submit_button(
                    "▶ Run Simulation",
                    type="primary",
                    width="stretch"
                )

    if test_clicked:
        if test_input == "":
            st.session_state["test_done"] = False
            st.warning("Please enter a string.")
        else:
            accepted, path, error = test_string(
                test_input,
                start_state,
                final_states,
                transition
            )
            if error:
                st.session_state["test_done"] = False
                st.error(error)
            else:
                st.session_state["test_done"] = True
                st.session_state["simulation_result"] = {
                    "input": test_input,
                    "accepted": accepted,
                    "path": path
                }

    # =====================================================
    # RESULT
    # =====================================================

    if st.session_state.get("test_done") and "simulation_result" in st.session_state:
        result = st.session_state["simulation_result"]
        accepted = result["accepted"]
        path = result["path"]

        st.markdown('<div class="section-heading">SIMULATION TRACE</div>', unsafe_allow_html=True)
        result_col1, result_col2 = st.columns([1, 2])
        with result_col1:
            st.caption("INPUT")
            st.code(" ".join(result["input"]), language=None)
        with result_col2:
            st.caption("STATE TRAVERSAL")
            st.code(" → ".join(display_state_name(state) for state in path), language=None)

        if accepted:
            st.markdown(
                f'<div class="result-card accepted">'
                f'<div class="result-title">✓ ACCEPTED</div>'
                f'<div class="result-copy">The input string is accepted by the DFA.<br>'
                f'Final state: <b>{display_state_name(path[-1])}</b></div></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-card rejected">'
                f'<div class="result-title">✕ REJECTED</div>'
                f'<div class="result-copy">The input string is not accepted by the DFA.<br>'
                f'Final state: <b>{display_state_name(path[-1])}</b></div></div>',
                unsafe_allow_html=True
            )


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown('<div class="section-heading">How it works</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">From a language definition to a concrete acceptance decision.</div>',
    unsafe_allow_html=True
)

steps = [
    ("01", "Define", "Choose the DFA language type, pattern and alphabet."),
    ("02", "Generate", "The simulator constructs the DFA."),
    ("03", "Visualize", "Inspect its states and transitions."),
    ("04", "Simulate", "Enter an input string."),
    ("05", "Decide", "The DFA determines acceptance."),
]
step_cards = "".join(
    f'<div class="step-card"><div class="step-number">{step[0]}</div>'
    f'<div class="step-title">{step[1]}</div>'
    f'<div class="step-copy">{step[2]}</div></div>'
    for step in steps
)
st.markdown(f'<div class="step-grid">{step_cards}</div>', unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">DFA Lab · Formal Languages &amp; Automata</div>
""", unsafe_allow_html=True)