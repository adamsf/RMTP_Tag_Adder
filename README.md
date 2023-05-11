# Russian Language tag adder

Created by Francis Adams for the Russian and Post-Soviet Studies department at the College of William and Mary

## Project Scope

Software that allows any given Russian word to be added to a list of tags, with each declension for every grammatical case in Russian accounted for.

In its current version, some words may not be properly tagged and will require manual overwriting to add the grammatically correct versions:

- fleeting vowels
- female last names that end in a consonant  
- names that end in o that should not be declined (Марио, etc.)
- plurals
- е vs ё

## Installation and Running

This program runs on any version of Python 3 

To run as easy as possible, install anaconda and use anaconda prompt

### Dependencies

In its current version, no library dependencies exist

### Instructions

Clone or download the repository, navigate to ./tag_adder 

inside the folder, add a file called input.txt to be used in the running program

#### Tags

There are 6 different types of tags that the RMTP tagger tries to categorize each word into:
- Metapersons (Interviewers/ees, transcribers, translators, other contributors)
- Persons (Actors, directors, or anyone else referenced in interviews)
- Titles of media (films, etc.)
- Places (Cities, countries, theatres, etc.)
- Genres
- National cinema


#### Attributes

Each of these 6 tags have different attributes that the tagger looks for. IDs are written as one word with camelback notation.

- Metapersons: ID, English Surname, English first name, gender, Russian Surname (if applicable), Viewer age (if applicable)
- Persons: ID, role, surname, forename, gender, nationality, keys (Russian words/phrases that identify the specified person)
- Titles of media: ID, English Title, Russian title, director, medium, country, genre, year, imdb link, keys 
- Places: ID, full name, type of place, identifying keys
- Genres: ID, keys
- National cinema: ID, keys

#### Syntax for input.txt file 

For each of the different tag types, the type of tag needs to be specified, followed by each of the attributes separated with a comma.

- ex. metaperson, Adams, Francis, m 
- metaperson, Zhanakeev, Turgunbek, m, Жанакеев, sov

The tags that require keywords be specified have a slightly different syntax. The program needs to know how many 
different phrases there will be in addition to how to create keys for each of the six Russian cases. When writing the input for this,
the last two parameters separated by commas need to have each phrase separated by a semicolon and the word types matching it:
- ex. person, ..., noun adj; adj, володымыр зеленський; зеленський

#### Running the program 

In the anaconda prompt window, navigate to the Tag_adder folder and type and run: python tag_creator.py

As long as the input.txt file contains no errors and is located in the same folder, the program runs as intended.

When the program finishes running, a file named output.txt is created and will be located in the tag_adder folder.

This file contains the XML tags to be added to the RMTP tagger's index.xml file. The new tags can be copied and pasted into the correct location 
in the XML file and will be tagged when the tagger is run. Reminder that some grammatical errors may be generated by the tag creator programs
and may need to be fixed manually.
