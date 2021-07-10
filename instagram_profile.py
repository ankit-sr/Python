import instaloader

ig = instaloader.Instaloader()

dp = input("Enter hte username : ")

ig.download_profile(dp, profile_pic_only = True)