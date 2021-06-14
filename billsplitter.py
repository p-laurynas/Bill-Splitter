import random

class BillSplitter:

    def __init__(self):
        self.people = None
        self.bill_value = None
        self.lucky_person = None
        self.bills = None

    def main(self):
        self.collect_people()
        if self.people:
            self.collect_bill()
            self.who_is_lucky()
            self.split_bill()

    def collect_people(self):
        try:
            no_of_people = int(input('Enter the number of friends joining (including you):\n'))
            if no_of_people < 1:
                raise ValueError
        except ValueError:
            print('\nNo one is joining for the party')
        else:
            print('\nEnter the name of every friend (including you), each on a new line:')
            self.people = [input() for _ in range(no_of_people)]

    def collect_bill(self):
        self.bill_value = float(input('Enter the total bill value:\n'))

    def who_is_lucky(self):
        someone_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if someone_lucky == 'Yes':
            self.lucky_person = random.choice(self.people)
            print(f'{self.lucky_person} is the lucky one!')
        else:
            print('No one is going to be lucky')

    def split_bill(self):
        no_of_people = len(self.people) - 1 if self.lucky_person else len(self.people)
        if self.bill_value % no_of_people == 0:
            split_value = self.bill_value // no_of_people
        else:
            split_value = round(self.bill_value / no_of_people, 2)

        self.bills = {person: split_value for person in self.people}
        if self.lucky_person:
            self.bills[self.lucky_person] = 0
        print(self.bills)


if __name__ == '__main__':
    BillSplitter().main()
