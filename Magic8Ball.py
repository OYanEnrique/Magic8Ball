#Magic8Ball by Yan Enrique

from random import choice

answers=['Yeah, that is great!','Hmm...I do not think so!', 'No, that is horrible!', 'I do not want to answer that!', 'Yes!', 'No!', 'Maybe', 'Ask something else, please!', 'Do not speak to me!', 'You are so annoying...', '...', 'If it makes you happy, yes!', 'If it makes you happy, no!', 'If it makes you unhappy, yes!', 'If it makes you unhappy, no!', 'No...eww', 'No, that is suspicious, that is weird']

final_answer=choice(answers)

question=str(input('Please make a Yes or No question!\n')).lower()

print(final_answer)