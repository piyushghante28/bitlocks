import streamlit as st

def main():
    st.title("Welcome to BitLocks")
    logo_image = 'BitLocks_logo.png'  # Replace 'bitlocks_logo.png' with the actual file name of your logo
    st.image(logo_image, use_column_width=True)
    st.markdown("### Quick Links:")
    encrypt_button = '[Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)'
    decrypt_button = '[Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)'
    st.markdown(encrypt_button, unsafe_allow_html=True)
    st.markdown(decrypt_button, unsafe_allow_html=True)

    st.write("BitLocks revolutionizes data security by simplifying the process of encrypting and storing sensitive files, making it easier and safer for individuals and businesses to protect their valuable information.")
    st.write("Traditionally, encrypting files and securely storing them involves complex procedures and specialized knowledge. BitLocks streamlines this process with its user-friendly interface, allowing users to encrypt their files with advanced AES encryption effortlessly. By abstracting the complexities of encryption, BitLocks empowers users of all levels of technical expertise to safeguard their data without hassle.")

    st.write("Moreover, BitLocks enhances data security by leveraging the InterPlanetary File System (IPFS) for storage. By distributing encrypted files across a decentralized network, BitLocks reduces reliance on centralized storage solutions, minimizing the risk of data breaches and ensuring data integrity. This decentralized approach not only makes data storage more secure but also increases resilience against censorship and tampering.")

    st.write("What sets BitLocks apart is its seamless integration with the Verbwire API for IPFS storage. While implementing IPFS storage can be complex, BitLocks simplifies the process by seamlessly leveraging the power of the Verbwire API. This integration ensures smooth execution and reliable storage of encrypted files on IPFS, without requiring users to navigate the intricacies of IPFS implementation.")

    st.write("Whether it's securing personal documents, financial records, or confidential business files, BitLocks provides peace of mind by offering robust encryption and decentralized storage. Users can trust BitLocks to protect their sensitive information from unauthorized access and data breaches, thereby simplifying data security tasks and making them more effective.")

    st.write("In summary, BitLocks simplifies the process of encrypting and storing files while enhancing data security through advanced encryption and decentralized storage on IPFS by using Verbwire API.")

    
if __name__ == "__main__":
    main()
