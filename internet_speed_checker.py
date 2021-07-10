import speedtest

test = speedtest.Speedtest()

print(f"Download Speed: {test.download()}")

print(f"Upload Speed: {test.upload()}")