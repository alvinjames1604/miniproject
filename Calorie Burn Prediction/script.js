const calorieForm = document.getElementById('calorieForm');
const resultDiv = document.getElementById('result');

calorieForm.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get input values
    const gender = document.getElementById('gender').value;
    const age = parseInt(document.getElementById('age').value);
    const height = parseInt(document.getElementById('height').value);
    const weight = parseInt(document.getElementById('weight').value);
    const duration = parseInt(document.getElementById('duration').value);
    const heartRate = parseInt(document.getElementById('heartRate').value);
    const bodyTemp = parseInt(document.getElementById('bodyTemp').value);

    // Calculate calories burnt (replace with your calculation logic)
    const caloriesBurnt = calculateCalories(gender, age, height, weight, duration, heartRate, bodyTemp);

    // Display result
    resultDiv.textContent = `Estimated calories burnt: ${caloriesBurnt}`;
});

function calculateCalories(gender, age, height, weight, duration, heartRate, bodyTemp) {
    // Implement your calorie calculation logic here, considering gender
    // This is a placeholder. You'll need to replace it with a suitable formula
    return Math.floor(Math.random() * 500) + 200; // Temporary random value
}
