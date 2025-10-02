def signup_user():
    """Continuously takes user email and stories it in a file until the user exits."""
    while True:
        email = input("Enter you email for signup (or type 'exit' to quit): ")
        if email.lower() == 'exit':
            print("Exiting signup process. Goodbye!")
            break
        
        with open("emails.txt", "a") as file:
            file.write(email + "\n")
            
        print(f"Email {email} stored successfully.")
        

if __name__ == "__main__":
    signup_user()
        
