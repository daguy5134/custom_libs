import time


def word_1_by_1(
	text: str,
	line_limit: int,
	delay: float = 0.5
) -> None:
	"""
	
	Prints a text one word at a time, similar to AI bot
		
	:param text: Text to show.
	:param line_limit: Limit of words per line.
	:param delay: Delay between showing each word (defaults to 0.5)
	:return: None
	"""
	list_words = text.split()
	word_count = 0
	for i in range(len(list_words)):
		word_count += 1
		if word_count > line_limit:
			print()
			word_count = 0
		print(list_words[i], end=" ")
		time.sleep(delay)
