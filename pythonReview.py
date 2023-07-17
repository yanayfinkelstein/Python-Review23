
def create_youtube_video(description, title):
	video = {"title": title, "description": description, "likes": likes, "dislikes":dislikes, "comments":comments}
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
		
	
		

