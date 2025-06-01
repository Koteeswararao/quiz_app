import streamlit as st

# --- Quiz Questions ---
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Wordsworth", "William Shakespeare", "Leo Tolstoy", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Who is the girl friend of Bharath?",
        "options": ["Samantha", "Kajal", "Rashmika", "Mrunal"],
        "answer": "Samantha"
    }
]

# --- Page Config ---
st.set_page_config(page_title="🧠 Quiz Game", layout="centered")

st.title("🧠 Quiz Game")
st.subheader("Test your general knowledge!")

# --- State Management ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)
if "completed" not in st.session_state:
    st.session_state.completed = False

# --- Quiz Display ---
if not st.session_state.completed:
    q_index = st.session_state.q_index
    q = questions[q_index]

    st.write(f"**Question {q_index + 1}:** {q['question']}")
    selected = st.radio("Choose an option:", q["options"], index=q["options"].index(st.session_state.answers[q_index]) if st.session_state.answers[q_index] else 0, key=f"q_{q_index}")
    
    st.session_state.answers[q_index] = selected

    # Navigation Buttons
    col1, col2 = st.columns(2)
    with col1:
        if q_index < len(questions) - 1:
            if st.button("Next ➡️"):
                st.session_state.q_index += 1
        else:
            if st.button("✅ Submit"):
                st.session_state.score = sum(
                    1 for i, q in enumerate(questions) if st.session_state.answers[i] == q["answer"]
                )
                st.session_state.completed = True
    with col2:
        if q_index > 0:
            if st.button("⬅️ Back"):
                st.session_state.q_index -= 1

# --- Final Score Display ---
if st.session_state.completed:
    st.markdown("---")
    st.header("🏁 Quiz Completed!")
    st.success(f"Your Score: {st.session_state.score} / {len(questions)}")

    if st.button("🔁 Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.answers = [None] * len(questions)
        st.session_state.completed = False

