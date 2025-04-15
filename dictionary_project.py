dictionary = {
    "apple": "A fruit that is typically red, green, or yellow in color.",
    "book": "A collection of pages with written or printed words, bound together.",
    "car": "A road vehicle that has an engine and is used for transportation.",
    "dog": "A loyal and friendly animal that is often kept as a pet.",
    "elephant": "A very large animal with a trunk, found mostly in Africa and Asia.",
    "python": "A high-level programming language.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A block of code which only runs when it is called.",
    "variable": "A storage location paired with an associated symbolic name.",
    "loop": "A sequence of instructions that repeats until a condition is met.",
    "computer": "An electronic device that processes data and performs tasks according to a set of instructions.",
    "internet": "A global network connecting millions of computers for communication and information sharing.",
    "science": "The study of the structure and behavior of the physical and natural world through observation and experiment.",
    "planet": "A large celestial body that orbits a star and does not produce light of its own.",
    "music": "The art of arranging sounds in time to produce a composition through melody, harmony, rhythm, and timbre.",
    "friend": "A person whom one knows and has a bond of mutual affection with.",
    "school": "An institution for educating children or providing instruction in a particular subject.",
    "robot": "A machine capable of carrying out a complex series of actions automatically.",
    "rain": "Water droplets that fall from clouds in the sky to the ground.",
    "tree": "A tall plant with a trunk and branches made of wood.",
    "forest": "A large area covered chiefly with trees and undergrowth.",
    "river": "A natural flowing watercourse, usually freshwater, flowing towards an ocean or sea.",
    "mountain": "A large natural elevation of the earth's surface rising abruptly from the surrounding level.",
    "desert": "A barren area of landscape where little precipitation occurs and living conditions are hostile for plant and animal life.",
    "ocean": "A vast body of saline water that covers almost three-quarters of the Earth's surface.",
    "climate": "The weather conditions prevailing in an area in general or over a long period.",
    "volcano": "A mountain or hill, typically conical, having a crater or vent through which lava, rock fragments, and gas are being or have been erupted.",
    "earthquake": "A sudden and violent shaking of the ground, often caused by movements of the Earth's crust.",
    "ecosystem": "A community of interacting organisms and their physical environment.",
    "glacier": "A slowly moving mass of ice formed by the accumulation and compaction of snow on mountains or near the poles.",
    "algorithm": "A step-by-step procedure used to solve a problem or perform a task, often by a computer.",
    "software": "A set of instructions, data, or programs used to operate computers and execute specific tasks.",
    "hardware": "The physical components of a computer system, such as the CPU, keyboard, or hard drive.",
    "network": "A group of interconnected computers and devices that can share resources and information.",
    "browser": "A software application used to access and view websites on the internet.",
    "database": "An organized collection of data that can be easily accessed, managed, and updated.",
    "encryption": "The process of converting information into a code to prevent unauthorized access.",
    "server": "A computer or system that provides resources, data, or services to other computers over a network.",
    "cloud": "A system of remote servers used to store, manage, and process data online instead of on a local server.",
    "programming": "The process of designing and writing instructions for computers to follow.",
    "galaxy": "A vast system of stars, dust, and gas bound together by gravity.",
    "planet": "A celestial body orbiting a star, massive enough to be rounded by its own gravity.",
    "asteroid": "A small rocky object that orbits the sun, mostly found in the asteroid belt.",
    "comet": "An icy body that releases gas or dust and often has a visible tail when near the sun.",
    "meteor": "A small body of matter from outer space that enters Earth's atmosphere and burns up, creating a streak of light.",
    "nebula": "A giant cloud of dust and gas in space, often the birthplace of stars.",
    "orbit": "The curved path of a celestial object around a star, planet, or moon.",
    "telescope": "An instrument used to observe distant objects by collecting electromagnetic radiation.",
    "gravity": "The force that attracts two bodies toward each other, especially the force that gives weight to physical objects.",
    "universe": "All of space and time, including planets, stars, galaxies, and all matter and energy."
    }

print("------------------------------------------------")
print("        Welcome to the Simple Dictionary App     ")
print("------------------------------------------------")
print("This app helps you find the meaning of simple words.")
print("Type a word to look it up. Type 'exit' to quit.")
print("------------------------------------------------\n")

while True:
    user_input = input("Enter a word to search (or type 'exit' to quit): ")
    word = user_input.lower()

    if word == "exit":
        print("\nThank you for using the Dictionary App!")
        print("Goodbye!")
        break  
    
    if word in dictionary:
        meaning = dictionary[word]
        print(f"\nMeaning of '{word}':")
        print(f"{meaning}\n")
    else:
        print(f"\nSorry, the word '{word}' was not found in the dictionary.\n")


