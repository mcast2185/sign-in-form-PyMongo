
$("form[name=signup_form]").submit(function(e){
  let $form = $(this);
  let $error = $form.find(".error");
  let data = $form.serialize();
  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp){
      window.location.href ="/dashboard/"
    },
    error: function(resp){
      console.log(resp);
      $error.text(resp.responseJSON.error).removeClass('error--hidden')
    }
  });
  e.preventDefault();
});

$("form[name=login_form]").submit(function(e){
  let $form = $(this);
  let $error = $form.find(".error");
  let data = $form.serialize();
  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp){
      window.location.href ="/dashboard/"
    },
    error: function(resp){
      console.log(resp);
      $error.text(resp.responseJSON.error).removeClass('error--hidden')
    }
  });
  e.preventDefault();
});

$(":input").on('focus', function(){
  let text = document.querySelector('input').placeholder
  $(this).css('letter-spacing', '.5px')
  $(this).css({'box-shadow': '3px 5px 3px rgba(0,0,0,0.3)', 'transition': 'ease-in-out'})
  $(this).focusout(function(){
    $(this).css({'box-shadow': 'none', 'letter-spacing': '0px'})
  });
})



// $(this).animate({
//   color: 'rgba(0,0,0,0.1)',
//   textAlign: 'right',
//   textTransform: 'scaleX(50%)',
//   transition: 'ease-out'
// }, 1500)












