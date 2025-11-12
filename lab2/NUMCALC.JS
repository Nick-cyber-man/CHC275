const prompt = require('prompt-sync')();
switch (prompt("what opperation?")){
    case "+":
        console.log(+prompt("num1")+ +prompt("num2"));break;
    case "*":
        console.log(+prompt("num1")* +prompt("num2"));break;
    case "/":
        console.log(+prompt("num1")/ +prompt("num2"));break;
    case "-": 
        console.log(+prompt("num1")- +prompt("num2"));break;
}
