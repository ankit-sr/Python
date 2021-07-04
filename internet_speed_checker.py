import speedtest

test = speedtest.Speedtest()

down = test.download()

up = test.upload()

print(f"Download Speed: {down}")

print(f"Upload Speed: {up}")