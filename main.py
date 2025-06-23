from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

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


@app.route('/')
def index():
    return ' ' '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Generate WhatsApp pair codes instantly with this secure tool">
    <title>𝐆𝐞𝐭 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐂𝐫𝐞𝐝𝐬</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap" rel="stylesheet" />

    <style>
        :root {
            --primary: #ff2a6d;
            --accent: #05d9e8;
            --bg: #0d0221;
            --bg-secondary: #170a3a;
            --text: #d1f7ff;
            --input-bg: #261447;
            --border: #05d9e8;
            --success: #00ff85;
            --warning: #ff9a03;
            --primary-rgb: 255, 42, 109;
            --accent-rgb: 5, 217, 232;
            --shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(135deg, #0d0221 0%, #261447 50%, #0d0221 100%);
            background-size: 400% 400%;
            color: var(--text);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 15px;
            animation: gradientBG 15s ease infinite;
            line-height: 1.6;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            width: 100%;
            max-width: 500px;
            background: rgba(23, 10, 58, 0.9);
            border-radius: 16px;
            padding: 32px 22px;
            box-shadow: var(--shadow);
            border: 2px solid var(--border);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }

        .container:hover {
            transform: translateY(-5px);
        }

        .header {
            text-align: center;
            margin-bottom: 24px;
        }

        .logo {
            width: 80px;
            height: 80px;
            margin: 0 auto 12px;
            background: var(--primary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 38px;
            color: var(--text);
            box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.5);
            border: 2px solid var(--accent);
            position: relative;
            transition: transform 0.3s ease;
        }

        .logo:hover {
            transform: rotate(15deg) scale(1.1);
        }

        .logo-inner {
            position: relative;
            z-index: 2;
        }

        .logo-pulse {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: var(--primary);
            opacity: 0.7;
            z-index: 1;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 42, 109, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 15px rgba(255, 42, 109, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 42, 109, 0); }
        }

        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.7rem;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 1px;
            margin-bottom: 5px;
            text-shadow: 0 0 10px rgba(var(--primary-rgb), 0.7);
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            min-height: 2.5rem;
            display: inline-block;
        }

        .subtitle {
            font-size: 1rem;
            color: rgba(var(--accent-rgb), 0.8);
            margin-bottom: 22px;
        }

        .input-group {
            margin-bottom: 18px;
        }

        .input-label {
            display: block;
            margin-bottom: 7px;
            font-weight: 600;
            font-size: 14px;
            color: var(--text);
            letter-spacing: 0.5px;
        }

        .input-field {
            width: 100%;
            padding: 13px 14px;
            border: 2px solid var(--border);
            border-radius: 14px;
            background: var(--input-bg);
            color: var(--text);
            font-size: 16px;
            transition: all 0.3s;
            font-family: inherit;
        }

        .input-field:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 15px rgba(var(--primary-rgb), 0.6);
        }

        .input-field::placeholder {
            color: rgba(var(--accent-rgb), 0.5);
        }

        .btn {
            width: 100%;
            padding: 13px;
            border: none;
            border-radius: 14px;
            color: var(--text);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
            font-family: 'Orbitron', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .btn-primary {
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
            box-shadow: 0 4px 15px rgba(var(--primary-rgb), 0.4);
            margin-bottom: 16px;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(var(--primary-rgb), 0.6);
            background: linear-gradient(90deg, var(--accent) 0%, var(--primary) 100%);
        }

        .code-display {
            background: rgba(var(--accent-rgb), 0.1);
            padding: 15px;
            border-radius: 13px;
            text-align: center;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 14px;
            min-height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid var(--border);
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }

        .code-display:hover {
            transform: scale(1.01);
            box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.3);
        }

        .error-message {
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 16px;
            text-shadow: 0 0 8px rgba(255, 42, 109, 0.7);
        }

        .loading {
            display: none;
            text-align: center;
            margin: 18px 0;
        }

        .loading i {
            font-size: 28px;
            color: var(--accent);
            animation: spin 1s linear infinite;
            text-shadow: 0 0 10px rgba(var(--accent-rgb), 0.7);
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .footer {
            text-align: center;
            margin-top: 24px;
            font-size: 15px;
            font-weight: 900;
            color: var(--primary);
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .scanlines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom,
                    transparent 0%,
                    rgba(255, 42, 109, 0.03) 50%,
                    transparent 100%);
            background-size: 100% 4px;
            pointer-events: none;
            z-index: -1;
            animation: scanline 8s linear infinite;
        }

        @keyframes scanline {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }

        .tooltip {
            position: relative;
            display: inline-block;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: var(--bg-secondary);
            color: var(--text);
            text-align: center;
            border-radius: 6px;
            padding: 8px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
            border: 1px solid var(--border);
            font-size: 14px;
            font-weight: normal;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }

        /* Toggle Switch Styles */
        .toggle-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background: var(--input-bg);
            border: 2px solid var(--border);
            border-radius: 14px;
            padding: 5px;
            width: 100%;
            margin: 0 auto;
            position: relative;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
        }

        .toggle-option {
            flex: 1;
            text-align: center;
            padding: 10px;
            color: var(--text);
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.3s ease;
            z-index: 2;
            position: relative;
        }

        .toggle-option:hover {
            color: var(--accent);
        }

        .toggle-background {
            position: absolute;
            top: 5px;
            left: 5px;
            width: calc(50% - 5px);
            height: calc(100% - 10px);
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
            border-radius: 14px;
            transition: transform 0.3s ease;
            box-shadow: 0 0 15px rgba(var(--primary-rgb), 0.6);
            z-index: 1;
        }

        input[name="sendType"] {
            display: none;
        }

        input[value="file"]:checked ~ .toggle-background {
            transform: translateX(0);
        }

        input[value="base64"]:checked ~ .toggle-background {
            transform: translateX(100%);
        }

        /* Responsive adjustments */
        @media (max-width: 480px) {
            .container {
                padding: 20px 15px;
                border-radius: 12px;
            }

            .code-display {
                font-size: 16px;
                min-height: 44px;
                padding: 12px;
            }

            .logo {
                width: 65px;
                height: 65px;
                font-size: 32px;
            }

            .title {
                font-size: 1.4rem;
            }

            .btn {
                padding: 12px;
                font-size: 15px;
            }

            .toggle-container {
                max-width: 250px;
            }

            .toggle-option {
                font-size: 12px;
                padding: 8px;
            }
        }

        /* Accessibility focus styles */
        :focus-visible {
            outline: 3px solid var(--accent);
            outline-offset: 3px;
        }

        /* Print styles */
        @media print {
            body { background: none; color: #000; }
            .container { box-shadow: none; border: none; background: none; }
            .btn, .scanlines, .logo-pulse, .toggle-background { display: none; }
        }

        .typing-cursor {
            display: inline-block;
            color: var(--accent);
            animation: blink 1s step-end infinite;
            margin-left: 2px;
        }

        @keyframes blink {
            from, to { opacity: 1; }
            50% { opacity: 0; }
        }
    </style>
</head>

<body>
    <div class="scanlines" aria-hidden="true"></div>
    <div class="container">
        <div class="header">
            <div class="logo">
                <div class="logo-pulse" aria-hidden="true"></div>
                <div class="logo-inner">
                    <i class="fas fa-robot" aria-hidden="true"></i>
                </div>
            </div>
            <h1 class="title" id="typing-title"></h1>
            <p class="subtitle">Generate your WhatsApp pair code in seconds</p>
        </div>

        <div class="input-group">
            <div class="input-group">
                <label class="input-label">Select Output Format</label>
                <div class="toggle-container">
                    <input type="radio" name="sendType" id="file" value="file" checked>
                    <label for="file" class="toggle-option">Creds.json</label>
                    <input type="radio" name="sendType" id="base64" value="base64">
                    <label for="base64" class="toggle-option">Access Token</label>
                    <div class="toggle-background"></div>
                </div>
            </div>
            <label for="mobileNumber" class="input-label">
                Enter your WhatsApp number with country code
                <span class="tooltip">
                    <i class="fas fa-info-circle" aria-hidden="true"></i>
                    <span class="tooltiptext">Format: +[country code][number] (e.g., +1234567890)</span>
                </span>
            </label>
            <input type="tel" id="mobileNumber" class="input-field" placeholder="e.g. +994402197773" pattern="\+[0-9]{10,}" required inputmode="tel">
        </div>

        <button class="btn btn-primary" id="submit" aria-label="Generate pair code">
            <i class="fas fa-fire" aria-hidden="true"></i> Generate Pair Code
        </button>

        <div class="loading" id="loading" aria-live="polite">
            <i class="fas fa-spinner" aria-hidden="true"></i>
        </div>

        <div class="code-display" id="codeDisplay" aria-live="polite" style="font-family: Arial, sans-serif;">
            Your pair code will appear here
        </div>

        <button class="btn btn-primary" id="copy" onclick="copyCode()" disabled aria-label="Copy code to clipboard">
            <i class="fas fa-copy" aria-hidden="true"></i> Copy Code
        </button>

        <div class="footer">
            CODED BY TABBU ARAIN <span aria-hidden="true">💚</span>
        </div>
    </div>

    <script>
        function loadScript(src) {
            return new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = src;
                script.onload = resolve;
                script.onerror = reject;
                document.body.appendChild(script);
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            const mobileNumberInput = document.getElementById("mobileNumber");
            const codeDisplay = document.getElementById("codeDisplay");
            const loadingSpinner = document.getElementById("loading");
            const copyBtn = document.getElementById("copy");
            const submitBtn = document.getElementById("submit");

            mobileNumberInput.addEventListener('input', function() {
                this.style.borderColor = this.checkValidity() ? 'var(--success)' : 'var(--border)';
            });

            submitBtn.addEventListener("click", async (e) => {
                e.preventDefault();

                if (!mobileNumberInput.checkValidity()) {
                    codeDisplay.innerHTML = `<div class="error-message">
                        <i class="fas fa-exclamation-circle"></i> Please enter a valid WhatsApp number
                    </div>`;
                    mobileNumberInput.focus();
                    return;
                }

                const mobileNumber = mobileNumberInput.value.trim();
                const selectedType = document.querySelector('input[name="sendType"]:checked').value;

                loadingSpinner.style.display = "block";
                codeDisplay.innerHTML = 'Generating code...';
                submitBtn.disabled = true;

                try {
                    if (typeof axios === 'undefined') {
                        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/axios/1.0.0-alpha.1/axios.min.js');
                    }

                    const response = await axios(`/code?number=${mobileNumber.replace(/[^0-9]/g, "")}&type=${selectedType}`, {
                        timeout: 10000
                    });

                    const code = response.data.code || "Service Unavailable";
                    if (code === "Service Unavailable") {
                        codeDisplay.innerHTML = `<div class="error-message">
                            <i class="fas fa-exclamation-circle"></i> Service Unavailable
                        </div>`;
                    } else {
                        codeDisplay.innerHTML = `<div class="success-message">
                            <i class="fas fa-check-circle"></i> ${selectedType === "file" ? "CODE: " + code : code}
                        </div>`;
                        copyBtn.disabled = false;
                    }
                } catch (error) {
                    console.error("Error generating code:", error);
                    let errorMessage = 'Error generating code. Please try again.';

                    if (error.response) {
                        errorMessage = error.response.data.message || errorMessage;
                    } else if (error.request) {
                        errorMessage = 'Network error. Please check your connection.';
                    }

                    codeDisplay.innerHTML = `<div class="error-message">
                        <i class="fas fa-exclamation-circle"></i> ${errorMessage}
                    </div>`;
                } finally {
                    loadingSpinner.style.display = "none";
                    submitBtn.disabled = false;
                }
            });

            mobileNumberInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    submitBtn.click();
                }
            });
        });

        function copyCode() {
            const codeDisplay = document.getElementById("codeDisplay");
            const code = codeDisplay.innerText.replace('CODE: ', '').trim();

            if (!code || code === "Your pair code will appear here") return;

            navigator.clipboard.writeText(code).then(() => {
                const copyBtn = document.getElementById("copy");
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                copyBtn.style.background = 'var(--success)';

                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                    copyBtn.style.background = '';
                }, 2000);
            }).catch(err => {
                console.error("Failed to copy text: ", err);
                codeDisplay.innerHTML = `<div class="error-message">
                    <i class="fas fa-exclamation-circle"></i> Failed to copy code
                </div>`;
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            const titleText = "Get WP Creds.json and Access Token";
            const titleElement = document.getElementById('typing-title');
            let i = 0;

            const cursor = document.createElement('span');
            cursor.className = 'typing-cursor';
            cursor.textContent = '|';
            titleElement.appendChild(cursor);

            function typeWriter() {
                if (i < titleText.length) {
                    const char = document.createTextNode(titleText.charAt(i));
                    titleElement.insertBefore(char, cursor);
                    i++;
                    setTimeout(typeWriter, 100);
                } else {
                    setTimeout(() => {
                        cursor.style.opacity = '0';
                        setTimeout(() => cursor.remove(), 10000000);
                    }, 10000000);
                }
            }

            setTimeout(typeWriter, 500);
        });
    </script>
</body>
</html>

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
