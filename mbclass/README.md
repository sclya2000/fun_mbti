# MBTI Guesser
To run this, install Django, sklearn, and pandas. 
Then go to the root directory of the project and run 
python3 manage.py runserver

The key files of the project are personality.py, models.py, views.py, and the 
html files under the 'template' folder. The walkthrough video link is in a 
file called Video.md

The project is built with Django with a text classifier component. 
The model has a single class, Note. A Note object represents text that a 
user submits to be analyzed by a text classifier. 
Each Note object has a "body" (the text that a user wrote), time created, 
and "personality" (is determined by a text classifier method).

The text classifier has a method with a single parameter that is a string 
that represents what the user typed. When called, it first formats the string 
from the parameter into a dataframe that can be vectorized later on. 
The dataset is then read, and then cleaned up with the "filter_text" helper 
function that gets rid of '|||' and URLs from the dataset. The dataset is 
split into testing and training sets in an 80:20 ratio. 
A CountVectorizer is then created and used to vectorize all of the text in 
the datasets as well as the original 'msg' parameter. A logistic regression 
model from Sci-Kit Learn is then created, fitted with the training data, 
and used to predict the personality type of the parameter. The predicted 
personality type of 'msg' is returned at the end. 

After you type in some text into the box at the bottom and click the button, 
it calls the "splash" function in views. There, the logistic regression model 
is called and predicts the personality type. A Note object is then created 
and the updated splash page is rendered with the newest text at the top of 
the splash page. 

Clicking "See Meyers Briggs" under any of the listed texts will call the 
"analyze" function and render the page with just the text, the personality 
type of that text, and a description of what that personality is. Underneath 
is some descriptions of what the Meyers Briggs letters mean.
