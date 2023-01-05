


const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const tabBtn = document.getElementById("tab-btn")
const deleteBtn = document.getElementById("delete-btn")
const leadList = document.getElementById("lead-list")


function renderLeads(leads){

    let listItems = ""
    for(var i=0; i<leads.length; i++){
        // leadList.innerHTML += "<li>" + myLeads[i] + "</li>"
        /*
        const li = document.createElement("li")
        li.textContent = myLeads[i]
        leadList.append(li)
        */
        listItems += `
            <li>
                <a target='_blank' href='${leads[i]}'>
                    ${leads[i]}
                </a>
            </li>`

    }

    leadList.innerHTML = listItems
}


if(!localStorage.getItem("myLeads")){
    myLeadsStr = JSON.stringify([])
    localStorage.setItem("myLeads", myLeadsStr)
}else{
    renderLeads(JSON.parse(localStorage.getItem("myLeads")))
}


inputBtn.addEventListener("click", function(){

    let myLeads = JSON.parse(localStorage.getItem("myLeads"))

    if(inputEl.value != ""){
        myLeads.push(inputEl.value)
        inputEl.value = ""
        localStorage.setItem("myLeads", JSON.stringify(myLeads))
        renderLeads(JSON.parse(localStorage.getItem("myLeads")))
    }
})


deleteBtn.addEventListener("dblclick", function(){

    localStorage.clear()
    myLeadsStr = localStorage.setItem("myLeads", JSON.stringify([]))
    renderLeads(JSON.parse(localStorage.getItem("myLeads")))
})


tabBtn.addEventListener("click", function(){

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        // since only one tab should be active and in the current window at once
        // the return variable should only have one entry


        let myLeads = JSON.parse(localStorage.getItem("myLeads"))

        myLeads.push(tabs[0].url)
        localStorage.setItem("myLeads", JSON.stringify(myLeads))
        renderLeads(JSON.parse(localStorage.getItem("myLeads")))
    })

})
