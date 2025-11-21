import pandas
import numpy as np

emails = pandas.read_csv("emails.csv")

# print(emails.head())

def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words'] = emails['text'].apply(process_email)

# print(emails[['text', 'words']].head())

probSpam = sum(emails['spam'])/len(emails)

probHam = 1 - probSpam

# Finding the posterior with Bayes' Theorem

word = 0
model = {}

for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam': 1, 'ham': 1}
        if word in model:
            if email['spam']:
                model[word]['spam'] += 1
            else:
                model[word]['ham'] += 1

# Implementing the naive Bayes algorithm

def predict_naive_bayes(email):
    """Naive Bayes Prediction Algorithm

    Args:
        email (str): the text of a single email to classify

    Returns:
        float: Probability that the email is spam (0.0 to 1.0).
    """
    total = len(emails)
    num_spam = sum(emails['spam'])
    num_ham = total - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam'] / num_spam * total)
            hams.append(model[word]['ham'] / num_ham * total)
    prod_spams = np.float64(np.prod(spams) * num_spam)
    prod_hams = np.float64(np.prod(hams) * num_ham)
    return prod_spams / (prod_spams + prod_hams)

print(predict_naive_bayes("Congratulations! You've won a free ticket to Bahamas. Click here to claim your prize."))

print(predict_naive_bayes("Hi mom how are you doing today?"))

print(predict_naive_bayes('meet me at the lobby of the hotel at nine am'))

print(predict_naive_bayes('asdfgh'))

print(predict_naive_bayes('You have won a lottery of $1000000! Claim now!'))

print(predict_naive_bayes('Important update about your account security'))

print(predict_naive_bayes('Get cheap meds now, limited time offer!'))

print(predict_naive_bayes('buy cheap lottery easy money now'))

"""Summary
• Bayes’ theorem is a technique widely used in probability, statistics, and machine learning.
• Bayes’ theorem consists of calculating a posterior probability, based on a prior probability
and an event.
• The prior probability is a basic calculation of a probability, given very little information.
• Bayes’ theorem uses the event to make a much better estimate of the probability in
question.
• The naive Bayes algorithm is used when one wants to combine a prior probability
together with several events.
• The word naive comes from the fact that we are making a naive assumption, namely, that
the events in question are all independent.
"""