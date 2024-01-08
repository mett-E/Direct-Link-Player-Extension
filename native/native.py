import json
import sys
import subprocess

videoplayer_executable_path = "\\path\\to\\your\\videoplayer.exe"


def process_message(message):
    command = message.get("command", "")
    if command:
        try:
            result = execute_command(command)
            send_response(result)
        except Exception as e:
            send_error(str(e))


def execute_command(command):
    cmd_command = f"{videoplayer_executable_path} {command}"
    subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def send_response(response):
    sys.stdout.buffer.write(json.dumps({"result": response}).encode("utf-8"))
    sys.stdout.flush()


def send_error(error_message):
    sys.stdout.buffer.write(json.dumps({"error": error_message}).encode("utf-8"))
    sys.stdout.flush()


def read_input():
    raw_message_length = sys.stdin.buffer.read(4)
    if not raw_message_length:
        return None
    message_length = int.from_bytes(raw_message_length, byteorder="little")
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)


if __name__ == "__main__":
    while True:
        message = read_input()
        if message is None:
            break
        process_message(message)
