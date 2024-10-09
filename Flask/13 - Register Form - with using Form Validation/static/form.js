// alert('are you sure !!')

const form = document.getElementById("form")
const uname = document.getElementById("uname")
const email = document.getElementById("email")
const password = document.getElementById("password")
const cpassword = document.getElementById("cpassword")


form.addEventListener("submit" , (e) =>{
    e.preventDefault()

    validate()
})

function validate(){
    let nameValue = uname.value.trim()
    let emailValue = email.value.trim()
    let passwordValue = password.value.trim()
    let cpasswordValue = cpassword.value.trim()


     if(nameValue===''){
        setError(uname,'user name cannot be empty')
        
    }
    else if(nameValue.length<3){
        setError(uname,'user name should be minimum 3 characters')
    }
    else{        
        setSuccesss(uname)
    }
    //email check
    if(emailValue===''){
        setError(email,'Eamil cannot be empty')

    }  
    else if(!emailCheck(emailValue)){
        setError(email,'Enter Valid Email Id')
    }
    else{        
        setSuccesss(email)
    }

    
    //Password check

    if(passwordValue===''){
        setError(password,'password cannot be empty')
    }
    else if(passwordValue.length<8){
        setError(password,'Password should be minimum 8 characters')
    }
    else{        
        setSuccesss(password)
    }

      
    //Confirm Password check

    if(cpasswordValue===''){
        setError(cpassword,'password cannot be empty')
    }
    else if(cpasswordValue !==passwordValue){
        setError(cpassword,'passwords not matched')
    }
    else{        
        setSuccesss(cpassword)
    }
    
//  No need to learn , if you want just copy it
    function setError(input,message){ 
        let parent = input.parentElement;             // we need to enter manually ( parentElement , classList )
        let small = parent.querySelector('small')
        small.innerText = message
        parent.classList.add('error')
        parent.classList.remove('success')
    }
    function setSuccesss(input){
        let parent = input.parentElement;
        parent.classList.add('success')               // This 'success' we need to write as same as CSS file
        parent.classList.remove('error')              // This 'error' we need to write as same as CSS file
    }


    function emailCheck(input){
        let emailReg = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
        let valid = emailReg.test(input)       
        return valid
    }
}

//  This below code is used to print the enter data in console as "object"
// Just copy and past it


// NOTE-
// "submit" must be same as the ( button "type" in HTML also should be same )

form.addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    const formData = new FormData(event.target); 
    const formObject = Object.fromEntries(formData.entries()); 
    
    console.log(formObject); 
});

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    this.submit();
});




