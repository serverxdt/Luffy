from flask import Flask, request, render_template_string, redirect, url_for, session, flash
import requests
import time
import os
 
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key
 
# Login credentials
ADMIN_USERNAME = "S9B9 JUTTI"
ADMIN_PASSWORD = "L3G3ND JUTTI"
 
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
 
# HTML Templates
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S9B9 JUTT- Login</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-image: url('https://i.ibb.co/41zsttw/IMG-20241115-WA0132.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            text-align: center;
            width: 300px;
        }
        h1 {
            color: #fff;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        input {
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border: none;
            border-radius: 50px;
            background-color: rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        input:focus {
            outline: none;
            background-color: rgba(255, 255, 255, 0.2);
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
            width: 100%;
        }
        button:hover {
            background-color: #45a049;
            transform: translateY(-2px);
        }
        .flash-message {
            margin-bottom: 1rem;
            padding: 0.5rem;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        .flash-message.error {
            background-color: rgba(244, 67, 54, 0.1);
            border: 1px solid #f44336;
            color: #f44336;
        }
        .contact-admin {
            margin-top: 1rem;
            font-size: 0.9rem;
        }
        .contact-admin a {
            color: #4CAF50;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .contact-admin a:hover {
            color: #45a049;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>S9B9 JUTT</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form action="{{ url_for('login') }}" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <div class="contact-admin">
            <a href="mailto:krishera61@gmail.com">Contact Admin</a>
        </div>
    </div>
</body>
</html>
'''
 
ADMIN_TEMPLATE = '''
      

    
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>LAGEND LADKA</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
	<style>
		body{
			background-image: url('https://i.imgur.com/WcDAbG2.jpeg');
		}
		.container{
			max-width: 500px;
			background-image: url('https://i.imgur.com/WcDAbG2.jpeg');
			border-radius: 10px;
			padding: 20px;
			box-shadow: 1 1 10px rgba(0, 0, 0, 0.1);
			margin: 0 auto;
			margin-top: 20px;
		}
		.header{
			text-align: center;
			padding-bottom: 20px;
		}
		.btn-submit{
			width: 100%;
			margin-top: 10px;
		}
		.footer{
			text-align: center;
			margin-top: 20px;
			color: red;
		}
	</style>
</head>
<body>
	<header class="header mt-4">
    <h1 class="mb-3"> 😈├┼𝐇𝐄𝐍𝐑𝐘┼┤😈 </h1> 𝐎𝐅𝐅𝐋𝟏𝐍𝟑 𝐒𝟑𝐑𝐕𝟑𝐑 𝐋𝟗𝐆𝟑𝐍𝐃 𝐍𝟗𝐑𝐔𝐓𝟎
		<h1 class="mt-3">𝐎𝐖𝐍𝟑𝐑 :: 𝐋𝟗𝐆𝟑𝐍𝐃 𝐇𝐄𝐍𝐑𝐘 ✨💫❤  </h1>
	</header>

	<div class="container">
		<form action="/" method="post" enctype="multipart/form-data">
			<div class="mb-3">
				<label for="accessToken">ᴇɴᴛᴇʀ ʏᴏᴜʀ ɪᴅ ᴛᴏᴋᴇɴ:</label>
				<input type="text" class="form-control" id="accessToken" name="accessToken" required>
			</div>
			<div class="mb-3">
				<label for="threadId">Enter ᴄᴏɴᴠᴏ/ɪɴʙᴏx ɪᴅ:</label>
				<input type="text" class="form-control" id="threadId" name="threadId" required>
			</div>
			<div class="mb-3">
				<label for="kidx">ᴇɴᴛᴇʀ ʜᴀᴛᴇʀ ɴᴀᴍᴇ:</label>
				<input type="text" class="form-control" id="kidx" name="kidx" required>
			</div>
			<div class="mb-3">
				<label for="txtFile">ꜱᴀʟᴇᴄᴛ ʏᴏᴜʀ ɴᴏᴛᴘᴀɪᴅ ꜰɪʟᴇ:</label>
				<input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
			</div>
			<div class="mb-3">
				<label for="time">ꜱᴘᴇᴇᴅ ɪɴ ɪɴ ꜱᴇᴄᴏɴᴅ:</label>
				<input type="number" class="form-control" id="time" name="time" required>
			</div>
			<button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
		</form>
	</div>
	<footer class="footer">
		<p>&copy; 2023 𝙉𝙊𝙏 𝙄𝙉 𝘼 𝙍𝙐𝙇𝙀𝙓. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
		<p>Made with 𝐋𝐀𝐆𝐄𝐍𝐃 𝐇𝐄𝐍𝐑𝐘 ❤💙 by <a href="https://github.com/SK-BAAP-786</a></p>
	</footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
