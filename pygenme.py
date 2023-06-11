import genanki

def create_anki_deck(phrases):
    # Define the Anki deck model
    deck_model = genanki.Model(
        1607392319,
        'Phrases Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    # Create the Anki deck
    deck = genanki.Deck(
        2059400110,
        'Phrases Deck')

    # Add cards to the deck
    for phrase in phrases:
        if ':' not in phrase:
            continue
        question, answer = phrase.strip().split(':', 1)
        question = question.strip() + "?"
        answer = answer.strip()
        note = genanki.Note(
            model=deck_model,
            fields=[question, answer]
        )
        deck.add_note(note)

    # Create the Anki package and export the deck
    package = genanki.Package(deck)
    package.write_to_file('phrases.apkg')

# Read phrases from the text file
with open('phrases.txt', 'r', encoding='utf-8') as file:
    phrases = file.read().split('\n\n')

# Create Anki deck
create_anki_deck(phrases)
