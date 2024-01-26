import base64
from twilio.rest import Client

# Fungsi untuk melakukan enkripsi Caesar
def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk mengirim pesan WhatsApp
def send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, encrypted_message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              from_='whatsapp:' + from_whatsapp_number,
                              body=encrypted_message,
                              to='whatsapp:' + to_whatsapp_number
                          )
    print("Message sent successfully!")

# Konfigurasi
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
from_whatsapp_number = 'YOUR_TWILIO_WHATSAPP_NUMBER'
to_whatsapp_number = 'RECIPIENT_WHATSAPP_NUMBER'

# Pesan yang akan dikirim
plain_message = "Jangan lupa sholat dan selalu hormati orang tua anda."

# Melakukan enkripsi pesan menggunakan Caesar Cipher dengan pergeseran 3
shift = 3
encrypted_message = caesar_encrypt(plain_message, shift)

# Melakukan encoding Base64 terhadap pesan terenkripsi
encoded_message = base64.b64encode(encrypted_message.encode()).decode()

# Mengirim pesan WhatsApp terenkripsi
send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, encoded_message)