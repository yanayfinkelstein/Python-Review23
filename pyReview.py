print("fuck you")

def create_youtube_video(description, title):
	video = {"title": title, "description": description, "likes": 0, "dislikes":0, "comments":{}}
	return video
def like(dictionary):
	if "likes" in dictionary:
		dictionary["likes"] = dictionary["likes"] + 1
		return dictionary


def dislike(dictionary):
	if "dislikes" in dictionary:
		dictionary["dislikes"] = dictionary["dislikes"] + 1
		return dictionary
def add_comment(video, username, comment_text):
		comments = {username: comment_text}
		video["comments"][username]=comment_text
		return comments


title = input("what's the title of the video?")
description = input("whats the video's description?")
video = create_youtube_video(description,title)
for i in range(6):
	like(video)
dislike(video)
print(video)
