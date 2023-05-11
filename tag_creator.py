from noun_decliner import decline_nouns

#index types: metaperson, person, title, place, genres, national cinemas 
filename = 'input.txt'

#metaperson required attributes: ID, surname, surnameRus*, forename, gender, age* 
'''
Tag will be entered in order: ID, surnameEng, forename, gender, surnameRus, viewerAge
'''
def tag_metaperson(attrs:list):
    tag_txt = ''
    id, surname, forename, gender = attrs[:4]
    tag_txt += '<person xml:id="' + id + '">\n'
    tag_txt += '\t<surnameEng>' + surname + '</surnameEng>\n'
    if len(attrs) >= 5:
        tag_txt += '\t<surnameRus>' + attrs[4] + '</surnameRus>\n'
    tag_txt += '\t<forename>' + forename + '</forename>\n'
    tag_txt += '\t<gender>' + gender +  '</gender>\n'
    if len(attrs) >= 6:
        tag_txt += '\t<viewerAge>' + attrs[5] + '</viewerAge>\n'
    tag_txt += '</person>'
    return tag_txt


'''
Tags entered in order: ID, role, surname, forename, gender, nationality, wordtype, key_1, key_2, ..., key_n
'''
def tag_person(attrs:list):
    tag_txt = ''
    id, role, surname, forename, gender, nationality = attrs[:6]
    tag_txt += '<person xml:id="' + id + '">\n'
    tag_txt += '\t<role>' + role + '</role>\n'
    tag_txt += '\t<surnameEng>' + surname + '</surnameEng>\n'
    tag_txt += '\t<forename>' + forename + '</forename>\n'
    tag_txt += '\t<gender>' + gender +  '</gender>\n'
    tag_txt += '\t<nationality>' + nationality + '</nationality>\n'
    tag_txt += '\t<keys>\n'
    wordtypes = attrs[6].split('; ')
    keys = attrs[7].split('; ')   
    for key, wordtype in zip(keys, wordtypes):
        words = key.split()
        wordtype = wordtype.split()
        decls = []
        keyphrase = ''
        for word, wt in zip(words, wordtype):         
            decl = decline_nouns(word, wt)
            decls.append(decl)
        for col in range(len(decls[0])):
            for row in range(len(decls)):
                keyphrase += decls[row][col] + ' '
            keyphrase += ', '
        keyphrases = keyphrase.split(' , ')
        #print(keyphrases)
        #remove duplicates
        keyphrases = [*set(keyphrases)]
        for phrase in keyphrases: #get rid of blank entry at end of list
            if phrase == '':
                continue
            tag_txt += '\t\t<key>' + phrase + '</key>\n'
    tag_txt += '\t</keys>\n'
    tag_txt += '</person>'
    return tag_txt


'''
Tags entered in order: id, titleEng, titleRus, director, medium, country, genre, year, imdb, wordtype, key_1, ..., key_n
'''
def tag_title(attrs:list):
    tag_txt = ''
    id, titleEng, titleRus, director, medium, country, genre, year, imdb = attrs[:9]
    tag_txt += '<title xml:id="' + id + '">\n'
    tag_txt += '\t<fullTitleEng>' + titleEng + '</fullTitleEng>\n'
    tag_txt += '\t<fullTitleRus>' + titleRus + '</fullTitleRus>\n'
    tag_txt += '\t<director>' + director + '</director>\n'
    tag_txt += '\t<medium>' + medium + '</medium>\n'
    tag_txt += '\t<country>' + country + '</country>\n'
    tag_txt += '\t<genre>' + genre + '</genre>\n'
    tag_txt += '\t<year>' + year + '</year\n'
    tag_txt += '\t<imdb>' + imdb + '</imdb>\n'
    tag_txt += '\t<keys>\n'
    wordtypes = attrs[9].split('; ')
    keys = attrs[10].split('; ')   
    for key, wordtype in zip(keys, wordtypes):
        words = key.split()
        wordtype = wordtype.split()
        decls = []
        keyphrase = ''
        for word, wt in zip(words, wordtype):         
            decl = decline_nouns(word, wt)
            decls.append(decl)
        for col in range(len(decls[0])):
            for row in range(len(decls)):
                keyphrase += decls[row][col] + ' '
            keyphrase += ', '
        keyphrases = keyphrase.split(' , ')
        #print(keyphrases)
        #remove duplicates
        keyphrases = [*set(keyphrases)]
        for phrase in keyphrases: #get rid of blank entry at end of list
            if phrase == '':
                continue
            tag_txt += '\t\t<key>' + phrase + '</key>\n'
    tag_txt += '\t</keys>\n'
    tag_txt += '</title>'
    return tag_txt

'''
Tags entered in order: ID, fullName, placeType, key_1, ..., key_n
'''
def tag_place(attrs:list):
    tag_txt = ''
    id, fullname, placetype = attrs[:3]
    tag_txt += '<place xml:id="' + id + '">\n'
    tag_txt += '\t<fullName>' + fullname + '</fullName>\n'
    tag_txt += '\t<placeType>' + placetype + '</placeType>\n'
    tag_txt += '\t<keys>\n'
    wordtypes = attrs[3].split('; ')
    keys = attrs[4].split('; ')   
    for key, wordtype in zip(keys, wordtypes):
        words = key.split()
        wordtype = wordtype.split()
        decls = []
        keyphrase = ''
        for word, wt in zip(words, wordtype):         
            decl = decline_nouns(word, wt)
            decls.append(decl)
        for col in range(len(decls[0])):
            for row in range(len(decls)):
                keyphrase += decls[row][col] + ' '
            keyphrase += ', '
        keyphrases = keyphrase.split(' , ')
        #print(keyphrases)
        #remove duplicates
        keyphrases = [*set(keyphrases)]
        for phrase in keyphrases: #get rid of blank entry at end of list
            if phrase == '':
                continue
            tag_txt += '\t\t<key>' + phrase + '</key>\n'
    tag_txt += '\t</keys>\n'
    tag_txt += '</place>'
    return tag_txt

'''
Tags entered in order: ID, key_1, ..., key_n
'''
def tag_genre(attrs:list):
    tag_txt = ''
    id = attrs[0]
    tag_txt += '<genre xml:id="' + id + '">\n'
    tag_txt += '\t<keys>\n'
    wordtypes = attrs[1].split('; ')
    keys = attrs[2].split('; ')   
    for key, wordtype in zip(keys, wordtypes):
        words = key.split()
        wordtype = wordtype.split()
        decls = []
        keyphrase = ''
        for word, wt in zip(words, wordtype):         
            decl = decline_nouns(word, wt)
            decls.append(decl)
        for col in range(len(decls[0])):
            for row in range(len(decls)):
                keyphrase += decls[row][col] + ' '
            keyphrase += ', '
        keyphrases = keyphrase.split(' , ')
        #print(keyphrases)
        #remove duplicates
        keyphrases = [*set(keyphrases)]
        for phrase in keyphrases: #get rid of blank entry at end of list
            if phrase == '':
                continue
            tag_txt += '\t\t<key>' + phrase + '</key>\n'
    tag_txt += '\t</keys>\n'
    tag_txt += '</genre>'
    return tag_txt

'''
Tags entered in order: ID, key_1, ..., key_n
'''
def tag_natl_cinema(attrs:list):
    tag_txt = ''
    id = attrs[0]
    tag_txt += '<nationalCinema xml:id="' + id + '">\n' 
    tag_txt += '\t<keys>\n'
    wordtypes = attrs[1].split('; ')
    keys = attrs[2].split('; ')   
    for key, wordtype in zip(keys, wordtypes):
        words = key.split()
        wordtype = wordtype.split()
        decls = []
        keyphrase = ''
        for word, wt in zip(words, wordtype):         
            decl = decline_nouns(word, wt)
            decls.append(decl)
        for col in range(len(decls[0])):
            for row in range(len(decls)):
                keyphrase += decls[row][col] + ' '
            keyphrase += ', '
        keyphrases = keyphrase.split(' , ')
        #print(keyphrases)
        #remove duplicates
        keyphrases = [*set(keyphrases)]
        for phrase in keyphrases: #get rid of blank entry at end of list
            if phrase == '':
                continue
            tag_txt += '\t\t<key>' + phrase + '</key>\n'
    tag_txt += '\t</keys>\n'
    tag_txt += '</nationalCinema>'
    return tag_txt


with open(filename, encoding = 'utf-8') as file:
    text = file.read().splitlines()
    for line in text:
        attrs = line.split(', ')
        #print(attrs)
        new_tag = ''
        tag_type = attrs[0]
        if tag_type == 'metaperson':
            new_tag = tag_metaperson(attrs[1:])
        elif tag_type == 'person':
            new_tag = tag_person(attrs[1:])
        elif tag_type == 'title':
            new_tag = tag_title(attrs[1:])
        elif tag_type == 'place':
            new_tag = tag_place(attrs[1:])
        elif tag_type == 'genre':
            new_tag = tag_genre(attrs[1:])
        elif tag_type == 'nationalCinema':
            new_tag = tag_natl_cinema(attrs[1:])

        with open('output.txt', encoding='utf-8', mode='a') as outfile:
            outfile.write(new_tag + '\n\n')

print('Tags successfully generated. Please see output.txt file to retrieve. \
      \nNote: some keys may be slightly inaccurate due to grammatical irregularities.\
      \nManual fixes may be required.')