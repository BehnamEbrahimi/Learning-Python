class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')

    # LBYL (Non-Pythonic): Look Before You Leap
    if hasattr(thing, 'quack'):  # True if either attribute or method
        if callable(thing.quack):  # True if method
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

    # Pythonic: Duck Typing: If it walks like a duck and it quacks like a duck, then it must be a duck.  EAFP: Easier to ask forgiveness than permission. this concept means try to do sth if it works great! if not handle the error
        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(e)


d = Duck()
quack_and_fly(d)
p = Person()
quack_and_fly(p)
