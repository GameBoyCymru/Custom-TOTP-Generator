from flask import Flask, render_template, request, jsonify, url_for
import hashlib
import base64
import random
import qrcode
import os
import hashlib
import time

app = Flask(__name__)

def generate_custom_seed(input_data):
    current_time = str(time.time()).encode()
    hash_object = hashlib.sha256(current_time)
    hashed_time = int(hash_object.hexdigest(), 16) % 1000000
    combined_input = f"{input_data}{hashed_time}"
    hash_object = hashlib.sha256(combined_input.encode())
    seed = base64.b32encode(hash_object.digest()).decode('utf-8')
    return seed

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            account_name = request.form['account_name']
            issuer = request.form['issuer']
            seed = generate_custom_seed(account_name + issuer)
            otp_auth_uri = f"otpauth://totp/{issuer}:{account_name}?secret={seed}&issuer={issuer}&algorithm=SHA1&digits=6&period=30"
            
            qr_code_path = os.path.join(app.static_folder, '2fa_qr_code.png')
            generate_qr_code(otp_auth_uri, qr_code_path)
            
            return jsonify({
                'qr_code_url': url_for('static', filename='2fa_qr_code.png'),
                'otp_auth_uri': otp_auth_uri
            })
        except Exception as e:
            app.logger.error(f"Error generating QR code: {e}")
            return jsonify({'error': str(e)}), 500

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)