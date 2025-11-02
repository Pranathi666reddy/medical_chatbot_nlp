function sendMessage() {
  let userInput = document.getElementById("userInput").value;
  let chatBox = document.getElementById("chat-box");

  if (userInput.trim() === "") return;

  chatBox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

  // Simple health logic
  let reply = getBotResponse(userInput.toLowerCase());

  chatBox.innerHTML += `<div><strong>Bot:</strong> ${reply}</div>`;
  document.getElementById("userInput").value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}

function getBotResponse(input) {
  if (input.includes("fever") && input.includes("cough")) {
    return "You may have a mild flu or cold. Drink fluids and rest. Consult a doctor if it persists.";
  } else if (input.includes("chest pain")) {
    return "Chest pain can be serious. Please consult a cardiologist immediately.";
  } else if (input.includes("headache")) {
    return "It might be due to dehydration, stress, or eye strain. Rest and drink water.";
  } else if (input.includes("diabetes")) {
    return "For diabetes, maintain a balanced diet, avoid sugar, and monitor blood glucose regularly.";
  } else {
    return "I'm not sure. Please consult a healthcare professional for accurate advice.";
  }
}
