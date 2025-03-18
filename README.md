# ATM System

## Overview
This is a simple ATM (Automated Teller Machine) simulation program written in Python. The program allows users to perform basic banking operations such as withdrawing money, depositing money, generating or resetting a PIN, and viewing a mini statement.

## Features
- **Withdrawal:** Users can withdraw money from their account after entering the correct PIN.
- **Deposit:** Users can deposit money into their account.
- **Pin Generation/Reset:** Users can generate a new PIN if they don’t have one or reset an existing PIN.
- **Mini Statement:** Users can view their account details, including balance and personal information.

## How It Works
1. The program starts by displaying a welcome message and the available options.
2. Users can choose an option by entering the corresponding number.
3. Based on the selected option, users will be prompted to enter their account details.
4. For transactions requiring authentication, users must enter their PIN.
5. The program ensures security by validating account numbers and PINs before proceeding with any transactions.
6. The user can exit the program by selecting option 5.

## Usage
1. Run the program in a Python environment.
2. Choose an option from the menu:
   - Enter `1` for Withdrawal
   - Enter `2` for Deposit
   - Enter `3` for PIN Generation/Reset
   - Enter `4` for Mini Statement
   - Enter `5` to Exit
3. Follow the prompts to complete the desired transaction.

## Account Information Format
The accounts are stored in a dictionary with the following format:
```python
accounts = {
    1001 : ["Hemanthsai","17-11-2000",10000,7777],
    1002 : ["Yaswanth","21-04-2003",20000,9999],
    1003 : ["Chintu","11-11-2011",50000,None]    
}
```
- **Key:** Account Number
- **Values:** List containing
  - Account Holder Name
  - Date of Birth (DD-MM-YYYY)
  - Account Balance
  - PIN (or `None` if not set)

## Security Considerations
- The PIN must be entered correctly for withdrawal and mini statement operations.
- Users can reset their PIN if they remember their old one.
- A new PIN can be generated if the account does not already have one.

## Future Improvements
- Implement database integration for better data management.
- Add transaction history.
- Implement a graphical user interface (GUI) for better user experience.
- Introduce additional security features like OTP verification.

## Requirements
- Python 3.x

## Running the Program
Simply execute the script in a Python environment:
```sh
python atm.py
```

## Author
- Developed by [DURGAPU HEMANTHSAI]

# CONSOLED-BASED-ATM
