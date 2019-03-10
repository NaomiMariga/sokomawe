/*// Create the XHR object.
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // XHR for Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // XDomainRequest for IE.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    // CORS not supported.
    xhr = null;
  }
  return xhr;
} */
//Display a slide show
function reload() {
  var slides = document.getElementById("image-slides");
  var target = Math.round(Math.random(slides) * 4) + 1;
  slides.src = `material/images/${target}.png`;
}
// Display registration form and hide the rest
$("#form_register").on("shown.bs.collapse", function() {
  // do something…
  $("#form_login").collapse("hide");
  $("#form_reset").collapse("hide");
});
//Display login form and hide the rest
$("#form_login").on("shown.bs.collapse", function() {
  // do something…
  $("#form_register").collapse("hide");
  $("#form_reset").collapse("hide");
});
//Display the reset password form and hide the rest
$("#form_reset").on("shown.bs.collapse", function() {
  $("#form_login").collapse("hide");
  $("#form_register").collapse("hide");
});

let home_page = document.querySelector("#home_page");
let main_page = document.querySelector("#main_page");
let site_news = document.querySelector("#site_news");
/*
function getTitle(text) {
  return text.match('<title>(.*)?</title>')[1];
}
*/
/*function makeCorsRequest() {
  // This is a sample server that supports CORS.
  let url = "https://sokopoa.herokuapp.com/registration"
  var xhr = createCORSRequest('POST', url);
  if (!xhr) {
    alert('CORS not supported');
    return;
  }
  
    // Response handlers.
    xhr.onload = function() {
      var text = xhr.responseText;
      var title = getTitle(text);
      alert('Response from CORS request to ' + url + ': ' + title);
    };
  
    xhr.onerror = function() {
      alert('Woops, there was an error making the request.');
    };
  
    xhr.send();
}*/
//Create Account 
function registration(){
  let fname = document.querySelector('#fname').value;
  let surname = document.querySelector('#surname').value;
  let id = document.querySelector('#id').value;
  let phone = document.querySelector('#phone').value;
  let email = document.querySelector('#email').value;
  let username = document.querySelector('#username').value;
  let password = document.querySelector('#password').value;
  console.log(password);
  $.ajax({
    url:"/registration",
    type:"POST",
    data:{
      fname:fname,
      surname:surname,
      id:id,
      phone:phone,
      email:email,
      username:username,
      password:password
    },
    dataType: "json",
    Success: response => {
      console.log(response);
      response = typeof response === "string" ? JSON.parse(response) : response;
      if (response.success){
        window.alert(response.message);
        console.log(response.message);
        $('#form_login').collapse("show");
      } else{
        window.alert(response.message);
        fname = "";
        surname = "";
        id = "";
        phone = "";
        email = "";
        username = "";
        password = "";
        console.log(response.message);
      }
    },
    error: function (error) {
      window.alert("An error occurred" + error);
      console.log(error);
  }
  });
};
// login
function login() {
  home_page.classList.add("d-none");
  if (main_page.classList.contains("d-none")) {
    main_page.classList.remove("d-none");
    site_news.classList.add("d-none");
  }
}
// logout
function Logout() {
  main_page.classList.add("d-none");
  if (home_page.classList.contains("d-none")) {
    home_page.classList.remove("d-none");
  }
}
