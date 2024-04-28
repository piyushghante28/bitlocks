import streamlit as st

def main():
    st.set_page_config(
    page_title="BitLocks",
    page_icon="❤️",
    layout="centered",
)

    st.title("🔥 Welcome to BitLocks! 🔥")
    logo_image = 'BitLocks_logo.jpg'  # Replace 'bitlocks_logo.png' with the actual file name of your logo
    st.image(logo_image, width=150)
    st.markdown("### Quick Links:")
    encrypt_button = '[🔒 Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)'
    decrypt_button = '[🔓 Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)'
    st.markdown(encrypt_button, unsafe_allow_html=True)
    st.markdown(decrypt_button, unsafe_allow_html=True)

    st.write("BitLocks simplifies data security by encrypting and storing sensitive files with ease. Our user-friendly interface empowers users of all levels of expertise to safeguard their data.")

    st.write("We leverage the InterPlanetary File System (IPFS) for secure storage, distributing files across a decentralized network to minimize the risk of breaches and ensure data integrity.")

    st.write("Our seamless integration with the Verbwire API for IPFS storage ensures smooth execution and reliable file storage without the hassle.")

    st.write("Secure personal documents, financial records, or confidential business files with confidence. BitLocks offers robust encryption and decentralized storage.")

    st.write("In summary, BitLocks simplifies encryption and storage while enhancing security through advanced techniques and decentralized storage.")

    

if __name__ == "__main__":
    main()
