from django.db import models
import core.personality as p


# Create your models here.
class Note(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    personality = models.TextField()

#   A string representation of just the body of the Note object
    def __str__(self):
        return self.body

#   My official representation of the object with body and personality
    def __repr__(self):
        return " Text: {}, HELLO: {}".format(self.body, self.personality)

#   Gets the description of the personality type of the Note object
    def get_description(self):
        mb = self.personality
        mbti = {'INTJ': ('Architect: Imaginative and strategic thinkers, ' +
                         'with a plan for everything'),
                'INTP': ('Logician: Innovative inventors with an ' +
                         'unquenchable thirst for knowledge'),
                'ENTJ': ('Commander: Bold, imaginative and strong-willed ' +
                         'leaders, always finding a way – or making one'),
                'ENTP': ('Debater: Smart and curious thinkers who cannot ' +
                         'resist an intellectual challenge'),
                'INFJ': ('Advocate: Quiet and Mystical, yet very inspiring ' +
                         'and tireless idealists'),
                'INFP': ('Mediator: Poetic, kind, altruistic. Always eager' +
                         'to help a good cause'),
                'ENFJ': ('Protagonist: Charismatic and inspiring leaders, ' +
                         'able to mesmerize their listeners'),
                'ENFP': ('Campaigner: Enthusiastic, creative, and sociable' +
                         ' free spirits; can always find a reason to smile'),
                'ISTJ': ('Logistician: Practical and fact-minded individuals' +
                         ' whose reliability cannot be doubted'),
                'ISFJ': ('Defender: Very dedicated and warm protectors, ' +
                         'always ready to defend their loved ones'),
                'ESTJ': ('Executive: Excellent administrators, unsurpassed ' +
                         'at managing things or people'),
                'ESFJ': ('Consul: Extraordinarily caring, social and popular' +
                         ' people, always eager to help'),
                'ISTP': ('Bold and practical experimenters, masters of all ' +
                         'kinds of tools'),
                'ISFP': ('Adventurer: Flexible and charming artists, always ' +
                         ' ready to explore and experience something new'),
                'ESTP': ('Entreprenuer: Smart, energetic and very perceptive' +
                         ' people, who truly enjoy living on the edge'),
                'ESFP': ('Entertainer: Spontaneous, energetic and enthusiastic'
                         + ' people – life is never boring around them.')}
        return mbti.get(mb)
