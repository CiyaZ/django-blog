from django import template
import hashlib


class Gravatar(template.Node):
    def __init__(self, email):
        self.email = template.Variable(email)

    def render(self, context):
        email = self.email.resolve(context)
        avatar_size = 60
        return 'https://s.gravatar.com/avatar/' + \
               hashlib.md5(email.lower().encode('utf8')).hexdigest() + \
               '?s=' + str(avatar_size)


register = template.Library()


@register.tag
def gravatar(parser, token):
    tag_name, email = token.split_contents()
    return Gravatar(email)
