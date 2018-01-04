from sys import argv # Load argv modleu - means args can be defined at command line

script, user_name, bird = argv # Although this seems kind of backwards
prompt = ' --->'

print(f"Hi {user_name}, I'm the {script} script.") # Use f before string to allow vars
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

print(f"I am a {bird}.")
