import base64

def encode_to_base64(input_text):
    input_bytes = input_text.encode('utf-8')  # Convert the input string to bytes
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_text = encoded_bytes.decode('utf-8')  # Convert the encoded bytes back to a string
    return encoded_text