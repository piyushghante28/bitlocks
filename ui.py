import streamlit as st

def main():
    st.title("Welcome to BitLocks")

    st.markdown("### Quick Links:")
    if st.button("Encrypt Files with BitLocks"):
        st.write("[Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)")
    if st.button("Decrypt Files with BitLocks"):
        st.write("[Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)")

if __name__ == "__main__":
    main()
