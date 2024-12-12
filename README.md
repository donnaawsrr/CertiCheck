# CertiCheck - EXE Signature Verifier

CertiCheck is a lightweight Windows tool designed to verify the digital signature of executable files (.exe). It uses Microsoft's `signtool` to validate the authenticity of files, ensuring they are properly signed and secure.

## Features

- Simple and intuitive graphical user interface (GUI).
- Quickly verify the digital signature of any executable file.
- Displays clear results, including errors or issues found.
- Portable and easy to use, requiring minimal setup.

## How It Works

1. Browse and select an executable file.
2. Click "Verify Signature" to check the file's digital signature.
3. View the result in the application, including details about validity or errors.

## Requirements

- Windows Operating System.
- `signtool.exe` must be installed and available in the system's PATH.

## Usage

CertiCheck is designed for both developers and users who want to ensure the integrity and authenticity of executable files. It is especially useful for:

- Verifying downloaded software before installation.
- Testing your own signed applications during development.
- Checking files for security purposes in enterprise environments.

## Disclaimer

CertiCheck relies on `signtool.exe`, a Microsoft-provided utility. Ensure you have it installed and configured properly for the best results.
