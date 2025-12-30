import bcrypt
import getpass

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def main():
    print("Password Hashing Utility for Supabase")
    print("=" * 40)
    
    passwords = {
        'hr.jpr@grew.one': 'Ankit@0708',
        'rakesh.s@grew.one': 'Rakesh@1234',
        'View@gmail.com': 'View@1234'
    }
    
    print("\nHashed Passwords (for SQL insertion):")
    print("-" * 40)
    
    for email, password in passwords.items():
        hashed = hash_password(password)
        print(f"Email: {email}")
        print(f"Original: {password}")
        print(f"Hashed: {hashed}")
        print()

if __name__ == "__main__":
    main()