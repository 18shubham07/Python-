import subprocess

def main():
    # Variables
    db_name = "example_database"
    db_user = "example_user"
    
    # Read MySQL password from user input securely
    db_password = get_password()

    # Install MySQL Server
    install_mysql()

    # Start MySQL Service
    start_mysql()

    # Secure MySQL Installation
    secure_mysql(db_password)

    # Create Database and User
    create_database_user(db_name, db_user, db_password)

    print(f"MySQL database '{db_name}' and user '{db_user}' have been created.")

def get_password():
    from getpass import getpass
    return getpass(prompt="Enter MySQL root password: ")

def install_mysql():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "mysql-server"])

def start_mysql():
    subprocess.run(["sudo", "systemctl", "start", "mysql"])
    subprocess.run(["sudo", "systemctl", "enable", "mysql"])

def secure_mysql(password):
    mysql_secure_script = f"y\n{password}\n{password}\ny\ny\ny\ny\n"
    subprocess.run(["sudo", "mysql_secure_installation"], input=mysql_secure_script.encode())

def create_database_user(db_name, db_user, db_password):
    subprocess.run(["sudo", "mysql", "-e", f"CREATE DATABASE {db_name};"])
    subprocess.run(["sudo", "mysql", "-e", f"CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_password}';"])
    subprocess.run(["sudo", "mysql", "-e", f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost';"])
    subprocess.run(["sudo", "mysql", "-e", "FLUSH PRIVILEGES;"])

if __name__ == "__main__":
    main()
