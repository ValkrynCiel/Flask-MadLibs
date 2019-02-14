"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started



story1 = Story(["place", "noun", "verb", "adjective", "plural_noun"], """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.""") 

story2 = Story(["noun", "adjective", "location", "verb", "plural_noun"], """ Once upon a {noun}, a {adjective} panda wandered to {location}. I love to {verb} good {plural_noun}.""")

story3 = Story(["adjective", "verb", "plural_nouns", "adverb", "noun", "verb2"], """ There was once a {adjective} dog that liked to {verb} {plural_nouns}. It did not like to {adverb} chase after the {noun} that {verb2} all day.""")

story = story3
