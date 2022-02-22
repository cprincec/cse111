from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        determiner = get_determiner(1) 
        assert determiner in single_determiners

    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):
        quantity = random.randint(2, 11)
        determiner = get_determiner(quantity)
        assert determiner in plural_determiners



def test_get_noun():
    
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(12):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
                                                                                                        
    for _ in range(12):
        noun = get_noun(10)
        assert noun in plural_nouns



def test_get_verb():
    
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range(12):
        verb = get_verb(1, "present")
        assert verb in single_present_verbs

    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(12):

        quantity = random.randint(2, 100)
        verb = get_verb(quantity, "present")
        assert verb in plural_present_verbs
    
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(12):
        verb = get_verb(1 or 2, "past")
        assert verb in past_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(12): 
        verb = get_verb(1 or 2, "future")
        assert verb in future_verbs


def test_get_preposition():
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    
    for _ in range(20):
        preposition = get_preposition()
        assert preposition in prepositions


def test_get_prepositional_phrase():

    single_determiners = ["a", "one", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(20):
        
        prep_phrase = get_prepositional_phrase(1)

        #unpack the preposition, determiner and noun randomly returned from the 
        #get_prepositional_phrase function into three seperate variables.
        prep_phrase_preposition, prep_phrase_single_determiner, prep_phrase_single_noun = prep_phrase

        #verify that the values returned from the get_prepositional_phrase function 
        #can be found in the correct list of available values
        assert prep_phrase_preposition in prepositions
        assert prep_phrase_single_determiner in single_determiners
        assert prep_phrase_single_noun in single_nouns

    
    plural_determiners = ["two", "some", "many", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(20):
        prep_phrase = get_prepositional_phrase(2)
        prep_phrase_preposition, prep_phrase_plural_determiner, prep_phrase_plural_noun = prep_phrase

        assert prep_phrase_preposition in prepositions
        assert prep_phrase_plural_determiner in plural_determiners
        assert prep_phrase_plural_noun in plural_nouns


    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

