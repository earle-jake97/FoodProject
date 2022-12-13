# FoodProject
 This is a project that uses API calls to pick a random restaurant near you with given parameters.
 
 How to run:
 1. Within the FoodProject directory, run "uvicorn main:app --reload"
 2. Within the FoodProject/food-finder directory, run "npm start" after a certain amount of time a react application will open in your browser.
 3. Fill in the Address and City text boxes with your desired parameters, and optionally choose a mile radius.
 4. Click the Pick Restaurant button and it will select a restaurant for you. You can continue rerolling until you exhaust your options.
 
 This project works by utilizing three API calls. The first one takes your address and turns it into coordinates. The second one takes your coordinates, as well as radius and will return locations on the map labelled as restaurants and fast food. The third one will return the first result of an image search that uses the name of the currently displayed restaurant/fast food location.
