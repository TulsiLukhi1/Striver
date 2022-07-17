navbar = document.querySelector(".navbar").querySelectorAll("li");
console.log(navbar);

navbar.forEach(element => {
    element.addEventListener("click",function(){
        navbar.forEach(nav=>nav.classList.remove("active"))

        this.classList.add("active")
    });
});


// CUSTOM SELECT



const selected = document.querySelector(".selected");
const optionContainer = document.querySelector(".option-container");

const optionList = document.querySelectorAll(".option")

selected.addEventListener("click",()=>{
  optionContainer.classList.toggle("active-category");
});

optionList.forEach(option =>{
  option.addEventListener("click",()=>{
    selected.innerHTML=option.querySelector("label").innerHTML;
    optionContainer.classList.remove("active-category")
  })
})
