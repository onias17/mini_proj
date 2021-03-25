import random

def precept():
    categories = {
        'marriage': [
            
        ],
        'love': [
            '1 John 5\n3. For this is the love of God, that we keep his commandments: and his commandments are not grievous.',
        ]
    }
    
    precept = input("Chose a category:\n")

    for prophets in categories:
        print(prophets)

def marriage():
    precepts = [
        'Hebrews 13\n4. Marriage is honourable in all, and the bed undefiled: but whoremongers and adulterers God will judge.', 
        'Exodus 21\n10. If he take him another wife; her food, her rainment, and her duty of marriage, shall he not diminish.'
    ]

print(precept())

