var randomWords;
var wrd;

try {
    randomWords = require('random-english-words');
    console.log("randomWords loaded");
    wrd = randomWords(7);
}
catch (err) {
    console.log("Error: " + randomWords);
}

console.log (wrd);
