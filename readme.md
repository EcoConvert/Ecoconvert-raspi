## Overview
- Simple QR code generation and validation system using JWT tokens. 

## Features
- **JWT Encoding**: Encodes payload data (e.g., points) into a JWT.
- **QR Code Generation**: Converts the JWT into a QR code image.
- **QR Code Scanning & Decoding**: Reads the QR code and extracts the JWT.
- **Token Validation**: Validates the JWT and checks if the token has already been redeemed using Redis.

## Setup
1. Clone this repository.
2. Install the required dependencies
```bash
pip install -r requirements.txt
```
3. Createa a `.env` file and define the `SECRET_KEY`
4. Ensure Redis is installed and running on `localhost` with default port `6379`
5. Run the script.

## Limitation 
**Current Limitations**
1. Token Expiry Not Implemented
2. Static Points Value
3. Basic Error Handling
4. No Database Integration -> If possible, integrate database with counts of PET bottles

## Improvements
1. Add Token Expiration
2. Dynamic Payload Generation
3. Better Error Handling
4. Database Integration
5. User Interface -> Idea is simple web with dashboard, where there's a scanner for QR Code that will use webcam.
