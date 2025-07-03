import streamlit as st

st.set_page_config(page_title="Welcome to Forum Centre! 🗨️", layout="centered")

st.title("Welcome to Forum Centre! 🗨️")
st.write("Ask questions, give answers, and learn together!")

# Store forum posts
if "forum" not in st.session_state:
    st.session_state.forum = []

# 📝 Post a New Question
st.header("📝 Post a New Question")
with st.form("ask_form"):
    username = st.text_input("👤 Enter your name", key="q_user")
    question = st.text_area("❓ What's your question?", key="q_text")
    post = st.form_submit_button("✅ Post Question")
    if post and username and question:
        st.session_state.forum.append({
            "username": username,
            "question": question,
            "replies": []
        })
        st.success("✅ Question posted!")

# 📋 View Forum Threads
st.header("📋 Forum Threads")
if not st.session_state.forum:
    st.info("⚠️ No questions yet.")
else:
    for i, post in enumerate(st.session_state.forum):
        st.subheader(f"🔹 Q{i+1} by {post['username']} 🧑‍💻")
        st.write(f"❓ {post['question']}")
        with st.expander("💬 View & Add Replies"):
            if post["replies"]:
                for reply in post["replies"]:
                    st.write(f"↪️ **{reply['username']}** 🗣️: {reply['reply']}")
            else:
                st.write("🕐 No replies yet.")
            with st.form(f"reply_form_{i}"):
                reply_user = st.text_input("👤 Your name", key=f"r_user_{i}")
                reply_text = st.text_area("✍️ Your reply", key=f"r_text_{i}")
                reply_btn = st.form_submit_button("✅ Submit Reply")
                if reply_btn and reply_user and reply_text:
                    post["replies"].append({
                        "username": reply_user,
                        "reply": reply_text
                    })
                    st.success("✅ Reply posted!")
