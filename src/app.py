import subprocess


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


def run_command(cmd):
    # Menjalankan command tanpa shell=True
    result = subprocess.run(
        cmd.split(), capture_output=True, text=True
    )
    return result.stdout