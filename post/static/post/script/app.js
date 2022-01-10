$(document).ready(function () {
  $("form").submit(function (event) {
    var formData = {
      user_name: $(".username").val(),
      title: $(".title").val(),
      description: $(".descrition").val(),
      image: $(".image").val(),
      
    };

    $.ajax({
      type: "POST",
      url: "post/edit/",
      data: formData,
      dataType: "json",
      encode: true,
    }).done(function (data) {
      console.log(data);
    });

    event.preventDefault();
  });
});