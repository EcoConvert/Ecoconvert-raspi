import datetime
import os
import time
import uuid

import jwt
import qrcode
import redis
from dotenv import load_dotenv
from PIL import Image
from pyzbar.pyzbar import decode

# Load environment variables
load_dotenv()

# Load secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Setup Redis
redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)


# Revert time if need
# time_convert = datetime.datetime.fromtimestamp(payload["iat"]).strftime("%Y-%m-%d %H:%M:%S")


# Empty parameters for now, in the future, it will need to get the points
def encode_jwt():
    payload = {"points": 50, "iat": int(datetime.datetime.now().timestamp()), "jti": str(uuid.uuid4())}
    valid_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

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

        # Get the 'jti' then check if the points is already redeemed
        jti = decoded["jti"]
        print(str(jti))

        # Check if the token is already redeemed
        if redis_client.exists(jti):
            return "Token already redeemed"
        else:
            # Mark the token as redeem, changing the JTI 7 days try
            # Subject to change, can be a month
            redis_client.setex(jti, 7 * 24 * 60 * 60, "redeemed")
            return "Points redeemed successfully"

    except jwt.InvalidTokenError:
        return "Invalid Token"
    except jwt.ExpiredSignatureError:
        return "Token has expired"


# Generate JWT and QR
# a = encode_jwt()
# print(a)

print(decode_and_validate("token.png"))
