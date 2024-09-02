

lang_ch_auto = [
"Bulgarian" ,
"Simplified Chinese (China)" ,
"Czech (Czech Republic)" ,
"Danish (Denmark)" ,
"Dutch (Netherlands)" ,
"English (United States)" ,
"English (United Kingdom)" ,
"Estonian (Estonia)" ,
"Finnish (Finland)" ,
"French (France)" ,
"German (Germany)" ,
"Greek (Greece)" ,
"Hungarian (Hungary)" ,
"Indonesian (Indonesia)" ,
"Italian (Italy)" ,
"Japanese (Japan)" ,
"Korean (South Korea)" ,
"Latvian (Latvia)" ,
"Lithuanian (Lithuania)" ,
"Norwegian Bokmål (Norway)" ,
"Polish (Poland)" ,
"Portuguese" ,
"Portuguese (Brazil)" ,
"Romanian (Romania)" ,
"Russian (Russia)" ,
"Slovak (Slovakia)" ,
"Slovenian (Slovenia)" ,
"Spanish" ,
"Swedish (Sweden)" ,
"Turkish (Turkey)" ,
"Ukrainian (Ukraine)" ,
"Catalan" ,
"Arabic" ,
"Persian" ,
"English" ,
"Albanian" ,
"Armenian" ,
"Dutch" ,
"Azerbaijani" ,
"Bosnian" ,
"Bengali" ,
"French" ,
"Malay" ,
"Dzongkha" ,
"Norwegian" ,
"Faroese" ,
"Finnish" ,
"Georgian" ,
"Greek" ,
"German" ,
"Danish" ,
"Estonian" ,
"Hebrew" ,
"Hindi" ,
"Hungarian" ,
"Icelandic" ,
"Italian" ,
"Japanese" ,
"Korean" ,
"Kazakh" ,
"Khmer" ,
"Lao" ,
"Latvian" ,
"Lithuanian" ,
"Luxembourgish" ,
"Macedonian" ,
"Malagasy" ,
"Malayalam" ,
"Maltese" ,
"Maori" ,
"Marathi" ,
"Mongolian" ,
"Nepali" ,
"Pashto" ,
"Polish" ,
"Punjabi" ,
"Romanian" ,
"Russian" ,
"Samoan" ,
"Serbian" ,
"Sindhi" ,
"Sinhala" ,
"Slovak" ,
"Slovenian" ,
"Somali" ,
"Sesotho" ,
"Swahili" ,
"Swedish" ,
"Filipino" ,
"Tamil" ,
"Tatar" ,
"Telugu" ,
"Thai" ,
"Tibetan" ,
"Tigrinya" ,
"Tongan" ,
"Turkish" ,
"Turkmen" ,
"Ukrainian" ,
"Urdu" ,
"Uyghur" ,
"Uzbek" ,
"Vietnamese" ,
"Welsh" ,
"Western Frisian" ,
"Xhosa" ,
"Yiddish" ,
"Yoruba" ,
"Zulu" ,
"Afrikaans" ,
"Amharic" ,
"Basque" ,
"Belarusian" ,
"Cebuano" ,
"Chichewa" ,
"Chinese (google translate)" ,
"Corsican" ,
"Croatian" ,
"Czech" ,
"Esperanto" ,
"Galician" ,
"Gujarati" ,
"Haitian Creole" ,
"Hausa" ,
"Hawaiian" ,
"Hmong" ,
"Igbo" ,
"Indonesian" ,
"Irish" ,
"Javanese" ,
"Kannada" ,
"Kurdish (Kurmanji)" ,
"Kyrgyz" ,
"Latin" ,
"Myanmar (Burmese)" ,
"Scots Gaelic" ,
"Shona" ,
"Sundanese" ,
"Tajik"
]

def Langs ():
    
    options = []

    # Loop through the original list and create SelectOption objects
    for language in lang_ch_auto:
    # Assuming you want to use the first two characters of the language name as the emoji
        emoji = lang_to_flag[language]
        label = language
        description = f'{language} language'
    
    # Create the SelectOption and append it to the options list
        option = f'discord.SelectOption(label=\'{label}\', emoji=\'{emoji}\', description=\'{description}\', default=False)'
        options.append(option)
    return options


options = Langs()
print('options = ['.strip('"\''))
for i in options : 
    print(i.strip('"\'') + ',')
print(']'.strip('"\''))
input()