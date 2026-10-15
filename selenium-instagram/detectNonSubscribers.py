followers = list()
follows = list()

with open("followers.txt", "r", encoding="UTF-8") as followersFile:
    while True:
        follower = followersFile.readline().rstrip('\n')
        if not follower:
            break
        followers.append(follower)

with open("follows.txt", "r", encoding="UTF-8") as followsFile:
    while True:
        follow = followsFile.readline().rstrip('\n')
        if not follow:
            break
        follows.append(follow)

with open("detectedNonFollowers.txt", "w") as detectedNonFollowersFile:
    for follow in follows:
        if follow not in followers:
            detectedNonFollowersFile.write(follow + "\n")