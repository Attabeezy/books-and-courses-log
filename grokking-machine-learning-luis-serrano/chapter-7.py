"""
To wrap up, these quantities are the following in both of our models:
Medical model:
• Recall and sensitivity: among the sick people (positives), how many were correctly
diagnosed as sick?
• Precision: among the people diagnosed as sick, how many were actually sick?
• Specificity: among the healthy people (negatives), how many were correctly diagnosed as
healthy?
Email model:
• Recall and sensitivity: among the spam emails (positives), how many were correctly
deleted?
• Precision: among the deleted emails, how many were actually spam?
• Specificity: among the ham emails (negatives), how many were correctly sent to the
inbox?
Summary
• Being able to evaluate a model is as important as being able to train one.
• We can use several important metrics to evaluate a model. The ones we learned in this
chapter are accuracy, recall, precision, F-score, specificity, and sensitivity.
• Accuracy calculates the ratio between correct predictions and total predictions. It is
useful but can fail in certain cases, especially when the positive and negative labels are
unbalanced.
• Errors are divided into two categories: false positives and false negatives.
– A false positive is a negatively labeled point, which the model incorrectly predicts as
positive.
– A false negative is a positively labeled point, which the model incorrectly predicts as
negative.
• For some models, false negatives and false positives are given different levels of
importance.
• Recall and precision are useful metrics to evaluate models, especially when the models
give false negatives and false positives different levels of importance.
– Recall measures how many of the positive points were correctly predicted by the
model. Recall is low when the model creates many false negatives. For this reason,
recall is a useful metric in models in which we don’t want many false negatives, such
as models for medical diagnosis.
– Precision measures how many of the points that the model predicted as positive are
actually positive. Precision is low when the model creates many false positives. For
this reason, precision is a useful metric in models in which we don’t want many false
positives, such as spam email models.
• F1-score is a useful metric that combines recall and precision. It returns a value in
between recall and precision but which is closer to the smaller of the two.
• Fb-score is a variation of F1-score, in which one can adjust the parameter b to give either
precision or recall a higher importance. Higher values of b give recall more importance,
and lower values of b give precision more importance. Fb-score is particularly useful to
evaluate models in which either precision or recall is more important than the other one,
but we still care about both metrics.
• Sensitivity and specificity are two useful metrics that help us evaluate models. They are
highly used in medical fields.
– Sensitivity, or true positive ratio, measures how many of the positive points were
correctly predicted by the model. Sensitivity is low when the model creates many false
negatives. For this reason, sensitivity is a useful metric to use in medical models
where we don’t want to accidentally leave many healthy patients without treatment.
– Specificity, or true negative ratio, measures how many of the negative points were
correctly predicted by the model. Specificity is low when the model creates many false
positives. For this reason, specificity is a useful metric in medical models where we
don’t want to accidentally treat or do further invasive tests on patients who are
healthy.
• Recall and sensitivity are the exact same thing. However, precision and specificity are not
the same thing. Precision makes sure that most of the predicted positives are truly
positive, and specificity checks that most of the true negatives have been detected.
• As we increase the threshold in a model, we decrease its sensitivity and increase its
specificity.
• The ROC, or receiver operating characteristic curve, is a useful graph that helps us keep
track of the sensitivity and specificity of the model for each different value of the
threshold.
• The ROC also helps us determine how good a model is, using the area under the curve,
or AUC. The closer the AUC is to 1, the better the model. The closer the AUC is to 0.5,
the worse the model.
• By looking at the ROC curve, we can make decisions on what threshold to use to give us
good values for both the sensitivity and the specificity, depending on how much of each
our model expects. This makes the ROC curve one of the most popular and useful ways
to evaluate and improve a model.
"""