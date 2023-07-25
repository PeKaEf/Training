import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logging.root.setLevel(logging.NOTSET)


def calculator(counting, numb1, numb2):

    equals = 0

    if counting == 1:
        logging.info("Dodaję {} do {}".format(numb1, numb2))
        equals = numb1+numb2
        logging.info("Wynik to {}.".format(equals))
    elif counting == 2:
        logging.info("Odejmuję {} od {}".format(numb1, numb2))
        equals = numb1 - numb2
        logging.info("Wynik to {}.".format(equals))
    elif counting == 3:
        logging.info("Mnożę {} razy {}".format(numb1, numb2))
        equals = numb1 * numb2
        logging.info("Wynik to {}.".format(equals))
    elif counting == 4:
        if numb2 == 0:
            logging.info("Dzielisz przez zero!")
        else:
            logging.info("Dzielę {} przez {}".format(numb1, numb2))
            equals = numb1 / numb2
            logging.info("Wynik to {}.".format(equals))

if __name__ =="__main__":
    counting = int(sys.argv[1])
    numb1 = int(sys.argv[2])
    numb2 = int(sys.argv[3])
    calculator(counting, numb1, numb2)
