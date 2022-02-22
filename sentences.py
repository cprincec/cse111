import random

def main():

    determiner1 = get_determiner(1)
    noun1 = get_noun(1)
    verb1 = get_verb(1, "past")
    single_prep_phrase1 = get_prepositional_phrase(1)
    single_prep_phrase1_1 = get_prepositional_phrase(1)
    

    determiner2 = get_determiner(1)
    noun2 = get_noun(1)
    verb2 = get_verb(1, "present")
    single_prep_phrase2 = get_prepositional_phrase(1)
    single_prep_phrase2_2 = get_prepositional_phrase(1)
    

    determiner3 = get_determiner(1)
    noun3 = get_noun(1)
    verb3 = get_verb(1, "future")
    single_prep_phrase3 = get_prepositional_phrase(1)
    single_prep_phrase3_3 = get_prepositional_phrase(1)
    

    determiner4 = get_determiner(2)
    noun4 = get_noun(2)
    verb4 = get_verb(2, "past")
    plural_prep_phrase4 = get_prepositional_phrase(4)
    plural_prep_phrase4_4 = get_prepositional_phrase(4)

    determiner5 = get_determiner(2).capitalize()
    noun5 = get_noun(2)
    verb5 = get_verb(2, "present")
    plural_prep_phrase5 = get_prepositional_phrase(3)
    plural_prep_phrase5_5 = get_prepositional_phrase(3)


    determiner6 = get_determiner(2).capitalize()
    noun6 = get_noun(2)
    verb6 = get_verb(2, "future")
    plural_prep_phrase6 = get_prepositional_phrase(2)
    plural_prep_phrase6_6 = get_prepositional_phrase(2)


    print()
    print("SENTENCES WITH SINGULAR DETERMINERS:")
    print(f"{determiner1} {noun1}", end=" ")
    print(*single_prep_phrase1, sep = " ", end=" ")
    print(verb1, end=" ")
    print(*single_prep_phrase1_1, sep = " ")


    print(f"{determiner2} {noun2}", end=" ")
    print(*single_prep_phrase2, sep = " ", end=" ")
    print(verb2, end=" ")
    print(*single_prep_phrase2_2, sep = " ")


    print(f"{determiner3} {noun3}", end=" ")
    print(*single_prep_phrase3, sep = " ", end=" ")
    print(verb3, end=" ")
    print(*single_prep_phrase3_3, sep = " ")

    
    print()
    print("SENTENCES WITH PLURAL DETERMINERS:")
    print(f"{determiner4} {noun4}", end=" ")
    print(*plural_prep_phrase4, sep= " ", end=" ")
    print(verb4, end=" ")
    print(*plural_prep_phrase4_4, sep= " ")


    print(f"{determiner5} {noun5}", end=" ")
    print(*plural_prep_phrase5, sep= " ", end=" ")
    print(verb5, end=" ")
    print(*plural_prep_phrase5_5, sep= " ")


    print(f"{determiner6} {noun6}", end=" ")
    print(*plural_prep_phrase6, sep= " ", end=" ")
    print(verb6, end=" ")
    print(*plural_prep_phrase6_6, sep= " ")
    print()


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(determiners)
    return determiner


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """    

    if quantity == 1 and tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
   
    elif quantity != 1 and tense == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    elif tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    prep = random.choice(prepositions)
    return prep


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    if quantity == 1:
        determiners = ["a", "one", "the"]
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        preps = get_preposition()
    else:
        determiners = ["two", "some", "many", "the"]
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        preps = get_preposition()
    
    
    determiner = random.choice(determiners)
    noun = random.choice(nouns)
 
    return preps, determiner, noun

if __name__ == "__main__":
    main()
