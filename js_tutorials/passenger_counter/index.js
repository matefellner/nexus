

let count = 0;


function increment() {
    console.log("clicked")
    count = count + 1;
    document.getElementById("count-el").textContent = count
}

function save(){

    document.getElementById("previos-entries").textContent += count + " - "
    count = 0;
    document.getElementById("count-el").textContent = count

}
