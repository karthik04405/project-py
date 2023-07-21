print("Welcome to my quiz!")

playing = input("Do you want to continue? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :) ")
score = 0

answer = input("what does IP stand for? ")
if answer.lower() == "internet protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does CND stand for? ")
if answer.lower() == "computer network defense":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does DNS stand for? ")
if answer.lower() == "domain name system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does FTP stand for? ")
if answer.lower() == "file transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does IDE stand for? ")
if answer.lower() == "integrated development environment":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does API stand for? ")
if answer.lower() == "application programming interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hyper text transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does VPN stand for? ")
if answer.lower() == "virtual private network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")