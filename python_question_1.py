import logging
logging.basicConfig(filename="Python_question_1.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

def max_frequency(string):
    try:
        string = str.lower(string)
        all_words = string.split()
        words = []
        freq = {}

        for i in all_words:
            if i not in words:
                words.append(i)

        for i in words:
            freq[i] = string.count(i)

        max_freq = max(zip(freq.values(),freq.keys()))[0]

        logging.info(f"Words along with their frequencies are: {freq}")
        logging.info(f"Max frequency of any word is: {max_freq}")
        return max_freq
    except Exception as e:
        logging.error(e)
if __name__ ==  "__main__":
    a = input("Enter a sentence")
    max_frequency(a)