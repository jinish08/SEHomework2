import subprocess


def random_array(arr):
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i", "1-20", "-n", "1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
