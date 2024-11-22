import datetime
import os

import jwt
import qrcode
from dotenv import load_dotenv
from PIL import Image
from pyzbar.pyzbar import decode

# Load environment variables
load_dotenv()

# Load secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Revert time if need
# time_convert = datetime.datetime.fromtimestamp(payload["iat"]).strftime("%Y-%m-%d %H:%M:%S")


# Empty parameters for now, in the future, it will need to get the points
def encode_jwt(point: int):
    payload = {
        "points": point,
        "iat": int(datetime.datetime.now().timestamp()),
    }
    valid_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print(payload)

    # Generate QR Code
    qr = qrcode.make(valid_token)
    qr_path = "token.png"
    qr.save(qr_path)
    print("QR Code saved as 'token.png'")

    return qr_path


# Decode the QR code and extract payload
def decode_and_validate(qr_image_path: str):
    # Decode the image
    qr_image = Image.open(qr_image_path)
    # Get the data and convert to string
    decoded_data = decode(qr_image)[0].data.decode("utf-8")

    # Try-Catch
    try:
        # Decode the jwt
        decoded = jwt.decode(decoded_data, SECRET_KEY, algorithms=["HS256"])
        return {"status": "Success", "decoded_token": decoded}
    except jwt.InvalidTokenError:
        return {"status": "Error", "message": "Token has expired"}
    except jwt.ExpiredSignatureError:
        return {"status": "Error", "message": "Invalid Token"}


# Generate JWT and QR
# a = encode_jwt()
# print(a)


if __name__ == "__main__":
    points_input = int(input("How many points: "))
    a = encode_jwt(points_input)

    b = decode_and_validate(a)
    print(b)
