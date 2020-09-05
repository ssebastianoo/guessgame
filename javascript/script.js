var num;
var rangeA;
var rangeB;
var tries = 0;

function update() {
    const body = document.getElementById("container");
    num = Math.round((rangeA + rangeB) / 2)
    body.innerHTML = `
<a id = "number">${num}</a>
<button type = "button" id = "yes" onclick = "yes()">yes</button>
<button type = "button" id = "major" onclick = "major()">major</button>
<button type = "button" id = "minor" onclick = "minor()">minor</button>
`;
}

function submit() {
    rangeA = document.getElementById("rangeA");
    rangeB = document.getElementById("rangeB");

    if (parseInt(rangeA.value)) {
        a = 0
    } else { 
        if (parseInt(rangeA.value) === 0) {
            a = 0
        } else {
            return document.getElementById("error").innerText = "not a valid range!"
        }
    };

    if (parseInt(rangeB.value)) {
        a = 0
    } else { 
        if (parseInt(rangeB.value) === 0) {
            a = 0
        } else {
            return document.getElementById("error").innerText = "not a valid range!"
        }
    };

    rangeA = parseInt(document.getElementById("rangeA").value);
    rangeB = parseInt(document.getElementById("rangeB").value);

    if (rangeA > rangeB) {
        a = rangeA;
        b = rangeB;
        rangeA = b;
        rangeB = a;
    }
    tries += 1;
    update();
}

function major() {
    rangeA = num 
    tries += 1;
    update()
}

function minor() {
    rangeB= num 
    tries += 1;
    update()
}

function yes() {
    const body = document.getElementById("container");
    body.innerHTML = `<h1>I won in ${tries} tries!</h1>
<a href = "/">play again</a>`
}