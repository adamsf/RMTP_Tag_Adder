#noun, adj
#as of now, the program cannot properly tag
    # fleeting vowels
    # instrumental male last names
    # female last names that end in a consonant  
    # names that end in o that should not be declined (Марио, etc.)
    # plurals (does not seem necessary unless told otherwise)
    # е vs ё
#those can be manually changed for now 
fem_noun_endings = 'яа'
masc_noun_endings = 'бвгджзйклмнпрстфцчшщ'
neuter_noun_endings = 'ео'
hushes = 'чшщжц'
velars = 'кгх'

mn_hard_decl = ['', 'а', 'у', 'ом', 'е']
mn_soft_decl = ['й', 'я', 'ю', 'ем', 'е']

fem_hard_decl = ['у', 'ы', 'е', 'ой', 'е']
fem_soft_decl = ['ю', 'и', 'е', 'ей', 'е']

mn_adj_hard_decl = ['ый', 'ого', 'ому', 'ым', 'ом']
mn_adj_soft_decl = ['ий', 'его', 'ему', 'им', 'ем']

fem_adj_decl = ['ую', 'ой', 'ой', 'ой', 'ой']

def decline_nouns(word, type='noun'):
    declensions = [word]
    ending = word[-1]
    #print(ending)
    if type == 'adj':
        ending = word[-2:]

    #masc noun endings
    if ending in masc_noun_endings:
        if ending == 'й':
            for d in mn_soft_decl:
                if word[-2] == 'и' and d == 'е':
                    declensions.append(word[:-1] + 'и')
                else:
                    declensions.append(word[:-1] + d)
        else:
            for d in mn_hard_decl:
                if ending[-1] in hushes and d == 'ом':
                    declensions.append(word + 'ем')
                #add male last name instrumental case 
                elif word[-2:] in ['ов', 'ин'] and d == 'ом':
                    yn = input('Is ' + word + ' a last name? (y/n): ')
                    if yn == 'y':
                        declensions.append(word + 'ым')
                    else:
                        declensions.append(word + d)
                else:
                    declensions.append(word + d)
    #fem noun endings
    elif ending in fem_noun_endings:
        if ending == 'я':
            for d in fem_soft_decl:
                if d == 'е' and word[-2] == 'и':
                    continue
                declensions.append(word[:-1] + d)
        else:
            yn = ''
            for d in fem_hard_decl:
                if word[-2] in hushes + velars and d == 'ы':
                    declensions.append(word[:-1] + 'и')
                elif word[-3:] in ['ова', 'ина'] and d in ['ы', 'е']:
                    if yn == '':
                        yn = input('Is ' + word + ' a last name? (y/n): ')
                    if yn == 'y':
                        declensions.append(word[:-1] + 'ой')
                    else:
                        declensions.append(word[:-1] + d)
                elif word[-2] in hushes and d == 'ой':
                    declensions.append(word[:-1] + 'ей')
                else:
                    declensions.append(word[:-1] + d)
    #neuter noun endings
    elif ending in neuter_noun_endings:
        if ending == 'е':
            for i in range(len(mn_hard_decl)):
                if word[-2] in hushes + velars:
                    declensions.append(word[:-1] + mn_hard_decl[i])
                elif mn_hard_decl[i] == 'е' and word[-2] == 'и':
                    declensions.append(word[:-1] + 'и')
                else:
                    declensions.append(word[:-1] + mn_soft_decl[i])
        else:
            for d in mn_hard_decl:
                if ending[-1] in hushes and d == 'ом':
                    declensions.append(word[:-1] + 'ем')
                elif d == '':
                    declensions.append(word)
                else:
                    declensions.append(word[:-1] + d)
    elif ending == 'ый':
        for d in mn_adj_hard_decl:
            declensions.append(word[:-2] + d)
    elif ending == 'ий':
        if word[-3] in hushes + 'н':
            for d in mn_adj_soft_decl:
                declensions.append(word[:-2] + d)
        else:
            for d in mn_adj_hard_decl:
                if word[-3] in hushes + velars and d == 'ым':
                    declensions.append(word[:-2] + 'им')
                elif word[-3] in hushes + velars and d == 'ый':
                    declensions.append(word[:-2] + 'ий')
                else:
                    declensions.append(word[:-2] + d)
    elif ending == 'ая':
        for d in fem_adj_decl:
            if word[-3] in hushes and d == 'ой':
                declensions.append(word[:-2] + 'ей')
            else:
                declensions.append(word[:-2] + d)
    elif ending == 'ее':
        for d in mn_adj_soft_decl:
            if d == 'ий':
                declensions.append(word)
            else:
                declensions.append(word[:-2] + d)
    elif ending == 'ое':
        for d in mn_adj_hard_decl:
                if word[-3] in hushes + velars and d == 'ым':
                    declensions.append(word[:-2] + 'им')
                elif d == 'ый':
                    declensions.append(word)
                else:
                    declensions.append(word[:-2] + d)
    elif ending == 'ь':
        mf = input('Is ' + word +' m or f? (m/f): ')
        if mf == 'f':
            declensions.append(word)
            declensions.append(word[:-1] + 'и')
            declensions.append(word[:-1] + 'и')
            declensions.append(word[:-1] + 'ью')
            declensions.append(word[:-1] + 'и')
        else:
            for d in mn_soft_decl:
                if word[-2] in hushes + velars and d == 'я':
                    declensions.append(word[:-1] + 'а')
                elif word[-2] in hushes + velars and d == 'ю':
                    declensions.append(word[:-1] + 'у')
                elif d == 'й':
                    declensions.append(word)
                else:
                    declensions.append(word[:-1] + d)
           
    return declensions             
        