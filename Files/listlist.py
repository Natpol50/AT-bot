import discord

langues = { 
'🇧🇬': 'BG',     # Bulgaria (Bulgarian)
'🇨🇳': 'ZH',  # China (Simplified Chinese)
'🇲🇴': 'ZH',  # Macao SAR China (Simplified Chinese)
'🇨🇿': 'CS',     # Czech Republic (Czech)
'🇩🇰': 'DA',     # Denmark (Danish)
'🇬🇱': 'DA',     # Greenland (Danish)
'🇳🇱': 'NL',     # Netherlands (Dutch)
'🇧🇶': 'NL',     # Caribbean Netherlands (Dutch)
'🇨🇼': 'NL',     # Curaçao (Dutch)
'🇦🇼': 'NL',     # Aruba (Dutch)
'🇸🇷': 'NL',     # Suriname (Dutch)
'🇺🇸': 'EN-US',     # United States (English)
'🇬🇧': 'EN-GB',     # United Kingdom (English)
'🇪🇪': 'ET',     # Estonia (Estonian)
'🇫🇮': 'FI',     # Finland (Finnish)
'🇫🇷': 'FR',     # France (French)
'🇩🇪': 'DE',     # Germany (German)
'🇦🇹': 'DE',     # Austria (German)
'🇱🇮': 'DE',     # Liechtenstein (German)
'🇬🇷': 'EL',     # Greece (Greek)
'🇨🇾': 'EL',     # Cyprus (Greek)
'🇭🇺': 'HU',     # Hungary (Hungarian)
'🇮🇩': 'ID',     # Indonesia (Indonesian)
'🇮🇹': 'IT',     # Italy (Italian)
'🇸🇲': 'IT',     # San Marino (Italian)
'🇯🇵': 'JA',     # Japan (Japanese)
'🇰🇷': 'KO',     # South Korea (Korean)
'🇰🇵': 'KO',     # North Korea (Korean)
'🇱🇻': 'LV',     # Latvia (Latvian)
'🇦🇬': 'EN-US',     # Antigua & Barbuda (English)
'🇦🇮': 'EN-US',     # Anguilla (English)
'🇦🇺': 'EN-US',     # Australia (English)
'🇦🇸': 'EN-US',     # American Samoa (English)
'🇦🇽': 'EN-US',     # Ascension Island (English)
'🇧🇧': 'EN-US',     # Barbados (English)
'🇧🇲': 'EN-US',     # Bermuda (English)
'🇧🇸': 'EN-US',     # Bahamas (English)
'🇧🇼': 'EN-US',     # Botswana (English)
'🇧🇿': 'EN-US',     # Belize (English)
'🇨🇦': 'EN-US',     # Canada (English)
'🇨🇰': 'EN-US',     # Cook Islands (English)
'🇩🇲': 'EN-US',     # Dominica (English)
'🇫🇯': 'EN-US',     # Fiji (English)
'🇬🇩': 'EN-US',     # Grenada (English)
'🇬🇬': 'EN-US',     # Guernsey (English)
'🇬🇭': 'EN-US',     # Ghana (English)
'🇬🇲': 'EN-US',     # Gambia (English)
'🇬🇸': 'EN-US',     # South Georgia & South Sandwich Islands (English)
'🇬🇾': 'EN-US',     # Guyana (English)
'🇮🇪': 'EN-US',     # Ireland (English)
'🇮🇲': 'EN-US',     # Isle of Man (English)
'🇯🇪': 'EN-US',     # Jersey (English)
'🇯🇲': 'EN-US',     # Jamaica (English)
'🇰🇮': 'EN-US',     # Kiribati (English)
'🇰🇳': 'EN-US',     # St. Kitts & Nevis (English)
'🇰🇾': 'EN-US',     # Cayman Islands (English)
'🇱🇨': 'EN-US',     # St. Lucia (English)
'🇱🇷': 'EN-US',     # Liberia (English)
'🇱🇸': 'EN-US',     # Lesotho (English)
'🇲🇭': 'EN-US',     # Marshall Islands (English)
'🇲🇸': 'EN-US',     # Montserrat (English)
'🇲🇺': 'EN-US',     # Mauritius (English)
'🇲🇼': 'EN-US',     # Malawi (English)
'🇳🇦': 'EN-US',     # Namibia (English)
'🇳🇫': 'EN-US',     # Norfolk Island (English)
'🇳🇬': 'EN-US',     # Nigeria (English)
'🇳🇺': 'EN-US',     # Niue (English)
'🇳🇿': 'EN-US',     # New Zealand (English)
'🇵🇬': 'EN-US',     # Papua New Guinea (English)
'🇵🇭': 'EN-US',     # Philippines (English)
'🇵🇳': 'EN-US',     # Pitcairn Islands (English)
'🇵🇼': 'EN-US',     # Palau (English)
'🇸🇧': 'EN-US',     # Solomon Islands (English)
'🇸🇬': 'EN-US',     # Singapore (English)
'🇸🇭': 'EN-US',     # St. Helena (English)
'🇸🇯': 'EN-US',     # Svalbard & Jan Mayen (English)
'🇸🇱': 'EN-US',     # Sierra Leone (English)
'🇸🇸': 'EN-US',     # South Sudan (English)
'🇸🇿': 'EN-US',     # Eswatini (English)
'🇹🇹': 'EN-US',     # Trinidad & Tobago (English)
'🇹🇻': 'EN-US',     # Tuvalu (English)
'🇺🇬': 'EN-US',     # Uganda (English)
'🇺🇲': 'EN-US',     # U.S. Outlying Islands (English)
'🇻🇨': 'EN-US',     # St. Vincent & Grenadines (English)
'🇻🇬': 'EN-US',     # British Virgin Islands (English)
'🇻🇮': 'EN-US',     # U.S. Virgin Islands (English)
'🇿🇼': 'EN-US',     # Zimbabwe (English)
'🇿🇲': 'EN-US',     # Zambia (English)
'🇧🇫': 'FR',     # Burkina Faso (French)
'🇧🇮': 'FR',     # Burundi (French)
'🇧🇯': 'FR',     # Benin (French)
'🇨🇨': 'FR',     # Cocos (Keeling) Islands (French)
'🇨🇩': 'FR',     # Congo - Kinshasa (French)
'🇨🇫': 'FR',     # Central African Republic (French)
'🇨🇬': 'FR',     # Congo - Brazzaville (French)
'🇨🇮': 'FR',     # Côte d'Ivoire (French)
'🇨🇲': 'FR',     # Cameroon (French)
'🇨🇵': 'FR',     # Clipperton Island (French)
'🇩🇯': 'FR',     # Djibouti (French)
'🇫🇰': 'FR',     # Falkland Islands (French)
'🇬🇦': 'FR',     # Gabon (French)
'🇬🇫': 'FR',     # French Guiana (French)
'🇬🇳': 'FR',     # Guinea (French)
'🇬🇵': 'FR',     # Guadeloupe (French)
'🇭🇲': 'FR',     # Heard & McDonald Islands (French)
'🇲🇨': 'FR',     # Monaco (French)
'🇲🇫': 'FR',     # St. Martin (French)
'🇲🇱': 'FR',     # Mali (French)
'🇲🇶': 'FR',     # Martinique (French)
'🇳🇨': 'FR',     # New Caledonia (French)
'🇳🇪': 'FR',     # Niger (French)
'🇵🇫': 'FR',     # French Polynesia (French)
'🇵🇲': 'FR',     # St. Pierre & Miquelon (French)
'🇷🇪': 'FR',     # Réunion (French)
'🇸🇨': 'FR',     # Seychelles (French)
'🇸🇳': 'FR',     # Senegal (French)
'🇹🇨': 'FR',     # Turks & Caicos Islands (French)
'🇹🇩': 'FR',     # Chad (French)
'🇹🇫': 'FR',     # French Southern Territories (French)
'🇹🇬': 'FR',     # Togo (French)
'🇻🇺': 'FR',     # Vanuatu (French)
'🇼🇫': 'FR',     # Wallis & Futuna (French)
'🇾🇹': 'FR',     # Mayotte (French)
'🇧🇪': 'X',     # Belgium (Not defined)
'🇨🇭': 'X',     # Switzerland (Not defined)
'🇱🇹': 'LT',     # Lithuania (Lithuanian)
'🇧🇻': 'NB',     # Bouvet Island (Norwegian)
'🇳🇴': 'NB',     # Norway (Norwegian)
'🇵🇱': 'PL',     # Poland (Polish)
'🇦🇴': 'PT-PT',     # Angola (Portuguese)
'🇧🇷': 'PT-BR',     # Brazil (Portuguese/Brazilian)
'🇨🇻': 'PT-PT',     # Cape Verde (Portuguese)
'🇬🇼': 'PT-PT',     # Guinea-Bissau (Portuguese)
'🇲🇿': 'PT-PT',     # Mozambique (Portuguese)
'🇵🇹': 'PT-PT',     # Portugal (Portuguese)
'🇸🇹': 'PT-PT',     # São Tomé & Príncipe (Portuguese)
'🇹🇱': 'PT-PT',     # Timor-Leste (Portuguese)
'🇲🇩': 'RO',     # Moldova (Romanian)
'🇷🇴': 'RO',     # Romania (Romanian)
'🇷🇺': 'RU',     # Russia (Russian)
'🇸🇰': 'SK',     # Slovakia (Slovak)
'🇸🇮': 'SL',     # Slovenia (Slovenian)
'🇦🇷': 'ES',     # Argentina (Spanish)
'🇧🇴': 'ES',     # Bolivia (Spanish)
'🇨🇱': 'ES',     # Chile (Spanish)
'🇨🇴': 'ES',     # Colombia (Spanish)
'🇨🇷': 'ES',     # Costa Rica (Spanish)
'🇨🇺': 'ES',     # Cuba (Spanish)
'🇩🇴': 'ES',     # Dominican Republic (Spanish)
'🇪🇦': 'ES',     # Ceuta & Melilla (Spanish)
'🇪🇨': 'ES',     # Ecuador (Spanish)
'🇪🇸': 'ES',     # Spain (Spanish)
'🇬🇶': 'ES',     # Equatorial Guinea (Spanish)
'🇬🇹': 'ES',     # Guatemala (Spanish)
'🇭🇳': 'ES',     # Honduras (Spanish)
'🇮🇨': 'ES',     # Canary Islands (Spanish)
'🇲🇽': 'ES',     # Mexico (Spanish)
'🇳🇮': 'ES',     # Nicaragua (Spanish)
'🇵🇦': 'ES',     # Panama (Spanish)
'🇵🇪': 'ES',     # Peru (Spanish)
'🇵🇷': 'ES',     # Puerto Rico (Spanish)
'🇵🇾': 'ES',     # Paraguay (Spanish)
'🇸🇻': 'ES',     # El Salvador (Spanish)
'🇺🇾': 'ES',     # Uruguay (Spanish)
'🇻🇪': 'ES',     # Venezuela (Spanish)
'🇸🇪': 'SV',     # Sweden (Swedish)
'🇹🇷': 'TR',     # Turkey (Turkish)
'🇺🇦': 'UK'     # Ukraine (Ukrainian)
}
Deepl_language_dict = {
    'BG': 'Bulgarian',
    'ZH': 'Simplified Chinese (China)',
    'CS': 'Czech (Czech Republic)',
    'DA': 'Danish (Denmark)',
    'NL': 'Dutch (Netherlands)',
    'EN-US': 'English (United States)',
    'EN-GB': 'English (United Kingdom)',
    'ET': 'Estonian (Estonia)',
    'FI': 'Finnish (Finland)',
    'FR': 'French (France)',
    'DE': 'German (Germany)',
    'EL': 'Greek (Greece)',
    'HU': 'Hungarian (Hungary)',
    'ID': 'Indonesian (Indonesia)',
    'IT': 'Italian (Italy)',
    'JA': 'Japanese (Japan)',
    'KO': 'Korean (South Korea)',
    'LV': 'Latvian (Latvia)',
    'LT': 'Lithuanian (Lithuania)',
    'NB': 'Norwegian Bokmål (Norway)',
    'PL': 'Polish (Poland)',
    'PT-PT': 'Portuguese',
    'ptbr': 'Portuguese (Brazil)',
    'RO': 'Romanian (Romania)',
    'RU': 'Russian (Russia)',
    'SK': 'Slovak (Slovakia)',
    'SL': 'Slovenian (Slovenia)',
    'ES': 'Spanish',
    'SV': 'Swedish (Sweden)',
    'TR': 'Turkish (Turkey)',
    'UK': 'Ukrainian (Ukraine)',
    'X': 'Not defined'
}
Deepl_language_dict_inverted = {
"Bulgarian": "BG",  
"Simplified Chinese (China)": "ZH",
"Czech (Czech Republic)": "CS",
"Danish (Denmark)": "DA",
"Dutch (Netherlands)": "NL",
"English (United States)": "EN-US",
"English (United Kingdom)": "EN-GB",
"Estonian (Estonia)": "ET",
"Finnish (Finland)": "FI",
"French (France)": "FR",
"German (Germany)": "DE",
"Greek (Greece)": "EL",
"Hungarian (Hungary)": "HU",
"Indonesian (Indonesia)": "ID",
"Italian (Italy)": "IT",
"Japanese (Japan)": "JA",
"Korean (South Korea)": "KO",
"Latvian (Latvia)": "LV",
"Lithuanian (Lithuania)": "LT",
"Norwegian Bokmål (Norway)": "NB",
"Polish (Poland)": "PL",
"Portuguese": "PT-PT",
"Portuguese (Brazil)": "PT-BR",
"Romanian (Romania)": "RO",
"Russian (Russia)": "RU",
"Slovak (Slovakia)": "SK",
"Slovenian (Slovenia)": "SL",
"Spanish": "ES",
"Swedish (Sweden)": "SV",
"Turkish (Turkey)": "TR",
"Ukrainian (Ukraine)": "UK",
}
Google_language_dict = {
        '🇦🇩': 'ca',     # Andorra (Catalan)
        '🇦🇪': 'ar',     # United Arab Emirates (Arabic)
        '🇦🇫': 'fa',     # Afghanistan (Dari and Pashto)
        '🇦🇬': 'en',     # Antigua & Barbuda (English)
        '🇦🇮': 'en',     # Anguilla (English)
        '🇦🇱': 'sq',     # Albania (Albanian)
        '🇦🇲': 'hy',     # Armenia (Armenian)
        '🇦🇴': 'pt',     # Angola (Portuguese)
        '🇦🇷': 'es',     # Argentina (Spanish)
        '🇦🇸': 'en',     # American Samoa (English)
        '🇦🇹': 'de',     # Austria (German)
        '🇦🇺': 'en',     # Australia (English)
        '🇦🇼': 'nl',     # Aruba (Dutch)
        '🇦🇽': 'en',     # Ascension Island (English)
        '🇦🇿': 'az',     # Azerbaijan (Azerbaijani)
        '🇧🇦': 'bs',     # Bosnia & Herzegovina (Bosnian, Croatian, Serbian)
        '🇧🇧': 'en',     # Barbados (English)
        '🇧🇩': 'bn',     # Bangladesh (Bengali)
        '🇧🇪': 'nl',     # Belgium (Dutch, French, German)
        '🇧🇫': 'fr',     # Burkina Faso (French)
        '🇧🇬': 'bg',     # Bulgaria (Bulgarian)
        '🇧🇭': 'ar',     # Bahrain (Arabic)
        '🇧🇮': 'fr',     # Burundi (French)
        '🇧🇯': 'fr',     # Benin (French)
        '🇧🇲': 'en',     # Bermuda (English)
        '🇧🇳': 'ms',     # Brunei (Malay)
        '🇧🇴': 'es',     # Bolivia (Spanish)
        '🇧🇶': 'nl',     # Caribbean Netherlands (Dutch)
        '🇧🇷': 'pt',     # Brazil (Portuguese)
        '🇧🇸': 'en',     # Bahamas (English)
        '🇧🇹': 'dz',     # Bhutan (Dzongkha)
        '🇧🇻': 'no',     # Bouvet Island (Norwegian)
        '🇧🇼': 'en',     # Botswana (English)
        '🇧🇾': 'be',     # Belarus (Belarusian)
        '🇧🇿': 'en',     # Belize (English)
        '🇨🇦': 'en',     # Canada (English)
        '🇨🇨': 'fr',     # Cocos (Keeling) Islands (French)
        '🇨🇩': 'fr',     # Congo - Kinshasa (French)
        '🇨🇫': 'fr',     # Central African Republic (French)
        '🇨🇬': 'fr',     # Congo - Brazzaville (French)
        '🇨🇭': 'de',     # Switzerland (German, French, Italian, Romansh)
        '🇨🇮': 'fr',     # Côte d'Ivoire (French)
        '🇨🇰': 'en',     # Cook Islands (English)
        '🇨🇱': 'es',     # Chile (Spanish)
        '🇨🇲': 'fr',     # Cameroon (French)
        '🇨🇳': 'zh-CN',  # China (Simplified Chinese)
        '🇨🇴': 'es',     # Colombia (Spanish)
        '🇨🇵': 'fr',     # Clipperton Island (French)
        '🇨🇷': 'es',     # Costa Rica (Spanish)
        '🇨🇺': 'es',     # Cuba (Spanish)
        '🇨🇻': 'pt',     # Cape Verde (Portuguese)
        '🇨🇼': 'nl',     # Curaçao (Dutch)
        '🇨🇾': 'el',     # Cyprus (Greek)
        '🇨🇿': 'cs',     # Czech Republic (Czech)
        '🇩🇪': 'de',     # Germany (German)
        '🇩🇯': 'fr',     # Djibouti (French)
        '🇩🇰': 'da',     # Denmark (Danish)
        '🇩🇲': 'en',     # Dominica (English)
        '🇩🇴': 'es',     # Dominican Republic (Spanish)
        '🇩🇿': 'ar',     # Algeria (Arabic)
        '🇪🇦': 'es',     # Ceuta & Melilla (Spanish)
        '🇪🇨': 'es',     # Ecuador (Spanish)
        '🇪🇪': 'et',     # Estonia (Estonian)
        '🇪🇬': 'ar',     # Egypt (Arabic)
        '🇪🇭': 'ar',     # Western Sahara (Arabic)
        '🇪🇷': 'ti',     # Eritrea (Tigrinya)
        '🇪🇸': 'es',     # Spain (Spanish)
        '🇪🇹': 'am',     # Ethiopia (Amharic)
        '🇫🇮': 'fi',     # Finland (Finnish)
        '🇫🇯': 'en',     # Fiji (English)
        '🇫🇰': 'fr',     # Falkland Islands (French)
        '🇫🇲': 'en',     # Micronesia (English)
        '🇫🇴': 'fo',     # Faroe Islands (Faroese)
        '🇫🇷': 'fr',     # France (French)
        '🇬🇦': 'fr',     # Gabon (French)
        '🇬🇧': 'en',     # United Kingdom (English)
        '🇬🇩': 'en',     # Grenada (English)
        '🇬🇪': 'ka',     # Georgia (Georgian)
        '🇬🇫': 'fr',     # French Guiana (French)
        '🇬🇬': 'en',     # Guernsey (English)
        '🇬🇭': 'en',     # Ghana (English)
        '🇬🇮': 'en',     # Gibraltar (English)
        '🇬🇱': 'da',     # Greenland (Danish)
        '🇬🇲': 'en',     # Gambia (English)
        '🇬🇳': 'fr',     # Guinea (French)
        '🇬🇵': 'fr',     # Guadeloupe (French)
        '🇬🇶': 'es',     # Equatorial Guinea (Spanish)
        '🇬🇷': 'el',     # Greece (Greek)
        '🇬🇸': 'en',     # South Georgia & South Sandwich Islands (English)
        '🇬🇹': 'es',     # Guatemala (Spanish)
        '🇬🇺': 'ch',     # Guam (Chamorro)
        '🇬🇼': 'pt',     # Guinea-Bissau (Portuguese)
        '🇬🇾': 'en',     # Guyana (English)
        '🇭🇰': 'zh-HK',  # Hong Kong SAR China (Traditional Chinese)
        '🇭🇲': 'fr',     # Heard & McDonald Islands (French)
        '🇭🇳': 'es',     # Honduras (Spanish)
        '🇭🇷': 'hr',     # Croatia (Croatian)
        '🇭🇹': 'ht',     # Haiti (Haitian Creole)
        '🇭🇺': 'hu',     # Hungary (Hungarian)
        '🇮🇨': 'es',     # Canary Islands (Spanish)
        '🇮🇩': 'id',     # Indonesia (Indonesian)
        '🇮🇪': 'en',     # Ireland (English)
        '🇮🇱': 'he',     # Israel (Hebrew)
        '🇮🇲': 'en',     # Isle of Man (English)
        '🇮🇳': 'hi',     # India (Hindi)
        '🇮🇶': 'ar',     # Iraq (Arabic)
        '🇮🇷': 'fa',     # Iran (Persian)
        '🇮🇸': 'is',     # Iceland (Icelandic)
        '🇮🇹': 'it',     # Italy (Italian)
        '🇯🇪': 'en',     # Jersey (English)
        '🇯🇲': 'en',     # Jamaica (English)
        '🇯🇴': 'ar',     # Jordan (Arabic)
        '🇯🇵': 'ja',     # Japan (Japanese)
        '🇰🇪': 'sw',     # Kenya (Swahili)
        '🇰🇬': 'ky',     # Kyrgyzstan (Kyrgyz)
        '🇰🇭': 'km',     # Cambodia (Khmer)
        '🇰🇮': 'en',     # Kiribati (English)
        '🇰🇲': 'ar',     # Comoros (Arabic)
        '🇰🇳': 'en',     # St. Kitts & Nevis (English)
        '🇰🇵': 'ko',     # North Korea (Korean)
        '🇰🇷': 'ko',     # South Korea (Korean)
        '🇰🇼': 'ar',     # Kuwait (Arabic)
        '🇰🇾': 'en',     # Cayman Islands (English)
        '🇰🇿': 'kk',     # Kazakhstan (Kazakh)
        '🇱🇦': 'lo',     # Laos (Lao)
        '🇱🇧': 'ar',     # Lebanon (Arabic)
        '🇱🇨': 'en',     # St. Lucia (English)
        '🇱🇮': 'de',     # Liechtenstein (German)
        '🇱🇰': 'si',     # Sri Lanka (Sinhala, Tamil)
        '🇱🇷': 'en',     # Liberia (English)
        '🇱🇸': 'en',     # Lesotho (English)
        '🇱🇹': 'lt',     # Lithuania (Lithuanian)
        '🇱🇺': 'lb',     # Luxembourg (Luxembourgish)
        '🇱🇻': 'lv',     # Latvia (Latvian)
        '🇱🇾': 'ar',     # Libya (Arabic)
        '🇲🇦': 'ar',     # Morocco (Arabic)
        '🇲🇨': 'fr',     # Monaco (French)
        '🇲🇩': 'ro',     # Moldova (Moldavian)
        '🇲🇪': 'sr',     # Montenegro (Montenegrin)
        '🇲🇫': 'fr',     # St. Martin (French)
        '🇲🇬': 'mg',     # Madagascar (Malagasy)
        '🇲🇭': 'en',     # Marshall Islands (English)
        '🇲🇰': 'mk',     # North Macedonia (Macedonian)
        '🇲🇱': 'fr',     # Mali (French)
        '🇲🇲': 'my',     # Myanmar (Burmese)
        '🇲🇳': 'mn',     # Mongolia (Mongolian)
        '🇲🇴': 'zh-CN',  # Macao SAR China (Simplified Chinese)
        '🇲🇶': 'fr',     # Martinique (French)
        '🇲🇷': 'ar',     # Mauritania (Arabic)
        '🇲🇸': 'en',     # Montserrat (English)
        '🇲🇹': 'mt',     # Malta (Maltese)
        '🇲🇺': 'en',     # Mauritius (English)
        '🇲🇻': 'dv',     # Maldives (Dhivehi)
        '🇲🇼': 'en',     # Malawi (English)
        '🇲🇽': 'es',     # Mexico (Spanish)
        '🇲🇾': 'ms',     # Malaysia (Malay)
        '🇲🇿': 'pt',     # Mozambique (Portuguese)
        '🇳🇦': 'en',     # Namibia (English)
        '🇳🇨': 'fr',     # New Caledonia (French)
        '🇳🇪': 'fr',     # Niger (French)
        '🇳🇫': 'en',     # Norfolk Island (English)
        '🇳🇬': 'en',     # Nigeria (English)
        '🇳🇮': 'es',     # Nicaragua (Spanish)
        '🇳🇱': 'nl',     # Netherlands (Dutch)
        '🇳🇴': 'no',     # Norway (Norwegian)
        '🇳🇵': 'ne',     # Nepal (Nepali)
        '🇳🇺': 'en',     # Niue (English)
        '🇳🇿': 'en',     # New Zealand (English)
        '🇴🇲': 'ar',     # Oman (Arabic)
        '🇵🇦': 'es',     # Panama (Spanish)
        '🇵🇪': 'es',     # Peru (Spanish)
        '🇵🇫': 'fr',     # French Polynesia (French)
        '🇵🇬': 'en',     # Papua New Guinea (English)
        '🇵🇭': 'en',     # Philippines (English)
        '🇵🇰': 'ur',     # Pakistan (Urdu)
        '🇵🇱': 'pl',     # Poland (Polish)
        '🇵🇲': 'fr',     # St. Pierre & Miquelon (French)
        '🇵🇳': 'en',     # Pitcairn Islands (English)
        '🇵🇷': 'es',     # Puerto Rico (Spanish)
        '🇵🇸': 'ar',     # Palestinian Territories (Arabic)
        '🇵🇹': 'pt',     # Portugal (Portuguese)
        '🇵🇼': 'en',     # Palau (English)
        '🇵🇾': 'es',     # Paraguay (Spanish)
        '🇶🇦': 'ar',     # Qatar (Arabic)
        '🇷🇪': 'fr',     # Réunion (French)
        '🇷🇴': 'ro',     # Romania (Romanian)
        '🇷🇸': 'sr',     # Serbia (Serbian)
        '🇷🇺': 'ru',     # Russia (Russian)
        '🇷🇼': 'rw',     # Rwanda (Kinyarwanda, French, English)
        '🇸🇦': 'ar',     # Saudi Arabia (Arabic)
        '🇸🇧': 'en',     # Solomon Islands (English)
        '🇸🇨': 'fr',     # Seychelles (French)
        '🇸🇩': 'ar',     # Sudan (Arabic)
        '🇸🇪': 'sv',     # Sweden (Swedish)
        '🇸🇬': 'en',     # Singapore (English)
        '🇸🇭': 'en',     # St. Helena (English)
        '🇸🇮': 'sl',     # Slovenia (Slovene)
        '🇸🇯': 'en',     # Svalbard & Jan Mayen (English)
        '🇸🇰': 'sk',     # Slovakia (Slovak)
        '🇸🇱': 'en',     # Sierra Leone (English)
        '🇸🇲': 'it',     # San Marino (Italian)
        '🇸🇳': 'fr',     # Senegal (French)
        '🇸🇴': 'so',     # Somalia (Somali)
        '🇸🇷': 'nl',     # Suriname (Dutch)
        '🇸🇸': 'en',     # South Sudan (English)
        '🇸🇹': 'pt',     # São Tomé & Príncipe (Portuguese)
        '🇸🇻': 'es',     # El Salvador (Spanish)
        '🇸🇾': 'ar',     # Syria (Arabic)
        '🇸🇿': 'en',     # Eswatini (English)
        '🇹🇨': 'fr',     # Turks & Caicos Islands (French)
        '🇹🇩': 'fr',     # Chad (French)
        '🇹🇫': 'fr',     # French Southern Territories (French)
        '🇹🇬': 'fr',     # Togo (French)
        '🇹🇭': 'th',     # Thailand (Thai)
        '🇹🇯': 'tg',     # Tajikistan (Tajik)
        '🇹🇰': 'tk',     # Tokelau (Tokelauan)
        '🇹🇱': 'pt',     # Timor-Leste (Portuguese)
        '🇹🇲': 'tk',     # Turkmenistan (Turkmen)
        '🇹🇳': 'ar',     # Tunisia (Arabic)
        '🇹🇴': 'to',     # Tonga (Tongan)
        '🇹🇷': 'tr',     # Turkey (Turkish)
        '🇹🇹': 'en',     # Trinidad & Tobago (English)
        '🇹🇻': 'en',     # Tuvalu (English)
        '🇹🇼': 'zh-TW',  # Taiwan (Traditional Chinese)
        '🇹🇿': 'sw',     # Tanzania (Swahili)
        '🇺🇦': 'uk',     # Ukraine (Ukrainian)
        '🇺🇬': 'en',     # Uganda (English)
        '🇺🇲': 'en',     # U.S. Outlying Islands (English)
        '🇺🇸': 'en',     # United States (English)
        '🇺🇾': 'es',     # Uruguay (Spanish)
        '🇺🇿': 'uz',     # Uzbekistan (Uzbek)
        '🇻🇦': 'la',     # Vatican City (Latin)
        '🇻🇨': 'en',     # St. Vincent & Grenadines (English)
        '🇻🇪': 'es',     # Venezuela (Spanish)
        '🇻🇬': 'en',     # British Virgin Islands (English)
        '🇻🇮': 'en',     # U.S. Virgin Islands (English)
        '🇻🇳': 'vi',     # Vietnam (Vietnamese)
        '🇻🇺': 'fr',     # Vanuatu (French)
        '🇼🇫': 'fr',     # Wallis & Futuna (French)
        '🇼🇸': 'sm',     # Samoa (Samoan)
        '🇾🇪': 'ar',     # Yemen (Arabic)
        '🇾🇹': 'fr',     # Mayotte (French)
        '🇿🇦': 'af',     # South Africa (Afrikaans)
        '🇿🇲': 'en',     # Zambia (English)
        '🇿🇼': 'en',     # Zimbabwe (English)
    }
Google_language_dict_inverted = {
    'ca': 'Catalan',
    'ar': 'Arabic',
    'fa': 'Dari and Pashto',
    'en': 'English',
    'sq': 'Albanian',
    'hy': 'Armenian',
    'pt': 'Portuguese',
    'es': 'Spanish',
    'nl': 'Dutch',
    'az': 'Azerbaijani',
    'bs': 'Bosnian, Croatian, Serbian',
    'bn': 'Bengali',
    'bg': 'Bulgarian',
    'ar': 'Arabic',
    'fr': 'French',
    'ms': 'Malay',
    'dz': 'Dzongkha',
    'no': 'Norwegian',
    'fo': 'Faroese',
    'fi': 'Finnish',
    'ka': 'Georgian',
    'el': 'Greek',
    'de': 'German',
    'da': 'Danish',
    'et': 'Estonian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'lo': 'Lao',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'ne': 'Nepali',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'sr': 'Serbian',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovene',
    'so': 'Somali',
    'st': 'Southern Sotho',
    'es': 'Spanish',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tl': 'Tagalog',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'th': 'Thai',
    'bo': 'Tibetan',
    'ti': 'Tigrinya',
    'to': 'Tongan',
    'tr': 'Turkish',
    'tk': 'Turkmen',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'fy': 'Western Frisian',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-CN': 'Chinese (Simplified)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'tk': 'Turkmen',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'fy': 'Western Frisian',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-CN': 'Chinese (Simplified)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'tk': 'Turkmen',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'fy': 'Western Frisian',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-CN': 'Chinese (Simplified)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'tk': 'Turkmen',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'fy': 'Western Frisian',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}
langues_n_gt_invert = {
"Catalan": "ca",  
"Arabic": "ar",
"Persian": "fa",
"English": "en",
"Albanian": "sq",
"Armenian": "hy",
"Portuguese": "pt",
"Spanish": "es",
"Dutch": "nl",
"Azerbaijani": "az",
"Bosnian": "bs",
"Bengali": "bn",
"Bulgarian": "bg",
"French": "fr",
"Malay": "ms",
"Dzongkha": "dz",
"Norwegian": "no",
"Faroese": "fo",
"Finnish": "fi",
"Georgian": "ka",
"Greek": "el",
"German": "de",
"Danish": "da",
"Estonian": "et",
"Hebrew": "iw",
"Hindi": "hi",
"Hungarian": "hu",
"Icelandic": "is",
"Italian": "it",
"Japanese": "ja",
"Korean": "ko",
"Kazakh": "kk",
"Khmer": "km",
"Lao": "lo",
"Latvian": "lv",
"Lithuanian": "lt",
"Luxembourgish": "lb",
"Macedonian": "mk",
"Malagasy": "mg",
"Malayalam": "ml",
"Maltese": "mt",
"Maori": "mi",
"Marathi": "mr",
"Mongolian": "mn",
"Nepali": "ne",
"Pashto": "ps",
"Polish": "pl",
"Punjabi": "pa",
"Romanian": "ro",
"Russian": "ru",
"Samoan": "sm",
"Serbian": "sr",
"Sindhi": "sd",
"Sinhala": "si",
"Slovak": "sk",
"Slovenian": "sl",
"Somali": "so",
"Sesotho": "st",
"Swahili": "sw",
"Swedish": "sv",
"Filipino": "tl",
"Tamil": "ta",
"Tatar": "tt",
"Telugu": "te",
"Thai": "th",
"Tibetan": "bo",
"Tigrinya": "ti",
"Tongan": "to",
"Turkish": "tr",
"Turkmen": "tk",
"Ukrainian": "uk",
"Urdu": "ur",
"Uyghur": "ug",
"Uzbek": "uz",
"Vietnamese": "vi",
"Welsh": "cy",
"Western Frisian": "fy",
"Xhosa": "xh",
"Yiddish": "yi",
"Yoruba": "yo",
"Zulu": "zu",
"Afrikaans": "af",
"Amharic": "am",
"Basque": "eu",
"Belarusian": "be",
"Cebuano": "ceb",
"Chichewa": "ny",
"Chinese (google translate)": "zh-CN",
"Corsican": "co",
"Croatian": "hr",  
"Czech": "cs",
"Esperanto": "eo",
"Galician": "gl",
"Gujarati": "gu",
"Haitian Creole": "ht",
"Hausa": "ha",
"Hawaiian": "haw",
"Hmong": "hmn",
"Igbo": "ig",
"Indonesian": "id",
"Irish": "ga",
"Javanese": "jw",
"Kannada": "kn",
"Kurdish (Kurmanji)": "ku",
"Kyrgyz": "ky",
"Latin": "la",
"Myanmar (Burmese)": "my",
"Scots Gaelic": "gd",
"Shona": "sn",
"Sundanese": "su",
"Tajik": "tg",
}
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

lang_to_flag = {
    "Bulgarian": '🇧🇬',
    "Simplified Chinese (China)": '🇨🇳',
    "Czech (Czech Republic)": '🇨🇿',
    "Danish (Denmark)": '🇩🇰',
    "Dutch (Netherlands)": '🇳🇱',
    "English (United States)": '🇺🇸',
    "English (United Kingdom)": '🇬🇧',
    "Estonian (Estonia)": '🇪🇪',
    "Finnish (Finland)": '🇫🇮',
    "French (France)": '🇫🇷',
    "German (Germany)": '🇩🇪',
    "Greek (Greece)": '🇬🇷',
    "Hungarian (Hungary)": '🇭🇺',
    "Indonesian (Indonesia)": '🇮🇩',
    "Italian (Italy)": '🇮🇹',
    "Japanese (Japan)": '🇯🇵',
    "Korean (South Korea)": '🇰🇷',
    "Latvian (Latvia)": '🇱🇻',
    "Lithuanian (Lithuania)": '🇱🇹',
    "Norwegian Bokmål (Norway)": '🇳🇴',
    "Polish (Poland)": '🇵🇱',
    "Portuguese": '🇵🇹',
    "Portuguese (Brazil)": '🇧🇷',
    "Romanian (Romania)": '🇷🇴',
    "Russian (Russia)": '🇷🇺',
    "Slovak (Slovakia)": '🇸🇰',
    "Slovenian (Slovenia)": '🇸🇮',
    "Spanish": '🇪🇸',
    "Swedish (Sweden)": '🇸🇪',
    "Turkish (Turkey)": '🇹🇷',
    "Ukrainian (Ukraine)": '🇺🇦',
    "Catalan": '🇨🇦',
    "Arabic": '🇸🇦',
    "Persian": '🇮🇷',
    "English": '🇬🇧',
    "Albanian": '🇦🇱',
    "Armenian": '🇦🇲',
    "Dutch": '🇳🇱',
    "Azerbaijani": '🇦🇿',
    "Bosnian": '🇧🇦',
    "Bengali": '🇧🇩',
    "French": '🇫🇷',
    "Malay": '🇲🇾',
    "Dzongkha": '🇧🇹',
    "Norwegian": '🇳🇴',
    "Faroese": '🇫🇴',
    "Finnish": '🇫🇮',
    "Georgian": '🇬🇪',
    "Greek": '🇬🇷',
    "German": '🇩🇪',
    "Danish": '🇩🇰',
    "Estonian": '🇪🇪',
    "Hebrew": '🇮🇱',
    "Hindi": '🇮🇳',
    "Hungarian": '🇭🇺',
    "Icelandic": '🇮🇸',
    "Italian": '🇮🇹',
    "Japanese": '🇯🇵',
    "Korean": '🇰🇷',
    "Kazakh": '🇰🇿',
    "Khmer": '🇰🇭',
    "Lao": '🇱🇦',
    "Latvian": '🇱🇻',
    "Lithuanian": '🇱🇹',
    "Luxembourgish": '🇱🇺',
    "Macedonian": '🇲🇰',
    "Malagasy": '🇲🇬',
    "Malayalam": '🇮🇳',
    "Maltese": '🇲🇹',
    "Maori": '🇳🇿',
    "Marathi": '🇮🇳',
    "Mongolian": '🇲🇳',
    "Nepali": '🇳🇵',
    "Pashto": '🇦🇫',
    "Polish": '🇵🇱',
    "Punjabi": '🇮🇳',
    "Romanian": '🇷🇴',
    "Russian": '🇷🇺',
    "Samoan": '🇼🇸',
    "Serbian": '🇷🇸',
    "Sindhi": '🇵🇰',
    "Sinhala": '🇱🇰',
    "Slovak": '🇸🇰',
    "Slovenian": '🇸🇮',
    "Somali": '🇸🇴',
    "Sesotho": '🇱🇸',
    "Swahili": '🇹🇿',
    "Swedish": '🇸🇪',
    "Filipino": '🇵🇭',
    "Tamil": '🇮🇳',
    "Tatar": '🇷🇺',
    "Telugu": '🇮🇳',
    "Thai": '🇹🇭',
    "Tibetan": '🇨🇳',
    "Tigrinya": '🇪🇷',
    "Tongan": '🇹🇴',
    "Turkish": '🇹🇷',
    "Turkmen": '🇹🇲',
    "Ukrainian": '🇺🇦',
    "Urdu": '🇵🇰',
    "Uyghur": '🇨🇳',
    "Uzbek": '🇺🇿',
    "Vietnamese": '🇻🇳',
    "Welsh": '🏴󠁧󠁢󠁷󠁬󠁳󠁿',
    "Western Frisian": '🇳🇱',
    "Xhosa": '🇿🇦',
    "Yiddish": '🇮🇱',
    "Yoruba": '🇳🇬',
    "Zulu": '🇿🇦',
    "Afrikaans": '🇿🇦',
    "Amharic": '🇪🇹',
    "Basque": '🇪🇸',
    "Belarusian": '🇧🇾',
    "Cebuano": '🇵🇭',
    "Chichewa": '🇲🇼',
    "Chinese (google translate)": '🇨🇳',
    "Corsican": '🇫🇷',
    "Croatian": '🇭🇷',
    "Czech": '🇨🇿',
    "Esperanto": '❓',
    "Galician": '🇪🇸',
    "Gujarati": '🇮🇳',
    "Haitian Creole": '🇭🇹',
    "Hausa": '🇳🇬',
    "Hawaiian": '❓',
    "Hmong": '❓',
    "Igbo": '🇳🇬',
    "Indonesian": '🇮🇩',
    "Irish": '🇮🇪',
    "Javanese": '🇮🇩',
    "Kannada": '🇮🇳',
    "Kurdish (Kurmanji)": '🇭🇺',
    "Kyrgyz": '🇰🇬',
    "Latin": '❓',
    "Myanmar (Burmese)": '🇲🇲',
    "Scots Gaelic": '❓',
    "Shona": '🇿🇼',
    "Sundanese": '🇮🇩',
    "Tajik": '🇹🇯'
}



options =[
discord.SelectOption(label='Bulgarian',emoji='🇧🇬',description='Bulgarian language',default=False),
discord.SelectOption(label='SimplifiedChinese(China)',emoji='🇨🇳',description='SimplifiedChinese(China) language',default=False),
discord.SelectOption(label='Czech(CzechRepublic)',emoji='🇨🇿',description='Czech(CzechRepublic) language',default=False),
discord.SelectOption(label='Danish(Denmark)',emoji='🇩🇰',description='Danish(Denmark) language',default=False),
discord.SelectOption(label='Dutch(Netherlands)',emoji='🇳🇱',description='Dutch(Netherlands) language',default=False),
discord.SelectOption(label='English(UnitedStates)',emoji='🇺🇸',description='English(UnitedStates) language',default=False),
discord.SelectOption(label='English(UnitedKingdom)',emoji='🇬🇧',description='English(UnitedKingdom) language',default=False),
discord.SelectOption(label='Estonian(Estonia)',emoji='🇪🇪',description='Estonian(Estonia) language',default=False),
discord.SelectOption(label='Finnish(Finland)',emoji='🇫🇮',description='Finnish(Finland) language',default=False),
discord.SelectOption(label='French(France)',emoji='🇫🇷',description='French(France) language',default=False),
discord.SelectOption(label='German(Germany)',emoji='🇩🇪',description='German(Germany) language',default=False),
discord.SelectOption(label='Greek(Greece)',emoji='🇬🇷',description='Greek(Greece) language',default=False),
discord.SelectOption(label='Hungarian(Hungary)',emoji='🇭🇺',description='Hungarian(Hungary) language',default=False),
discord.SelectOption(label='Indonesian(Indonesia)',emoji='🇮🇩',description='Indonesian(Indonesia) language',default=False),
discord.SelectOption(label='Italian(Italy)',emoji='🇮🇹',description='Italian(Italy) language',default=False),
discord.SelectOption(label='Japanese(Japan)',emoji='🇯🇵',description='Japanese(Japan) language',default=False),
discord.SelectOption(label='Korean(SouthKorea)',emoji='🇰🇷',description='Korean(SouthKorea) language',default=False),
discord.SelectOption(label='Latvian(Latvia)',emoji='🇱🇻',description='Latvian(Latvia) language',default=False),
discord.SelectOption(label='Lithuanian(Lithuania)',emoji='🇱🇹',description='Lithuanian(Lithuania) language',default=False),
discord.SelectOption(label='NorwegianBokmål(Norway)',emoji='🇳🇴',description='NorwegianBokmål(Norway) language',default=False),
discord.SelectOption(label='Polish(Poland)',emoji='🇵🇱',description='Polish(Poland) language',default=False),
discord.SelectOption(label='Portuguese',emoji='🇵🇹',description='Portuguese language',default=False),
discord.SelectOption(label='Portuguese(Brazil)',emoji='🇧🇷',description='Portuguese(Brazil) language',default=False),
discord.SelectOption(label='Romanian(Romania)',emoji='🇷🇴',description='Romanian(Romania) language',default=False),
discord.SelectOption(label='Russian(Russia)',emoji='🇷🇺',description='Russian(Russia) language',default=False),
discord.SelectOption(label='Slovak(Slovakia)',emoji='🇸🇰',description='Slovak(Slovakia) language',default=False),
discord.SelectOption(label='Slovenian(Slovenia)',emoji='🇸🇮',description='Slovenian(Slovenia) language',default=False),
discord.SelectOption(label='Spanish',emoji='🇪🇸',description='Spanish language',default=False),
discord.SelectOption(label='Swedish(Sweden)',emoji='🇸🇪',description='Swedish(Sweden) language',default=False),
discord.SelectOption(label='Turkish(Turkey)',emoji='🇹🇷',description='Turkish(Turkey) language',default=False),
discord.SelectOption(label='Ukrainian(Ukraine)',emoji='🇺🇦',description='Ukrainian(Ukraine) language',default=False),
discord.SelectOption(label='Catalan',emoji='🇨🇦',description='Catalan language',default=False),
discord.SelectOption(label='Arabic',emoji='🇸🇦',description='Arabic language',default=False),
discord.SelectOption(label='Persian',emoji='🇮🇷',description='Persian language',default=False),
discord.SelectOption(label='English',emoji='🇬🇧',description='English language',default=False),
discord.SelectOption(label='Albanian',emoji='🇦🇱',description='Albanian language',default=False),
discord.SelectOption(label='Armenian',emoji='🇦🇲',description='Armenian language',default=False),
discord.SelectOption(label='Dutch',emoji='🇳🇱',description='Dutch language',default=False),
discord.SelectOption(label='Azerbaijani',emoji='🇦🇿',description='Azerbaijani language',default=False),
discord.SelectOption(label='Bosnian',emoji='🇧🇦',description='Bosnian language',default=False),
discord.SelectOption(label='Bengali',emoji='🇧🇩',description='Bengali language',default=False),
discord.SelectOption(label='French',emoji='🇫🇷',description='French language',default=False),
discord.SelectOption(label='Malay',emoji='🇲🇾',description='Malay language',default=False),
discord.SelectOption(label='Dzongkha',emoji='🇧🇹',description='Dzongkha language',default=False),
discord.SelectOption(label='Norwegian',emoji='🇳🇴',description='Norwegian language',default=False),
discord.SelectOption(label='Faroese',emoji='🇫🇴',description='Faroese language',default=False),
discord.SelectOption(label='Finnish',emoji='🇫🇮',description='Finnish language',default=False),
discord.SelectOption(label='Georgian',emoji='🇬🇪',description='Georgian language',default=False),
discord.SelectOption(label='Greek',emoji='🇬🇷',description='Greek language',default=False),
discord.SelectOption(label='German',emoji='🇩🇪',description='German language',default=False),
discord.SelectOption(label='Danish',emoji='🇩🇰',description='Danish language',default=False),
discord.SelectOption(label='Estonian',emoji='🇪🇪',description='Estonian language',default=False),
discord.SelectOption(label='Hebrew',emoji='🇮🇱',description='Hebrew language',default=False),
discord.SelectOption(label='Hindi',emoji='🇮🇳',description='Hindi language',default=False),
discord.SelectOption(label='Hungarian',emoji='🇭🇺',description='Hungarian language',default=False),
discord.SelectOption(label='Icelandic',emoji='🇮🇸',description='Icelandic language',default=False),
discord.SelectOption(label='Italian',emoji='🇮🇹',description='Italian language',default=False),
discord.SelectOption(label='Japanese',emoji='🇯🇵',description='Japanese language',default=False),
discord.SelectOption(label='Korean',emoji='🇰🇷',description='Korean language',default=False),
discord.SelectOption(label='Kazakh',emoji='🇰🇿',description='Kazakh language',default=False),
discord.SelectOption(label='Khmer',emoji='🇰🇭',description='Khmer language',default=False),
discord.SelectOption(label='Lao',emoji='🇱🇦',description='Lao language',default=False),
discord.SelectOption(label='Latvian',emoji='🇱🇻',description='Latvian language',default=False),
discord.SelectOption(label='Lithuanian',emoji='🇱🇹',description='Lithuanian language',default=False),
discord.SelectOption(label='Luxembourgish',emoji='🇱🇺',description='Luxembourgish language',default=False),
discord.SelectOption(label='Macedonian',emoji='🇲🇰',description='Macedonian language',default=False),
discord.SelectOption(label='Malagasy',emoji='🇲🇬',description='Malagasy language',default=False),
discord.SelectOption(label='Malayalam',emoji='🇮🇳',description='Malayalam language',default=False),
discord.SelectOption(label='Maltese',emoji='🇲🇹',description='Maltese language',default=False),
discord.SelectOption(label='Maori',emoji='🇳🇿',description='Maori language',default=False),
discord.SelectOption(label='Marathi',emoji='🇮🇳',description='Marathi language',default=False),
discord.SelectOption(label='Mongolian',emoji='🇲🇳',description='Mongolian language',default=False),
discord.SelectOption(label='Nepali',emoji='🇳🇵',description='Nepali language',default=False),
discord.SelectOption(label='Pashto',emoji='🇦🇫',description='Pashto language',default=False),
discord.SelectOption(label='Polish',emoji='🇵🇱',description='Polish language',default=False),
discord.SelectOption(label='Punjabi',emoji='🇮🇳',description='Punjabi language',default=False),
discord.SelectOption(label='Romanian',emoji='🇷🇴',description='Romanian language',default=False),
discord.SelectOption(label='Russian',emoji='🇷🇺',description='Russian language',default=False),
discord.SelectOption(label='Samoan',emoji='🇼🇸',description='Samoan language',default=False),
discord.SelectOption(label='Serbian',emoji='🇷🇸',description='Serbian language',default=False),
discord.SelectOption(label='Sindhi',emoji='🇵🇰',description='Sindhi language',default=False),
discord.SelectOption(label='Sinhala',emoji='🇱🇰',description='Sinhala language',default=False),
discord.SelectOption(label='Slovak',emoji='🇸🇰',description='Slovak language',default=False),
discord.SelectOption(label='Slovenian',emoji='🇸🇮',description='Slovenian language',default=False),
discord.SelectOption(label='Somali',emoji='🇸🇴',description='Somali language',default=False),
discord.SelectOption(label='Sesotho',emoji='🇱🇸',description='Sesotho language',default=False),
discord.SelectOption(label='Swahili',emoji='🇹🇿',description='Swahili language',default=False),
discord.SelectOption(label='Swedish',emoji='🇸🇪',description='Swedish language',default=False),
discord.SelectOption(label='Filipino',emoji='🇵🇭',description='Filipino language',default=False),
discord.SelectOption(label='Tamil',emoji='🇮🇳',description='Tamil language',default=False),
discord.SelectOption(label='Tatar',emoji='🇷🇺',description='Tatar language',default=False),
discord.SelectOption(label='Telugu',emoji='🇮🇳',description='Telugu language',default=False),
discord.SelectOption(label='Thai',emoji='🇹🇭',description='Thai language',default=False),
discord.SelectOption(label='Tibetan',emoji='🇨🇳',description='Tibetan language',default=False),
discord.SelectOption(label='Tigrinya',emoji='🇪🇷',description='Tigrinya language',default=False),
discord.SelectOption(label='Tongan',emoji='🇹🇴',description='Tongan language',default=False),
discord.SelectOption(label='Turkish',emoji='🇹🇷',description='Turkish language',default=False),
discord.SelectOption(label='Turkmen',emoji='🇹🇲',description='Turkmen language',default=False),
discord.SelectOption(label='Ukrainian',emoji='🇺🇦',description='Ukrainian language',default=False),
discord.SelectOption(label='Urdu',emoji='🇵🇰',description='Urdu language',default=False),
discord.SelectOption(label='Uyghur',emoji='🇨🇳',description='Uyghur language',default=False),
discord.SelectOption(label='Uzbek',emoji='🇺🇿',description='Uzbek language',default=False),
discord.SelectOption(label='Vietnamese',emoji='🇻🇳',description='Vietnamese language',default=False),
discord.SelectOption(label='Welsh',emoji='🏴󠁧󠁢󠁷󠁬󠁳󠁿',description='Welsh language',default=False),
discord.SelectOption(label='WesternFrisian',emoji='🇳🇱',description='WesternFrisian language',default=False),
discord.SelectOption(label='Xhosa',emoji='🇿🇦',description='Xhosa language',default=False),
discord.SelectOption(label='Yiddish',emoji='🇮🇱',description='Yiddish language',default=False),
discord.SelectOption(label='Yoruba',emoji='🇳🇬',description='Yoruba language',default=False),
discord.SelectOption(label='Zulu',emoji='🇿🇦',description='Zulu language',default=False),
discord.SelectOption(label='Afrikaans',emoji='🇿🇦',description='Afrikaans language',default=False),
discord.SelectOption(label='Amharic',emoji='🇪🇹',description='Amharic language',default=False),
discord.SelectOption(label='Basque',emoji='🇪🇸',description='Basque language',default=False),
discord.SelectOption(label='Belarusian',emoji='🇧🇾',description='Belarusian language',default=False),
discord.SelectOption(label='Cebuano',emoji='🇵🇭',description='Cebuano language',default=False),
discord.SelectOption(label='Chichewa',emoji='🇲🇼',description='Chichewa language',default=False),
discord.SelectOption(label='Chinese(googletranslate)',emoji='🇨🇳',description='Chinese(googletranslate) language',default=False),
discord.SelectOption(label='Corsican',emoji='🇫🇷',description='Corsican language',default=False),
discord.SelectOption(label='Croatian',emoji='🇭🇷',description='Croatian language',default=False),
discord.SelectOption(label='Czech',emoji='🇨🇿',description='Czech language',default=False),
discord.SelectOption(label='Esperanto',emoji='❓',description='Esperanto language',default=False),
discord.SelectOption(label='Galician',emoji='🇪🇸',description='Galician language',default=False),
discord.SelectOption(label='Gujarati',emoji='🇮🇳',description='Gujarati language',default=False),
discord.SelectOption(label='HaitianCreole',emoji='🇭🇹',description='HaitianCreole language',default=False),
discord.SelectOption(label='Hausa',emoji='🇳🇬',description='Hausa language',default=False),
discord.SelectOption(label='Hawaiian',emoji='❓',description='Hawaiian language',default=False),
discord.SelectOption(label='Hmong',emoji='❓',description='Hmong language',default=False),
discord.SelectOption(label='Igbo',emoji='🇳🇬',description='Igbo language',default=False),
discord.SelectOption(label='Indonesian',emoji='🇮🇩',description='Indonesian language',default=False),
discord.SelectOption(label='Irish',emoji='🇮🇪',description='Irish language',default=False),
discord.SelectOption(label='Javanese',emoji='🇮🇩',description='Javanese language',default=False),
discord.SelectOption(label='Kannada',emoji='🇮🇳',description='Kannada language',default=False),
discord.SelectOption(label='Kurdish(Kurmanji)',emoji='🇭🇺',description='Kurdish(Kurmanji) language',default=False),
discord.SelectOption(label='Kyrgyz',emoji='🇰🇬',description='Kyrgyz language',default=False),
discord.SelectOption(label='Latin',emoji='❓',description='Latin language',default=False),
discord.SelectOption(label='Myanmar(Burmese)',emoji='🇲🇲',description='Myanmar(Burmese) language',default=False),
discord.SelectOption(label='ScotsGaelic',emoji='❓',description='ScotsGaelic language',default=False),
discord.SelectOption(label='Shona',emoji='🇿🇼',description='Shona language',default=False),
discord.SelectOption(label='Sundanese',emoji='🇮🇩',description='Sundanese language',default=False),
discord.SelectOption(label='Tajik',emoji='🇹🇯',description='Tajik language', default=False),
]

if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")