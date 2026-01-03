// Num Implementation
function Num(value) {
  // Validate input
  if (typeof value !== "number" || isNaN(value)) {
    throw new TypeError("Not a Number");
  }
  if (value < 1 || value > 10) {
    throw new TypeError("Out of range");
  }

  // Store the validated value
  this.value = value;
}

// Override valueOf to enable arithmetic operations
Num.prototype.valueOf = function () {
  return this.value;
};

// Override toString for string representation
Num.prototype.toString = function () {
  return String(this.value);
};

// Global variables
let numInstances = {};
let instanceCounter = 0;

// Initialize particles
function createParticles() {
  const particlesContainer = document.getElementById("particles");
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "%";
    particle.style.width = Math.random() * 4 + 2 + "px";
    particle.style.height = particle.style.width;
    particle.style.animationDelay = Math.random() * 20 + "s";
    particle.style.animationDuration = Math.random() * 10 + 10 + "s";
    particlesContainer.appendChild(particle);
  }
}

// Initialize number line
function initNumberLine() {
  const numberLine = document.querySelector(".number-line");
  for (let i = 0; i <= 11; i++) {
    const tick = document.createElement("div");
    tick.className = "number-tick";
    tick.style.left = (i / 11) * 100 + "%";

    const label = document.createElement("div");
    label.className = "number-label";
    label.style.left = (i / 11) * 100 + "%";
    label.textContent = i;

    numberLine.appendChild(tick);
    numberLine.appendChild(label);
  }
}

// Update value indicator
function updateValueIndicator(value) {
  const indicator = document.getElementById("valueIndicator");
  const position = ((value - 0) / 11) * 100;
  indicator.style.left = position + "%";
  indicator.setAttribute("data-value", value);
}

// Show error message
function showError(message) {
  const errorDisplay = document.getElementById("errorDisplay");
  const successDisplay = document.getElementById("successDisplay");
  errorDisplay.textContent = message;
  errorDisplay.style.display = "block";
  successDisplay.style.display = "none";
  setTimeout(() => {
    errorDisplay.style.display = "none";
  }, 5000);
}

// Show success message
function showSuccess(message) {
  const errorDisplay = document.getElementById("errorDisplay");
  const successDisplay = document.getElementById("successDisplay");
  successDisplay.textContent = message;
  successDisplay.style.display = "block";
  errorDisplay.style.display = "none";
  setTimeout(() => {
    successDisplay.style.display = "none";
  }, 5000);
}

// Create Num instance
function createNum() {
  const input = document.getElementById("numInput").value.trim();
  const value = parseFloat(input);

  try {
    const num = new Num(value);
    const instanceName = `num${++instanceCounter}`;
    numInstances[instanceName] = num;

    updateValueIndicator(value);
    showSuccess(`Created ${instanceName} = ${value}`);

    // Add to terminal
    addTerminalLine(`> const ${instanceName} = new Num(${value});`);
    addTerminalLine(`< ${instanceName}.toString() = "${num.toString()}"`);

    document.getElementById("numInput").value = "";
  } catch (error) {
    showError(error.message);
    addTerminalLine(`> new Num(${input})`);
    addTerminalLine(`! ${error.message}`);
  }
}

// Perform arithmetic operation
function performOperation() {
  const op1 = document.getElementById("op1").value.trim();
  const op2 = document.getElementById("op2").value.trim();
  const operator = document.getElementById("operator").value;

  try {
    const num1 = parseFloat(op1);
    const num2 = parseFloat(op2);

    const n1 = new Num(num1);
    const n2 = new Num(num2);

    let result;
    let operation;

    switch (operator) {
      case "+":
        result = n1 + n2;
        operation = "Addition";
        break;
      case "-":
        result = n1 - n2;
        operation = "Subtraction";
        break;
      case "*":
        result = n1 * n2;
        operation = "Multiplication";
        break;
      case "/":
        result = n1 / n2;
        operation = "Division";
        break;
    }

    displayOperationResult(operation, `${num1} ${operator} ${num2}`, result);
    showSuccess(`${operation} successful!`);

    addTerminalLine(`> new Num(${num1}) ${operator} new Num(${num2})`);
    addTerminalLine(`< ${result}`);

    document.getElementById("op1").value = "";
    document.getElementById("op2").value = "";
  } catch (error) {
    showError(error.message);
    addTerminalLine(`> Operation failed: ${error.message}`);
  }
}

// Perform comparison
function performComparison() {
  const comp1 = document.getElementById("comp1").value.trim();
  const comp2 = document.getElementById("comp2").value.trim();
  const comparator = document.getElementById("comparator").value;

  try {
    const num1 = parseFloat(comp1);
    const num2 = parseFloat(comp2);

    const n1 = new Num(num1);
    const n2 = new Num(num2);

    let result;
    let operation;

    switch (comparator) {
      case "<":
        result = n1 < n2;
        operation = "Less than";
        break;
      case ">":
        result = n1 > n2;
        operation = "Greater than";
        break;
      case "<=":
        result = n1 <= n2;
        operation = "Less than or equal";
        break;
      case ">=":
        result = n1 >= n2;
        operation = "Greater than or equal";
        break;
      case "==":
        result = n1 == n2;
        operation = "Equal";
        break;
      case "!=":
        result = n1 != n2;
        operation = "Not equal";
        break;
    }

    displayComparisonResult(operation, `${num1} ${comparator} ${num2}`, result);
    showSuccess(`Comparison result: ${result}`);

    addTerminalLine(`> new Num(${num1}) ${comparator} new Num(${num2})`);
    addTerminalLine(`< ${result}`);

    document.getElementById("comp1").value = "";
    document.getElementById("comp2").value = "";
  } catch (error) {
    showError(error.message);
    addTerminalLine(`> Comparison failed: ${error.message}`);
  }
}

// Display operation result
function displayOperationResult(operation, expression, result) {
  const resultsContainer = document.getElementById("operationResults");
  const resultCard = document.createElement("div");
  resultCard.className = "result-card";
  resultCard.innerHTML = `
                <div class="result-label">${operation}</div>
                <div class="result-value">${expression} = ${result}</div>
            `;
  resultsContainer.appendChild(resultCard);
}

// Display comparison result
function displayComparisonResult(operation, expression, result) {
  const resultsContainer = document.getElementById("operationResults");
  const resultCard = document.createElement("div");
  resultCard.className = "result-card";
  resultCard.innerHTML = `
                <div class="result-label">${operation}</div>
                <div class="result-value">${expression} = ${result}</div>
            `;
  resultsContainer.appendChild(resultCard);
}

// Copy code to clipboard
function copyCode() {
  const codeText = document.querySelector("pre").textContent;
  navigator.clipboard.writeText(codeText).then(() => {
    const btn = document.querySelector(".copy-btn");
    btn.textContent = "Copied!";
    btn.classList.add("copied");
    setTimeout(() => {
      btn.textContent = "Copy Code";
      btn.classList.remove("copied");
    }, 2000);
  });
}

// Terminal functionality
function addTerminalLine(text) {
  const terminal = document.getElementById("terminal");
  const line = document.createElement("div");
  line.className = "terminal-line";
  line.textContent = text;
  terminal.appendChild(line);
  terminal.scrollTop = terminal.scrollHeight;
}

function handleTerminalInput(event) {
  if (event.key === "Enter") {
    const input = document.getElementById("terminalInput").value.trim();
    if (input) {
      addTerminalLine(`$ ${input}`);

      // Handle commands
      if (input === "help") {
        addTerminalLine("Available commands:");
        addTerminalLine("  help - Show this help message");
        addTerminalLine("  clear - Clear terminal");
        addTerminalLine("  test - Run tests");
        addTerminalLine("  instances - Show created instances");
      } else if (input === "clear") {
        const terminal = document.getElementById("terminal");
        terminal.innerHTML =
          '<div class="terminal-line">$ Num.js Interactive Terminal v1.0.0</div><div class="terminal-line">$ Type \'help\' for available commands</div><div class="terminal-line">$ <span class="cursor" id="terminalCursor"></span></div>';
      } else if (input === "test") {
        runTests();
      } else if (input === "instances") {
        if (Object.keys(numInstances).length === 0) {
          addTerminalLine("No instances created yet.");
        } else {
          for (const [name, instance] of Object.entries(numInstances)) {
            addTerminalLine(`  ${name} = ${instance.value}`);
          }
        }
      } else {
        try {
          const result = eval(input);
          addTerminalLine(`< ${result}`);
        } catch (error) {
          addTerminalLine(`! ${error.message}`);
        }
      }

      document.getElementById("terminalInput").value = "";
    }
  }
}

// Test suite
function runTests() {
  const testResults = document.getElementById("testResults");
  testResults.innerHTML = "";

  const tests = [
    {
      name: "Function exists",
      test: () => typeof Num === "function",
      expected: true
    },
    {
      name: "Creates object",
      test: () => new Num(4) instanceof Object,
      expected: true
    },
    {
      name: "TypeError for non-number",
      test: () => {
        try {
          new Num("test");
          return false;
        } catch (e) {
          return e instanceof TypeError && e.message === "Not a Number";
        }
      },
      expected: true
    },
    {
      name: "TypeError for value 0",
      test: () => {
        try {
          new Num(0);
          return false;
        } catch (e) {
          return e instanceof TypeError && e.message === "Out of range";
        }
      },
      expected: true
    },
    {
      name: "TypeError for negative value",
      test: () => {
        try {
          new Num(-5);
          return false;
        } catch (e) {
          return e instanceof TypeError && e.message === "Out of range";
        }
      },
      expected: true
    },
    {
      name: "TypeError for value 10",
      test: () => {
        try {
          new Num(10);
          return false;
        } catch (e) {
          return e instanceof TypeError && e.message === "Out of range";
        }
      },
      expected: true
    },
    {
      name: "TypeError for value > 10",
      test: () => {
        try {
          new Num(20);
          return false;
        } catch (e) {
          return e instanceof TypeError && e.message === "Out of range";
        }
      },
      expected: true
    },
    {
      name: "Addition works",
      test: () => new Num(3) + new Num(4) === 7,
      expected: true
    },
    {
      name: "Subtraction works",
      test: () => new Num(3) - new Num(4) === -1,
      expected: true
    },
    {
      name: "Multiplication works",
      test: () => new Num(3) * new Num(4) === 12,
      expected: true
    },
    {
      name: "Division works",
      test: () => new Num(3) / new Num(4) === 0.75,
      expected: true
    },
    {
      name: "Less than comparison",
      test: () => new Num(3) < new Num(4),
      expected: true
    },
    {
      name: "Greater than comparison",
      test: () => new Num(3) > new Num(4),
      expected: false
    },
    {
      name: "toString() method",
      test: () => new Num(5).toString() === "5",
      expected: true
    }
  ];

  let passed = 0;
  let failed = 0;

  tests.forEach((test, index) => {
    const result = test.test();
    const passedTest = result === test.expected;

    if (passedTest) passed++;
    else failed++;

    const resultCard = document.createElement("div");
    resultCard.className = "result-card";
    resultCard.style.borderColor = passedTest
      ? "var(--success-color)"
      : "var(--error-color)";
    resultCard.innerHTML = `
                    <div class="result-label">Test ${index + 1}</div>
                    <div class="result-value" style="color: ${
                      passedTest ? "var(--success-color)" : "var(--error-color)"
                    }">
                        ${passedTest ? "✓" : "✗"} ${test.name}
                    </div>
                `;
    testResults.appendChild(resultCard);
  });

  // Summary
  const summaryCard = document.createElement("div");
  summaryCard.className = "result-card";
  summaryCard.style.gridColumn = "1 / -1";
  summaryCard.innerHTML = `
                <div class="result-label">Test Summary</div>
                <div class="result-value" style="color: var(--success-color)">
                    ${passed} Passed, ${failed} Failed
                </div>
            `;
  testResults.appendChild(summaryCard);

  addTerminalLine(
    `> Test suite completed: ${passed}/${tests.length} tests passed`
  );
}

function clearTests() {
  document.getElementById("testResults").innerHTML = "";
  addTerminalLine("> Test results cleared");
}

// Initialize everything
document.addEventListener("DOMContentLoaded", function () {
  createParticles();
  initNumberLine();
  updateValueIndicator(5);
  addTerminalLine("$ System initialized successfully");
  addTerminalLine("$ Ready to accept commands");
});

// Add some initial animation
window.addEventListener("load", function () {
  document.body.style.opacity = "0";
  document.body.style.transition = "opacity 1s ease";
  setTimeout(() => {
    document.body.style.opacity = "1";
  }, 100);
});
