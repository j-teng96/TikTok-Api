from ChatstatTikTokApi import ChatstatTikTokApi

with ChatstatTikTokApi() as api:
    for user in api.search.users("therock"):
        print(user.username)

    for sound in api.search.sounds("funny"):
        print(sound.title)

    for hashtag in api.search.hashtags("funny"):
        print(hashtag.name)
