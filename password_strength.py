import re
import random
import string
import streamlit as st

def check_common_password(password):
    common_passwords = ["password123", "123456", "qwerty", "password", "admin", "letmein"]
    if password.lower() in common_passwords:
        return False, "❌ This is a common password. Choose a more secure one."
    return True, ""

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 2
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score >= 6:
        return "✅ Strong Password!", feedback
    elif score >= 4:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔒 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    common_ok, common_msg = check_common_password(password)
    if not common_ok:
        st.error(common_msg)
    else:
        strength, feedback = check_password_strength(password)
        st.subheader(strength)
        for msg in feedback:
            st.warning(msg)

if st.button("Generate Strong Password"):
    st.success("Generated Password: " + generate_strong_password())
