import subprocess  # nosec B404


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


def run_command(cmd):
    # Menjalankan command tanpa shell=True
    result = subprocess.run(  # nosec B603
        cmd.split(), capture_output=True, text=True
    )
    return result.stdout