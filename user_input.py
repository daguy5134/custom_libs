import os


def is_int(
	input_prompt: str,
	error_display: str,
	error_prompt: str = False,
	validation_display: str = False
) -> int:
	"""
	
	Ask for user input until type is int.
	
	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: int
	"""
	if not error_prompt:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		try:
			input_var = int(input_var)
			break
		except TypeError:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def is_float(
		input_prompt: str,
		error_display: str,
		error_prompt: str = None,
		validation_display: str = False
) -> float:
	"""
	
	Ask for user input until type is float
	
	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: float
	"""
	if error_prompt is None:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		try:
			input_var = float(input_var)
			break
		except TypeError:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def file_exist(
		input_prompt: str,
		error_display: str,
		error_prompt: str = None,
		validation_display: str = False
) -> str:
	"""
	
	Ask for user input until matches an existing file
	
	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: str
	"""
	if error_prompt is None:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		if os.path.isfile(input_var):
			break
		else:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def matches_str(
		input_prompt: str,
		error_display: object,
		expected_result: object,
		error_prompt: object = False,
		validation_display: object = False
) -> str:
	"""
	
	Verify if user input is a specified str
	
	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param expected_result: The expected answer.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: str
	"""
	if not error_prompt:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		if input_var == expected_result:
			break
		else:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def in_list(
		input_prompt: str,
		error_display: str,
		expected_list: list | set | tuple,
		error_prompt: str = False,
		validation_display: object = False
) -> str:
	"""
	
	Verify if user input in a specified collection
	
	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param expected_list: A collection (list, set or tuple) containing valid answers.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: str
	"""
	if not error_prompt:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		if input_var in expected_list:
			break
		else:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def in_dict_key(
		input_prompt: str,
		error_display: str,
		expected_dict: dict,
		error_prompt: str = False,
		validation_display: object = False
) -> str:
	"""

	Verify if user input is a key in a specified dict

	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param expected_dict: A dict where the keys are valid answers.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: str
	"""
	if not error_prompt:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		if input_var in expected_dict:
			break
		else:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display, end="")
	return input_var


def in_dict_value(
		input_prompt: str,
		error_display: str,
		expected_dict: dict,
		error_prompt: str = False,
		validation_display: object = False
) -> str:
	"""

	Verify if user input is a value in a specified dictionary

	:param input_prompt: The prompt to ask for user input.
	:param error_display: Message to show in case the input isn't valid.
	:param expected_dict: A dict where the values are valid answers.
	:param error_prompt: The prompt for user input if the answer isn't valid (defaults to input_prompt).
	:param validation_display: What to show when the answer is valid (defaults to nothing).
	:rtype: str
	"""
	if not error_prompt:
		error_prompt = input_prompt
	input_var = input(input_prompt)
	while True:
		if input_var in expected_dict.values():
			break
		else:
			print(error_display)
		input_var = input(error_prompt)
	if not validation_display:
		pass
	else:
		print(validation_display)
	return input_var
