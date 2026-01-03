function Num(value) {
  // Validate input
  if (typeof value !== 'number' || isNaN(value)) {
    throw new TypeError('Not a Number');
  }
  if (value < 1 || value > 10) {
    throw new TypeError('Out of range');
  }

  // Store the validated value
  this.value = value;
}

// Override valueOf to enable arithmetic operations
Num.prototype.valueOf = function() {
  return this.value;
};

// Override toString for string representation
Num.prototype.toString = function() {
  return String(this.value);
};
