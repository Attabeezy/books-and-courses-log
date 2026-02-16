import pandas as pd
import numpy as np

emails = pd.read_csv("emails.csv")

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

# print(predict_naive_bayes("Congratulations! You've won a free ticket to Bahamas. Click here to claim your prize."))

# print(predict_naive_bayes("Hi mom how are you doing today?"))

# print(predict_naive_bayes('meet me at the lobby of the hotel at nine am'))

# print(predict_naive_bayes('asdfgh'))

# print(predict_naive_bayes('You have won a lottery of $1000000! Claim now!'))

# print(predict_naive_bayes('Important update about your account security'))

# print(predict_naive_bayes('Get cheap meds now, limited time offer!'))

# print(predict_naive_bayes('buy cheap lottery easy money now'))

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

# Exercise 8.1
# Determine if the following pairs of events A and B are independent or dependent.
# Throwing three fair coins:
# a.
# A: prob of first coin on heads = 1/2
# B: prob of second coin on heads = 1/2
# Hence, A and B are independent.
# 
# b.
# A: prob of first coin on heads = 1/2
# B: prob of odd number of heads = prob of only first coin on heads + prob of only third coin on heads + prob of only second coin on heads + prob of all three coins on heads
# B = {HTT, THT, TTH, HHH}; P(B) = 4/(2^3) = 4/8 = 1/2
# Hence, A and B are dependent.
# 
#  
# Rolling two dice:
# c.
# A: prob of first showing 1; B: second one shows 2
# P(A) = 1/6; P(B) = 1/6
# Hence, A and B are independent
#
# d.
# A: First die shows 3.
# B: Second die shows a higher value than the first (Die 2 > Die 1).

# Total possible outcomes, n(S) = 6 * 6 = 36
# A outcomes, n(A) = {(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)}. So, n(A) = 6.
# A and B outcomes, n(A ∩ B) = {(3, 4), (3, 5), (3, 6)}. So, n(A ∩ B) = 3.
# B outcomes, n(B) = (1, 2-6) + (2, 3-6) + (3, 4-6) + (4, 5-6) + (5, 6) = 5 + 4 + 3 + 2 + 1 = 15. So, n(B) = 15.

# P(A) = n(A) / n(S) = 6 / 36 = 1/6
# P(A ∩ B) = n(A ∩ B) / n(S) = 3 / 36 = 1/12
# P(B) = n(B) / n(S) = 15 / 36 = 5/12

# Calculate P(A) * P(B):
# P(A) * P(B) = (1/6) * (15/36) = 15 / 216 = 5/72

# Compare P(A ∩ B) and P(A) * P(B):
# P(A ∩ B) = 1/12 (which is 6/72)
# P(A) * P(B) = 5/72
# Since 6/72 != 5/72, the condition for independence is NOT met.

# Alternative check using Conditional Probability (Condition: P(B|A) = P(B))
# P(B|A) = P(A ∩ B) / P(A) = (3/36) / (6/36) = 3 / 6 = 1/2
# P(B) = 5/12
# Since 1/2 != 5/12, the events are dependent.

# Hence, A and B are dependent.

# e. A: raining outside; B: it's Monday
# Given that the day of the week does not justify whether it rains or not, the events are independent
# 
# f. A: raining outside; B: it's June
# 
# 
# 
# Exercise 8.2
# Preamble:
# There is an office where we have to go regularly for some paperwork. This office has two clerks,
# Aisha and Beto. We know that Aisha works there three days a week, and Beto works the other
# two. However, the schedules change every week, so we never know which three days Aisha is
# there, and which two days Beto is there.
# 
# a. If we show up on a random day to the office, what is the probability that Aisha is the clerk?
# Prob(Aisha) = n(Aisha working days)/n(Total Working Days) = 3/5
# 
# b. What is the prob that Aisha is the clerk seeing that the clerk is wear red in the office from outside?
# Note: Aisha wears read one-third of the time & Beto wears read half of the time
# Prob(Aisha|red) = Prod(red|Aisha) / Prob(red) = Prob(red|Aisha) + Prob(red|Beto)
# Prob(Aisha|red) = (1/3 * 3/5) / ((1/3 * 3/5) + (1/2 * 2/5)) = 1/2
# 
# 
# 
# Exercise 8.3
# Binary representation (X=1, Missing=0)
binary_patient_data = {
    'Patient': ['Patient 1', 'Patient 2', 'Patient 3', 'Patient 4', 'Patient 5', 'Patient 6', 'Patient 7', 'Patient 8'],
    'Cough (C)': [0, 1, 1, 1, 1, 0, 0, 0],
    'Fever (F)': [1, 1, 0, 1, 0, 1, 1, 0],
    'Difficulty breathing (B)': [1, 0, 1, 1, 0, 1, 0, 0],
    'Tiredness (T)': [1, 1, 1, 0, 0, 0, 0, 1],
    'Diagnosis': ['Sick', 'Sick', 'Sick', 'Sick', 'Healthy', 'Healthy', 'Healthy', 'Healthy']
}

df = pd.DataFrame(binary_patient_data)

# Building the model for patients
model = {}

for index, patients in df.iterrows():
    diagnosis = patients['Diagnosis']
    for symptom in ['Cough (C)', 'Fever (F)', 'Difficulty breathing (B)', 'Tiredness (T)']:
        if symptom not in model:
            model[symptom] = {'Sick': 1, 'Healthy': 1}
        if patients[symptom] == 1:
            model[symptom][diagnosis] += 1
        else:
            model[symptom][diagnosis] += 0
            
            
def predict_naive_bayes_patient(symptoms):
    total = len(df)
    num_sick = sum(df['Diagnosis'] == 'Sick')
    num_healthy = total - num_sick
    spreds = [1.0]
    hpreds = [1.0]
    for symptom in symptoms:
        if symptom in model:
            spreds.append(model[symptom]['Sick'] / num_sick * total)
            hpreds.append(model[symptom]['Healthy'] / num_healthy * total)
    prod_spreds = np.float64(np.prod(spreds) * num_sick)
    prod_hpreds = np.float64(np.prod(hpreds) * num_healthy)
    return prod_spreds / (prod_spreds + prod_hpreds)
# 'Cough (C)', 'Fever (F)', 'Difficulty breathing (B)', 'Tiredness (T)'
print(predict_naive_bayes_patient([0, 1, 0, 0, 'Sick']))

# a. Probability that a patient is sick given that the patient has a cough
print(predict_naive_bayes_patient([1, 0, 0, 0, 'Sick']))

# b. Probability that a patient is sick given that the patient is not tired
print(predict_naive_bayes_patient([1, 1, 1, 0, 'Sick']))

# c. Probability that a patient is sick given that the patient has a cough and a fever
print(predict_naive_bayes_patient([1, 1, 0, 0, 'Sick']))

# d. Probability that a patient is sick given that the patient has a cough and a fever, but no difficulty breathing
print(predict_naive_bayes_patient([1, 1, 0, 0, 'Sick']))