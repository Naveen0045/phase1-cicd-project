from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
    <head>
        <title>AWS CI/CD Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                margin-top: 100px;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                width: 600px;
                margin: auto;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: green;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>PHASE-2 ECS FARGATE SUCCESS 🚀</h1>

            <p><b>Application:</b> Flask Web App</p>

            <p><b>Deployment:</b> GitHub ➜ ECR ➜ ECS Fargate</p>

            <p><b>Container ID:</b> {hostname}</p>

            <p><b>Timestamp:</b> {datetime.datetime.now()}</p>

            <p><b>Status:</b> Running Successfully ✅</p>
        </div>
    </body>

    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "UP",
        "service": "phase2-ecs-fargate"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
