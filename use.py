import pickle

with open('spam_model.model', 'rb') as f:
  loaded_data = pickle.load(f)

loaded_model = loaded_data['model']
loaded_feature_extraction = loaded_data['feature_extraction']

def predict(message):
  global loaded_model
  global loaded_feature_extraction
  input_mail = [message]

  input_data_features = loaded_feature_extraction.transform(input_mail)
  prediction = loaded_model.predict(input_data_features)
  print(prediction)

  if (prediction[0]==1):
    print('Not Spam mail')
  else:
    print('Spam mail')

message = "I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times"
print("For example: " + message)
predict(message)

while True:
  new_mess = input("\npress ctrl + C to close) Enter your mail to check: ")
  print("\nResults For: " + message)
  predict(new_mess)

  


