favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set() does not output repeated collection elements.
    print(language.title())