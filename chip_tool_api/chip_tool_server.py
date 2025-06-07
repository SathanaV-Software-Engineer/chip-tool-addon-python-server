from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Set full path of chip-tool binary here
CHIP_TOOL_PATH = "/usr/local/bin/chip-tool"  # replace with your actual path

@app.route('/')
def index():
    return "CHIP Tool API is running!"

@app.route('/run', methods=['POST'])
def run_chip_tool():
    data = request.get_json()
    args = data.get('args')
    if not args:
        return jsonify({"error": "Missing 'args' in request"}), 400

    # Use full path to chip-tool here
    cmd = f"{CHIP_TOOL_PATH} {args}"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return jsonify({
            "command": cmd,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
