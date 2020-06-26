console.log("We are live")

$( ".client_sterge" ).on("click", function() {
    var client_id = $(this).attr('id')
    var returncode = confirm("Esti sigur ca vrei sa stergi clientul?")
    if (returncode) {
        $.ajax({
            type: "GET",
            url: '/clienti/sterge/' + client_id,
            dataType: "json",
            success: function(data, textStatus) {
                if (data) {
                    window.location.href = '/clienti/1';
                } else {
                    console.log("OK")
                }
            }
        })
    }
  })

  $( ".abonament_sterge" ).on("click", function() {
    var abonament_id = $(this).attr('id')
    var returncode = confirm("Esti sigur ca vrei sa stergi abonamentul?")
    if (returncode) {
        $.ajax({
            type: "GET",
            url: '/abonament/sterge/' + abonament_id,
            dataType: "json",
            success: function(data, textStatus) {
                if (data) {
                    window.location.href = '/abonament/1';
                } else {
                    console.log("OK")
                }
            }
        })
    }
  })
