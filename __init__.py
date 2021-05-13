from mycroft import MycroftSkill, intent_file_handler


class WelcomePerson(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('person.welcome.intent')
    def handle_person_welcome(self, message):
        self.speak_dialog('person.welcome')


def create_skill():
    return WelcomePerson()

