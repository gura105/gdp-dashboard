import streamlit_authenticator as stauth

password = "PasswordsAreHashedAndThereforeSafe"

hashed_password = stauth.Hasher([password]).generate()

print(hashed_password)

# ['$2b$12$7JTIe3YFtG6IebKUQ6wpbOX9r4IRE9JynqIDgy658LWm6x69ecHgm']
