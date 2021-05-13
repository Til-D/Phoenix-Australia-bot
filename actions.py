from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class PTSDHelperAction(Action):

    def name(self) -> str:
        return "action_ptsd_helper"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
        question = tracker.get_slot('question')
        age = tracker.get_slot('age')
        gender = tracker.get_slot('gender')
        aboriginal_people = tracker.get_slot('aboriginal_people')
        disater = tracker.get_slot('disater')
        military = tracker.get_slot('military')
        emergency = tracker.get_slot('emergency')
        vehicle_accident = tracker.get_slot('vehicle_accident')
        sexual_assault = tracker.get_slot('sexual_assault')
        terrorism = tracker.get_slot('terrorism')
        victim_crime = tracker.get_slot('victim_crime')
        victim_violence = tracker.get_slot('victim_violence')
        refugees = tracker.get_slot('refugees')
        scores = float(tracker.get_slot('scores'))
        email = tracker.get_slot('email')

        print('Current Question: ' + question)
        print('Latest_message: ')
        print(tracker.latest_message)
        print(
            '----------------------------------------------------------------------------')
        latest_message = tracker.latest_message['intent']['name']
        buttons = [
            {
                "title": "yes",
                "payload": "yes"
            },
            {
                "title": "no",
                "payload": "no"
            },
        ]
        if question == '':
            dispatcher.utter_message(
                text="Have you known about PTSD?", buttons=buttons)
            return [SlotSet('question', 'q_know_ptsd')]
        elif question == 'q_know_ptsd':
            if latest_message == 'affirm':
                dispatcher.utter_message(
                    text="So do you think you may be experiencing PTSD?", buttons=buttons)
                return [SlotSet('question', 'q_experience_ptsd')]
            elif latest_message == 'deny':
                dispatcher.utter_message(
                    text="PTSD is a chronic psychiatric disorder accompanying by stressful and anxiety feelings, which are caused by non-forgotten bad memories.")
                dispatcher.utter_message(
                    text="So do you think you may be experiencing PTSD?", buttons=buttons)
                return [SlotSet('question', 'q_experience_ptsd')]
        elif question == 'q_experience_ptsd':
            if latest_message == 'affirm':
                dispatcher.utter_message(
                    text="I'm going to ask you only a few questions, wihch helps you to know yourself better.", buttons=buttons)  # ask if user wants a test
                return [SlotSet('question', 'q_yourself_ptsd')]
            elif latest_message == 'deny':
                dispatcher.utter_message(
                    text="Do you have some family members or friends who are experiencing PTSD?", buttons=buttons)
                return [SlotSet('question', 'q_family_ptsd')]
        elif question == 'q_family_ptsd':
            if latest_message == 'affirm':
                dispatcher.utter_message(
                    text="They may be having a bad time. You can help them through this hard time.")
                dispatcher.utter_message(
                    text="There are some resources about PTSD details and some treatments that can help.")
                dispatcher.utter_message(
                    text="FAMILY RESOURCES RECOMMENDATIONS")     # add recommendations
                return []
            elif latest_message == 'deny':
                dispatcher.utter_message(
                    text="Are you a health practitioner or working in PTSD related fields?", buttons=buttons)
                return [SlotSet('question', 'q_practitioner_ptsd')]
        elif question == 'q_practitioner_ptsd':
            if latest_message == 'affirm':
                dispatcher.utter_message(
                    text="There are some resources about PTSD and some treaments may help PTSD patients recover.")
                dispatcher.utter_message(       # add recommendations
                    text="1. PTSD guideline - Children and adolescents: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-3.-Children-and-adolescents.pdf" +
                    "\n2. PTSD guideline - Interventions: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-4.-Interventions.pdf" +
                    "\n3. PTSD guideline - Treatment recommendations: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-6.-Treatment-recommendations.pdf" +
                    "\n4. PTSD guideilne - Special populations: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-1-Aboriginal-and-Torres-Strait-Islander-Peoples-1.pdf")
                return []
            elif latest_message == 'deny':
                dispatcher.utter_message(
                    text="RECOMMENDATION?")     # add recommendations
                return []
        elif question == 'q_yourself_ptsd':
            if latest_message == 'deny':
                dispatcher.utter_message(
                    text="There are some recommendations and resources for you to treat PTSD.")
                dispatcher.utter_message(       # give recommendation
                    text="1. PTSD guideline - Children and adolescents: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-3.-Children-and-adolescents.pdf" +
                    "\n2. PTSD guideline - Treatment recommendations: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-6.-Treatment-recommendations.pdf" +
                    "\n3. PTSD guideilne - Special populations: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-1-Aboriginal-and-Torres-Strait-Islander-Peoples-1.pdf")
                return []
            elif latest_message == 'affirm':    # record personal information
                dispatcher.utter_message(
                    text="Excellent! This is an anonymous test and the results will only be shown to you. So you can trust me totally. ")
                dispatcher.utter_message(
                    text="Now let's talk about you.")
                dispatcher.utter_message(
                    text="What's your age?")
                return[SlotSet('question', 'q_age')]
        elif question == 'q_age':
            age_input = int(tracker.latest_message['text'])
            buttons_gender = [
                {
                    "title": "Female",
                    "payload": "female"
                },
                {
                    "title": "Male",
                    "payload": "male"
                },
                {
                    "title": "Other",
                    "payload": "other"
                },
            ]
            dispatcher.utter_message(
                text="What's your gender", buttons=buttons_gender)
            return [SlotSet('question', 'q_gender'), SlotSet('age', age_input)]
        elif question == 'q_gender':
            gender_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Are you Aboriginal and Torres Strait Islander people?", buttons=buttons)
            return [SlotSet('question', 'q_Aboriginal'), SlotSet('gender', gender_input)]
        elif question == 'q_Aboriginal':
            aboriginal_people_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Are you experiencing a disater?", buttons=buttons)    # start a test for special population
            return [SlotSet('question', 'q_disater'), SlotSet('aboriginal_people', aboriginal_people_input)]
        elif question == 'q_disater':
            disater_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Are you a military or ex-military?", buttons=buttons)
            return [SlotSet('question', 'q_military'), SlotSet('disater', disater_input)]
        elif question == 'q_military':
            military_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Are you an emergency services persoonel?", buttons=buttons)
            return [SlotSet('question', 'q_emergency'), SlotSet('military', military_input)]
        elif question == 'q_emergency':
            emergency_input = tracker.latest_message['text']
            dispatcher.utter_message(text="In the past month, ...")
            dispatcher.utter_message(
                text="Have you had a motor vehicle accident or another traumatic injury survivors?", buttons=buttons)
            return [SlotSet('question', 'q_vehicle_accident'), SlotSet('emergency', emergency_input)]
        elif question == 'q_vehicle_accident':
            vehicle_accident_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Have you experienced a sexual assault?", buttons=buttons)
            return [SlotSet('question', 'q_sexual_assault'), SlotSet('vehicle_accident', vehicle_accident_input)]
        elif question == 'q_sexual_assault':
            sexual_assault_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Have you experienced terrorism?", buttons=buttons)
            return [SlotSet('question', 'q_terrorism'), SlotSet('sexual_assault', sexual_assault_input)]
        elif question == 'q_terrorism':
            terrorism_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Have you been a victime of crime?", buttons=buttons)
            return [SlotSet('question', 'q_victim_crime'), SlotSet('terrorism', terrorism_input)]
        elif question == 'q_victim_crime':
            victim_crime_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Have you been a victim of intimate partner violence?", buttons=buttons)
            return [SlotSet('question', 'q_victim_violence'), SlotSet('victim_crime', victim_crime_input)]
        elif question == 'q_victim_violence':
            victim_violence_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Have you been a refugee and asylum seekers?", buttons=buttons)
            return [SlotSet('question', 'q_refugees'), SlotSet('victim_violence', victim_violence_input)]

        elif question == 'q_refugees':      # start 5-item measure
            refugees_input = tracker.latest_message['text']
            dispatcher.utter_message(
                text="Had nightmares about the event(s) or thought about the event(s) when you did not want to?", buttons=buttons)
            return [SlotSet('question', 'q_test_1'), SlotSet('refugees', refugees_input)]
        elif question == 'q_test_1':
            dispatcher.utter_message(
                text="Tried hard not to think about the event(s) or went out of your way to avod situations that reminded you of the event(s)?", buttons=buttons)
            if latest_message == 'affirm':
                scores = scores + 1.0
            return [SlotSet('question', 'q_test_2'), SlotSet('scores', scores)]
        elif question == 'q_test_2':
            dispatcher.utter_message(
                text="Been constantly on guard, watchful or startled?", buttons=buttons)
            if latest_message == 'affirm':
                scores = scores + 1.0
            return[SlotSet('question', 'q_test_3'), SlotSet('scores', scores)]
        elif question == 'q_test_3':
            dispatcher.utter_message(
                text="Felt numb or detached from people, activities or your surroundings?", buttons=buttons)
            if latest_message == 'affirm':
                scores = scores + 1.0
            return [SlotSet('question', 'q_test_4'), SlotSet('scores', scores)]
        elif question == 'q_test_4':
            dispatcher.utter_message(
                text="Guilty or unable to stop blaming yourself or others for the event(s) or any problems the enent(s) may have caused?", buttons=buttons)
            if latest_message == 'affirm':
                scores = scores + 1.0
            return [SlotSet('question', 'q_test_5'), SlotSet('scores', scores)]
        elif question == 'q_test_5':
            if latest_message == 'affirm':
                scores = scores + 1.0
            dispatcher.utter_message(text="Thanks for your answers.")
            print(scores)
            dispatcher.utter_message(
                text="Your score is " + str(scores) + "/5.0.")
            if scores < 3.0:
                dispatcher.utter_message(
                    text="It seems that you're fine right now, although sometimes you may have bad mood.")
                dispatcher.utter_message(
                    text="There are some recommendations for you to help overcome some bad emotions.")  # add recommendaitons
                dispatcher.utter_message(text="GIVE RECOMMENDATIONS")
            elif scores >= 3.0:
                dispatcher.utter_message(
                    text="It seems that you may have PTSD.")
                dispatcher.utter_message(
                    text="Before recommendations, do you want to tell us your email? So that we can track you and provide you with better treatment.", buttons=buttons)
                return [SlotSet('question', 'q_email')]
        elif question == 'q_email':
            if latest_message == 'affirm':
                dispatcher.utter_message(text="Please input your email.")
                return [SlotSet('question', 'q_PTSD_recommendation')]
            elif latest_message == 'deny':
                self.recommend(dispatcher, age, aboriginal_people, disater, military, emergency,
                               vehicle_accident, sexual_assault, terrorism, victim_crime, victim_violence, refugees)
        elif question == 'q_PTSD_recommendation':
            email = tracker.latest_message['text']
            self.recommend(dispatcher, age, aboriginal_people, disater, military, emergency,
                           vehicle_accident, sexual_assault, terrorism, victim_crime, victim_violence, refugees)

    def recommend(self, dispatcher, age, aboriginal_people, disater, military, emergency, vehicle_accident, sexual_assault, terrorism, victim_crime, victim_violence, refugees):
        dispatcher.utter_message(
            text="There are some recommendations and resources for you to treat PTSD.")
        dispatcher.utter_message(
            text="PTSD guideline - Treatment recommendations: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-6.-Treatment-recommendations.pdf")
        if age <= 17:
            dispatcher.utter_message(
                text="PTSD guideline - Children and adolescents: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-3.-Children-and-adolescents.pdf")
        elif age >= 65:
            dispatcher.utter_message(
                text="PTSD guideline - Older people: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-6.-PTSD-in-older-people-1.pdf")
        if aboriginal_people == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Aboriginal and Torres Strait Islander Peoples: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-1-Aboriginal-and-Torres-Strait-Islander-Peoples-1.pdf")
        if disater == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Disasters: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-2.-Disasters-1.pdf")
        if emergency == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Emergency services personnel: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-3.-Emergency-services-personnel-1.pdf")
        if military == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Military and ex-military personnel: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-4.-Military-and-ex-military-personnel-1.pdf")
        if vehicle_accident == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Motor vehicle accident: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-5.-Motor-vehicle-accident-and-other-traumatic-injury-survivors-1.pdf")
        if sexual_assault == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Sexual assault: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-8.-Sexual-assault-1.pdf")
        if terrorism == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Terrorism: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-9.-Terrorism-1.pdf")
        if victim_crime == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Victims of crime: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-10.-Victims-of-crime-1.pdf")
        if victim_violence == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Victims of Intimate Partner Violence: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-11.-Victims-of-intimate-partner-violence-1.pdf")
        if refugees == 'yes':
            dispatcher.utter_message(
                text="PTSD guideline - Refugees and asylum seekers: https://www.phoenixaustralia.org/wp-content/uploads/2020/07/Chapter-9-7.-Refugees-and-asylum-seekers-1.pdf")
