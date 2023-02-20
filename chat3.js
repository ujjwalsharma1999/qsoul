const input = document.getElementById("input");
const output = document.getElementById("output");
const submit = document.getElementById("submit");

submit.addEventListener("click", () => {
  const inputData = input.value;
  output.value += "\n" + inputData;
  // Send the input data to the chatbot backend and get the response
  const responseData = "This is the chatbot's response to '" + inputData + "'.";
  output.value += "\n" + responseData;
});