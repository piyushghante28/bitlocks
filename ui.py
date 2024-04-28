import streamlit as st

def main():
    st.title("Welcome to BitLocks")
    st.beta_set_page_config(page_title='your_title', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
    
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

    # st.markdown("### Quick Links:")
    # if st.button("Encrypt Files with BitLocks"):
    #     st.write("[Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)")
    # if st.button("Decrypt Files with BitLocks"):
    #     st.write("[Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)")

if __name__ == "__main__":
    main()
