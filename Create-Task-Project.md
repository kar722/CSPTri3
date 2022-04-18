---
title: Create Task Project
layout: template
filename: Create-Task-Project
--- 

Replit Link: https://replit.com/@KarthikValluri/CSPTri3-1#create%20task/index.html

3. i. Describes the overall purpose of the program
ii. Describes what functionality of the program is demonstrated in the video
iii. Describes the input and output of the program demonstrated in the video
ai. The overall purpose of the program is providing recipes for people to make at home so they can further their creativity and discover new talents and hobbies. 
ii. The search function is demonstrated in the video, along with the get recipe button which gives you the recipe. 
iii. The input demonstrated is soup, giving the output of different soups across the world. 

3b. i. The first program code segment must show how data have been stored in the list.
ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. Then, provide a written response that does all three of the following:
iii. Identifies the name of the list being used in this response
iv. Describes what the data contained in the list represent in your program
v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
```
function getMealList(){
        let searchInputTxt = document.getElementById('search-input').value.trim();

        let url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchInputTxt}`
        fetch(url)
            .then(response => response.json())
            .then(data => {
```
```
let html = "";
                if(data.meals){
                    data.meals.forEach(meal => {
                        html += `
                    <div class = "meal-item" data-id = "${meal.idMeal}">
                        <div class = "meal-img">
                            <img src = "${meal.strMealThumb}" alt = "food">
                        </div>
                        <div class = "meal-name">
                            <h3>${meal.strMeal}</h3>
                            <a href = "#" class = "recipe-btn">Get Recipe</a>
                        </div>
                    </div>
```

3c.Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.
i. The first program code segment must be a student-developed procedure that:
   □ Defines the procedure’s name and return type (if necessary)
   □ Contains and uses one or more parameters that have an effect on the functionality of the procedure
   □ Implements an algorithm that includes sequencing, selection, and iteration
ii. The second program code segment must show where your student-developed procedure is being called in your program.
iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
```
function mealRecipeModal(meal){
        console.log(meal);
        meal = meal[0];
        let html = `
        <h2 class = "recipe-title">${meal.strMeal}</h2>
        <p class = "recipe-category">${meal.strCategory}</p>
        <div class = "recipe-instruct">
            <h3>Instructions:</h3>
            <p>${meal.strInstructions}</p>
        </div>
        <div class = "recipe-meal-img">
            <img src = "${meal.strMealThumb}" alt = "">
        </div>
        <div class = "recipe-link">
            <a href = "${meal.strYoutube}" target = "_blank">Watch Video</a>
        </div>
    `;
        mealDetailsContent.innerHTML = html;
        mealDetailsContent.parentElement.classList.add('showRecipe');
    }
```
```
                `;
                    });
                    mealList.classList.remove('notFound');
                } else{
                    html = "huh?";
                    mealList.classList.add('notFound');
                }

                mealList.innerHTML = html;
```

iii. The procedure in the code is the modal to show the recipe and instructions for the food of your choice.

iv. The algorithm takes the information from the list and displays it in HTML.
