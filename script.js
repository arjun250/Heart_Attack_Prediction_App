async function predict() {
    const age = document.getElementById("age").value;
    const sysBP = document.getElementById("sysBP").value;
    const prevalentHyp = document.getElementById("prevalentHyp").value;

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ age, sysBP, prevalentHyp })
    });

    const result = await response.json();

    const output = result.prediction === 1
        ? "⚠️ High Risk of Heart Attack"
        : "✅ Low Risk of Heart Attack";

    document.getElementById("predictionResult").innerText =
        `${output} (Probability: ${result.probability})`;
}
