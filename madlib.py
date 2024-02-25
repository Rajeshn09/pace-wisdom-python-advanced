def mad_libs():
    # Mad Libs Game template
    mad_libs_template = (
        "One {} day, I decided to visit the {}. "
        "As soon as I arrived, I noticed a {} right in the middle of the {}. "
        "It was so {} that I couldn't resist taking a selfie with it.\n\n"
        
        "While exploring, I encountered a {} {} wearing a {} hat. "
        "It seemed to be in a hurry, perhaps late for a {}. "
        "I followed it and ended up at a {} {} {}.\n\n"
        
        "Inside, I met a {} who was busy {}. "
        "They kindly offered me a cup of {}, and we chatted about {}. "
        "It was a {} conversation that I'll never forget.\n\n"
        
        "After saying goodbye, I left the {} with a {} heart, grateful for such a {} adventure."
    )

    # User input for filling in the blanks
    adjective1 = input("Enter an adjective: ")
    place = input("Enter a place: ")
    noun = input("Enter a noun: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    event = input("Enter an event: ")
    adjective3 = input("Enter yet another adjective: ")
    location = input("Enter a location: ")
    occupation = input("Enter an occupation: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    beverage = input("Enter a beverage: ")
    plural_noun = input("Enter a plural noun: ")
    adjective4 = input("Enter a final adjective: ")
    emotion = input("Enter an emotion: ")

    # mad_libs_template.format() used to replace the placeholder with ordered inputs. 
    mad_libs_story = mad_libs_template.format(
        adjective1, place, noun, adjective2, place, 
        adjective3, animal, color, event, 
        adjective4, adjective2, location, 
        occupation, verb_ing, beverage, plural_noun, 
        adjective4, place, emotion, adjective1
    )

    
    print(mad_libs_story)

# Calling mad_libs() function
mad_libs()
